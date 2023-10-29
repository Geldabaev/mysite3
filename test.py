"""
python manage.py shell
>>> from django.contrib.auth.models import User
>>> from blog.models import MyPost
>>> user = User.objects.get(username='yunus')
>>> user
>>> MyPost(author=user, title='Python Developer', text='Питон молывлм мвоыалмвы')
>>> m1 = _
>>> m1.save()
>>> m1.title4
>>> m1.pk
>>> from django.db import connection
>>> connection.queries
>>> exit()
ipython
django-extensions
INSTALLED_APPS = [
    "django_extensions",
]
pyhton manage.py shell_plus --print-sql
"""