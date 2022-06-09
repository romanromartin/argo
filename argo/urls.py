
from django.contrib import admin
from django.urls import path
from outdoor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('price/', views.price, name='price'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('managment/', views.managment, name='managment'),
    path('all_products/', views.all_products, name='all_products'),
    path('product/<id_product>/', views.products, name='product'),
    path('product/<id_product>/<id_subproduct>/', views.detail, name='detail'),


]
