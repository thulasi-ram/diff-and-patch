import inspect


def fully_qualified_name(obj):
    if not inspect.isclass(obj):
        _obj = obj.__class__
    else:
        _obj = obj
    return "{m}.{kls}".format(m=_obj.__module__, kls=_obj.__name__)
