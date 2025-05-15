# Basic Ecommerce-Scraper

A lightweight e-commerce product scraper and management system built with Python and Flask. This project allows you to fetch, store, and manage product information from various e-commerce platforms.

## Project Overview

E-Scraper is a Python-based web application that combines the power of Flask for web interface with efficient product data scraping capabilities. It provides a user-friendly interface to manage product information, including titles, prices, descriptions, categories, and ratings. The application stores data in a SQLite database and offers features for adding, editing, and filtering products.

## Features

- 🚀 **Simple and Intuitive Interface**: Clean web interface for managing products
- 📦 **Product Management**: Add, edit, and delete products with ease
- 🔍 **Category Filtering**: Filter products by categories
- 💾 **SQLite Database**: Efficient local storage of product information
- 🔄 **Real-time Updates**: Instant reflection of changes in the product list
- 🛡️ **Error Handling**: Graceful handling of missing data and errors
- 🔧 **Environment Configuration**: Easy setup through environment variables

## Technologies Used

- **Backend**:
  - Python 3.x
  - Flask (Web Framework)
  - SQLite (Database)
  - python-dotenv (Environment Management)
- **Frontend**:
  - HTML/CSS
  - JavaScript
  - Bootstrap (UI Framework)
- **Development Tools**:
  - Git (Version Control)
  - pip (Package Management)

## Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/zaidkx7/e-scraper.git
   cd e-scraper
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory:
   ```
   DB_PATH=products.db
   API_URL=https://fakestoreapi.com/products
   ```

5. **Initialize the Database**
   The database will be automatically created when you first run the application.

## Usage Guide

1. **Start the Application**
    
    run the scraper once before running the application
   ```bash
   python modules\scraper.py
   python main.py
   ```

2. **Access the Web Interface**
   Open your browser and navigate to `http://localhost:5000`

3. **Managing Products**
   - View all products on the home page
   - Filter products by category using the dropdown menu
   - Add new products using the "Add Product" button
   - Edit existing products by clicking the edit icon
   - Delete products using the delete button

## Folder Structure
```
e-scraper/
├── modules/
├── static/
├── templates/
├── config.py
├── main.py
└── requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please:
1. Check the existing issues
2. Create a new issue with a detailed description of the problem
3. Include steps to reproduce the issue