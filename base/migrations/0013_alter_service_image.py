# Generated by Django 4.2.1 on 2023-05-23 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default='base\x0ciles\\images\\Logo_SRAD.png', upload_to='base/files/images'),
        ),
    ]