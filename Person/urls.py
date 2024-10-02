from django.urls import path
from .views import Allperson
urlpatterns = [
    path('Allperson/',Allperson.as_view()),
    
    
]
