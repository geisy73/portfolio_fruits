from django.contrib import admin

# Register your models here.

from .models import Customer, DiseaseF, Fruit, Element, Fruit_Element, Customer_Disease, Composition, Disease_Element, Customer

admin.site.register(DiseaseF)
admin.site.register(Fruit)
admin.site.register(Element)
admin.site.register(Fruit_Element)
admin.site.register(Customer_Disease)
admin.site.register(Composition)
admin.site.register(Disease_Element)
admin.site.register(Customer)


