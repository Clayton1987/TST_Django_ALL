from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=30)
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)  # widget é usado

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        mail = EmailMessage(
            subject="Email enviado pelo sistema django2",
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@django2.com','outro@seuemail.com'],
            headers={'Reply-To': email}
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('__all__')  # todos os campos do modelo
        # fields = ['nome', 'descricao', 'preco', 'estoque', 'imagem']  # apenas os campos especific