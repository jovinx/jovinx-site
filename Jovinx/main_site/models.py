
from django.db import models
from jsonfield import JSONField

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='services/', unique=True)
    description = models.TextField()
    fontawesome_icon = models.CharField(max_length=25)
    sub_services = JSONField()

    def __str__(self):
        return self.title

class Client(models.Model):
    company_name = models.CharField(max_length=200)
    company_logo_url = models.ImageField(upload_to='clients/', unique=True)

    def __str__(self):
        return self.company_name

class Testimony(models.Model):
    customer_fullname = models.CharField(max_length=100)
    company = models.CharField(max_length=80, null=True)
    testimony = models.TextField(max_length=300)
    thumbnail_url = models.ImageField(upload_to="testimonies/thumbnails/", null=True, unique=True)

    def __str__(self):
        return self.customer_fullname
    
#Galleries
class WebGallery(models.Model):
    site_name = models.CharField(max_length=100)
    site_link = models.URLField(max_length=100)
    mobile_img_url = models.ImageField( upload_to="gallery/site/web/", unique=True)
    web_img_url = models.ImageField( upload_to="gallery/site/mobile/", unique=True)

    def __str__(self):
        return self.site_name

class GraphicsGallery(models.Model):
    GRAPHICS_TYPES = (
        ('Logo', 'Logo'),
        ('Banner', 'Banner'),
        ('Flyer', 'Flyer'),
        ('Book Cover', 'Book Cover'),
        ('Ticket', 'Ticket'),
        ('Business Card', 'Business Card'),
        ('Frame', 'Frame'),
        ('Invitation Card', 'Invitation Card'),
        ('Poster', 'Poster')
    )
    category = models.CharField(max_length=50, choices=GRAPHICS_TYPES)
    small_img_url = models.ImageField(upload_to="gallery/graphics/", unique=True)
    large_img_url = models.ImageField(upload_to="gallery/graphics/", unique=True)

    def __str__(self):
        return self.category

class IllustrationGallery(models.Model):

    ILLUSTRATION_TYPES = (
        ('Technical','Technical'),
        ('Scientific', 'Scientific'),
        ('Medical', 'Medical'),
        ('Book', 'Book'),
        ('Children', 'Children'),
        ('Comic', 'Comic'),
        ('Publication', 'Publication'),
        ('Advertisment', 'Advertisment'),
        ('Product', 'Product'),
        ('Teaching', 'Teaching'),
        ('Charts', 'Charts')
    )
    
    category = models.CharField(max_length=50, choices=ILLUSTRATION_TYPES)
    small_img_url = models.ImageField(upload_to="gallery/illustraton/", unique=True)
    large_img_url = models.ImageField(upload_to="gallery/illustraton/", unique=True)

    def __str__(self):
        return self.category


class ArtGallery(models.Model):

    ART_TYPES = [
        ('Pen Art', 'Pen Art'),
        ('Pencil Art', 'Pencil Art'),
        ('Painting', 'Painting')
    ]
    category = models.CharField(max_length=50, choices=ART_TYPES)
    small_img_url = models.ImageField(upload_to="gallery/graphics/", unique=True)
    large_img_url = models.ImageField(upload_to="gallery/graphics/", unique=True)

    def __str__(self):
        return self.category

class MotionGraphicsGallery(models.Model):
    MOTION_GRAPHICS_TYPES = (
        ('Educational', 'Educational'),
        ('Cartoon', 'Cartoon'),
        ('Advertisment', 'Advertisment')
    )
    category = models.CharField(max_length=50, choices=MOTION_GRAPHICS_TYPES)
    small_img_url = models.FileField(upload_to="gallery/motiongraphics/", unique=True)
    large_img_url = models.FileField(upload_to="gallery/motiongraphics/", unique=True)

    def __str__(self):
        return self.category
  