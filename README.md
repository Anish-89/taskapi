📌 Task Manager REST API

A professional RESTful API built with Django + Django REST Framework (DRF) and MySQL, featuring:

✅ CRUD operations for Tasks and Categories

✅ JWT Authentication

✅ Search, Filters & Ordering

✅ Swagger/OpenAPI documentation

✅ Responsive HTML landing page

✅ Ready for Docker & Render deployment

🚀 Features

Task & Category Management

Create, Read, Update, Delete tasks & categories

Priority levels (High, Medium, Low)

Due date validation (cannot be in past)

Track completion status & overdue tasks

Advanced API Features

JWT Authentication (/api/auth/token/)

Filtering (e.g., /api/tasks/?is_completed=false)

Searching (e.g., /api/tasks/?search=report)

Ordering (e.g., /api/tasks/?ordering=due_date)

Documentation

Swagger UI available at /api/docs/

OpenAPI schema at /api/schema/

Deployment

Dockerfile included

Compatible with Render, Railway, Heroku, etc.

🛠️ Installation
1. Clone the repo
git clone https://github.com/<your-username>/taskapi.git
cd taskapi

2. Create a virtual environment
python -m venv venv
# Activate it
venv\Scripts\activate    # Windows
source venv/bin/activate # macOS/Linux

3. Install dependencies
pip install -r requirements.txt

4. Setup database

Create a MySQL database:

CREATE DATABASE taskdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'taskuser'@'%' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON taskdb.* TO 'taskuser'@'%';
FLUSH PRIVILEGES;


Create a .env file in project root:

DEBUG=True
SECRET_KEY=changeme123
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=mysql://taskuser:strongpassword@127.0.0.1:3306/taskdb?charset=utf8mb4

5. Run migrations
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

6. Run server
python manage.py runserver


Open in browser:

Home → http://127.0.0.1:8000/

Swagger Docs → http://127.0.0.1:8000/api/docs/

API root → http://127.0.0.1:8000/api/

🔑 Authentication (JWT)

Obtain token

POST /api/auth/token/

{
  "username": "Admin",
  "password": "anishjha"
}


Refresh token

POST /api/auth/refresh/


Use Authorization: Bearer <access_token> header for protected endpoints.

📚 API Endpoints
Categories

GET /api/categories/ → List categories

POST /api/categories/ → Create category

GET /api/categories/{id}/ → Retrieve category

PATCH /api/categories/{id}/ → Update category

DELETE /api/categories/{id}/ → Delete category

Tasks

GET /api/tasks/ → List tasks

POST /api/tasks/ → Create task

GET /api/tasks/{id}/ → Retrieve task

PATCH /api/tasks/{id}/ → Update task

DELETE /api/tasks/{id}/ → Delete task

Filters:

/api/tasks/?is_completed=true

/api/tasks/?priority=1

/api/tasks/?search=report

/api/tasks/?ordering=due_date



📖 Documentation

Swagger UI: /api/docs/

OpenAPI Schema: /api/schema/

Import /api/schema/ into Postman to generate a collection automatically.

📌 Tech Stack

Backend: Django, Django REST Framework

Database: MySQL (PlanetScale / local)

Auth: JWT (SimpleJWT)

Docs: drf-spectacular (Swagger UI)

Deployment: Render

🤝 Contributing

Feel free to fork this repo, raise issues, or submit PRs.

📜 License
This project is licensed under the MIT License.