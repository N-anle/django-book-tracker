from django.db import models
from django.contrib.auth.models import User

# Create your models here.

rating_choices = [
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5')
]

class BookRecord(models.Model):
    

    user = models.ForeignKey(User,on_delete=models.CASCADE )
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices= rating_choices)
    total_pages = models.IntegerField()
    current_page = models.IntegerField()
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.title} - {self.author}"