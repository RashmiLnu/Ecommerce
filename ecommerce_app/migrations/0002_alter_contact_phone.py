# Generated by Django 5.0.1 on 2024-04-10 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.IntegerField(),
        ),
    ]