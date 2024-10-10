import datetime
from django.shortcuts import redirect, render
from django.contrib import messages

from app.forms import CadastroUsuarioForm

def index(request):
    return render(request,'index.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request,form.errors.as_text())
            return redirect('cadastro')
    else:
        form = CadastroUsuarioForm()
    return render(request,'login/cadastro.html',{'form':form})