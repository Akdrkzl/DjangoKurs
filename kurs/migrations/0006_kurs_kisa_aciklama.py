# Generated by Django 4.2.5 on 2023-09-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurs', '0005_kurs_resim'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurs',
            name='kisa_aciklama',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
