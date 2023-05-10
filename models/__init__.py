#!/usr/bin/python3
"""
=========================
models/__init__.py module
=========================
"""
from models.engine.file_storage import FileStorage

# create a unique FileStorage instance for your application
storage = FileStorage()

# call reload() method on this variable
storage.reload()
