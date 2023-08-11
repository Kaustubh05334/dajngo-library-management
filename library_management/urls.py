"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from library.views import dashboard,members_view,books_view,add_book,add_member,lend_book,lendings,return_book,search_books,debt_view,settle_debt,import_books,catch_all_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dashboard,name="home"),
    path('members/',members_view,name="members"),
    path('books/',books_view,name="books"),
    path('books/add/', add_book, name='add_book'),
    path('members/add/', add_member, name='add_member'),
    path('lend/', lend_book, name='lend_book'),
    path('lendings/', lendings, name='lendings'),
    path('return/', return_book, name='return_book'),
    path('search/',search_books, name='search_books'),
    path('view-debt/',debt_view, name='debt_view'),
    path('settle-debt/<int:member_id>/',settle_debt,name="settle_debt"),
    path("import-books/",import_books,name="import_books"),


    re_path(r'^(?P<path>.*)/$', catch_all_view, name='catch_all'),
]
