from django.shortcuts import render

def landingpage_view(request):
    return render(request, 'kayaportfolio/index.html')