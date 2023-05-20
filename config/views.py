from django.shortcuts import render, redirect


def home(request):
    template_name = 'home.html'
    return render(request, template_name)