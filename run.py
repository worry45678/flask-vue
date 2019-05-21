#!/usr/bin/env python
import os
from app import create_app


app = create_app('app.config')

app.run(debug=True, port=9999, host='0.0.0.0')
