from django.contrib import admin
from .models import Platform, Category, Game, Review, Favorite

admin.site.register(Platform)
admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Favorite)
