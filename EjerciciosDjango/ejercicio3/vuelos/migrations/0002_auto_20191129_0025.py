# Generated by Django 2.2.7 on 2019-11-28 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuelos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserva',
            options={'ordering': ['cliente', 'fecha_reserva'], 'verbose_name': 'Reserva', 'verbose_name_plural': 'Reservas'},
        ),
    ]
