# Generated by Django 3.0.5 on 2020-04-12 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Location')),
                ('show_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Show')),
            ],
            options={
                'verbose_name': 'Representation',
                'verbose_name_plural': 'Representations',
            },
        ),
    ]
