import hashlib


def my_md5(string):
    m = hashlib.md5()
    m.update(string.encode())
    return m.hexdigest()


