"""Main module."""
import json
from python_gitlab_api.actions.groups import Groups
from python_gitlab_api.actions.projects import Projects
from python_gitlab_api.actions.users import Users
from python_gitlab_api.auth.user import auth_user
from python_gitlab_api.cli import cli_args


def main():
    """Main function."""
    args = cli_args()
    gitlab_connection = auth_user(args)

    action_map = {'all-groups': all_groups, 'all-projects': all_projects,
                  'all-users': all_users,
                  'current-user-attrs': current_user_attrs}

    action = action_map[args.action]
    action(gitlab_connection)


def current_user_attrs(gitlab_connection):
    """Returns attribute information for user."""

    user = Users(gitlab_connection)
    user_attrs = user.current_user_attrs()
    print(json.dumps(user_attrs))


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


def all_users(gitlab_connection):
    """Returns all users."""
    users = Users(gitlab_connection)
    users_all = users.all()
    print(json.dumps(users_all))


if __name__ == "__main__":
    main()
