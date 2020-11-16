from django.db import models

# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length = 100)
    description = models.CharField(max_length  = 200)
    image  = models.ImageField(upload_to = "portfolio/images/")
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title
class Experience(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def overview_lines(self):
        return filter(None, (line for line in self.description.splitlines()))
