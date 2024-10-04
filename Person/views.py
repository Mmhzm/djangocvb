from django.shortcuts import render
from django.views.generic import CreateView,DetailView,DeleteView,ListView,UpdateView
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import person
from django.urls import reverse_lazy


# Create your views here.
class Allperson(ListView):
    model=person
    template_name='indexperson.html'

class Detailperson(DetailView):
    model=person   
    template_name='indexdetail.html'

class Createperson(CreateView):
    model=person
    template_name='indexcreate.html'
    fields=['name','family','age','national_id']

class Updateperson(UpdateView):
    model=person
    template_name='indexupdate.html'
    fields=['name','family','age','national_id']

class Deleteperson(DeleteView):
    model=person
    success_url=reverse_lazy('all')
    template_name='indexdelete.html'




    

