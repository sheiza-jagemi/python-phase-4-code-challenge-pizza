#!/usr/bin/env python3

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database and tables created successfully!")