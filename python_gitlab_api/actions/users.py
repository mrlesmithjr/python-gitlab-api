"""Provides the GitLab Users class."""


class Users:
    """Main GitLab User class."""

    def __init__(self, gitlab_connection):
        """Init a thing"""
        self.gitlab_connection = gitlab_connection

    def current_user_attrs(self):
        """Retrieves user attributes and returns them."""

        current_user = self.gitlab_connection.user
        current_user_attrs = current_user.attributes

        return current_user_attrs
