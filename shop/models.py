from django.db import models
from read_statistics.models import ReadNumExpandMethod, ReadDetail 
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class ShopType(models.Model):
    type_name = models.CharField(max_length=10) # 吃的、喝的、玩的、学习、生活、打扮

    def __str__(self):
        return self.type_name

class Shop(models.Model, ReadNumExpandMethod):
    name = models.CharField(max_length=20)
    shop_type = models.ForeignKey(ShopType, on_delete=models.DO_NOTHING)
    content = models.TextField()
    read_details = GenericRelation(ReadDetail)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['name']

