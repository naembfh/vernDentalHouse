# Generated by Django 4.2.3 on 2023-10-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_consultation'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='isConsultate',
            field=models.BooleanField(default=False),
        ),
    ]
