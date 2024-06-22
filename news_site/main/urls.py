from django.urls import path
from .views import HomeView, PaperView, AboutView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("paper/<int:pk>", PaperView.as_view(), name="paper-detail"),
    path("about", AboutView.as_view(), name="about")
]