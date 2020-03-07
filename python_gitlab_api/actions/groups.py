"""Provides the GitLab Groups class."""


class Groups:
    """Main GitLab Groups class."""

    def __init__(self, gitlab_connection):
        """Init a thing"""

        self.gitlab_connection = gitlab_connection

    def all(self, search):
        """
        Retrieves all of the groups the user is a member of and returns them.
        """
        groups = {}

        all_groups = self.gitlab_connection.groups.list(
            all=True, search=search)

        for group in all_groups:
            group_attrs = group.attributes
            groups[group_attrs['name']] = group_attrs

        return groups

    def members(self, search):
        """Retrieves all group members and returns them."""

        groups = {}

        all_groups = self.gitlab_connection.groups.list(
            all=True, search=search)

        for group in all_groups:
            groups[group.name] = {'members': []}
            members = group.members.list()
            for member in members:
                groups[group.name]['members'].append(
                    {'access_level': member.access_level,
                     'expires_at': member.expires_at, 'id': member.id,
                     'name': member.name, 'username': member.username,
                     'state': member.state})

        return groups
