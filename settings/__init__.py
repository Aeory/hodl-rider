import os

if os.environ.get("DEV"):
    from .dev import *
else:
    from .prod import *
