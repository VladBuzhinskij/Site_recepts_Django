from django.contrib import admin
from django.urls import path,include
from recept import views

app_name="recept"
urlpatterns = [
    path('', views.Categorie, name='category'),
    path('<slug:subcategory_slug>/', views.ReceptsList, name='ReceptsList'),
    path('recept/<slug:recept_slug>', views.Recept, name='recept'),
    path('new_recept', views.NewRecept, name='new_recept'),

    
    

]