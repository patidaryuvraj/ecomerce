# Generated by Django 3.2.18 on 2023-03-20 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderupdate',
            old_name='timetamp',
            new_name='timestamp',
        ),
    ]
