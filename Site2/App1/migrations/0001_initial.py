# Generated by Django 2.2.5 on 2019-09-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro', models.IntegerField()),
                ('birth', models.DateField(verbose_name='Fecha Nacimiento')),
                ('color', models.CharField(max_length=40)),
                ('stage', models.CharField(choices=[('INJ', 'Lesionado'), ('PCOM', 'Pre-Competitivo'), ('COM', 'Competitivo'), ('REP', 'Reproductivo'), ('PAMA', 'Pre-Amansa'), ('AMA', 'Amansa')], default='COM', max_length=4)),
            ],
        ),
    ]
