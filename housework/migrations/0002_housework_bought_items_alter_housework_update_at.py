# Generated by Django 4.0.4 on 2022-05-31 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housework', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='housework',
            name='bought_items',
            field=models.BooleanField(blank=True, null=True, verbose_name='買ったもの'),
        ),
        migrations.AlterField(
            model_name='housework',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='更新日時'),
        ),
    ]
