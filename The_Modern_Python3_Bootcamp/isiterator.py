def is_iterator(obj):
    """checks if obj is iterator"""
    if (
            hasattr(obj, '__iter__') and
            hasattr(obj, '__next__') and
            callable(obj.__iter__) and
            obj.__iter__() is obj
        ):
        return True
    return False