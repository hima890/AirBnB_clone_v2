#!/usr/bin/python3
"""
Module: __init__ module for AirBnB_clone project

"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
