# Generated by Django 2.1 on 2019-09-13 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-submit_date',), 'permissions': [('can_moderate', 'Can moderate reviews')], 'verbose_name': 'review', 'verbose_name_plural': 'reviews'},
        ),
    ]
