# Generated by Django 4.0.6 on 2022-07-28 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fam', '0003_alter_family_birthday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family',
            old_name='phone',
            new_name='age',
        ),
    ]
