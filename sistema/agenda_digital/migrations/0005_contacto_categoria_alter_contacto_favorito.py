# Generated by Django 5.0.4 on 2024-05-18 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda_digital', '0004_alter_usuario_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='categoria',
            field=models.CharField(max_length=60, null=True, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='favorito',
            field=models.BooleanField(default=False, verbose_name='Favorito'),
        ),
    ]
