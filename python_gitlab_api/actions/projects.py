class Projects:
    def __init__(self, gl):
        """Init a thing"""

        self.gl = gl

    def all(self):
        projects = {}

        all_projects = self.gl.projects.list(owned=True, all=True)

        for project in all_projects:
            project_attrs = project.attributes
            projects[project_attrs['name']] = project_attrs

        return projects
