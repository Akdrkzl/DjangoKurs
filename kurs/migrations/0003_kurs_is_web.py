# Generated by Django 4.2.5 on 2023-09-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurs', '0002_kurs'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurs',
            name='is_web',
            field=models.BooleanField(default=False),
        ),
    ]
