def logtime(func):
    def wrapper():
        # do something before
        val = func()
        # do something after
        return val
    return wrapper