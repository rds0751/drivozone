# Generated by Django 2.1 on 2019-09-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20190911_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Vehicle_type',
            field=models.CharField(max_length=20),
        ),
    ]