# Generated by Django 2.0.1 on 2018-03-02 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0015_auto_20180302_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailSubscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
