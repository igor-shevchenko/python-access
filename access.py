from functools import wraps
import inspect

__all__ = ('private', 'protected', 'public')

def private(fn):
    class_name = inspect.stack()[1][3] # assume that classes with same names are same
    @wraps(fn)
    def wrapped(*args, **kwargs):
        prev_frame = inspect.currentframe().f_back
        if prev_frame.f_locals.has_key('self'):
            caller = prev_frame.f_locals['self'] # assume that first arg in calling method is 'self'
            instance = args[0]
            if instance == caller and class_name == instance.__class__.__name__:
                return fn(*args, **kwargs)
        raise Exception("Can't call private method %s" % fn.__name__)
    return wrapped

def protected(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        prev_frame = inspect.currentframe().f_back
        if prev_frame.f_locals.has_key('self'):
            caller = prev_frame.f_locals['self'] # assume that first arg in calling method is 'self'
            instance = args[0]
            if instance == caller:
                return fn(*args, **kwargs)
        raise Exception("Can't call protected method %s" % fn.__name__)
    return wrapped

def public(fn):
    return fn