# Generated by Django 2.2.24 on 2025-02-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_remove_owner_flats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='flats', to='property.Owner', verbose_name='Владельцы'),
        ),
    ]
