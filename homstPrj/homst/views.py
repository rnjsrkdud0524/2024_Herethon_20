from django.shortcuts import render, redirect, get_object_or_404
from .models import SearchRecord, SafetyFilter, Accommodation, Post
from .forms import SearchRecordForm, PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    form = SearchRecordForm()
    safety_filters = SafetyFilter.objects.all()
    return render(request, 'homst/main.html', {'form': form, 'safety_filters': safety_filters})

def mypage(request):
    return render(request, 'homst/mypage.html')

def search_results(request):
    if request.method == 'GET':
        form = SearchRecordForm(request.GET)
        if form.is_valid():
            destination = form.cleaned_data['destination']
            travel_date = form.cleaned_data['travel_date']
            travel_date2 = form.cleaned_data['travel_date2']
            people = form.cleaned_data['people']
            safety_filters_ids = request.GET.getlist('safety_filter')
            safety_filters = SafetyFilter.objects.filter(id__in=safety_filters_ids)
            sort_by = request.GET.get('sort_by', '')

            accommodations = Accommodation.objects.filter(
            location__icontains=destination,
            safety_filters__in=safety_filters
            ).distinct()

            sort_by = request.GET.get('sort_by')
            if sort_by == 'price_asc':
                accommodations = accommodations.order_by('price')
            elif sort_by == 'price_desc':
                accommodations = accommodations.order_by('-price')
            elif sort_by == 'rating_asc':
                accommodations = accommodations.order_by('review_score')
            elif sort_by == 'rating_desc':
                accommodations = accommodations.order_by('-review_score')


            search_results_count = accommodations.count()

            return render(request, 'homst/search_results.html', {
                'accommodations': accommodations,
                'search_results_count': search_results_count,
                'destination': destination,
                'travel_date': travel_date,
                'travel_date2': travel_date2,
                'people': people,
                'safety_filters': safety_filters,
                'form':form,
                'sort_by': sort_by
            })
    
    else:
        form = SearchRecordForm()

    safety_filters = SafetyFilter.objects.all()
    return render(request, 'homst/main.html', {'form': form, 'safety_filters': safety_filters})
        
def record_detail(request, record_id):
    accommodation = get_object_or_404(Accommodation, id=record_id)
    context = {
        'accommodation': accommodation,
    }
    return render(request, 'homst/record_detail.html', context)

def community(request):
    posts = Post.objects.all()
    return render(request, 'homst/community.html', {'posts': posts})

@login_required
def community_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community')
    else:
        form = PostForm()
    return render(request, 'homst/community_create.html', {'form': form})

def community_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'homst/community_detail.html', {'post': post})

def community_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'homst/community_update.html', {'form': form, 'post': post})

def community_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('community')
    return render(request, 'homst/community_delete.html', {'post': post})