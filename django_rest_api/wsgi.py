import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_api.settings')
    try:
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
    except ImportError:
        raise ImportError("Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?")

if __name__ == '__main__':
    main()