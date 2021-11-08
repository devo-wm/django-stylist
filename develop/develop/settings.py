"""
Django settings for stylist project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&1mmk1e%&9p87fvr=&v84u6fx1)$7f&%)*t9#$zfnu$#h#+5v^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'crispy_forms',
    'stylist',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'develop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'stylist.context_processors.get_custom_styles',
            ],
        },
    },
]

WSGI_APPLICATION = 'develop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Media settings

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Stylist Settings

# STYLIST_DEFAULT_CSS = STATIC_URL + "css/default.css"
STYLIST_DEFAULT_CSS = os.path.join(MEDIA_ROOT, "css/default.css")
STYLIST_SCSS_TEMPLATE = os.path.join(BASE_DIR, "scss/base_template.scss")


STYLE_SCHEMA = {
    "primary": {
        "type": "color",
        "default": "#5c9d5b",
        "label": "Primary"
    },
    "primarygradientend": {
        "type": "color",
        "default": "#407440",
        "label": "Primary Gradient End"
    },
    "hover": {
        "type": "color",
        "default": "#407440",
        "label": "Hover"
    },
    "hover2": {
        "type": "color",
        "default": "#f0fce3",
        "label": "Hover 2"
    },
    "accent": {
        "type": "color",
        "default": "#7ea6d6",
        "label": "Accent"
    },
    "accentgradientend": {
        "type": "color",
        "default": "#5e7395",
        "label": "Accent Gradient End"
    },
    "accenthover": {
        "type": "color",
        "default": "#5875a3",
        "label": "Accent Hover"
    },
    "success": {
        "type": "color",
        "default": "#58cc24",
        "label": "Success"
    },
    "warning": {
        "type": "color",
        "default": "#ffcc33",
        "label": "Warning"
    },
    "danger": {
        "type": "color",
        "default": "#fc4848",
        "label": "Danger"
    },
    "richblack": {
        "type": "color",
        "default": "#0d0d0d",
        "label": "Rich Black"
    },
    "dark": {
        "type": "color",
        "default": "#38629d",
        "label": "Dark"
    },
    "darkgradientend": {
        "type": "color",
        "default": "#405377",
        "label": "Dark Gradient End"
    },
    "white": {
        "type": "color",
        "default": "#ffffff",
        "label": "White"
    },
    "white-50": {
        "type": "color",
        "default": "#ffffff88",
        "label": "White-50"
    },
    "black": {
        "type": "color",
        "default": "#101c33",
        "label": "Black"
    },
    "darkgrey": {
        "type": "color",
        "default": "#5c6066",
        "label": "Dark Grey"
    },
    "muted": {
        "type": "color",
        "default": "#91939a",
        "label": "Muted"
    },
    "secondary": {
        "type": "color",
        "default": "#d7d9db",
        "label": "Secondary"
    },
    "light": {
        "type": "color",
        "default": "#f0f0f0",
        "label": "Light"
    },
    "light-75": {
        "type": "color",
        "default": "#f0f0f0bf",
        "label": "Light-75"
    },
    "info": {
        "type": "color",
        "default": "#64ceff",
        "label": "Info"
    },
    "shadow": {
        "type": "color",
        "default": "#00000026",
        "label": "Shadow"
    },
    "line-height": {
        "type": "number",
        "default": "1.375",
        "label": "Base Line Height"
    },
    "letter-spacing-base": {
        "type": "px",
        "default": "-0.08px",
        "label": "Base Letter Spacing"
    },
    "font-size-base": {
        "type": "rem",
        "default": "1rem",
        "label": "Base Font Size"
    },
    "font-family-base": {
        "type": "font",
        "default": "Source Sans Pro",
        "label": "Font (Body Styles and Labels)"
    },
    "font-family-headings": {
        "type": "font",
        "default": "Nunito",
        "label": "Font (Display and Headers)"
    },
    "display4-weight": {
        "type": "number",
        "default": "700",
        "label": "Display 4 Font Weight"
    },
    "display4-letter-spacing": {
        "type": "px",
        "default": "-2.24px",
        "label": "Display 4 Letter Spacing"
    },
    "display4-line-height": {
        "type": "number",
        "default": "1.04",
        "label": "Display 4 Line Height"
    },
    "display4-font-size": {
        "type": "rem",
        "default": "3.5rem",
        "label": "Display 4 Font Size"
    },
    "display5-font-size": {
        "type": "rem",
        "default": "3.25rem",
        "label": "Display 5 Font Size"
    },
    "display5-weight": {
        "type": "number",
        "default": "600",
        "label": "Display 5 Font Weight"
    },
    "display5-letter-spacing": {
        "type": "px",
        "default": "-2.24px",
        "label": "Display 5 Letter Spacing"
    },
    "display5-line-height": {
        "type": "number",
        "default": "1.04",
        "label": "Display 5 Line Height"
    },
    "h1-font-size": {
        "type": "rem",
        "default": "2.5rem",
        "label": "H1 Font Size"
    },
    "h1-font-weight": {
        "type": "number",
        "default": "600",
        "label": "H1 Font Weight"
    },
    "h1-line-height": {
        "type": "number",
        "default": "1.1",
        "label": "H1 Line Height"
    },
    "h1-letter-spacing": {
        "type": "px",
        "default": "-1px",
        "label": "H1 Letter Spacing"
    },
    "h2-font-size": {
        "type": "rem",
        "default": "2rem",
        "label": "H2 Font Size"
    },
    "h2-font-weight": {
        "type": "number",
        "default": "600",
        "label": "H2 Font Weight"
    },
    "h2-line-height": {
        "type": "number",
        "default": "1.125",
        "label": "H2 Line Height"
    },
    "h2-letter-spacing": {
        "type": "px",
        "default": "-0.64px",
        "label": "H2 Letter Spacing"
    },
    "h3-font-size": {
        "type": "rem",
        "default": "1.75rem",
        "label": "H3 Font Size"
    },
    "h3-font-weight": {
        "type": "number",
        "default": "700",
        "label": "H3 Font Weight"
    },
    "h3-line-height": {
        "type": "number",
        "default": "1.08",
        "label": "H3 Line Height"
    },
    "h3-letter-spacing": {
        "type": "px",
        "default": "-0.7px",
        "label": "H3 Letter Spacing"
    },
    "h4-font-size": {
        "type": "rem",
        "default": "1.5rem",
        "label": "H4 Font Size"
    },
    "h4-font-weight": {
        "type": "number",
        "default": "600",
        "label": "H4 Font Weight"
    },
    "h4-line-height": {
        "type": "number",
        "default": "1.17",
        "label": "H4 Line Height"
    },
    "h4-letter-spacing": {
        "type": "px",
        "default": "-0.72px",
        "label": "H4 Letter Spacing"
    },
    "h5-font-size": {
        "type": "rem",
        "default": "1.25rem",
        "label": "H5 Font Size"
    },
    "h5-font-weight": {
        "type": "number",
        "default": "700",
        "label": "H5 Font Weight"
    },
    "h5-line-height": {
        "type": "number",
        "default": "1.1",
        "label": "H5 Line Height"
    },
    "h5-letter-spacing": {
        "type": "px",
        "default": "-0.4px",
        "label": "H5 Letter Spacing"
    },
    "h6-font-size": {
        "type": "rem",
        "default": "1.125rem",
        "label": "H6 Font Size"
    },
    "h6-font-weight": {
        "type": "number",
        "default": "700",
        "label": "H6 Font Weight"
    },
    "h6-line-height": {
        "type": "number",
        "default": "1.17",
        "label": "H6 Line Height"
    },
    "h6-letter-spacing": {
        "type": "px",
        "default": "-0.27px",
        "label": "H6 Letter Spacing"
    },
    "label-font-size": {
        "type": "rem",
        "default": "1rem",
        "label": "Label Font Size"
    },
    "label-line-height": {
        "type": "rem",
        "label": "Label Line Height",
        "default": "1.375rem"
    },
    "label-letter-spacing": {
        "type": "px",
        "label": "Label Letter Spacing",
        "default": "-0.08px"
    },
    "small-font-size": {
        "default": "0.8125rem",
        "type": "rem",
        "label": "Small Font Size"
    },
    "small-line-height": {
        "type": "number",
        "label": "Small Line Height",
        "default": "1.31"
    },
    "small-label-font-size": {
        "default": "0.625rem",
        "type": "rem",
        "label": "Small Label Font Size"
    },
    "small-label-line-height": {
        "type": "number",
        "label": "Small Label Line Height",
        "default": "1.4"
    }
}

