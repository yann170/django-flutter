from rest_framework import serializers
from .models import Membre  # Importe le modèle Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membre # Spécifie le modèle à sérialiser
        fields = '__all__'  # Inclut tous les champs du modèle dans le sérialiseur