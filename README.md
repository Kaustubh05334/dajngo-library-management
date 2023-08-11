# django-library-management
### [Demo](https://dajngo-library-management-nxkuqw9vy-kaustubh05334.vercel.app/)
This is a Library Management System built using Django, Tailwind CSS, and PostgreSQL. It is designed to be accessed exclusively by librarians and provides a range of features to efficiently manage library operations.

## Features
- Add Member: Librarians can add new members by providing their name, contact number, and Aadhar number. This information is used to create a member profile in the system.

- Add Books: Librarians can add books to the library catalog through a user-friendly form. The form captures details such as title, author, ISBN, publisher, and number of pages.

- Import Books: Librarians can import books from the Frappe API by either the book's name or the author's name. The system interacts with the Frappe API (https://frappe.io/api/method/frappe-library) to fetch book details and automatically adds them to the library catalog.

- Lended Books: The system provides a tabular representation of all lended books, along with information about the member to whom each book is lended. This helps librarians keep track of book loans and due dates.

- Members with Debt: The homepage displays a tabular representation of members who have an outstanding debt greater than 500. This feature helps librarians identify members who need attention.

- Debt Settlement: The system displays a tabular list of all members and their outstanding debts. Additionally, a dedicated page is provided for librarians to settle the debts of members, ensuring accurate financial records.

## Technologies Used
- Django: The web framework used to build the Library Management System.
- Tailwind CSS: The front-end framework used for styling and layout.
- PostgreSQL: The relational database used to store member, book, and lending information.
### Getting Started
Clone this repository: git clone https://github.com/your-username/library-management-system.git
Install project dependencies: pip install -r requirements.txt
Set up your PostgreSQL database and update database configuration in settings.py.
Apply migrations: python manage.py migrate
Create a superuser account: python manage.py createsuperuser
Run the development server: python manage.py runserver
Usage
Log in to the admin dashboard using the superuser credentials: http://localhost:8000/admin/
Add members, books, and manage lended books using the admin interface.
Access the library management features by navigating to the respective URLs:
Add Member: http://localhost:8000/add_member/
Add Books: http://localhost:8000/add_books/
Import Books: http://localhost:8000/import_books/
Lended Books: http://localhost:8000/lended_books/
Members with Debt: http://localhost:8000/
Debt Settlement: http://localhost:8000/debt_settlement/
