
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from contactos.forms import  UserRegisterForm

# login

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("pasword")
            
            user = authenticate(username = usuario, password = contra)
            
            if user is not None:
                login(request, user)

                return render (request, "app/home.html", {"mensaje": f"acceso total {usuario}"})    
                
            else:

                return render (request, "app/home.html", {"mensaje": "Error en los datos"})
        else:

            return render (request, "app/home.html", {"mensaje": "Formulario erroneo"} )
        
    form = AuthenticationForm()
        
    return render(request, "contactos/contactos.html", {"form": form})
    
#registro
def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, "app/home.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "contactos/registro.html", {"form": form})


