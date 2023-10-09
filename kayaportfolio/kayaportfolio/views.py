from django.shortcuts import render

def landingpage_view(request):
    return render(request, 'kayaportfolio/index.html')

def pos_details_view(request):
    return render(request, 'kayaportfolio/templates/kayaportfolio/pos-details.html')