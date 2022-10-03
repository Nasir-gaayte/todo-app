from django.db import models




class TrackerModel(models.Model):
    creater_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        abstract = True
        order_with_respect_to= ('creater_at')