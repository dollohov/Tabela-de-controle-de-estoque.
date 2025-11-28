from django.shortcuts import render, redirect, get_object_or_404  # type: ignore # Remover a duplicação de 'redirect'
from .models import Produto
from .forms import ProdutoForm


def tabela(request):
    produtos = Produto.objects.all()  # Recupera todos os produtos
    return render(request, 'estoque/tabela.html', {'produtos': produtos})

def cadastrar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo produto
            return redirect('tabela')  # Redireciona para a página de produtos após salvar
    else:
        form = ProdutoForm()  # Formulário vazio se o método for GET
    return render(request, 'estoque/cadastrar.html', {'form': form})

def editar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)  # Recupera o produto pelo ID
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)  # Preenche o formulário com os dados do produto existente
        if form.is_valid():
            form.save()  # Salva as alterações no banco de dados
            return redirect('tabela')  # Redireciona para a tabela de produtos após salvar
    else:
        form = ProdutoForm(instance=produto)  # Preenche o formulário com os dados do produto
    return render(request, 'estoque/editar.html', {'form': form, 'produto': produto})

def excluir(request, pk):
    produto = get_object_or_404(Produto, pk=pk)  # Recupera o produto pelo ID
    if request.method == 'POST':
        produto.delete()  # Deleta o produto do banco de dados
        return redirect('tabela')  # Redireciona para a tabela de produtos após a exclusão
    return render(request, 'estoque/excluir.html', {'produto': produto})  # Exibe a página de confirmação de exclusão

