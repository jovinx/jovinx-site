# Generated by Django 2.0.1 on 2018-02-07 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0009_remove_webgallery_mobile_img_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graphicsgallery',
            old_name='large_img_url',
            new_name='img_url',
        ),
        migrations.RemoveField(
            model_name='graphicsgallery',
            name='small_img_url',
        ),
    ]