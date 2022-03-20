from importlib.resources import path
from django.urls import path, re_path, include, reverse_lazy
from . import views
from diseases import views as diseases_views
from django.conf import settings
from django.conf.urls.static import static
from .models import DiseaseF, Element, Composition, Fruit_Element, Fruit
from django.template import loader

urlpatterns = [
    path('', diseases_views.fruit_therapy),
    #In Insomnia
    path('diseases_list/', diseases_views.diseases_list), 
    path('element_list/', diseases_views.element_list),
    #HTTP 
    path('fruit_therapy/', diseases_views.fruit_therapy),
    path('elements/', diseases_views.index_elements, name='element'),
    path('elements/<int:element_id>/', diseases_views.detail_element, name='detail_element'),
    path('compositions/', diseases_views.index_composition, name = 'composition'),
    path('compositions/<int:composition_id>/', diseases_views.detail, name='detail'),
    path('fruit/', diseases_views.index_fruit, name='fruit'),
    path('fruit/<int:pk>/', diseases_views.detail_fruit, name='detail_fruit'),
    path('disease/', diseases_views.index_disease, name='disease'),
    path('disease/<int:pk>/', diseases_views.detail_disease, name='detail_disease'),
    path('fruit_help/', diseases_views.fruit_help, name='fruit_help'),
    path('fruit_help/<int:disease_id>/', diseases_views.detail_disease_help, name='detail_disease_help'),
    path('fruit_help/<int:disease_id>/<int:element_id>/', diseases_views.detail_disease_help_element, name='detail_disease_help_element'),
    path('update/<int:element_id>/', views.update_fruit_detail, name='update_fruit_detail'),
    #using a form directly
    path('update/<int:element_id>/update/', views.update_fruit, name='update_fruit'),
    path('update/<int:element_id>/results/', views.update_fruit_results, name='update_fruit_results'),
    path('fruit/create/', views.FruitCreate.as_view(), name='fruit_create'),
    path('fruit/<int:pk>/update/', views.FruitUpdate.as_view(), name= 'fruit_update'),
    path('fruit/<int:pk>/delete/', views.FruitDelete.as_view(), name='fruit_delete'),
    path('disease/create', views.DiseaseCreate.as_view(), name='disease_create'),
    path('disease/<int:pk>/update/', views.DiseaseUpdate.as_view(), name= 'disease_update'),
    path('disease/<int:pk>/delete/', views.DiseaseDelete.as_view(), name='disease_delete'),
    path('all_fruits_disease/', views.all_fruits_disease, name='all_fruit_disease'),
    path('all_fruits_disease/<int:disease_id>/', views.all_fruits_disease_detaill, name='all_fruit_disease_detail'),
    
] 

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
  

