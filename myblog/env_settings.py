import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!


SECRET_KEY = 'fxhmz7=8lb!y5@g6xozio)i#c#^b!)-+c=z4zffdp@8q1y^-2s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['localhost']

DATABASES = {
    	'default': {
    		'ENGINE': 'django.db.backends.mysql',
    		'HOST': 'localhost',
    		'USER': 'myblog_db_user',
    		'PASSWORD': '300629qweR@',
    		'NAME': 'myblog_db',

    		}
}


STATIC_URL = '/static/'
PORTAL_URL = 'http://localhost:8000'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
    # /var/www/static
]

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static_cdn')

# email settings
ADMIN_EMAIL = 'mrjenass@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'mrjenass@gmail.com'
EMAIL_HOST_PASSWORD = '300629qwe@'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '196304156024-5b51dufmuecehirl47jnbtb3hh4q3ic9.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'dpUgd0Op7BxiVl0UiSNkrYYw'

SOCIAL_AUTH_FACEBOOK_KEY = '2074046732814967'
SOCIAL_AUTH_FACEBOOK_SECRET = '504cf62c1736ae35099eda30a851990f'

# Admins 
ADMINS = (('Andrii', 'a.kobryk@gmail.com'))
MANAGERS = (('Manager', 'a.kobryk@gmail.com'))