#Book Store Apis
# Description
# Project Overview:

The goal of this project was to create a robust RESTful API for an online bookstore using Python, Django, Django REST framework, and Celery. The API encompasses the following features:

# 1. User Registration and Authentication:

Implemented user registration, login, and logout functionalities.
Secured API endpoints with Token Authentication to protect user data.

# 2. CRUD Operations:

Books: Created, read, updated, and deleted books with attributes such as title, author, published date, ISBN, and category.
Authors: Managed CRUD operations for authors.
Categories: Handled CRUD operations for book categories.

# 3. Shopping Cart:

Implemented shopping cart functionalities, including adding books, viewing cart contents, removing books, and purchasing books in the cart.

# 4. Email Notifications:

Utilized Celery for background tasks to send email notifications to users after successful purchase of books in their cart.

# Implementation Details:

Python and Django were used to build the backend of the application.
Django REST Framework was employed to create the API, making it easy to design and document the endpoints.
A PostgreSQL database was chosen to store all the necessary data securely.
Extensive unit tests were written to ensure the reliability of API endpoints.
Docker was used for containerization, making it straightforward to set up and run the application in different environments.
GitHub Actions were configured for Continuous Integration (CI) and Continuous Deployment (CD), allowing for automated testing and deployment.

# Prerequisites:
Docker must be installed on your system

# How to Run
`git clone https://github.com/AliHamzaSafdar/book-library`
`cd book-library`
`docker-compose -f docker-compose-local.yml up --build`

then go to following link to see the endpoints and their documentation
`http://127.0.0.1:8000/docs/#/`



