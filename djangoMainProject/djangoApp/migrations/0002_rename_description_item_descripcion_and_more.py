# Generated by Django 5.1.2 on 2024-10-08 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='description',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='nombre',
        ),
        migrations.AddField(
            model_name='item',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
