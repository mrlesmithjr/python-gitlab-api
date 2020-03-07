"""Provides the GitLab Groups class."""
from python_gitlab_api.actions.users import Users


class Groups:
    """Main GitLab Groups class."""

    def __init__(self, gitlab_connection):
        """Init a thing"""

        self.gitlab_connection = gitlab_connection
        # Define groups dict
        self.groups = {}

    def all(self, search):
        """
        Retrieves all of the groups the user is a member of and returns them.
        """

        # Iterate over list of all groups returned
        for group in self.get(search):
            group_attrs = group.attributes
            self.groups[group_attrs['name']] = group_attrs

        return self.groups

    def members(self, search):
        """Retrieves all group members and returns them."""

        # Instantiate Users class in prep of user id lookup
        users = Users(self.gitlab_connection)

        # Iterate over list of all groups returned
        for group in self.get(search):
            self.groups[group.name] = {'members': []}

            # Retrieve list of members of group
            members = group.members.list()
            # Iterate over members of group and lookup member by id
            # Member id's attributes are added
            for member in members:
                self.groups[group.name]['members'].append(
                    users.lookup(member.id))

        return self.groups

    def get(self, search):
        """Retrieve list of all groups and return them."""

        # Retrieve list of all groups
        all_groups = self.gitlab_connection.groups.list(
            all=True, search=search)

        return all_groups
