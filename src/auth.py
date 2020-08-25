from flask_basicauth import BasicAuth


class CustomAuth(BasicAuth):
    def __init__(self, app, username: str, password: str) -> None:
        super().__init__(app)
        self.username = username
        self.password = password

    def check_credentials(self, username: str, password: str) -> bool:
        return username == self.username and password == self.password
