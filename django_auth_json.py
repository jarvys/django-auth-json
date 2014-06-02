from functools import wraps
from django.core.exceptions import PermissionDenied
from django.utils.decorators import available_attrs

from django_render_json import render_json


def user_passes_test(test_func, alternative):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            return render_json(alternative)
        return _wrapped_view
    return decorator


def login_required(alternative):
    return user_passes_test(
        lambda u: u.is_authenticated(),
        alternative
    )


def permission_required(perm, alternative, raise_exception=False):
    def check_perms(user):
        if not isinstance(perm, (list, tuple)):
            perms = (perm, )
        else:
            perms = perm

        if user.has_perms(perms):
            return True

        if raise_exception:
            raise PermissionDenied

        return False

    return user_passes_test(check_perms, alternative)

