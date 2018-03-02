# Generated by Django 2.0.1 on 2018-01-30 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_whyjovinx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimony',
            old_name='company',
            new_name='company_or_business',
        ),
        migrations.AddField(
            model_name='testimony',
            name='city',
            field=models.CharField(default='Lagos', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimony',
            name='job_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='whyjovinx',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
