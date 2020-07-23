from . models import *
from . profile import *

@profile()
def my_function():
    import time
    time.sleep(2)
    print('Exiting my function')
    
@profile()
def get_books_by_library_id(book_ids):
    from collections import defaultdict
    result=defaultdict(list)
    
    for book_id in book_ids:
        book=Book.objects.get(id=book_id)
        result[book.library_id].append(book)
    return result
    
@profile()
def get_books_by_library_id_one_query(book_ids):
    from collections import defaultdict
    books=Book.objects.filter(id__in=book_ids)
    result=defaultdict(list)
    
    for book in books:
        result[book.library_id].append(book)
    return result
    
@profile()
def get_books_by_author():
    from collections import defaultdict    
    books = Book.objects.all()
    result = defaultdict(list)
    for book in books:
        author = book.author
        title_and_author = '{} by {}'.format(
            book.title,
            author.name
        )
        result[book.library_id].append(title_and_author)
    return result
    
@profile()
def get_books_by_author_select_related():
    from collections import defaultdict
    books = Book.objects.all().select_related('author')
    result = defaultdict(list)
    for book in books:
        author = book.author
        title_and_author = '{} by {}'.format(
            book.title,
            author.name
        )
        result[book.library_id].append(title_and_author)
    return result
    
@profile()
def get_books_by_author_select_related_values():
    from collections import defaultdict
    books = (
        Book.objects
         .all()
         .select_related('author')
         .values('title', 'library_id', 'author__name','library__name')
    )
    result = defaultdict(list)
    for book in books.iterator():
        title_and_author = '{} by {}'.format(
            book['title'],
            book['author__name']
        )
        result[book['library_id']].append(title_and_author)
    
    return result
    
@profile()
def get_books_by_author_select_related_values_list():
    from collections import defaultdict
    books = (
        Book.objects
         .all()
         .select_related('author')
         .values_list('title', 'library_id', 'author__name')
    )
    result = defaultdict(list)
    for book in books.iterator():
        title_and_author = '{} by {}'.format(
            book[0],
            book[2]
        )
        result[book[1]].append(title_and_author)
    
    return result

@profile()  
def get_book_instances():
    return list(
        Book.objects
        .all()
        .select_related()
    )
# returns list of dictionaries representing model instances
@profile()
def get_book_dictionaries():
    return list(
        Book.objects
        .all()
        .select_related(None)
    )
# returns a list of dictionaries with the name of each book
@profile()
def get_book_dictionaries_title_only():
    return list(
        Book.objects
        .all()
        .select_related('author')
        .values('author__name')
    )
    
@profile()
def get_page_count_by_library_id():
    from collections import defaultdict
    result = defaultdict(int)
    books = Book.objects.all().prefetch_related('pages')
    for book in books:
        result[book.library_id]+=book.get_page_count()
    return result
    
@profile()
def get_page_count_by_library_id_using_annotation():                                                    
    from django.db.models import Count
    result = {}
    libraries = (
        Library.objects
        .all()
        .annotate(page_count=Count('libraries__pages'))
        .values_list('id', 'page_count')
    )
    for library_id, page_count in libraries:
        result[library_id] = page_count
    return result