from django.shortcuts import render
from django.views.generic import CreateView,DateDetailView,DeleteView,ListView,UpdateView
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import person


# Create your views here.
class Allperson(ListView):
    model=person
    template_name='indexperson.html'

