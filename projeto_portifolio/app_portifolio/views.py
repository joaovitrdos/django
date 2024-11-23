from django.shortcuts import render
from models import Usuario

def home(request):
    return render(request,'portifolio/home.html')

def usuario(request):
    #Salvar o dados da tela 
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir todos os Usuarios ja cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os dados para a pagina
    return render(request, 'usuarios/usuarios.html', usuarios)