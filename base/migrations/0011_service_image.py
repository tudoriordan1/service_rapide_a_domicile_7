# Generated by Django 4.2.1 on 2023-05-22 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_service_montant'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='images\\Logo_SRAD.png', upload_to='files/images'),
        ),
    ]
