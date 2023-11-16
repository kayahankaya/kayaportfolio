from django.shortcuts import render

def landingpage_view(request):
    return render(request, 'kayaportfolio/index.html')

def sample_view(request):
    return render(request, 'kayaportfolio/sample.html')
