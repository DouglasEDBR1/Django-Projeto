from django.db import models
from statics.randomName import RandomName


class Person(models.Model):
      

    first_name = models.CharField(max_length=30, verbose_name='Nome', default=RandomName)
    last_name = models.CharField(max_length=30, verbose_name='Sobrenome')
    age = models.IntegerField(verbose_name='Idade')
    birth_date = models.DateField(verbose_name='Data de Nascimento', blank=False, null=True)
    email = models.EmailField(verbose_name='Email', blank=False, null=True)
    surname = models.CharField(max_length=30, verbose_name='Apelido', blank=True, null=True)
    observation = models.TextField(verbose_name='Observação', blank=True, null=True)
    
   
    class Meta:
       ordering = ['first_name', 'last_name']

    
    