# Generated by Django 3.2.9 on 2021-12-03 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20211203_2131'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='topic',
            new_name='category',
        ),
    ]
