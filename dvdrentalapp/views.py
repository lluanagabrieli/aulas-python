from django.utils import timezone
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Address, Category, Customer, City, Language, Payment, Rental
from django.shortcuts import render, get_object_or_404, redirect

def customer(request):
    mycustomers = Customer.objects.all().values()
    template = loader.get_template('all_customers.html')
    context = {
        'mycustomer': mycustomers,
    }
    return HttpResponse(template.render(context, request))

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk = customer_id)
    if request.method == 'POST':
        customer.first_name = request.POST.get('first_name')
        customer.last_name = request.POST.get('last_name')
        customer.email = request.POST.get('email')
        customer.save()
        
        return redirect('/customer')
    return render(request, 'edit_customer.html', { 'customer': customer })
   
def detalhes(request, id):
    myDetalhes = Rental.objects.filter(customer_id = id)
    customer = get_object_or_404(Customer, pk = id)
    template = loader.get_template('detalhes.html')
    context = {
        'myDetalhe': myDetalhes,
        'customer_name': f"{customer.first_name} {customer.last_name}",
    }
    return HttpResponse(template.render(context, request))

# CATEGORIAS
def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'list_categories.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        # Cria uma instância do modelo Category e salva no banco
        category = Category(name=name, last_update=timezone.now())
        category.save()

        # Redireciona para a lista de categorias após a inserção ou onde preferir
        return redirect('/categories') # Substitua 'category_list' pela URL desejada
    
    # Se não for um POST request, exibe o formulário vazio
    return render(request, 'add_category.html')

# ************************************************************************************************************
# DESAFIO - LISTAR E EDITAR CIDADES
def cidade(request):
    minhasCidades = City.objects.all().values()
    template = loader.get_template('all_cidades.html')
    context = {
        'minhaCidade': minhasCidades,
    }
    return HttpResponse(template.render(context, request))

def edit_cidade(request, city_id):
    cidade = get_object_or_404(City, pk=city_id)
    if request.method == 'POST':
        cidade.city = request.POST.get('city')
        cidade.country = request.POST.get('country')

        cidade.save()
        return redirect('/cidade')
    return render(request, 'edit_city.html', {'cidade': cidade})


# DESAFIO - LISTAR E ADICIONAR LINGUAGENS
def listar_linguagens(request):
    linguagens = Language.objects.all()
    return render(request, 'desafio_listar_linguagem.html', {'linguagens': linguagens})

def adicionar_linguagem(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        linguagem = Language(name=name, last_update=timezone.now())
        linguagem.save()

        return redirect('/linguagens')
    return render(request, 'desafio_adicionar.html')

# ATIVIDADE
def home(request):
    meusClientes = Customer.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'meusClientes': meusClientes,
    }
    return HttpResponse(template.render(context, request))

def clientes(request):
    meusClientes = Customer.objects.all().values()
    template = loader.get_template('listar_clientes.html')
    context = {
        'meusClientes': meusClientes,
    }
    return HttpResponse(template.render(context, request))

def endereco(request, id):
    meuEndereco = Address.objects.filter(address_id = id)
    template = loader.get_template('endereco.html')
    context = {
        'meuEndereco': meuEndereco,
    }
    return HttpResponse(template.render(context, request))

def pagamento(request, id):
    meuPagamento = Payment.objects.filter(customer = id)
    template = loader.get_template('pagamentos.html')
    context = {
        'meuPagamento': meuPagamento,
    }
    return HttpResponse(template.render(context, request))

# AULA 27 - QUERYSET
# contains: registros que iniciam com o valor especifico (é caseSensitive) - WHERE first_name LIKE 'Ka%'
# icontains: nao é caseSensitive (qualquer parte da palavra) - WHERE last_name LIKE '%Mill%

# endswith: registros que terminam com o valor (é case) - WHERE first_name LIKE '%s'
# iendswith: registros que terminam com o valor (não é case)
    
# exact: registro com o valor exato/específico (é case) - WHERE first_name = 'Phyllis'
# iexact: não é case - WHERE first_name = 'phyllis'

# in: registros que sejam um dos valores de um interável (é case) - WHERE first_name IN ( ‘Phyllis’, 'Dennis’)

# gt: maior que - WHERE customer_id > 500
# gte: maior ou igual que - WHERE customer_id >= 500
# lt: menor que - WHERE customer_id < 500
# lte: menor ou igual a - WHERE customer_id <= 500
def listacustomer(request):
    mycustomers = Customer.objects.filter(customer_id__lt=500).values()

    template = loader.get_template('list_customer.html')
    context = {
        'listCustomer': mycustomers,
    }
    return HttpResponse(template.render(context, request))