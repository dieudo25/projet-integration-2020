# Generated by Django 3.0.5 on 2020-05-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200524_1815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['-status', '-time'], 'verbose_name': 'Réservation', 'verbose_name_plural': 'Réservations'},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de réservation'),
        ),
    ]
