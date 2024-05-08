from django.contrib import admin
from django.urls import path,include
from userss import views

app_name="userss"
urlpatterns = [

    path('registrayion/', views.Registration, name='registration'),
    path('login/', views.Login, name='login'),
    path('profile/', views.Profile, name='profile'),
    path('logout', views.logout, name='logout'),
    # path('search/',views.assort, name='search'),
    # path('<slug:category_slug>/<slug:subcategory_slug>/',views.assort, name='assort'),
    # path('<slug:category_slug>/',views.assort, name='assort'),
    # path('product/<slug:product_slug>',views.product,name="product"),
    
    


]