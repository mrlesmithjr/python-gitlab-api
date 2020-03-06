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

        all_projects = self.gitlab_connection.projects.list(
            owned=True, all=True)

        for project in all_projects:
            project_attrs = project.attributes
            projects[project_attrs['name']] = project_attrs

        return projects
