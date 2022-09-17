from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

from typing import Optional


class HomePageView(ListView):
    model: Optional[object] = Post
    template_name: str = 'home.html'
