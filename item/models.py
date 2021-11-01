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


class items(models.Model):
    Category = models.ForeignKey(category, related_name='item',on_delete=models.CASCADE)
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=12, decimal_places=2)
    item_img = models.ImageField(upload_to ='uploads/',blank=True,null=True)
    item_description= models.CharField(max_length=400)
    item_location= models.CharField(max_length=20)
    item_remaining_time = models.DateTimeField()
    ispection_start = models.DateTimeField()
    ispection_end = models.DateTimeField()
    min_increment = models.IntegerField()
    attribute = models.CharField(max_length=255)
    #New col
    thumbnail = models.ImageField(upload_to="uploads/",blank=True,null=True)
    item_date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('item_date_added',)
    def __str__(self):
        return self.name
    
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
