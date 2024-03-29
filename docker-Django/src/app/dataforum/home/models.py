from django.db import models

# Create your models here.
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
