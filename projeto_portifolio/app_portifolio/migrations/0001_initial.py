# Generated by Django 5.1.3 on 2024-11-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
