class Groups:
    def __init__(self, gl):
        """Init a thing"""

        self.gl = gl

    def all(self):
        groups = {}

        all_groups = self.gl.groups.list(all=True)

        for group in all_groups:
            group_attrs = group.attributes
            groups[group_attrs['name']] = group_attrs

        return groups
