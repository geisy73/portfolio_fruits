from rest_framework import serializers
#from app.diseases.models import Composition
#from app.diseases.models import Element
from diseases.models import DiseaseF, Element, Composition, Fruit_Element, Fruit, Disease_Element


class DiseaseFSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseF
        fields = ('id','name', 'descrip')
        
class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ('id','name', 'composition_id', 'um')

class CompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model: Composition
        fields = ('id', 'compound_name')

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ('id','name', 'scientific_name', 'water_percent')

class Fruit_ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit_Element
        fields = ('id','amount', 'element_id','fruit_id', 'amountg')

class Disease_ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease_Element
        fields = ('id','element_id', 'disease_id')