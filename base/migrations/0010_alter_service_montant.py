# Generated by Django 3.2.7 on 2023-05-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_service_montant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='montant',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
