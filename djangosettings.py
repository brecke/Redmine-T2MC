from django.conf import settings
from django.core import management


settings.configure(
    DEBUG=True, 
    TEMPLATE_DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE':   '', # django.db.backends.mysql
            'NAME':     '',
            'HOST':     '',
            'USER':     '',
            'PASSWORD': '',
            'PORT':     '', # 3306
        }
    })

management.setup_environ(settings)