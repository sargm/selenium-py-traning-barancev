import random

class User(object):

    def __init__(self, username=None, password=None,email=None):
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def Admin(cls):
        return cls(username="admin", password="admin")

    @classmethod
    def random(cls):
        random_nmb = random.randrange(0,10000)
        username_rnd = "admin" + str(random_nmb)
        password_rnd = "admin" + str(random_nmb)
        email_rnd = "admin" + str(random_nmb)+ "@test.test"
        return cls(username_rnd, password_rnd, email_rnd)


