from collections import UserList
from unicodedata import name
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from django.http import HttpResponse
from django.template import loader

from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from diseases.serializers import DiseaseFSerializer, ElementSerializer, CompositionSerializer, Fruit_ElementSerializer, FruitSerializer
from rest_framework.decorators import api_view
from .models import Composition, Customer, Disease_Element, DiseaseF, Element, Fruit, Fruit_Element, User, Customer

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Max, Aggregate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm

from django.contrib.auth.backends import BaseBackend
from django.views import generic

from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


# Create your views here.

def calculated_amoung_in_grams(unit, value):
    Fruit_Element.objects.all()
    fruit=Fruit_Element.objects.filter(element__um=unit, amountg=0)
    for f in fruit:
        f.amountg = f.amount*value
        f.save()
    Fruit_Element.objects.all()


#I'll delete this one
def dis_element(request):
    dis = DiseaseF.objects.all()
    if request.method == 'GET':
        diseases_serializer = DiseaseFSerializer(dis, many=True)
        list = []
        list.append(diseases_serializer.data)
        context = {'diseases': list}
        return render(request, 'dis_element.html', context)

# works
@api_view(['GET'])
def diseases_list(request):
    dis = DiseaseF.objects.all()

    if request.method == 'GET':
        diseases_serializer = DiseaseFSerializer(dis, many=True)
        return JsonResponse(diseases_serializer.data, safe=False)
        
# works
@api_view(['GET'])
def element_list(request):
    ele = Element.objects.all()

    if request.method == 'GET':
        element_serializer = ElementSerializer(ele, many=True)
        return JsonResponse(element_serializer.data, safe=False)

def detail(request, composition_id):
    composition = get_object_or_404(Composition, pk=composition_id)
    return render(request, 'diseases/detail.html', {'composition': composition})

def index_elements(request):
    element_list = Element.objects.order_by('name')
    context = {'element_list': element_list}
    return render(request, 'diseases/index_element.html', context)

def all_fruits_disease(request):
    #.order_by('name')
    dis_list = DiseaseF.objects.all().order_by('name')
    context = {'dis_list': dis_list}
    return render(request, 'diseases/all_fruits_disease.html', context)

def all_fruits_disease_detaill(request, disease_id):
    calculated_amoung_in_grams('g',1)
    calculated_amoung_in_grams('mg',0.001)
    calculated_amoung_in_grams('µg',0.000001)
    
    q=Fruit_Element.objects.values('fruit','fruit__name').annotate(maxamount=Max('amountg')).order_by('-maxamount')         
    list_element=q.filter(element__disease_element__disease=disease_id)
    name_disease = get_object_or_404(DiseaseF, pk=disease_id)
    context = {'list_element': list_element, 'name_disease': name_disease}
    return render(request, 'diseases/all_fruits_disease_detail.html', context)


def detail_element(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    #a = Disease_Element.get_deferred_fields(name)
    return render(request, 'diseases/detail_element.html', {'element': element})

def index_composition(request):
    composition_list = Composition.objects.all()
    context = {'composition_list': composition_list}
    return render(request, 'diseases/index_composition.html', context)

def index_disease(request):
    disease_list = DiseaseF.objects.all().order_by('name')
    context = {'disease_list': disease_list}
    return render(request, 'diseases/index_disease.html', context)

def detail_disease(request,pk):
    dis = get_object_or_404(DiseaseF, pk=pk)
    return render(request, 'diseases/detail_disease.html', {'disease': dis})

def index_fruit(request):
    #.order_by('name')
    fruit_list = Fruit.objects.all().order_by('name')
    context = {'fruit_list': fruit_list}
    return render(request, 'diseases/index_fruit.html', context)

def detail_fruit(request,pk):
    fruit = get_object_or_404(Fruit, pk=pk)
    return render(request, 'diseases/detail_fruit.html', {'fruit': fruit})

def fruit_therapy(request):  
    num_diseases=DiseaseF.objects.all().count()
    num_fruits=Fruit.objects.all().count()
    return render(request,'diseases/fruit_therapy.html', context={'num_diseases':num_diseases,'num_fruits':num_fruits})

def fruit_help(request):
    disease_list = DiseaseF.objects.all().order_by('name')
    context = {'disease_list': disease_list}
    return render(request, 'diseases/fruit_help.html', context)

def detail_disease_help(request,disease_id):
    disi=get_object_or_404(DiseaseF,pk=disease_id)
    return render(request, 'diseases/detail_disease_help.html', {'disease': disi})

def detail_disease_help_element(request,disease_id,element_id):
    elem = get_object_or_404(Element, pk=element_id)
    list_fruit = Fruit_Element.objects.filter(element=element_id)
    return render(request, 'diseases/detail_disease_help_element.html', {'list_fruit': list_fruit, 'elem': elem})

def update_fruit(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    try:
        
        selected_fruit_element = element.fruit_element_set.get(pk=request.POST['fruit_element'])
        amount = selected_fruit_element.amount
        
    except (KeyError, Fruit_Element.DoesNotExist):
        return render(request, 'diseases/update_fruit_detail.html', {
            'element': element,
            'error_message': "You didn't select an element yet."
        })
    else:
        selected_fruit_element.amount = amount
        selected_fruit_element.save()
        return HttpResponseRedirect(reverse('update_fruit_results', args=(element.id,)))
      
def update_fruit_detail(request, element_id):
    return HttpResponse("You're selecting amount for element: %s." % element_id)

def update_fruit_results(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    return render(request, 'diseases/update_fruit_results.html', {'element': element})

class FruitCreate(CreateView):
    model = Fruit
    fields = '__all__'

class FruitUpdate(UpdateView):
    model = Fruit
    fields = ['name','scientific_name','water_percent']

class FruitDelete(DeleteView):
    model = Fruit
    success_url = reverse_lazy('fruit')

class DiseaseCreate(CreateView):
    model = DiseaseF
    fields = '__all__'

class DiseaseUpdate(UpdateView):
    model = DiseaseF
    fields = ['name','descrip']

class DiseaseDelete(DeleteView):
    model = DiseaseF
    success_url = reverse_lazy('disease')

class SettingsBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
