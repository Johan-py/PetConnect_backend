# Generated by Django 5.2.4 on 2025-07-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mascota', models.CharField(editable=False, max_length=32, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('especie', models.CharField(max_length=50)),
            ],
        ),
    ]
