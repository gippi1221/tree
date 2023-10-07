from django.db import models

# Create your models here.
class TreeMenu(models.Model):
  name = models.CharField(max_length=255, default='default', null=False)
  title = models.CharField(max_length=255, null=False)
  parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
  url = models.CharField(max_length=200)

  def __str__(self):
    return self.title