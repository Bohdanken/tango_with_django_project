# Generated by Django 4.2.6 on 2024-02-06 11:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rango", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]