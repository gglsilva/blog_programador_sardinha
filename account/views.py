from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def user_login(request):
    """
    Login de usuario: quando o usuario clica no botão de login, o sistema chama este método Post
                    se o formulario for válido, tenta autenticar o usuario, se o retorno for diferente de None,
                    verifica se o usuario está ativo, se estiver, faz o login do usuario, se não, retorna um erro.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Autenticado com sucesso!')
                else:
                    return HttpResponse('Desculpe, sua conta está desativada.')
            else:
                return HttpResponse('Desculpe, não foi possível autenticar.')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    """
    Dashboard do usuario: quando o usuario está autenticado, o sistema chama este método
    """
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})