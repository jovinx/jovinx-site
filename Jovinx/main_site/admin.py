from django.contrib import admin
from .models import Service, Client, Testimony, WebGallery, GraphicsGallery, IllustrationGallery, ArtGallery, MotionGraphicsGallery

# Register your models here.
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Testimony)
admin.site.register(WebGallery)
admin.site.register(GraphicsGallery)
admin.site.register(ArtGallery)
admin.site.register(MotionGraphicsGallery)
admin.site.register(IllustrationGallery)
