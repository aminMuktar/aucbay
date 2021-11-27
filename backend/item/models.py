from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
class category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

                                             
    def get_absolute_url(self):
            return f'/{self.slug}/'

            
class item(models.Model):
    Category = models.ForeignKey(category, related_name='item',on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255,verbose_name="Item Name")
    item_price = models.DecimalField(max_digits=12, decimal_places=2,verbose_name="Item price")
    item_img = models.ImageField(upload_to ='uploads/',blank=True,null=True,verbose_name="Item img")
    item_description= models.CharField(max_length=400,verbose_name="Item Description")
    item_location= models.CharField(max_length=20,verbose_name="Item Location" )
    item_remaining_time = models.DateTimeField(verbose_name="Item Remaining Time")
    ispection_start = models.DateTimeField(verbose_name="Ispection Start" )
    ispection_end = models.DateTimeField(verbose_name="Ispection End" )     
    min_increment = models.IntegerField(verbose_name="Min Increment")
    attribute = models.CharField(max_length=255,verbose_name="Attribute" )
    #New col
    thumbnail = models.ImageField(upload_to="uploads/",blank=True,null=True,verbose_name="Thumbnail")
    item_date_added = models.DateTimeField(auto_now_add=True,verbose_name="Item Date Added")
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('item_date_added',)
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size) 
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)     
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
