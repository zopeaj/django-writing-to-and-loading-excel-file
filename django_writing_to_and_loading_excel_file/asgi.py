"""
ASGI config for django_writing_to_and_loading_excel_file project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_writing_to_and_loading_excel_file.settings')

application = get_asgi_application()
