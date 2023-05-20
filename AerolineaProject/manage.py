#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AerolineaProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


""" http://127.0.0.1:8000/
https://127.0.0.1:8000/
http://156.20.8.123:8000/
http://156.20.8.123/
http://www.aerolinea.com/

url -> inicio/index --> index() --> index.html -->http://127.0.0.1:8000/inicio/index
 """