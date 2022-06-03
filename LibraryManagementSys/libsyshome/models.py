from django.db import models

# Create your models here.

#BOOKS MODEL
class Books(models.Model):
    book_id = models.AutoField
    book_title = models.CharField(max_length=50)
    desc = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to="libsys/img", null=True, blank=True)
    book_pdf = models.FileField(upload_to="libsys/pdf", null=True, blank=True)

    def __str__(self):
        return self.book_title