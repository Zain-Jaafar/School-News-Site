# Generated by Django 5.0.6 on 2024-06-13 22:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_alter_paper_content_alter_paper_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="paper",
            name="date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]