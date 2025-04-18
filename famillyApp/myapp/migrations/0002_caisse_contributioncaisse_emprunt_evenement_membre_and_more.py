# Generated by Django 5.1.7 on 2025-04-11 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caisse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type_caisse', models.CharField(choices=[('epargne_obligatoire', 'Épargne obligatoire'), ('collation', 'Collation'), ('grand_cahier', 'Grand cahier'), ('emprunt', 'Emprunt')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ContributionCaisse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_contribution', models.DateTimeField(auto_now_add=True)),
                ('caisse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.caisse')),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_emprunt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('taux_interet', models.DecimalField(decimal_places=2, default=5, max_digits=5)),
                ('duree_remboursement', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_event', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_evenement', models.DateTimeField()),
                ('statut_event', models.CharField(choices=[('en_cours', 'En cours'), ('termine', 'Terminé'), ('annule', 'Annulé')], default='en_cours', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('ville', models.CharField(blank=True, max_length=20, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('actif', 'Actif'), ('inactif', 'Inactif')], default='actif', max_length=10)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipationEvenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_part', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_contribution', models.DateTimeField(auto_now_add=True)),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.evenement')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.membre')),
            ],
        ),
        migrations.CreateModel(
            name='Remboursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_rembourse', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_remboursement', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lieu', models.CharField(max_length=255)),
                ('date_reunion', models.DateTimeField()),
                ('nombre_participants', models.IntegerField(default=0)),
                ('montant_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='emprunt',
            name='membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.membre'),
        ),
        migrations.AddField(
            model_name='contributioncaisse',
            name='membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.membre'),
        ),
        migrations.AddField(
            model_name='remboursement',
            name='emprunt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.emprunt'),
        ),
    ]
