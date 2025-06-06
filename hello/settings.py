"""
Djangoプロジェクト「hello」の設定です。

Django 5.2.2を使用して「django-admin startproject」で生成されました。

このファイルの詳細については、以下を参照してください：
https://docs.djangoproject.com/en/5.2/topics/settings/

すべての設定とその値の完全なリストについては、以下を参照してください：
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# プロジェクト内のパスを次のように構築します: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent


# クイックスタート開発設定 - 本番環境には不適切です
# https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/ を参照してください

# セキュリティ警告: 本番環境では秘密鍵を秘密にしてください！
SECRET_KEY = 'django-insecure-%qn^yc)e*@z(4n2&29$1rv-2s*134)%4)#q8@n^%)pp4ljfiwx'

# セキュリティ警告: 本番環境ではデバッグをオフにしてください！
DEBUG = True

ALLOWED_HOSTS = []


# アプリケーション定義

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'hello.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hello.wsgi.application'


# データベース
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# パスワード検証
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# 国際化
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# 静的ファイル (CSS, JavaScript, 画像)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# デフォルトの主キーフィールドタイプ
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
