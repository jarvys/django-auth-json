from distutils.core import setup	

setup(
	name='django-auth-json',
	version='0.0.3',
	description='replace the login url parameter of django auth decorator with json',
	author='yangchen',
	author_email='yuhan534@126.com',
	url='https://github.com/jarvys/django-auth-json',
	install_requires=['django-render-json'],
	py_modules=['django_auth_json'],
	scripts=[],
	keywords=['django', 'auth', 'decorators', 'json']
)

