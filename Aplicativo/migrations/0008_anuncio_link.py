# Generated by Django 5.1 on 2024-08-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicativo', '0007_eletivas_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='link',
            field=models.URLField(max_length=100, null=True),
        ),
    ]
