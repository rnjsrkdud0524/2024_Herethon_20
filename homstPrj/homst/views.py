from django.shortcuts import render, redirect, get_object_or_404
from .models import SearchRecord, SafetyFilter
from .forms import SearchRecordForm

# Create your views here.

def main(request):
    form = SearchRecordForm()
    safety_filters = SafetyFilter.objects.all()
    return render(request, 'homst/main.html', {'form': form, 'safety_filters': safety_filters})

def community(request):
    return render(request, 'homst/community.html')

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

            
            search_results = SearchRecord.objects.filter(
                destination=destination,
                travel_date=travel_date,
                travel_date2=travel_date2,
                people=people,
                safety_filter__in=safety_filters
            ).distinct()
            
            search_results_count = search_results.count()

            return render(request, 'homst/search_results.html', {
                'search_results': search_results,
                'search_results_count': search_results_count,
                'destination': destination,
                'travel_date': travel_date,
                'travel_date2': travel_date2,
                'people': people,
                'safety_filters': safety_filters
            })
    
    else:
        form = SearchRecordForm()

    safety_filters = SafetyFilter.objects.all()
    return render(request, 'homst/main.html', {'form': form, 'safety_filters': safety_filters})
        
def record_detail(request, record_id):
    record = get_object_or_404(SearchRecord, id=record_id)
    context = {
        'record': record,
    }
    return render(request, 'homst/record_detail.html', context)