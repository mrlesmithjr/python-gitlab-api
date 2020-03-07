"""Provides the GitLab Users class."""


class Users:
    """Main GitLab User class."""

    def __init__(self, gitlab_connection):
        """Init a thing"""

        self.gitlab_connection = gitlab_connection
        # Define users dict
        self.users = {}

    def current_user_attrs(self):
        """Retrieves current users attributes and returns them."""

        # Define current user based on API connection
        current_user = self.gitlab_connection.user
        # Define current users attributes
        current_user_attrs = current_user.attributes

        return current_user_attrs

    def all(self, search):
        """Retrieves all users and returns them."""

        # If the GitLab instance is gitlab.com, this retrieves all users. Which
        # could be a huge issue. Best to use --search.

        # Retrieve all users. Searches based on --search which defaults to None
        all_users = self.gitlab_connection.users.list(all=True, search=search)

        # Iterate over all users returned
        for user in all_users:
            # Get user attributes to obtain user id for lookup
            user_attrs = user.attributes
            # Define users id
            user_id = user_attrs['id']

            # Add user to users dict including all attributes
            self.users[user.username] = self.lookup(user_id)

        return self.users

    def lookup(self, user_id):
        """Lookup user by id and return attributes."""

        # Lookup user by user id
        user_lookup = self.gitlab_connection.users.get(user_id)
        # Define users attributes in preparation of returning them
        user_attrs = user_lookup.attributes

        return user_attrs
