#!/usr/bin/python

import os
from tenable.io import TenableIO

print("Tenable Image Counter")
TioAccessKey=None
TioSecretKey=None
if 'TIO_ACCESS_KEY' in os.environ:
    TioAccessKey = os.environ['TIO_ACCESS_KEY']
    print("Tenable.io API key:",TioAccessKey)

if 'TIO_SECRET_KEY' in os.environ:
    TioSecretKey=os.environ['TIO_SECRET_KEY']

if TioAccessKey is None or TioSecretKey is None:
    print("Unable to connect to Tenable.io without both the access key and secret key")