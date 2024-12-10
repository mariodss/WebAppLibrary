from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.

def home(request):
    return render(request, "home.html", context={"current_tab": ""})

def readers(request):
    return render(request, "readers.html", context={"current_tab": "readers"})

def readers_tab(request):

    if request.method=="GET":
     readers = reader.objects.all()  # Fetch all reader objects
     return render(request, "readers.html", context={'current_tab': 'readers', 'readers': readers})
    
    else: 
        query=request.POST['query']
        readers = reader.objects.raw("select * from library_app_reader where reader_name like '%"+query+"%'")
        return render(request, "readers.html", context={'current_tab': 'readers', 'readers': readers, "query":query})
    
    
def save_reader(request):
    reader_item = reader(reference_id = request.POST['reader_ref_id'],
                         reader_name=request.POST['reader_name'],
                         reader_contact=request.POST['reader_contact'],
                         reader_address=request.POST['reader_address'],
                         active=True
                         )
    
    reader_item.save()
    return redirect('/readers')


def books(request):

     if request.method == "GET":
        books = book.objects.all()  # Fetch all books
        return render(request, "books.html", context={"current_tab": "books", "books": books})
     
     else:
        query=request.POST['query']
        filtered_books = book.objects.filter(title__icontains=query)  # Search for books with matching titles
        return render(request, "books.html", context={"current_tab": "books", "books": filtered_books, "query": query})
     

def add_book(request):
      book_item = book(title = request.POST['title'],
                         author=request.POST['author'],
                         isbn=request.POST['isbn'],
                         genre=request.POST['genre'],
                         published_date=request.POST['published_date'],
                         )
      
      book_item.save()
      return redirect ('/books')



bag = []

def my_bag(request):
    if request.method == 'POST':
         form = ReturnsForm(request.POST)
         if form.is_valid():
            reader = form.cleaned_data['reader_id']
            borrow_date = form.cleaned_data['borrow_date']
            return_date = form.cleaned_data['return_date']

             # Create a checkout entry
            checkout= Returns.objects.create(Reader=reader, borrow_date=borrow_date,return_date=return_date )
            checkout.Book.set(bag)  # Link all books in the bag to the checkout

            bag.clear()
            return redirect('/returns')
         
    else:
        form = ReturnsForm()

    return render(request, "my_bag.html", context={"bag": bag, "form":form, "current_tab": "my_bag"})



def add_to_my_bag(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        Book= book.objects.get(id=book_id)
        if Book not in bag:
            bag.append(Book)  # Add the book to the bag

        return redirect('/books')
    return HttpResponse("Invalid request", status=400)


def remove_from_bag(request):
     if request.method == "POST":
        book_id = request.POST.get("book_id")
        Book = book.objects.get(id=book_id)
        if Book in bag:
            bag.remove(Book)  # Remove the book from the bag
        return redirect('/mybag')
     return HttpResponse("Invalid request", status=400)

def returns(request):
    checkouts = Returns.objects.all()
    return render(request, "returns.html", context= {"checkouts": checkouts, "current_tab": "returns"})



    







      
    


         
    
