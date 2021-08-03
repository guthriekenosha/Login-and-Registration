import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Login_and_Reg.settings')

application = get_wsgi_application()
