# Generated by Django 4.1.7 on 2023-03-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lotus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mod', models.CharField(max_length=100)),
                ('desc_mod', models.CharField(max_length=2000)),
                ('cant_recursos', models.PositiveIntegerField(blank=True, null=True)),
                ('cant_temas', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
