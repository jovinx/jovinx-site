# Generated by Django 2.0.1 on 2018-02-07 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0010_auto_20180207_1256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='illustrationgallery',
            old_name='large_img_url',
            new_name='img_url',
        ),
        migrations.RemoveField(
            model_name='illustrationgallery',
            name='small_img_url',
        ),
    ]
