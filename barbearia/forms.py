from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = [
            'nome',
            'telefone',
            'email',
            'barbeiro',
            'observacoes'
        ]

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o nome do cliente'
                }
            ),

            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '(00) 00000-0000'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'cliente@email.com'
                }
            ),

            'barbeiro': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome do barbeiro'
                }
            ),

            'observacoes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite alguma observação...',
                    'rows': 4
                }
            ),
        }