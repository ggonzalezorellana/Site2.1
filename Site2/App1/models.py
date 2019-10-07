from django.db import models

# Create your models here.


class Animal(models.Model):
    INJ = 'INJ'
    PCOM = 'PCOM'
    COM = 'COM'
    REP = 'REP'
    PAMA = 'PAMA'
    AMA = 'AMA'

    STAGES = [
        ('INJ', 'Lesionado'),
        ('PCOM', 'Pre-Competitivo'),
        ('COM', 'Competitivo'),
        ('REP', 'Reproductivo'),
        ('PAMA', 'Pre-Amansa'),
        ('AMA', 'Amansa'),
    ]

    nro = models.IntegerField()
    name = models.CharField(max_length=100, null=True)
    birth = models.DateField('Fecha Nacimiento')
    color = models.CharField(max_length=40)
    stage = models.CharField(
        max_length=4,
        choices=STAGES,
        default=COM
    )

    def __str__(self):
        return '%s, Nro: %s, Color: %s, Estado %s.' % (self.name, self.nro, self.color, self.stage)