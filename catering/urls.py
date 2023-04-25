from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('about',views.about,name="about"),
    path('catering',views.catering,name="catering"),
    path('decoration',views.decoration,name="decoration"),
    path('photography',views.photography,name="photography"),
    path('makeup',views.makeup,name="makeup"),
    path('entertainment',views.entertainment,name="entertainment"),
    path('contact',views.contact,name="contact"),
]

