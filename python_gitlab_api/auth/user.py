"""Provides user authentication to GitLab API."""

import json
import netrc
import sys
import gitlab


class User:
    """Main user auth class."""

    def __init__(self, args):
        """Init a thing"""

        # Set url to --url
        self.url = args.url

        # Use --token if passed
        if args.token is not None:
            self.token = args.token
        # Use --netrcfile as fallback
        # Default is ~/.netrc
        else:
            self.netrcfile = args.netrcfile
            self.token = self.netrc()

    def auth(self):
        """Authorize user using token to GitLab API."""

        gitlab_connection = gitlab.Gitlab(self.url, self.token)
        gitlab_connection.auth()

        return gitlab_connection

    def netrc(self):
        """Use Netrc default or --netrcfile if passed as fallback."""

        try:
            parser = netrc.netrc(self.netrcfile)

            # Strip http from url for proper netrc machine lookup
            machine = self.url.replace('http://', '')
            # Strip https from url for proper netrc machine lookup
            machine = self.url.replace('https://', '')

            # Parse machine lookup values from netrc. Only need password
            _login, _username, password = parser.authenticators(machine)

            return password

        except FileNotFoundError as error:
            print(json.dumps({'error': f'{error}'}))
            sys.exit(1)
