# Generated by Django 2.2.7 on 2019-11-28 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PROGRAMAINDIVIDUALIZADO', '0004_auto_20191128_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informe',
            name='nombre',
            field=models.CharField(blank=True, default='dfsdf', max_length=50, null=True, verbose_name='Nombre'),
        ),
    ]
