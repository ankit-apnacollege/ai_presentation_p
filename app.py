import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from myapp.flaskapp import app
from error_handlers import register_error_handlers

# Register error handlers
register_error_handlers(app)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
