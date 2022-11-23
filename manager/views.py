from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def rules(request):
    return render(request, 'rules.html')

def characters(request):
    return render(request, 'characters.html')

def contact(request):
    return render(request, 'contact.html')

