from django.db import models


class Empresa(models.Model):
    razaoSocial = models.CharField(max_length=100, help_text='Nome da Empresa')

    def __str_(self):
        return self.razaoSocial
