import os

# Path to the directory containing your Django project
project_directory = r'C:\Users\Dr Poonam Pandey\Desktop\Hostel-Attendance-Management-MITB-Project-main\backend'

# Add the project directory to the PYTHONPATH
os.environ['PYTHONPATH'] = project_directory

# Now you should be able to import the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backends.settings')

# Import the ASGI application
from django.core.asgi import get_asgi_application
application = get_asgi_application()
