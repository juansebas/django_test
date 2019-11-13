from django.contrib import admin
from gestion_pedidos.models import Client, Article, Order


admin.site.register(Order)
admin.site.register(Article)
admin.site.register(Client)