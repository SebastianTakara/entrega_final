from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')
