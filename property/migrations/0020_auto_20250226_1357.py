# Generated by Django 2.2.24 on 2025-02-26 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20250225_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_text',
            new_name='text',
        ),
    ]
