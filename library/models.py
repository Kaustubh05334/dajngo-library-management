from django.db import models

# Create your models here.
class Member(models.Model):
    name=models.CharField(max_length=30)
    number=models.CharField(max_length=13)
    debt = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    aadhar_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=13)
    publisher = models.CharField(max_length=30)
    num_pages = models.CharField(max_length=40)
    per_day_charge = models.DecimalField(decimal_places=2,max_digits=6,default=5)
    qty = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
class Lended(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.book.title} - {self.member.name}'