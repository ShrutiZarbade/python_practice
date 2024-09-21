from django.db import models

#---------------------------------------------------------------------------------------------
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

#basic query - to get all the element 
books = Book.objects.all()

# contains query to find the name it contains "django"
# "__" indicates the field to lookup
author_name = Author.objects.filter(name__icontains="django")
author_name = Author.objects.filter(age__gt=25)

# Aggreate query - for finding average 
from django.db.models import Avg
Author.objects.aggregate(Avg(age))

# Example of order by query
Author.objects.order_by("publication_date")
#=========================================================================================================

#Prefetch_related and select_related

"""
Prefetch is used for many to many and reverse foreign key lookup
Understanding - Prefetch related perform 2 queries:
 1. It will fetch the author object in one query
 2. Second query will be related object then it fetchs the book objects
    in another query
 3. after both query django joins the result in python, 
    assigning related books to each author. Avoiding database hit while accessing Books
"""

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)


# Query for prefetched the Name of author from books
authors = Author.objects.prefetch_related("books")
for author in authors:
    print(author.name)
    for book in author:
        print(book.title)

# Similar way we can perform select_related which is use
"""
select_related perform on onetoonefield and with foreign key
while using select_related django perform a join operation of two table in
a single query 

"""

books = Book.objects.select_related('author')  # This performs a JOIN and fetches both books and their authors

for book in books:
    print(book.title)
    print(book.author.name)  # No additional query is executed to fetch the author, as it was fetched in the same query
