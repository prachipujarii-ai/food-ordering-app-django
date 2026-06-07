# Food Ordering App with Django
A web-based food ordering system built using **Django**.  
This project demonstrates Django fundamentals including **class-based views, context handling, admin interface customization, Bootstrap integration**, and **QR code generation with Pillow**.

## Features
- Food menu management with Django models
- Class-based views for clean and reusable logic
- Context dictionary for passing data to templates
- Admin interface for managing menu items
- Bootstrap styling for responsive UI
- QR code generation using Pillow
- SQLite3 database integration

## Project Structure
- **mysite/** → Project configuration (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`)
- **restaurant_menu/** → App with models, views, urls, migrations
- **templates/restaurant_menu/** → HTML templates (`index.html`, `menu_item_detail.html`, `base.html`)
- **qr.py** → QR code generation script
- **db.sqlite3** → Database file
- **manage.py** → Django project manager

## ⚙️ Setup Instructions

### 1. Create Project & App
```django-admin startproject mysite .```
```python manage.py startapp restaurant_menu```

### 2. Run Development Server
```python manage.py runserver```

### 3.Install Dependencies
```pip install pillow```

## Models Example
`author = models.ForeignKey(User, on_delete=models.PROTECT)`

`PROTECT` → Prevents deletion of author if menus exist.
`SET_NULL` → Keeps meals but sets author to NULL if deleted.

## Templates
`index.html` → Main interface (menu listing)
`menu_item_detail.html` → Detail view for specific menu item

## Context in Django
Context is a dictionary of key-value pairs passed to templates.
Keys become variables accessible in HTML.

## Admin Setup
`python manage.py createsuperuser`

Username: your_username
Password: your_password
Email: user@gmail.com

## Usage
1. Press `Ctrl+C` to stop the server.
2. Create superuser with `python manage.py createsuperuser`.
3. Login at `/admin` to manage menu items.
4. Explore the food ordering interface at `/`.

### Image 1:
<img width="1127" height="952" alt="image" src="https://github.com/user-attachments/assets/606a60c6-947a-4446-8f7e-335118c3289d" />

### Image 2:
<img width="1142" height="917" alt="image" src="https://github.com/user-attachments/assets/96221337-412c-4d7c-83d4-42b7fdf3ba25" />

## Author
Developed by Prachi Pujari
Email: `prchpujarii@gmail.com`



