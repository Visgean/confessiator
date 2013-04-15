from setuptools import setup

setup(name='Confessiator',
      version='1.0',
      description='Confess to facebook',
      author='Visgean Skeloru',
      author_email='visgean@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Django=1.4','django_social_auth', 'South', 'django-form-utils', 'django_debug_toolbar', 'simplejson', 'psycopg2', 'bpython', 'facebook-sdk',  ],
     )

