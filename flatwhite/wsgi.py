import os
import sys
from django.core.wsgi import get_wsgi_application

# Ensure project root is in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# Set default Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flatwhite.settings")

# WSGI application
application = get_wsgi_application()

# Vercel expects 'app' as the entrypoint
app = application
