from functools import wraps
from django.core.exceptions import PermissionDenied
from django.utils.decorators import available_attrs

from django_rendre_json import render_json


def user_passes_test(test_func, alternative):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            return render_json(request, alternative)
        return _wrapped_view
    return decorator


def login_required(function=None, alternative):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated(),
        alternative
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def permission_required(perm, alternative, raise_exception=False):
    def check_perms(user):
        if not isinstance(perm, (list, tuple)):
            perms = (perm, )
        else:
            perms = perm
        # First check if the user has the permission (even anon users)
        if user.has_perms(perms):
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False
    return user_passes_test(check_perms, alternative)

