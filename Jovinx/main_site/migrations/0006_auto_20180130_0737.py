# Generated by Django 2.0.1 on 2018-01-30 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0005_auto_20180130_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimony',
            name='company_or_business',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='job_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='thumbnail_url',
            field=models.ImageField(blank=True, upload_to='testimonies/thumbnails/'),
        ),
    ]
