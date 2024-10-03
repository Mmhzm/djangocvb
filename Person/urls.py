from django.urls import path
from .views import Allperson,Detailperson
urlpatterns = [
    path('Allperson/',Allperson.as_view()),
    path('Detailperson/<int:pk>/',Detailperson.as_view()),
    
    
    
]
