from . import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', views.landing.as_view(), name='landing'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('test/', views.test.as_view(), name='test',),
]