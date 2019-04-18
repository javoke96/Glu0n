from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# class CityManager(models.Manager):
#     def create(self, name,pcity,status):
#         lcity = Cities.objects.all().order_by("-id")[0].name
#         city = self.create(name = name, pcity = lcity, status = status)
#         return city

class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null = False)
    pcity = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(null = False)

    @receiver(pre_save, sender='city.Cities')
    def cities_save_handler(sender, instance, *args, **kwargs):
         if instance.pcity is None or instance.pcity == "":
             if Cities.objects.all():
                 instance.pcity = Cities.objects.all().order_by("-id")[0].name

    # def save(self, *args, **kwargs):
    #     if self.pcity is None:
    #           self.pcity = Cities.objects.all().order_by("-id")[0].name
    #     super(Cities, self).save(*args, **kwargs)
    # def __init__(cls,name, pcity, status ):
    #     lcity = Cißties.objects.all().order_by("-id")[0].name
    #     city = cls( name=name, pcity=lcity, status = status)
    #     return city

    class Meta:
        db_table = "Cities2"

    def _str_(self):
        return "{}-{}-{}-{}".format(self.id, self.name, self.pcity, self.status)
