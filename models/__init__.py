#!/usr/bin/python3
"""
    Models initialization file.
    Reloads local storage files if existent,
    initializes empty storage if not.
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
