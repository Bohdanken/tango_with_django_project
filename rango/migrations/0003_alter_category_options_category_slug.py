# Generated by Django 4.2.6 on 2024-02-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rango", "0002_alter_category_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "categories"},
        ),
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
