# Generated by Django 4.0.4 on 2022-06-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housework', '0003_remove_housework_update_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='housework',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
    ]
