from django.urls import path, include  # Importe les fonctions pour définir les URLs
from rest_framework.routers import DefaultRouter  # Importe le routeur de DRF
from .views import ItemViewSet  # Importe la vue ItemViewSet

router = DefaultRouter()  # Crée un routeur par défaut
router.register(r'items', ItemViewSet)  # Enregistre la vue ItemViewSet avec l'URL 'items'

urlpatterns = [
    path('', include(router.urls)),  # Inclut les URLs générées par le routeur
]