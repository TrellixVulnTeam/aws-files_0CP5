# Generated by Django 3.0 on 2020-03-11 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0002_auto_20200311_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='box_office_collecctions_in_crores',
            new_name='box_office_collections_in_crores',
        ),
    ]
