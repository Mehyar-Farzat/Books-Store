# Online Books Store

Welcome to the Django Online Books Store repository! This project is an Online store built using Python, Django, and the Django REST framework, with a full API. The store contains books list and details, auther list and details, and reviews.
Books Store is a mobile application that allows users to browse through a collection of books, view details about individual books, and read reviews from other users. Users can also write their own reviews for books.

## Tech Stack

The Online Books Store utilizes the following technologies and frameworks:

- Backend: Django
- Python: A powerful programming language used for the backend development.
- Django: A high-level web framework that follows the model-view-controller (MVC) architectural pattern and provides a clean and efficient way to build web applications.
- Django REST framework: A powerful and flexible toolkit for building Web APIs.
- Database: SQLite (default Django database)
- Data Generation: Faker library for Python
- Git: A distributed version control system used for tracking changes in source code during software development.


### Installation and how to run it:

1. Clone the repository:
    ```
    git clone https://github.com/Mehyar-Farzat/Books-Store.git
    ```
2. Navigate to the project directory:
    ```
    cd Books-Store
    ```
3. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
4. Apply the migrations to create the database schema:
    ```
    python manage.py migrate
    ```
5. (Optional) Generate dummy data:
    ```
    python dummy_data.py
    ```
6. Start the Django development server:
    ```
    python manage.py runserver
    ```
7. Open your web browser and navigate to `http://localhost:8000` to see the application in action.





