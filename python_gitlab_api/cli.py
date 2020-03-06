"""Console script for python-gitlab-api."""

import argparse


def cli_args():
    """Parse CLI arguments."""

    parser = argparse.ArgumentParser(description='Manage GitLab via API.')

    parser.add_argument(
        'action', help='Define action to take.', choices=[
            'all-groups', 'all-groups-members', 'all-projects',
            'all-projects-members', 'all-users', 'current-user-attrs'])

    parser.add_argument('--search', help='Filter objects.')
    parser.add_argument('--token', help='Your GitLab API private token.')
    parser.add_argument('--url', help='Your GitLab API Url.',
                        default='https://gitlab.com')

    args = parser.parse_args()

    if args.token is None:
        parser.error('--token is required')

    return args
