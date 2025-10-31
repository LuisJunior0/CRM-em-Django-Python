from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Seu melhor Email' }))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Primeiro Nome' }))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sobrenome' }))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Usuário'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Obrigatório. 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser muito semelhante às suas outras informações pessoais.</li><li>Sua senha deve conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser uma senha comum.</li><li>Sua senha não pode ser inteiramente numérica.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Senha'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Digite a mesma senha novamente para verificação.</small></span>'



class AddRecordForm(forms.ModelForm):
	razao_social = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Razão Social", "class": "form-control"}), label="")
	nome_fantasia = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Nome Fantasia", "class": "form-control"}), label="")
	cnpj = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "CNPJ", "class": "form-control"}), label="")
	inscricao_estadual = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Inscrição Estadual (opcional)", "class": "form-control"}), label="")
	inscricao_municipal = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Inscrição Municipal (opcional)", "class": "form-control"}), label="")
	cep = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "CEP", "class": "form-control"}), label="")
	logradouro = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Logradouro", "class": "form-control"}), label="")
	complemento = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Complemento (opcional)", "class": "form-control"}), label="")
	bairro = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Bairro", "class": "form-control"}), label="")
	municipio = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Município", "class": "form-control"}), label="")
	uf = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "UF", "class": "form-control"}), label="")
	email = forms.CharField(required=True, widget=forms.EmailInput(attrs={"placeholder": "E-mail", "class": "form-control"}), label="")
	telefone_fixo = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Telefone Fixo", "class": "form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)