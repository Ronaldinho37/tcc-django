# Generated by Django 5.0.6 on 2024-08-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicativo', '0005_professores_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='admins',
            name='imagem',
            field=models.FileField(null=True, upload_to='imagem_admins'),
        ),
    ]
