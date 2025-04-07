from django.urls import path
from .views import recipe_list, recipe_ingredients, home, add_recipe, add_recipe_image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',home,name='home'),
   path('recipes/list/', recipe_list, name='recipe_list'),
   path('recipe/<int:recipe_id>/', recipe_ingredients, name='recipe_ingredients'),
   path('recipe/add/',add_recipe, name='add_recipe'),
   path('recipe/<int:recipe_id>/add_image',add_recipe_image, name='add_recipe_image'),
]

app_name = 'ledger'

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)