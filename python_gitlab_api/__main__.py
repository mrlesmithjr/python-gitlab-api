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
    gitlab_connection = auth_user(args)

    action_map = {'all-groups': all_groups, 'all-projects': all_projects,
                  'user-attrs': user_attrs}

    action = action_map[args.action]
    action(gitlab_connection)


def user_attrs(gitlab_connection):
    """Returns attribute information for user."""

    user = User(gitlab_connection)
    attrs = user.attrs()
    print(json.dumps(attrs))


def all_groups(gitlab_connection):
    """Returns all of the users groups."""

    groups = Groups(gitlab_connection)
    groups_all = groups.all()
    print(json.dumps(groups_all))


def all_projects(gitlab_connection):
    """Returns all of the users projects."""

    projects = Projects(gitlab_connection)
    projects_all = projects.all()
    print(json.dumps(projects_all))


if __name__ == "__main__":
    main()
