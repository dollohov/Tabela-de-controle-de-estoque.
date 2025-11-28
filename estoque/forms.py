# estoque/forms.py

from django import forms # type: ignore
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'valor_lote']
