"""Main module."""
import json
from python_gitlab_api.actions.groups import Groups
from python_gitlab_api.actions.projects import Projects
from python_gitlab_api.actions.user import User
from python_gitlab_api.auth.user import auth_user
from python_gitlab_api.cli import cli_args


def main():
    """Main function."""
    args = cli_args()
    gl = auth_user(args)

    action_map = {'all-groups': all_groups, 'all-projects': all_projects,
                  'user-attrs': user_attrs}

    action = action_map[args.action]
    action(gl)


def user_attrs(gl):
    user = User(gl)
    attrs = user.attrs()
    print(json.dumps(attrs))


def all_groups(gl):
    groups = Groups(gl)
    groups_all = groups.all()
    print(json.dumps(groups_all))


def all_projects(gl):
    projects = Projects(gl)
    projects_all = projects.all()
    print(json.dumps(projects_all))


if __name__ == "__main__":
    main()
