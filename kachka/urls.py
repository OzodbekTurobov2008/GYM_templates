from django.urls import path
from .views import home_view,contact_view,why_view,trainer_view,base_view



urlpatterns = [
    path('',home_view, name="home-page"),
    path('trainer/',trainer_view,  name="trainer-page"),
    path('why/',why_view, name="why-page"),
    path('contact/', contact_view, name="cantact-page"),
     path('base/', base_view, name="base-page"),
    
    
]






