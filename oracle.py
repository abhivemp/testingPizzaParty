import random


class OracleAPI:
    """
    This is a class that acts like an API
    that returns a random number.
    THIS CLASS DOES NOT NEED TO BE UNIT TESTED
    DIRECTLY i.e. there does not need to be a
    'test_oracle.py'.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def authenticated(self):
        return self._authenticated

    @authenticated.setter
    def authenticated(self):
        if not (self.username and self.password):
            raise TypeError("username and password required.")
        self._authenticated = True

    def random_number(self, from_, to_):
        """
        This will generate a random number between the 'from_' and the 'to_' params.
        """
        if not self.authenticated:
            raise Exception("Not authenticated.")
        return round(random.uniform(from_, to_))
