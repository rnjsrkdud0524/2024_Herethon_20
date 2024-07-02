from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def community(request):
    posts = Post.objects.all()
    return render(request, 'community/community.html', {'posts': posts})