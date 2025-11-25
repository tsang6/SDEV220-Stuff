# Thawng Sang
# Flask for managing a Book collection with CRUD operations
# 24/11/2025

from flask import Flask, request

app = Flask(__name__)

books = []

# GET all books
@app.route('/books')
def get_books():
    """Retrieve all books from the collection"""
    return {"books": books}

# GET a single book by ID
@app.route('/books/<int:id>')
def get_book(id):
    """Retrieve a specific book by its ID"""
    for book in books:
        if book['id'] == id:
            return book
    return {"error": "Book not found"}, 404

# Create new book
@app.route('/books', methods=['POST'])
def add_book():
    """Add a new book to the collection"""
    book = request.get_json()
    books.append(book)
    return book, 201

# Update existing book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    """Update an existing book's information"""
    book_data = request.get_json()
    for book in books:
        if book['id'] == id:
            book.update(book_data)
            return book
    return {"error": "Book not found"}, 404

# Remove book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    """Delete a book from the collection"""
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return {"message": "Book deleted"}
    return {"error": "Book not found"}, 404

# Run Flask
if __name__ == '__main__':

    app.run(debug=True)

