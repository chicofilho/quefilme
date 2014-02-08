from django.contrib import admin
from quefilme.movie.models import Movie, Rate, Comment

class MovieAdmin(admin.ModelAdmin):
    pass
admin.site.register(Movie, MovieAdmin)

class RateAdmin(admin.ModelAdmin):
	pass
admin.site.register(Rate, RateAdmin)

class CommentAdmin(admin.ModelAdmin):
	pass
admin.site.register(Comment, CommentAdmin)