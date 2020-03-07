"""Provides user authentication to GitLab API."""

from configparser import ConfigParser
import gitlab


def auth_user(args):
    """Authorize the user using personal access token."""

    # If --token is not passed use --tokenfile
    # --token or --tokenfile are required from python_gitlab_api.cli
    if args.token is None:
        parser = ConfigParser()
        parser.read(args.tokenfile)

        # Parse args.tokenfile file to get token
        token = parser.get('gitlab', 'token')

    else:
        token = args.token

    gitlab_connection = gitlab.Gitlab(args.url, token)
    gitlab_connection.auth()

    return gitlab_connection
