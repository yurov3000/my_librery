from reader import app, db
from reader.models import Book
from flask import render_template, send_from_directory, request, redirect

# index page
@app.route('/')
def index():
	page = request.args.get('page', 1, type=int)
	books = Book.query.order_by(Book.created_at.desc()).paginate(page=page, per_page=4)
	return render_template('index.html', books=books)

# upload picture book
@app.route("/uploads/<filename>")
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# book page
@app.route("/<int:book_id>/")
def book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template("book.html", book=book)

# thrillers books
@app.route("/fantasis/")
def fantasis():
    page = request.args.get('page', 1, type=int)
    books = Book.query.filter(Book.genre == 'фэнтези').paginate(page=page, per_page=4)
    return render_template('fantasis.html', books=books)

# best books
@app.route("/best/")
def best():
    page = request.args.get('page', 1, type=int)
    books = Book.query.filter(Book.rating > 4).paginate(page=page, per_page=4)
    return render_template("best.html", books=books)


# create book
@app.route("/create/")
def createRoute():
    return render_template("create.html")

@app.route("/create/", methods=['POST'])
def create():
    form = request.form
    title = form.get('title')
    description = form.get('description')
    genre = form.get('genre')
    author = form.get('author')
    rating = form.get('rating')
    notes = form.get('notes')
        
    book = Book(title=title, description=description, genre=genre, author=author, rating=rating, notes=notes)
    db.session.add(book)
    db.session.commit()
    return redirect('/')

# delete book
@app.route('/delete/<int:book_id>/', methods=['POST'])
def delete(book_id):
    if not book_id or book_id != 0:
        book = Book.query.get_or_404(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
        return redirect('/')

# update
# @app.route('/update/<int:book_id>/')
# def update(book_id):
#     return print("function to change book information.") 