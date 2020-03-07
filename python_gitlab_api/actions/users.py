"""Provides the GitLab Users class."""


class Users:
    """Main GitLab User class."""

    def __init__(self, gitlab_connection):
        """Init a thing"""
        self.gitlab_connection = gitlab_connection

    def current_user_attrs(self):
        """Retrieves current users attributes and returns them."""

        current_user = self.gitlab_connection.user
        current_user_attrs = current_user.attributes

        return current_user_attrs

    def all(self, search):
        """Retrieves all users and returns them."""
        # If the GitLab instance is gitlab.com, this retrieves all users. Which
        # could be a huge issue.

        users = {}
        all_users = self.gitlab_connection.users.list(all=True, search=search)

        for user in all_users:
            users[user.name] = {'id': user.id, 'name': user.name,
                                'state': user.state, 'username': user.username}

        return users
