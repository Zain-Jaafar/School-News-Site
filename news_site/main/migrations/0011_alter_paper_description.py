# Generated by Django 5.0.6 on 2024-07-21 04:59

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0010_alter_paper_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paper",
            name="description",
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]