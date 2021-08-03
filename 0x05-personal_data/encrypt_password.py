#!/usr/bin/env python3
"""
function that expects one string argument name password
and returns a salted, hashed password, which is a byte string.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ function that expects one string argument name
    password and returns a salted, hashed password, which is a byte string """
    encodedPasswort = password.encode()
    hashPassword = bcrypt.hashpw(encodedPasword, bcrypt.gensalt())

    return hashPassword


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Implement an is_valid function that expects 2 arguments and
    returns a boolean """
    valid = False
    encodedPasswort = password.encode()
    if bcrypt.checkpw(encodedPasswort, hashed_password):
        valid = True
    return valid
