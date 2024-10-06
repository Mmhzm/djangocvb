from django.urls import path
from .views import listbook
urlpatterns = [
    path('allbook/',listbook.as_view())
    

]
