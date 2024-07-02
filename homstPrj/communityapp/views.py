from django.shortcuts import render
from .models import Post

# Create your views here.

def community(request):
    return render(request, 'community/community.html')