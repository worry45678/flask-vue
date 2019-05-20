#!/usr/bin/env python
import os
from app import create_app


app = create_app(os.getenv('PYTHON_CONFIG') or 'default')

app.run(debug=True, port=9999, host='0.0.0.0')
