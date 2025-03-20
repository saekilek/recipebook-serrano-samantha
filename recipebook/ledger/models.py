from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Ingredient(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("ledger:ingredients", args=[str(self.id)])

class Recipe(models.Model):
  name = models.CharField(max_length=200,default="Untitled Recipe")
  #Modified the recipe model to have author, creation, and update fields.
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("ledger:recipe_ingredients", args=[str(self.id)])

class RecipeIngredient(models.Model):
  quantity = models.CharField(max_length=200)
  ingredient = models.ForeignKey(
    Ingredient,
    on_delete=models.CASCADE
  )
  recipe = models.ForeignKey(
    Recipe,
    on_delete=models.CASCADE
  )

User=get_user_model()

class Profile(models.Model):
  user = models.OneToOneField(
    get_user_model(),
    on_delete=models.CASCADE
  )
  name = models.CharField(max_length=50)
  bio = models.CharField(max_length=255)

  def __str__(self):
    return self.name