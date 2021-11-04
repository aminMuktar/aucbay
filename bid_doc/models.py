from django.db import models
# Create your models here.
class biddoc(models.Model):
    doc_id          = models.IntegerField()
    denial_of_val   =models.IntegerField()
    init_price      =models.FloatField()
    deadline        =models.DateTimeField()


    def __str__ (self):
        return self.doc_id
