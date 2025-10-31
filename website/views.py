from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Import para a nova view
from .validators import validar_cnpj_api
from django.http import JsonResponse


def home(request):
    records = Record.objects.all()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Autenticação
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Você está logado!")
            return redirect('home')
        else:
            messages.success(request, "Ocorreu um erro durante a autenticação, tente novamente!")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "Você foi deslogado com sucesso!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Autenticação e login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Você foi registrado com sucesso!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "Você precisa estar logado para acessar essa pagina")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Registro de cliente deletado com sucesso!")
        return redirect('home')
    else:
        messages.success(request, "Voce precisa estar logado para deletar um cliente!")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Registro de Cliente Adicionado")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "Voce precisa estar logado para adicionar um Cliente")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "O Registro foi Alterado com Sucesso!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "Voce precisa estar logado para atualizar um Cliente")
        return redirect('home')


# NOVA VIEW: Consulta automática do CNPJ
def consulta_cnpj(request):
    """
    Recebe o CNPJ via GET e retorna os dados do cliente em JSON
    """
    cnpj = request.GET.get('cnpj', None)
    if cnpj:
        try:
            dados = validar_cnpj_api(cnpj)
            return JsonResponse({
                'razao_social': dados.get('nome', ''),
                'nome_fantasia': dados.get('fantasia', ''),
                'inscricao_estadual': dados.get('ie', ''),
                'inscricao_municipal': dados.get('im', ''),
                'cep': dados.get('cep', ''),
                'logradouro': dados.get('logradouro', ''),
                'complemento': dados.get('complemento', ''),
                'bairro': dados.get('bairro', ''),
                'municipio': dados.get('municipio', ''),
                'uf': dados.get('uf', '')
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'CNPJ não informado'})
