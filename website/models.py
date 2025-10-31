from django.db import models
from .validators import validar_cnpj_api


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	razao_social = models.CharField(max_length=150)         
	nome_fantasia = models.CharField(max_length=100)        
	cnpj = models.CharField(max_length=18, validators=[validar_cnpj_api])                  
	inscricao_estadual = models.CharField(max_length=20, blank=True, null=True)
	inscricao_municipal = models.CharField(max_length=20, blank=True, null=True)
	cep = models.CharField(max_length=9)                    
	logradouro = models.CharField(max_length=120)           
	complemento = models.CharField(max_length=50, blank=True, null=True)
	bairro = models.CharField(max_length=60)
	municipio = models.CharField(max_length=80)
	uf = models.CharField(max_length=2)                    
	email = models.CharField(max_length=120)
	telefone_fixo = models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.razao_social}")
