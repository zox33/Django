# Generated by Django 2.2.7 on 2019-11-28 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191128_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='categoria_padre',
        ),
        migrations.AddField(
            model_name='categoria',
            name='categoria_padre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Categorias', to='catalog.Categoria'),
        ),
    ]
