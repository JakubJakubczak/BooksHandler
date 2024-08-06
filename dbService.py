import sqlite3

# jeszcze parametry
def add_book():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()

    #EXECUTE

    conn.commit()
    conn.close()
    pass

def delete_book():
    pass

def edit_book():
    pass

def get_all_books():
    pass

def get_book():
    pass

def add_tag():
    pass

def delete_tag():
    pass

def edit_tag():
    pass

def get_all_tags():
    pass

def add_tag_to_book():
    pass

def get_all_books_with_tag():
    pass

def get_all_tags_of_book():
    pass

def add_description_to_book():
    pass

def add_quote():
    pass

def delete_quote():
    pass

def edit_quote():
    pass

def display_quotes_of_book():
    pass


def search_book_by_name():
    pass

def search_book_by_tags():
    pass

def search_book_by_quote():
    pass



