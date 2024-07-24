from django.urls import path, include
from .views import HomeView, PaperView, AboutView, ArchiveView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("paper/<slug:slug>", PaperView.as_view(), name="paper-detail"),
    path("about", AboutView.as_view(), name="about"),
    path("archive", ArchiveView.as_view(), name="archive"),
    path('tinymce/', include('tinymce.urls')),
]