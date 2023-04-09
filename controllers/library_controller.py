from app import app
from flask import render_template, request, redirect
from models.library_list import books, add_new_book, delete_book, get_book
from models.book import Book


@app.route('/')
def index():
    return render_template('index.html', title='Luptons Library', books=books)

@app.route('/books/<int:id>')
def book_details(id):
    return render_template('book.html', title='Book Details', book=get_book(id))

@app.route('/book', methods=['POST'])
def add_book_route():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_id = len(books) + 1
    new_book = Book(new_id, title, author, genre)
    add_new_book(new_book)
    return redirect('/')

@app.route('/books/delete/<int:id>', methods=['POST'])
def delete_book_route(id):
  delete_book(id)
  return redirect('/')
