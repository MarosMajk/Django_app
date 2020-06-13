from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm,ViewForm
# Create your views here.

def index(response):
    if response.method == "POST":
        form = ContactForm(response.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            ico = form.cleaned_data['ico']
            print(name,email,ico)


    form = ContactForm()
    return render(response, "formular/form.html",{"form":form})

def FormView_detail(response):    
    if response.method == "POST":
        form = ViewForm(response.POST)
        if form.is_valid():
            form.save()
            
    form = ViewForm()
    return render(response, "formular/form.html",{"form":form})
