# Generated by Django 2.1 on 2019-09-11 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='bedrooms',
            new_name='Vehicle_type',
        ),
    ]