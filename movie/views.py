from django.http import HttpResponse
from django.http import Http404
from movie.models import Movie, Rate, Comment
from django.shortcuts import render_to_response
import datetime
#from facebook import get_user_from_cookie
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from movie.forms import RateAllForm, AddMovie
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
import json
from random import shuffle

def search_movie(request):
	c = {}
	if request.GET:
		print 'GET'
	if request.is_ajax():
		r = []
		for obj in request.GET:
			print obj
			if request.GET[obj] != '':
				value = request.GET[obj]
				categories = obj.split('_')[1]
				if value<5:
					categories = obj.split('_')[0]
					
				up = int(value)*10 + 10
				down = int(value)*10 - 10
				rates = Rate.objects.filter(category=categories, rate__gt = down, rate__lt = up)
				for rate in rates:
					r.append({'id': rate.film.id, 'title': rate.film.title}) 
		print r
		response_data = r
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		movies = Movie.objects.all().order_by('-creation_date')[:5]
		comments = Comment.objects.all().order_by('-created_at')[:5]
		elements = []
		print len(movies)
		print len(comments)
		for mov in movies:
			elements.append({'movie': mov, 'type':'movie_with_comment'})
		for com in comments:
			elements.append({'comment': com, 'type':'comment'})
		shuffle(elements)
		c['content'] = elements
	return render_to_response('movie/index.html', RequestContext(request, c))

def view_movie(request, slug):
	try:
		m = Movie.objects.get(slug=slug)
		c = Comment.objects.filter(film = m)
		context = {'movie': m, 'comments': c}
		
		if(request.user):
			user = request.user
			context['user'] = user
			context.update(csrf(request))	
	except Movie.DoesNotExist:
		raise Http404
	return render_to_response('movie/view.html', RequestContext(request, context))

@login_required
def rate_movie(request, slug):
	user = request.user
	m = Movie.objects.get(slug=slug)
	c = {'movie': m}
	c.update(csrf(request))
	if(request.POST):
		rate = Rate(owner_id = user.id, rate = request.POST['rate'], film = m)
		rate.save()
	return render_to_response('movie/rate.html', c)	

@login_required
def rate_movie_categories(request, slug):
	user = request.user
	form = RateAllForm()
	c = {'form': form}
	c.update(csrf(request))
	if request.POST:
		movie = Movie.objects.get(slug=slug)
		form = RateAllForm(request.POST)
		if(form.is_valid()):
			form.save_user(user, movie)
		else:
			c = {'form': form}
			c.update(csrf(request))
	return render_to_response('movie/rate_all.html', c)	

def add_movie(request):
	user = request.user
	form = AddMovie()
	c = {'form': form}
	c.update(csrf(request))
	if request.POST:
		form = AddMovie(request.POST)
		if(form.is_valid()):
			form.save_movie(user)
		else:
			c = {'form': form}
			c.update(csrf(request))
	return render_to_response('movie/add.html', c)

def comment_movie(request, slug):
	if(request.POST):
		comment = request.POST['comment']
		movie = Movie.objects.get(slug=slug)
		Comment.objects.create(owner=request.user, film=movie, comment=comment)
	return HttpResponseRedirect(reverse('movie_view', args=[slug]))