# Generated by Django 2.0.1 on 2018-02-06 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0008_auto_20180130_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webgallery',
            name='mobile_img_url',
        ),
    ]
