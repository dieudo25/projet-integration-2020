# Generated by Django 3.0.4 on 2020-04-05 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200405_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=60, unique=True)),
                ('designation', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('locality_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Locality')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
                'db_table': 'locations',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
