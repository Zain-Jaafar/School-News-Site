from django.shortcuts import get_object_or_404, render, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import Paper


# Create your views here.

class HomeView(ListView):
    model = Paper
    template_name = "home.html"

class PaperView(DetailView):
    model = Paper
    template_name = "paper.html"

class AboutView(TemplateView):
    template_name = "about.html"


# def render_items(request, item_name):
#     item = get_object_or_404(Paper, content=item_name)
#     return render(request, 'paper.html', {'item': item })