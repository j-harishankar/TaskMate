# Django To-Do App

A simple and customizable To-Do web application built with [Django](https://www.djangoproject.com/). Manage your daily tasks efficiently with features like user authentication, task management, deadlines, and more.

---

## Features

- Create, update, and delete tasks
- Mark tasks as complete/incomplete
- Responsive UI



## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (optional but recommended)

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/j-harishankar/django-todo-app.git
    cd django-todo-app
    ```

2. **Create and activate a virtual environment (optional but recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (admin account)**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**

    ```bash
    python manage.py runserver
    ```

7. **Visit the app**

    Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Folder Structure

```
django-todo-app/
├── todo/               # Main app code
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
├── docs/               # Documentation & screenshots/demo
├── manage.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Deployment

To deploy on a production server, configure your settings for production, collect static files, and use a WSGI server like Gunicorn or uWSGI.
Refer to the [Django deployment checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/) for details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Resources

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Awesome Django](https://github.com/wsvincent/awesome-django)
