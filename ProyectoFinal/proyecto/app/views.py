from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

