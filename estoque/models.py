from django.db import models




class Categoria(models.Model):

    titulo = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo
    
class Produto(models.Model):

    nome = models.CharField(max_length=40)
    quantidade = models.FloatField()
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

    def gerar_desconto(self, desconto):
        return self.preco_venda - ((self.preco_venda * desconto) / 100)

    def lucro(self):

        lucro = self.preco_venda - self.preco_compra

        return  (lucro * 100) / self.preco_compra