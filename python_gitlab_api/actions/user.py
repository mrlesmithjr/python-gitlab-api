"""Provides the GitLab User class."""


class User:
    """Main GitLab User class."""

    def __init__(self, gitlab_connection):
        """Init a thing"""
        self.gitlab_connection = gitlab_connection

    def attrs(self):
        """Retrieves user attributes and returns them."""

        user = self.gitlab_connection.user
        user_attrs = user.attributes

        return user_attrs
