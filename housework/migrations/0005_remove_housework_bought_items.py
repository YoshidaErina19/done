# Generated by Django 4.0.4 on 2022-06-24 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housework', '0004_housework_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housework',
            name='bought_items',
        ),
    ]