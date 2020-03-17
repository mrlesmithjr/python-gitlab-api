"""Provides the GitLab Projects class."""
from gitlab_api.actions.users import Users


class Projects:
    """Main GitLab Projects class."""

    def __init__(self, gitlab_connection):
        """Init a thing"""

        self.gitlab_connection = gitlab_connection
        # Define projects dict
        self.projects = {}

    def all(self, search):
        """
        Retrieves all of the users projects and returns them.
        """

        # Iterate through all owned projects
        for project in self.owned(search):
            # Define project attributes
            project_attrs = project.attributes
            # Add project including attributes to projects dict
            self.projects[project_attrs['name']] = project_attrs

        return self.projects

    def members(self, search):
        """Retrieves all group members and returns them."""

        # Instantiate Users class in prep of user id lookup
        users = Users(self.gitlab_connection)

        # Iterate over owned projects
        for project in self.owned(search):
            self.projects[project.name] = {'members': []}

            # Retrieve list of project members recursively
            # Includes inherited members through ancestor groups
            members = project.members.all(all=True)
            # Iterate over members of project and lookup member by id
            # Member id's attributes are added
            for member in members:
                self.projects[project.name]['members'].append(
                    users.lookup(member.id))

        return self.projects

    def owned(self, search):
        """
        Retrieve all projects owned by current user based on API connection
        """

        # Retrieve list of all owned projects for current user
        all_owned_projects = self.gitlab_connection.projects.list(
            owned=True, all=True, search=search)

        return all_owned_projects

    def get(self, search):
        projects = self.gitlab_connection.projects.list(search=search)
        for project in projects:
            project_attrs = project.attributes
            self.projects[project.name] = project_attrs

        return self.projects
