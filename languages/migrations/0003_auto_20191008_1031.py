# Generated by Django 2.2.4 on 2019-10-08 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_auto_20191008_1014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paradigm',
            old_name='paradigm',
            new_name='name',
        ),
    ]
