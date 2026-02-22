import os
import sys
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Change to your project settings
    try:
        execute_from_command_line(sys.argv)
    except Exception as exc:
        raise SystemExit(exc)