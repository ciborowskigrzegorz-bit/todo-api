# Todo API 📝

A modern, fast, and secure Todo API built with FastAPI, featuring user authentication, CRUD operations, and comprehensive testing.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

## ✨ Features

- 🔐 **User Authentication** - Secure registration and login system
- 📋 **Todo Management** - Full CRUD operations for todo items
- 🏗️ **Clean Architecture** - Well-structured, maintainable codebase
- 🧪 **Comprehensive Testing** - Full test coverage with pytest
- 📚 **Auto Documentation** - Interactive API docs with Swagger UI
- 🔒 **Security** - JWT tokens, password hashing, user authorization
- ⚡ **High Performance** - Built with FastAPI for maximum speed

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip or pipenv

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ciborowskigrzegorz-bit/todo-api.git
   cd todo-api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   fastapi dev app/main.py
   ```

The API will be available at `http://localhost:8000`

## 📖 API Documentation

Once the server is running, you can access:

- **Interactive API Docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Docs (ReDoc)**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## 🏗️ Project Structure

```
todo-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── auth.py              # Authentication utilities
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # Authentication routes
│       └── todos.py         # Todo CRUD routes
├── tests/
│   ├── __init__.py
│   ├── test_auth.py         # Authentication tests
│   └── test_todos.py        # Todo functionality tests
├── requirements.txt         # Project dependencies
├── .env.example            # Environment variables template
├── pytest.ini             # Pytest configuration
└── README.md
```

## 🔐 Authentication

The API uses JWT-based authentication:

### Register a new user
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "secretpassword"
  }'
```

### Login
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=johndoe&password=secretpassword"
```

## 📋 Todo Operations

All todo operations require authentication. Include the JWT token in the Authorization header:

### Create a todo
```bash
curl -X POST "http://localhost:8000/todos/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI",
    "description": "Build a todo API with FastAPI",
    "completed": false
  }'
```

### Get all todos
```bash
curl -X GET "http://localhost:8000/todos/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### Update a todo
```bash
curl -X PUT "http://localhost:8000/todos/1" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI - Updated",
    "completed": true
  }'
```

### Delete a todo
```bash
curl -X DELETE "http://localhost:8000/todos/1" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_auth.py

# Run with coverage report
pytest --cov=app
```

The test suite includes:
- ✅ User registration and login
- ✅ Todo CRUD operations
- ✅ Authentication and authorization
- ✅ Error handling

## 🛠️ Development

### Environment Variables

Create a `.env` file with the following variables:

```env
# Database
DATABASE_URL=sqlite:///./todos.db

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Development
DEBUG=true
```

### Running in Development Mode

```bash
# With auto-reload
fastapi dev app/main.py

# Or using uvicorn directly
uvicorn app.main:app --reload --port 8000
```

### Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "Add new table"

# Apply migrations
alembic upgrade head
```

## 📦 Dependencies

Key technologies used:

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - SQL toolkit and ORM
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Data validation
- **[Passlib](https://passlib.readthedocs.io/)** - Password hashing
- **[python-jose](https://python-jose.readthedocs.io/)** - JWT handling
- **[pytest](https://docs.pytest.org/)** - Testing framework
- **[httpx](https://www.python-httpx.org/)** - HTTP client for testing

## 🚀 Deployment

### Using Docker

```bash
# Build the image
docker build -t todo-api .

# Run the container
docker run -p 8000:8000 todo-api
```

### Using Docker Compose

```bash
docker-compose up -d
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Write tests for new features
- Update documentation as needed
- Use type hints
- Keep functions small and focused

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Grzegorz Ciborowski**
- GitHub: [@ciborowskigrzegorz-bit](https://github.com/ciborowskigrzegorz-bit)

## 📞 Support

If you have any questions or run into issues:

1. Check the [documentation](http://localhost:8000/docs)
2. Search existing [issues](https://github.com/ciborowskigrzegorz-bit/todo-api/issues)
3. Create a [new issue](https://github.com/ciborowskigrzegorz-bit/todo-api/issues/new)

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

**Happy coding! 🚀**