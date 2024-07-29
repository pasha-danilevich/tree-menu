# models.py
from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='childrens', on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=100)

    childrens: 'MenuItem'
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
