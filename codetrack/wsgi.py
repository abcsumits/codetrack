"""
WSGI config for codetrack project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codetrack.settings')

application = get_wsgi_application()
<<<<<<< HEAD
app=applicationapp=application
=======
>>>>>>> ccef9f9d773890be98f28be10141903fd371e138
