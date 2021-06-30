from django.shortcuts import render
from django.http import  HttpResponse
from .forms import Valueform



def form_view(request):
    form = Valueform(request.POST or None)

    if form.is_valid():
            form.save()

            form = Valueform()
    return  render(request,'Form_Handeling.html', {"form": form})