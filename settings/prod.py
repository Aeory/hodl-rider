from settings.dev import *

RECAPTCHA = {
    'site_key': "6LcFdPEUAAAAACq9oaLfp-myWHVmyb6PEkV1cGfk",
    'secret_key': os.environ.get("RECAPTCHA_SECRET_KEY")
}

SECRET_KEY = os.environ.get('APP_SECRET_KEY')

logging.basicConfig(level=logging.INFO)
