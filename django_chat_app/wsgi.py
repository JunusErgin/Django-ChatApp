"""
WSGI config for django_chat_app project.

WSGI is the Web Server Gateway Interface. 
It is a specification that describes how a web server communicates with web applications, 
and how web applications can be chained together to process one request.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat_app.settings')

application = get_wsgi_application()
