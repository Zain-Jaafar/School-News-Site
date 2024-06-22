# Generated by Django 5.0.6 on 2024-06-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_paper_delete_article_delete_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="paper",
            name="content",
            field=models.FileField(null=True, upload_to="assets/papers/"),
        ),
        migrations.AlterField(
            model_name="paper",
            name="image",
            field=models.ImageField(null=True, upload_to="assets/images/categories/"),
        ),
    ]
