from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = BASE_DIR, 'static'



TEMPLATE_DIRS = BASE_DIR, 'templates'

MEDIA_URL = '/music/'

MEDIA_ROOT = BASE_DIR / 'music'

