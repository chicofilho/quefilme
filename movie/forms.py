from django import forms
from movie.models import *
import datetime

class RateAllForm(forms.Form):
	ac = forms.IntegerField(label='Action')
	ca = forms.IntegerField(label='Calm')
	ha = forms.IntegerField(label ='Happy')
	sa = forms.IntegerField(label='Sad')
	cu = forms.IntegerField(label='Cult')
	tr = forms.IntegerField(label='Trash')
	un = forms.IntegerField(label='Unknown')
	fa = forms.IntegerField(label='Famous')

	def save_user(self, user, film):
		for element in self.cleaned_data:
			print element
			Rate.objects.create(owner=user, film=film, category=element, rate=self.cleaned_data[element])

class AddMovie(forms.Form):
	title = forms.CharField()
	description = forms.CharField(widget=forms.Textarea)
	trailer_link = forms.URLField()
	year = forms.IntegerField()
	
	def save_movie(self, user):
		title = self.cleaned_data['title']
		description = self.cleaned_data['description']
		creation_date = datetime.datetime.now()
		trailer_link = self.cleaned_data['trailer_link']
		year = str(self.cleaned_data['year'])+'-01-03'
		slug = title.lower().replace(' ', '_')
		Movie.objects.create(owner = user, 
					title=title, 
					description=description, 
					creation_date=creation_date,
					trailer_link=trailer_link,
					year=year,
					slug=slug,
					)
