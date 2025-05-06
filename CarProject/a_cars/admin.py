from django.contrib import admin

# Do app a_cars eu importo o modelo Car. Lembando que Modelo é uma classe que representa uma tabela no banco de dados.
# O Django ORM (Object-Relational Mapping) converte automaticamente os objetos Python em registros de banco de dados e vice-versa.
from a_cars.models import Car,Brand


# Aqui eu configuro o que será exibido no admin do django.
class CarAdmin(admin.ModelAdmin):
  list_display = ('id', 'model', 'brand', 'factory_year', 'mode_year', 'plate', 'value', 'photo')
  search_fields = ('model', 'brand')

class BrandAdmin(admin.ModelAdmin):
  list_display = ('id','name',)
  search_fields = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin) 
