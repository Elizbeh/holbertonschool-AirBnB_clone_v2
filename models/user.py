#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """Representation of a user """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
