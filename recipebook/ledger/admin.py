from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage

class ProfileInLine(admin.StackedInline):
  model = Profile
  can_delete = False

class UserAdmin(BaseUserAdmin):
  inlines = [ProfileInLine]

class RecipeImageInLine(admin.TabularInline):
  model = RecipeImage
  extra = 1

class RecipeAdmin(admin.ModelAdmin):
  inlines = [RecipeImageInLine]

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)