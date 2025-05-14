import os
import requests

from config import DB
from dotenv import load_dotenv
from urllib.parse import urljoin

load_dotenv()

# Make sure to create a .env file and add your DB_PATH 
# For Example: DB_PATH=your_database.db
db = DB(os.getenv('DB_PATH'))


class Scraper:
    # Make sure to create .env file and add your API_URL, keep your confidential URLs safe in .env file
    # For Example: API_URL=https://fakestoreapi.com/products
    API_URL = urljoin(os.getenv('API_URL'), 'products')

    def scrape_products(self):
        response = requests.get(self.API_URL)
        return response.json()

    def save_products(self, products):
        db.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, title TEXT, price INT, description TEXT, category VARCHAR, image TEXT, rating FLOAT, count INT)')
        for product in products:
            if db.execute('SELECT * FROM products WHERE id = ?', (product['id'], )):
                print(f"Product {product['id']} already exists")
                continue
            db.execute('INSERT INTO products (title, price, description, category, image, rating, count) VALUES (?, ?, ?, ?, ?, ?, ?)', (
                product['title'], product['price'], product['description'], product['category'], product['image'], product['rating']['rate'], product['rating']['count']))
        db.close()

    def run(self):
        print("Scraping products...")
        products = self.scrape_products()
        print("Saving products...")
        self.save_products(products)
        print("Products saved successfully")


def run():
    return Scraper()


if __name__ == '__main__':
    run().run()
