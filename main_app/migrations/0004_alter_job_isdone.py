# Generated by Django 4.1.3 on 2022-11-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_contractor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]
