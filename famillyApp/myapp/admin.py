# admin.py
from django.contrib import admin
from .models import Membre, Evenement, Caisse, ParticipationEvenement, Emprunt, Remboursement, Reunion,ContributionCaisse

admin.site.register(Membre)
admin.site.register(Evenement)
admin.site.register(Caisse)
admin.site.register(ParticipationEvenement)
admin.site.register(Emprunt)
admin.site.register(Remboursement)
admin.site.register(Reunion)
admin.site.register(ContributionCaisse)
