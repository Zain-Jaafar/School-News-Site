# Generated by Django 5.0.6 on 2024-05-26 02:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_article"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="image",
            field=models.ImageField(null=True, upload_to="images/articles/"),
        ),
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(null=True, upload_to="images/categories/"),
        ),
    ]
