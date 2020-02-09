from django.shortcuts import render
from django.views.generic import ListView
from .models import Session

# Create your views here.


# def poster(request):
#     return render(request, 'cinema_box_office/index.html')


class Poster(ListView):
    model = Session
    template_name = 'cinema_box_office/index.html'