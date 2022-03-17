from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import handler400
from . import views

urlpatterns = [
    path('', views.index, name="IndexStore"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('checkout/', views.checkout, name="Checkout"),
    path('products/<int:myid>', views.productview, name="ProductView"),
    path('handelrequest/', views.handelrequest, name="HandleRequest")
    
]
