from distutils.core import setup	

setup(
	name='django-auth-decorators-json',
	version='0.0.1',
	description='replace login url of django auth decorator with json',
	author='yangchen',
	author_email='yuhan534@126.com',
	url='https://github.com/jarvys/django-auth-decorators-json',
	install_requires=['django_render_json'],
	py_modules=['auth_json'],
	scripts=[],
	keywords=['django', 'auth', 'decorators', 'json']
)

