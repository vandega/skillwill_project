# Generated by Django 4.2.5 on 2023-09-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dealership", "0004_alter_car_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="picture",
            field=models.ImageField(blank=True, null=True, upload_to="car_pictures/"),
        ),
    ]