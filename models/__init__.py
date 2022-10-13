#!/usr/bin/python3
"""
    Init file for models and engine
    variable and module pre-loading
"""


from .engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
