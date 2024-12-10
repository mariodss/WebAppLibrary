from django.urls import path
from .views import *

urlpatterns = [

    path('home', home, name='library_app'),
    path('readers', readers_tab, name="readers_tab"),
    path('readers/add',save_reader),
    path('books',books,name="books" ),
    path('books/add',add_book),
    path('mybag',my_bag, name="my_bag"),
    path('books/add_to_my_bag',add_to_my_bag, name="add_to_my_bag"),
    path('books/remove_from_bag', remove_from_bag, name="remove_from_bag"),
    path('returns', returns, name="returns"),


]