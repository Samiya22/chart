from django.shortcuts import render
from .models import *

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def example(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'examp.html', context)

def statik(request):
    socials = Social.objects.all()
    context = {
        'socials': socials
    }
    return render(request, 'statik.html', context)

def humans(request):
    humans = Humans.objects.all()
    context = {
        'humans': humans
    }
    return render(request, 'humans.html', context)


def imgchart(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'imgchart.html', context)


def telefonlar(request):
    posts = Telefonlar.objects.all()
    context = {
        'telefonlar': posts
    }
    return render(request, 'telefonlar.html', context)

def pie(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'pie.html', context)


def country(request):
    country = Country.objects.all()
    context = {
        'country': country
    }
    return render(request, 'country.html', context)


