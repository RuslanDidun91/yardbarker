# Generated by Django 4.1.3 on 2022-11-23 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_contractor_phone_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]