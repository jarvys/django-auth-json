# django-auth-json
> replace the login url parameter of django auth decorator with json as response

##Install
```bash
$ pip install django-auth-json
```

##Usage

###login_required
```Python
from django_auth_json import login_required

@login_required({'code': 1001})
def view(request):
	...
```

###user_passes_test
```Python
from django_auth_json import user_passes_test

@user_passes_test(lambda u: u.is_authenticated(), {'code': 1001})
def view(request):
	...
```

###permission_required
```Python
from django_auth_json import permission_required

@permission_required('polls.can_vote', {'code': 1001})
def view(request):
	...
```

