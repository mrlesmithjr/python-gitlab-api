"""Provides the GitLab Projects class."""


class Projects:
    """Main GitLab Projects class."""

    def __init__(self, gitlab_connection):
        """Init a thing"""

        self.gitlab_connection = gitlab_connection

    def all(self):
        """
        Retrieves all of the users projects and returns them.
        """

        projects = {}

        all_owned_projects = self.gitlab_connection.projects.list(
            owned=True, all=True)

        for project in all_owned_projects:
            project_attrs = project.attributes
            projects[project_attrs['name']] = project_attrs

        return projects

    def members(self):
        """Retrieves all group members and returns them."""

        projects = {}

        all_owned_projects = self.gitlab_connection.projects.list(
            owned=True, all=True)

        for project in all_owned_projects:
            projects[project.name] = {'members': []}
            members = project.members.list()
            for member in members:
                projects[project.name]['members'].append(
                    {'access_level': member.access_level,
                     'expires_at': member.expires_at, 'id': member.id,
                     'name': member.name, 'username': member.username,
                     'state': member.state})

        return projects
