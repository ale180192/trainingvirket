"""
WSGI config for trainingvirke project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path  # python3 only

# third-party
from dotenv import load_dotenv

# load environment vars

load_dotenv(verbose=True)


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trainingvirke.settings")

application = get_wsgi_application()
