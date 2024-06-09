# Project Launchpad

Launchpad is a simple Django project designed to facilitate the creation and management of a landing page. This project aims to provide an easy-to-use platform for launching and customizing landing pages quickly.

## Features

- **User-friendly and responsive interface**: Intuitive design powered by [Bootstrap](https://getbootstrap.com/) for easy navigation and management.

- **Admin panel**: A powerful admin interface for managing content and settings.

## Requirements

- Python 3.x

- Django 5.x or higher

- SQLite (default) or other database systems like PostgreSQL, MySQL

## Installation

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/Djangonauts-Philippines/launchpad
   cd launchpad
   ```

2. **Create and activate a virtual environment:**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`

## Configuration

### Database

By default, Launchpad uses SQLite. To configure a different database, modify the `DATABASES` setting in `launchpad/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or 'django.db.backends.mysql'
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',
        'PORT': 'your_database_port',
    }
}
```

### Static Files

Ensure you have correctly set up static files. Add the following settings in `launchpad/settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
```

Run the following command to collect static files:

```bash
python manage.py collectstatic
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure you follow best practices and write tests for any new functionality.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For questions, suggestions, or issues, please contact us at [your email address].

---

Feel free to customize this README file further to better suit your project's specific details and requirements.
