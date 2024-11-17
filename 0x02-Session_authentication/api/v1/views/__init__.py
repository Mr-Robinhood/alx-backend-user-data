#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

# Move all imports to the top
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

# Initialize Blueprint after imports
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Load user data from file
User.load_from_file()
