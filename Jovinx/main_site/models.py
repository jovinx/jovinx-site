
from django.db import models
from jsonfield import JSONField

# Create your models here.

class JovinxInfo(models.Model):
    founder = models.CharField(max_length=100, editable=False, default='John Obi Chinemerem')
    company_name = models.CharField(max_length=50, default="Jovinx Creative Company")
    site_url = models.URLField(default='http://www.jovinx.com.ng')
    logo_url = models.ImageField(upload_to='logo/')

    history = models.TextField(blank=True)

    official_phone = models.BigIntegerField(blank=True, null=True)
    mobile = models.BigIntegerField(blank=True, null=True)
    whatsapp = models.BigIntegerField(blank=True, null=True)

    official_mail_address = models.EmailField(blank=True)
    support_mail_address = models.EmailField(blank=True)
    job_mail_address = models.EmailField(blank=True)


    headquarters_address = models.TextField(blank=True, null=True)    
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)

    established = models.DateField()

    def __str__(self):
        return self.company_name


class Service(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='services/', unique=True)
    description = models.TextField()
    fontawesome_icon = models.CharField(max_length=25)
    sub_services = JSONField()

    def __str__(self):
        return self.title

class Client(models.Model):
    company_name = models.CharField(max_length=100)
    company_logo_url = models.ImageField(upload_to='clients/', unique=True)

    def __str__(self):
        return self.company_name

class Testimony(models.Model):
    customer_fullname = models.CharField(max_length=100)
    company_or_business = models.CharField(max_length=80, blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=25)
    testimony = models.TextField(max_length=300)
    thumbnail_url = models.ImageField(upload_to="testimonies/thumbnails/", blank=True)

    def __str__(self):
        return self.customer_fullname
    
#Galleries
class WebGallery(models.Model):
    site_name = models.CharField(max_length=100)
    site_link = models.URLField(max_length=100)
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
    img_url = models.ImageField(upload_to="gallery/graphics/", unique=True)

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
    img_url = models.ImageField(upload_to="gallery/illustraton/", unique=True)

    def __str__(self):
        return self.category


class ArtGallery(models.Model):

    ART_TYPES = [
        ('Pen Art', 'Pen Art'),
        ('Pencil Art', 'Pencil Art'),
        ('Painting', 'Painting')
    ]
    category = models.CharField(max_length=50, choices=ART_TYPES)
    img_url = models.ImageField(upload_to="gallery/graphics/", unique=True)

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
  
class WhyJovinx(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    message = models.TextField()
    received_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Message From "+self.first_name

class ServiceRequest(models.Model):

    SERVICES = Service.objects.all()
    SERVICE_LIST = []
    
    for data in SERVICES:
        service_tuple = (data.title, data.title)
        SERVICE_LIST.append(service_tuple)  

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    service_requested = models.CharField(max_length=200, choices=SERVICE_LIST)
    specifications = models.TextField(blank=True, null=True)
    received_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Service Request From "+self.first_name+' '+self.last_name
