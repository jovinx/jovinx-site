# Generated by Django 2.0.1 on 2018-01-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0006_auto_20180130_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='JovinxInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('founder', models.CharField(default='John Obi Chinemerem', editable=False, max_length=100)),
                ('company_name', models.CharField(default='Jovinx Creative Company', max_length=50)),
                ('site_url', models.URLField(default='jovinx.com.ng')),
                ('logo_url', models.ImageField(upload_to='logo/')),
                ('history', models.TextField(blank=True)),
                ('official_phone', models.BigIntegerField()),
                ('mobile', models.BigIntegerField()),
                ('whatsapp', models.BigIntegerField()),
                ('official_mail_address', models.EmailField(max_length=254)),
                ('support_mail_address', models.EmailField(max_length=254)),
                ('job_mail_address', models.EmailField(max_length=254)),
                ('headquarters_address', models.TextField()),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('established', models.DateField()),
            ],
        ),
    ]
