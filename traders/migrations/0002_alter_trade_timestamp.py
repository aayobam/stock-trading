# Generated by Django 4.0.2 on 2023-05-19 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='timestamp',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
