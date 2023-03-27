from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Etat:
    EN_ATTENTE = 1
    ACCEPTEE = 2
    TERMINEE = 3
    ANNULEE = 4

    CHOICES = (
        (EN_ATTENTE, 'En_attente'),
        (ACCEPTEE, 'Acceptee'),
        (TERMINEE, 'Terminee'),
        (ANNULEE, 'Annulee')
    )


class User(AbstractUser):
    UTILISATEUR = 1
    PROFESSIONNEL = 2

    ROLE_CHOICES = (
        (UTILISATEUR, 'Utilisateur'),
        (PROFESSIONNEL, 'Professionnel'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)


class Service(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return '%s' % self.nom


class ProfessionnelService(models.Model):
    taux_horaire = models.FloatField()
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.service_id.nom


class Soumission(models.Model):
    date_planification = models.DateField(default=timezone.now)
    date_terminee = models.DateField()
    description = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    professionnel_service_id = models.ForeignKey(ProfessionnelService, on_delete=models.CASCADE)
    etat = models.PositiveSmallIntegerField(choices=Etat.CHOICES, blank=True, null=True)

    def __str__(self):
        return f'{self.professionnel_service_id.service_id.nom}'
