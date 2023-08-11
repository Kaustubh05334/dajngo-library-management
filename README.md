# django-library-management
### [Demo](https://dajngo-library-management.vercel.app/)
This is a Library Management System built using Django, Tailwind CSS, and PostgreSQL. It is designed to be accessed exclusively by librarians and provides a range of features to efficiently manage library operations.

## Features
- Add Member: Librarians can add new members by providing their name, contact number, and Aadhar number. This information is used to create a member profile in the system.

![image](https://github.com/Kaustubh05334/django-library-management/assets/78357870/ec91657a-ad66-4421-acb0-ee42d155d006)

- Add Books: Librarians can add books to the library catalog through a user-friendly form. The form captures details such as title, author, ISBN, publisher, and number of pages.
  
![image](https://github.com/Kaustubh05334/django-library-management/assets/78357870/f7242a74-30a6-44dc-a1f3-d1fb56044a49)

- Import Books: Librarians can import books from the Frappe API by either the book's name or the author's name. The system interacts with the Frappe API (https://frappe.io/api/method/frappe-library) to fetch book details and automatically adds them to the library catalog.
  
![image](https://github.com/Kaustubh05334/django-library-management/assets/78357870/ee53ab81-0072-4e74-8051-b0299a039b55)

- Lended Books: The system provides a tabular representation of all lended books, along with information about the member to whom each book is lended. This helps librarians keep track of book loans and due dates.
  
![image](https://github.com/Kaustubh05334/django-library-management/assets/78357870/f8708dda-bf3a-4fb1-994f-48af95e769c3)

- Members with Debt: The homepage displays a tabular representation of members who have an outstanding debt greater than 500. This feature helps librarians identify members who need attention.
  
![image](https://github.com/Kaustubh05334/django-library-management/assets/78357870/728facfa-e91d-4d18-be96-693830069201)

- Debt Settlement: The system displays a tabular list of all members and their outstanding debts. Additionally, a dedicated page is provided for librarians to settle the debts of members, ensuring accurate financial records.
  
![image](https://github.com/Kaustubh05334/django-library-management/assets/78357870/f7e69ce2-98c2-433a-9651-8448ea8e30ea)

## Technologies Used
- Django: The web framework used to build the Library Management System.
- Tailwind CSS: The front-end framework used for styling and layout.
- PostgreSQL: The relational database used to store member, book, and lending information.

## Some Other Screenshots of The Website
![image](https://github.com/Kaustubh05334/django-library-management/assets/78357870/8c5d363d-1046-44ec-a7fb-65bab668b586)


![image](https://github.com/Kaustubh05334/django-library-management/assets/78357870/64204955-5781-4fac-97d9-7ec6deeb9f19)


![image](https://github.com/Kaustubh05334/django-library-management/assets/78357870/36d7bb66-3bb8-49f3-adfc-f12ee926a810)




### Getting Started
- Clone this repository: git clone [https://github.com/your-username/library-management-system.git](https://github.com/Kaustubh05334/django-library-management.git)
- Install project dependencies: pip install -r requirements.txt
- Set up your PostgreSQL database and update database configuration in settings.py.
- Apply migrations: python manage.py migrate
- Create a superuser account: python manage.py createsuperuser
- Run the development server: python manage.py runserver
