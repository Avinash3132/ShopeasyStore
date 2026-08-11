# 🛍️ ShopEasy — Django E-Commerce Store

A full-featured e-commerce web application built with Django, Bootstrap 5, and PostgreSQL/SQLite. Includes product listings, shopping cart, user authentication, checkout, order management, and a powerful admin panel.

---

## Features

- **Product Listing** — Browse all products with category filters, search, and sorting
- **Search & Filter** — Search by name/description, filter by category, sort by price or date
- **Image Gallery** — Multiple product images with lightbox viewer and keyboard navigation
- **Shopping Cart** — Session-based cart with add, update, and remove functionality
- **User Authentication** — Register, login, logout with profile page
- **Checkout & Orders** — Full checkout flow with shipping form and order confirmation
- **Order History** — View all past orders with status tracking
- **Django Admin** — Manage products, categories, orders with image previews
- **Responsive UI** — Mobile-friendly design using Bootstrap 5
- **Featured Products** — Highlight special products on the homepage

---

## Project Structure

```
shopeasy/
├── ecommerce/              # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/                  # Products & categories app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── cart/                   # Shopping cart app
│   ├── cart.py
│   ├── views.py
│   ├── urls.py
│   └── context_processors.py
├── orders/                 # Checkout & orders app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── accounts/               # User authentication app
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── static/
│   ├── css/style.css
│   └── js/main.js
├── templates/
│   ├── base.html
│   ├── store/
│   ├── cart/
│   ├── orders/
│   └── accounts/
├── media/                  # Uploaded product images
├── requirements.txt
└── manage.py
```

---

## Getting Started

### Prerequisites

- Python 3.11 or higher
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Avinash3132/ShopEasy.git
cd ShopEasy
```

**2. Create and activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Apply database migrations**
```bash
python manage.py migrate
```

**5. Create a superuser (admin account)**
```bash
python manage.py createsuperuser
```

**6. Run the development server**
```bash
python manage.py runserver
```

**7. Open in browser**
```
http://127.0.0.1:8000/
```

---

## Admin Panel

Access the Django admin panel at:
```
http://127.0.0.1:8000/admin/
```

Login with the superuser credentials you created. From the admin panel you can:
- Add/edit/delete **Categories** and **Products**
- Upload **product images** and **gallery images**
- View and manage **Orders** and update their status
- Manage **Users**

---

## 🌐 URL Reference

| Page           |      URL      |
|----------------|---------------|
| Homepage       | `/` |
| Product Detail | `/product/<slug>/` |
| Category Filter| `/category/<slug>/` |
| Shopping Cart  | `/cart/` |
| Checkout       | `/orders/checkout/` |
| My Orders      | `/orders/my-orders/` |
| Register       | `/accounts/register/` |
| Login          | `/accounts/login/` |
| Admin Panel    | `/admin/` |

---

## 🛠️ Tech Stack

| Technology         | Purpose |
|--------------------|--------------------|
| Django 6.0         | Backend framework |
| SQLite             | Database |
| Bootstrap 5.3      | Frontend UI |
| Bootstrap Icons    | Icon library |
| Pillow             | Image processing |
| django-crispy-forms| Form rendering |
| crispy-bootstrap5  | Bootstrap 5 form theme |
| Google Fonts       | Typography |

---

## Requirements

```text
Django==6.0.7
Pillow==12.3.0
django-crispy-forms==2.6
crispy-bootstrap5==2026.3
dj-database-url
psycopg[binary]
gunicorn
whitenoise
```

For production deployment, PostgreSQL is recommended. Local development
automatically falls back to SQLite when `DATABASE_URL` is not set.

---


## Deployment

This project is a Django server application and should be deployed to a
Python/Django-compatible host rather than Netlify as a static site.

See [`DEPLOYMENT.md`](DEPLOYMENT.md) for production settings, PostgreSQL setup,
static/media handling, and migration of the existing SQLite data.

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Avinash Patel 
CA/DF1/194789

Built with Django & Bootstrap 5.

---

*Happy Shopping! 🛍️*
