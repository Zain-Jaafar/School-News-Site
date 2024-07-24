from django.shortcuts import get_object_or_404, render, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import Paper


# Create your views here.

# Home page
class HomeView(ListView):
    model = Paper
    template_name = "home.html"
    ordering = ["-date"] # Orders the list of posts by date reversed

# Template for individual newspapers
class PaperView(DetailView):
    model = Paper
    template_name = "paper.html"

# About page
class AboutView(TemplateView):
    template_name = "about.html"

# Archive page
class ArchiveView(ListView):
    model = Paper
    template_name = "archive.html"
    ordering = ["date"]

