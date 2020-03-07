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

    action_map = {'all-groups': all_groups,
                  'all-groups-members': all_groups_members,
                  'all-projects': all_projects,
                  'all-projects-members': all_projects_members,
                  'all-users': all_users,
                  'current-user-attrs': current_user_attrs}

    search = args.search

    action = action_map[args.action]
    action(gitlab_connection, search)


def current_user_attrs(gitlab_connection, _search):
    """Returns attribute information for user."""

    user = Users(gitlab_connection)
    user_attrs = user.current_user_attrs()
    print(json.dumps(user_attrs))


def all_groups(gitlab_connection, search):
    """Returns all of the users groups."""

    groups = Groups(gitlab_connection)
    groups_all = groups.all(search)
    print(json.dumps(groups_all))


def all_groups_members(gitlab_connection, search):
    """Returns all groups and members of each group."""

    groups = Groups(gitlab_connection)
    members = groups.members(search)
    print(json.dumps(members))


def all_projects(gitlab_connection, search):
    """Returns all of the users projects."""

    projects = Projects(gitlab_connection)
    projects_all = projects.all(search)
    print(json.dumps(projects_all))


def all_projects_members(gitlab_connection, search):
    """Returns all of the users projects and members of each project."""

    projects = Projects(gitlab_connection)
    members = projects.members(search)
    print(json.dumps(members))


def all_users(gitlab_connection, search):
    """Returns all users."""
    users = Users(gitlab_connection)
    users_all = users.all(search)
    print(json.dumps(users_all))


if __name__ == "__main__":
    main()
