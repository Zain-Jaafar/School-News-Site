# Generated by Django 5.0.6 on 2024-07-23 03:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0011_alter_paper_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paper",
            name="description",
            field=models.TextField(max_length=400, null=True),
        ),
    ]
