user1 = {
    'name': 'Sorna',
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if user1["valid"]:
            fn(*args, **kwargs)

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
