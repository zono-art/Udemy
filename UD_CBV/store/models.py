from django.db import models
from django.urls import reverse_lazy
from django.dispatch import receiver
import os

# Create your models here.

class BaseModel(models.Model):
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()
    class Meta:
        abstract = True

class Books(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    class Mata:
        db_table = "books"
    def get_absolute_url(self):
        return reverse_lazy("store:detail_book", kwargs={"pk": self.pk})


class PicturesManager(models.Manager):
    def filter_by_book(self, book):
        return self.filter(book=book).all()


class Pictures(BaseModel):
    picture = models.FileField(upload_to="picture/")
    book = models.ForeignKey(
        "books", on_delete=models.CASCADE
    )
    objects = PicturesManager()

@receiver(models.signals.post_delete, sender=Pictures)
def delete_picture(sender, instance, **kwargs):
    #instanceに削除されたpictureのデータが入っている
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)


    

    




