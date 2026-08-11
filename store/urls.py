from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('home', RedirectView.as_view(url='/', permanent=False)),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]