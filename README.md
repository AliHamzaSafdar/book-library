# Book Store Apis<br>

# Project Overview:

The goal of this project was to create a robust RESTful API for an online bookstore using Python, Django, Django REST framework, and Celery. The API encompasses the following features:<br>

# 1. User Registration and Authentication:<br>

Implemented user registration, login, and logout functionalities.<br>
Secured API endpoints with Token Authentication to protect user data.<br>

# 2. CRUD Operations:<br>

Books: Created, read, updated, and deleted books with attributes such as title, author, published date, ISBN, and category.<br>
Authors: Managed CRUD operations for authors.<br>
Categories: Handled CRUD operations for book categories.<br>

# 3. Shopping Cart:<br>

Implemented shopping cart functionalities, including adding books, viewing cart contents, removing books, and purchasing books in the cart.

# 4. Email Notifications:<br>

Utilized Celery for background tasks to send email notifications to users after successful purchase of books in their cart.<br>

# Implementation Details:<br>

Python and Django were used to build the backend of the application.<br>
Django REST Framework was employed to create the API, making it easy to design and document the endpoints.<br>
A PostgreSQL database was chosen to store all the necessary data securely.<br>
Extensive unit tests were written to ensure the reliability of API endpoints.<br>
Docker was used for containerization, making it straightforward to set up and run the application in different environments.<br>
GitHub Actions were configured for Continuous Integration (CI) and Continuous Deployment (CD), allowing for automated testing and deployment.<br>

# Prerequisites:<br>
Docker must be installed on your system<br>

# How to Run<br>
`git clone https://github.com/AliHamzaSafdar/book-library`<br>
`cd book-library`<br>
`docker-compose -f docker-compose-local.yml up --build`<br>

then go to following link to see the endpoints and their documentation
`http://127.0.0.1:8000/docs/#/`
You will see the Image 
![Capture](https://github.com/AliHamzaSafdar/book-library/assets/92223723/541efbde-759a-4369-9474-7bdd59242456)



