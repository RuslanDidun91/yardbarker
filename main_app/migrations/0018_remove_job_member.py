# Generated by Django 4.1.3 on 2022-11-29 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_remove_member_id_alter_member_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='member',
        ),
    ]