from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models, reset_queries
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Composition(models.Model):
    compound_name = models.CharField(max_length=30, blank=False)
    
    def __str__(self):
        return self.compound_name

class Customer(models.Model):
    name = models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Fruit(models.Model):
    #name = models.CharField(max_length=50, unique=True, blank=False, default='')
    name = models.CharField(max_length=50, unique=True, blank=False)
    scientific_name = models.CharField(max_length=50, null=True, blank=True)
    energy = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)

    def get_absolute_url(self):
        return reverse('detail_fruit', args=[str(self.id)])

    def __str__(self):
        return self.name

class Element(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, default='')
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE)
    um = models.CharField(max_length=4, null=True, blank=True, default='')

    def __str__(self):
        return f'{str(self.name)} {"("} {str(self.um)} {")"}'

class DiseaseF(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, default='')
    descrip = models.TextField(null=True, blank=True, default='')

    def get_absolute_url(self):
        return reverse('detail_disease', args=[str(self.id)])

    def __str__(self):
        return self.name 


class Disease_Element(models.Model):
    disease = models.ForeignKey(DiseaseF, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.disease)} {str(self.element)}'


class Fruit_Element(models.Model):
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True, default=0.00)
    amountg = models.FloatField(null=True, blank=True, default=0.00)
    
    class Meta:
        ordering = ['-amount']

    def __str__(self):
        return f'{str(self.fruit)} {str(self.element)} {str(self.amount)}'


class Customer_Disease(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    disease = models.ForeignKey(DiseaseF, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.customer)} {str(self.disease)}'