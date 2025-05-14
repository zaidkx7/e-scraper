import os

from flask import Flask, render_template, request, redirect, url_for, abort
from config import DB
from dotenv import load_dotenv

load_dotenv()

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

db = DB(os.getenv('DB_PATH'))


@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html')


@app.route('/')
def index():
    db_path = os.path.join(PROJECT_DIR, os.getenv('DB_PATH'))
    if not os.path.exists(db_path):
        abort(404)

    table_exists = db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='products';", fetch='one'
    )
    if not table_exists:
        abort(404)

    filter = request.args.get('filter')
    categories = db.execute('SELECT DISTINCT category FROM products')
    if not filter or filter == 'all':
        products = db.execute('SELECT * FROM products')
    else:
        products = db.execute(
            'SELECT * FROM products WHERE category = ?', (filter, ))
    return render_template('index.html', products=products, categories=categories)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        id = request.form['id']
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        category = request.form['category']
        image = request.form['image']
        rating = request.form['rating']
        count = request.form['count']

        exist_id = db.execute(
            'SELECT * FROM products WHERE id = ?', (id, ), fetch='one')
        if exist_id is not None:
            return render_template('add.html', error='ID already exists')

        db.execute('INSERT INTO products (id, title, price, description, category, image, rating, count) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                   (id, title, price, description, category, image, rating, count))

        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        category = request.form['category']
        image = request.form['image']
        rating = request.form['rating']
        count = request.form['count']

        db.execute('UPDATE products SET title = ?, description = ?, price = ?, category = ?, image = ?, rating = ?, count = ? WHERE id = ?',
                   (title, description, price, category, image, rating, count, id))
        return redirect(url_for('index'))

    product = db.execute(
        'SELECT * FROM products WHERE id = ?', (id, ), fetch='one')
    return render_template('edit.html', product=product, id=id)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    db.execute('DELETE FROM products WHERE id = ?', (id, ))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
