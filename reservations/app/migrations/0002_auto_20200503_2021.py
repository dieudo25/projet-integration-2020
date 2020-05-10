# Generated by Django 3.0.5 on 2020-05-03 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='show',
            options={'ordering': ['-date_created'], 'verbose_name': 'Spectacle', 'verbose_name_plural': 'Spectacles'},
        ),
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(default='empty str'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.CharField(choices=[('EN', 'Anglais'), ('FR', 'Français'), ('NL', 'Néerlandais'), ('GE', 'Allemand'), ('SP', 'Espagnol'), ('IT', 'Italien'), ('PO', 'Portugais')], max_length=2),
        ),
    ]