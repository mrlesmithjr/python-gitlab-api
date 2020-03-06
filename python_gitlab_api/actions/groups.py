"""Provides the GitLab Groups class."""


class Groups:
    """Main GitLab Groups class."""

    def __init__(self, gitlab_connection):
        """Init a thing"""

        self.gitlab_connection = gitlab_connection

    def all(self):
        """
        Retrieves all of the groups the user is a member of and returns them.
        """

        groups = {}

        all_groups = self.gitlab_connection.groups.list(all=True)

        for group in all_groups:
            group_attrs = group.attributes
            groups[group_attrs['name']] = group_attrs

        return groups
