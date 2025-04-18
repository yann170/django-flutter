
from rest_framework import viewsets  # Importe les viewsets de DRF
from .models import  Membre # Importe le modèle Item
from .serializers import ItemSerializer  # Importe le sérialiseur ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Membre.objects.all()  # Récupère tous les objets Item de la base de données
    serializer_class = ItemSerializer  # Utilise ItemSerializer pour sérialiser les données