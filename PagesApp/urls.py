from django.urls import path
from . import views


urlpatterns = [
    path('',views.homePage),
    path('about/',views.aboutPage),
    path('contact/',views.contactPage),
    path('services/',views.servicePage),
    path('world/',views.helloWorld),
]
