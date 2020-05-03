# project/server/config.py
import settings
import logging
import os

logger = logging.getLogger(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = settings.APP_NAME
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    WTF_CSRF_ENABLED = False
    RECAPTCHA_PUBLIC_KEY = settings.RECAPTCHA.get('site_key')
    RECAPTCHA_PRIVATE_KEY = settings.RECAPTCHA.get('secret_key')
    RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}
    GOOGLE_ANALYTICS_ID = settings.GOOGLE_ANALYTICS['id']


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    RECAPTCHA_USE_SSL = False
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""

    WTF_CSRF_ENABLED = True

