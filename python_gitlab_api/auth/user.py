"""Provides user authentication to GitLab API."""

import gitlab


def auth_user(args):
    """Authorize the user using personal access token."""

    gitlab_connection = gitlab.Gitlab(args.url, args.token)
    gitlab_connection.auth()

    return gitlab_connection
