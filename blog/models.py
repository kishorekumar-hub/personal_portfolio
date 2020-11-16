from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description = models.TextField()
    blog_date = models.DateField(auto_now=False)

    def __str__(self):
        return self.blog_title
