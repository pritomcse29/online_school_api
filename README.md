# 🏫 Online School API

An online learning platform built using **Django**, **Django REST Framework**, and **Djoser** for authentication.

---

## 🚀 Features

- 🔐 **JWT Authentication using Djoser**
  - Register, login, logout, password reset
- 👨‍🏫 **Role-based access**
  - Admin, Instructor, Student
- 📚 **Course & Department Management**
- 📝 **Course Enrollment System**
- 🔎 **Search, Filter, and Ordering**
- 📖 **API Documentation** with Swagger (`drf-yasg`)
- ✅ Custom Permissions (AdminOnly, OwnerOnly, etc.)

---

## 🛠 Tech Stack

- Python 3.x  
- Django 4.2  
- Django REST Framework  
- Djoser  
- Simple JWT  
- drf-yasg (Swagger)  
- PostgreSQL / SQLite  

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/online-school.git
cd online-school

# 2. Create & activate virtual environment
 - python -m venv env
 - source env/bin/activate   # On Windows: env\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run migrations
python manage.py migrate

# 5. Create superuser
bash
Copy
Edit
python manage.py createsuperuser
# 6. Run server
bash
Copy
Edit
python manage.py runserver
🔐 Authentication (Djoser + JWT)
Djoser provides ready-to-use endpoints for authentication:

# Action	Endpoint
Register	POST /auth/users/
Login (JWT create)	POST /auth/jwt/create/
Refresh Token	POST /auth/jwt/refresh/
Logout	POST /auth/logout/
Current User Info	GET /auth/users/me/
Headers: Authorization: Bearer <your_token>

📘 API Documentation
Swagger UI:
http://127.0.0.1:8000/swagger/

👥 User Roles
Role	Permissions
Admin	Full access to all models
Instructor	Can manage their own courses
Student	Can enroll and view courses

🧠 Key Modules
courses/: Course & Department models + views

enrollments/: Enrollment system

api/permissions.py: Role-based permissions

auth/: Djoser for JWT auth

filters.py: Custom filters using django-filter

serializers.py: Serializers for all models

✅ To Do
 Video upload support for instructors

 Payment gateway integration

 Course reviews and ratings

 Frontend with React or Vue

🧪 Sample API Endpoints
Resource	Method	Endpoint
List Courses	GET	/api/courses/
Create Course	POST	/api/courses/
Course Details	GET	/api/courses/<id>/
Enroll Course	POST	/api/enrollments/
List Departments	GET	/api/departments/

🤝 Contributing
Feel free to fork this project and submit PRs.
Issues and suggestions are welcome too!

