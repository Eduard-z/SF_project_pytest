# create object and define properties for login: username and password
class SFLoginCreds:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"{self.username}, {self.password}"
