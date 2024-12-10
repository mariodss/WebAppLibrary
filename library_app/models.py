from django.db import models

# Create your models here.

class reader(models.Model):
    reference_id = models.CharField(max_length=200)
    reader_name=models.CharField(max_length=200)
    reader_contact=models.CharField(max_length=200)
    reader_address=models.TextField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.reader_name



class book(models.Model):

    title= models.CharField(max_length=200)
    author= models.CharField(max_length=200)
    isbn=models.CharField(max_length=13, unique=True)
    genre=models.CharField(max_length=100)
    published_date=models.DateField()

    def __str__(self):
        return self.title



class Returns(models.Model):
    Reader = models.ForeignKey(reader, on_delete=models.CASCADE)
    Book = models.ManyToManyField(book)
    borrow_date=models.DateField()
    return_date=models.DateField()

    def __str__(self):
         return f"{self.Reader.reader_name} - {self.borrow_date}"