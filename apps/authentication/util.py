# -*- encoding: utf-8 -*-
import os
import hashlib
import binascii

# Inspiration -> https://www.vitoshacademy.com/hashing-passwords-in-python/

def hash_pass(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest()
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return salt, pwdhash  # return salt and hashed password separately

def verify_pass(provided_password, stored_salt, stored_password):
    """Verify a stored password against one provided by user"""
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  stored_salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
