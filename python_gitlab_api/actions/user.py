class User:
    def __init__(self, gl):
        """Init a thing"""
        self.gl = gl

    def attrs(self):
        user = self.gl.user
        user_attrs = user.attributes

        return user_attrs
