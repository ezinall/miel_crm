from .base import *

try:
    from .local import *
except ImportError:
    print('Not find locale.py with "SECRET_KEY"')
