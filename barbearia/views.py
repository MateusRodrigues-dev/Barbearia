from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ClienteForm()

    return render(request, 'cliente_form.html', {'form': form})


def lista_clientes(request):
    clientes = Cliente.objects.all()

    return render(
        request,
        'clientes.html',
        {'clientes': clientes}
    )


def detalhe_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    return render(
        request,
        'cliente_detalhes.html',
        {'cliente': cliente}
    )

@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect('cliente_detalhes', id=cliente.id)

    else:
        form = ClienteForm(instance=cliente)

    return render(
        request,
        'cliente_form.html',
        {
            'form': form,
            'editar': True,
            'cliente': cliente
        }
    )

@login_required
def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')

    return render(
        request,
        'cliente_confirmar_exclusao.html',
        {'cliente': cliente}
    )