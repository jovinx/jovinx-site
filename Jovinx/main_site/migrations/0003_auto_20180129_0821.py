# Generated by Django 2.0.1 on 2018-01-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_auto_20180129_0653'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SiteGallery',
            new_name='WebGallery',
        ),
        migrations.AlterField(
            model_name='artgallery',
            name='category',
            field=models.CharField(choices=[('Pen Art', 'Pen Art'), ('Pencil Art', 'Pencil Art'), ('Painting', 'Painting')], max_length=50),
        ),
        migrations.AlterField(
            model_name='graphicsgallery',
            name='category',
            field=models.CharField(choices=[('Logo', 'Logo'), ('Banner', 'Banner'), ('Flyer', 'Flyer'), ('Book Cover', 'Book Cover'), ('Ticket', 'Ticket'), ('Business Card', 'Business Card'), ('Frame', 'Frame'), ('Invitation Card', 'Invitation Card'), ('Poster', 'Poster')], max_length=50),
        ),
        migrations.AlterField(
            model_name='illustrationgallery',
            name='category',
            field=models.CharField(choices=[('Technical', 'Technical'), ('Scientific', 'Scientific'), ('Medical', 'Medical'), ('Book', 'Book'), ('Children', 'Children'), ('Comic', 'Comic'), ('Publication', 'Publication'), ('Advertisment', 'Advertisment'), ('Product', 'Product'), ('Teaching', 'Teaching'), ('Charts', 'Charts')], max_length=50),
        ),
        migrations.AlterField(
            model_name='motiongraphicsgallery',
            name='category',
            field=models.CharField(choices=[('Educational', 'Educational'), ('Cartoon', 'Cartoon'), ('Advertisment', 'Advertisment')], max_length=50),
        ),
    ]