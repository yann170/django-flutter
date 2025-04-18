# models.py

from django.db import models

# Enum pour le statut de l'événement
class StatutEvent(models.TextChoices):
    EN_COURS = 'en_cours', 'En cours'
    TERMINE = 'termine', 'Terminé'
    ANNULE = 'annule', 'Annulé'


# Modèle pour la table Evenement
class Evenement(models.Model):
    type_event = models.CharField(max_length=100, null=True, blank=True)  # Type d'événement
    description = models.TextField(null=True, blank=True)  # Description de l'événement
    date_evenement = models.DateTimeField()  # Date et heure de l'événement
    statut_event = models.CharField(
        max_length=10,
        choices=StatutEvent.choices,
        default=StatutEvent.EN_COURS  # Statut par défaut (en cours)
    )

    def __str__(self):
        return f"{self.type_event} - {self.date_evenement.strftime('%Y-%m-%d %H:%M:%S')}"


# Modèle pour la table Member
class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    ville = models.CharField(max_length=20, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)  # Date de création du membre
    statut = models.CharField(
        max_length=10,
        choices=[('actif', 'Actif'), ('inactif', 'Inactif')],
        default='actif'
    )
    telephone = models.CharField(max_length=20, null=True, blank=True)  # Téléphone du membre

    def __str__(self):
        return f"{self.prenom} {self.nom}"


# Modèle pour la table Caisse
class Caisse(models.Model):
    TYPE_CAISSE_CHOICES = [
        ('epargne_obligatoire', 'Épargne obligatoire'),
        ('collation', 'Collation'),
        ('grand_cahier', 'Grand cahier'),
        ('emprunt', 'Emprunt'),
    ]

    montant = models.DecimalField(max_digits=10, decimal_places=2)  # Montant de la caisse
    type_caisse = models.CharField(max_length=20, choices=TYPE_CAISSE_CHOICES)

    def __str__(self):
        return f"{self.type_caisse} - {self.montant}"


# Modèle pour la table Participation à un evènement
class ParticipationEvenement(models.Model):
    membre = models.ForeignKey('Membre', on_delete=models.CASCADE)  # Relation avec le membre
    evenement = models.ForeignKey('Evenement', on_delete=models.CASCADE)  # Relation avec l'événement
    montant_part = models.DecimalField(max_digits=10, decimal_places=2)  # Montant de la participation
    date_contribution = models.DateTimeField(auto_now_add=True)  # Date de la participation

    def __str__(self):
        return f"{self.membre} a participé à {self.evenement} pour {self.montant_part} le {self.date_contribution.strftime('%Y-%m-%d %H:%M:%S')}"


# Modèle pour la table Emprunt
class Emprunt(models.Model):
    membre = models.ForeignKey('Membre', on_delete=models.CASCADE)  # Relation avec le membre emprunteur
    montant_emprunt = models.DecimalField(max_digits=10, decimal_places=2)  # Montant de l'emprunt
    taux_interet = models.DecimalField(max_digits=5, decimal_places=2, default=5)  # Taux d'intérêt de l'emprunt
    duree_remboursement = models.IntegerField(default=3)  # Durée du remboursement en mois

    def __str__(self):
        return f"Emprunt de {self.montant_emprunt} par {self.membre} à un taux de {self.taux_interet}%"


# Modèle pour la table Remboursement
class Remboursement(models.Model):
    emprunt = models.ForeignKey('Emprunt', on_delete=models.CASCADE)  # Relation avec l'emprunt
    montant_rembourse = models.DecimalField(max_digits=10, decimal_places=2)  # Montant remboursé
    date_remboursement = models.DateTimeField(auto_now_add=True)  # Date du remboursement

    def __str__(self):
        return f"Remboursement de {self.montant_rembourse} pour l'emprunt {self.emprunt} le {self.date_remboursement.strftime('%Y-%m-%d %H:%M:%S')}"


# Modèle pour la table Contributions aux caisses
class ContributionCaisse(models.Model):
    membre = models.ForeignKey('Membre', on_delete=models.CASCADE)  # Relation avec le membre
    caisse = models.ForeignKey('Caisse', on_delete=models.CASCADE)  # Relation avec la caisse
    montant = models.DecimalField(max_digits=10, decimal_places=2)  # Montant de la contribution
    date_contribution = models.DateTimeField(auto_now_add=True)  # Date de la contribution

    def __str__(self):
        return f"{self.membre} a contribué à la caisse {self.caisse} pour {self.montant} le {self.date_contribution.strftime('%Y-%m-%d %H:%M:%S')}"

# modèle pour ma table réunion
class Reunion(models.Model):
    lieu = models.CharField(max_length=255)  # Lieu de la réunion
    date_reunion = models.DateTimeField()  # Date et heure de la réunion
    nombre_participants = models.IntegerField(default=0)  # Nombre de participants
    montant_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Montant total des caisses
    description = models.TextField(null=True, blank=True)  # Description de la réunion

    def __str__(self):
        return f"Réunion du {self.date_reunion.strftime('%Y-%m-%d %H:%M:%S')} à {self.lieu}"



