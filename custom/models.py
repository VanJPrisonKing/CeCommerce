from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Order(models.Model):
    order_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.order_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class Information(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     information_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)