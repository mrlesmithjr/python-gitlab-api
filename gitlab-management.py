#!/usr/bin/env python

"""Manage GitLab using Python."""

import argparse
from os.path import expanduser
import json
import yaml
import gitlab

__author__ = "Larry Smith Jr."
__email___ = "mrlesmithjr@gmail.com"
__maintainer__ = "Larry Smith Jr."
__status__ = "Development"
# http://everythingshouldbevirtual.com
# @mrlesmithjr


def main():
    """Main function."""
    home = user_home()
    args = parse_args(home)
    gl = auth(args)
    current_user = user_details(gl)
    decide_action(args, current_user, gl)


def auth(args):
    """Authorize user."""
    gl = gitlab.Gitlab(args.url, args.token)
    gl.auth()
    return gl


def decide_action(args, current_user, gl):
    """Decide action to take based on positional arguments."""
    if args.action == "get_all_groups":
        get_all_groups(args, gl)
    elif args.action == "manage_ssh_keys":
        ssh_keys(args, current_user)


def get_all_groups(args, gl):
    """Get all groups that exist in account."""
    # Capture a list of groups
    all_groups_list = gl.groups.list()
    # Create dictionary to collect all groups
    all_groups = {}
    # Create an array to collect group(s) attributes
    groups = []

    # Iterate over list of groups
    for group in all_groups_list:
        groups.append(group.attributes)

    # Update dictionary with list of groups iterated over
    all_groups.update({"groups": groups})

    # Check if output flag has been defined to print in either json or yaml
    if args.output:
        if args.output == "yaml":
            print(yaml.dump(yaml.load(json.dumps(all_groups)),
                            default_flow_style=False))
        elif args.output == "json":
            print(json.dumps(all_groups, indent=4))
    else:
        print(all_groups)


def parse_args(home):
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Manage GitLab via API.")
    parser.add_argument("action", help="Define action to take.", choices=[
        "get_all_groups", "manage_ssh_keys"])
    parser.add_argument(
        "-o", "--output", help="Output format if desired.",
        choices=["json", "yaml"])
    parser.add_argument(
        "--sshpubkey", help="Your SSH Key File",
        default="%s/.ssh/id_rsa.pub" % home)
    parser.add_argument("--token", help="Your GitLab API private token.")
    parser.add_argument("--url", help="Your GitLab API Url.",
                        default="https://gitlab.com")
    args = parser.parse_args()
    return args


def ssh_keys(args, current_user):
    """Manage user ssh keys."""
    try:
        with open(args.sshpubkey, "r") as sshpubkey:
            _sshpubkey_contents = sshpubkey.read()
            _sshpubkey_found = True
    except IOError:
        print("%s file not found." % args.sshpubkey)
        _sshpubkey_found = False
    user_ssh_keys = current_user.keys.list()
    if _sshpubkey_found is True:
        _sshpubkey = _sshpubkey_contents.split()
        if user_ssh_keys is not None:
            matching_ssh_key_found = False
            # Loop through existing SSH keys and try to find a match.
            for key in user_ssh_keys:
                _key = key.attributes['key'].split()
                if "".join(_sshpubkey) == "".join(_key):
                    matching_ssh_key_found = True
                    break
                else:
                    matching_ssh_key_found = False
            print("Matching SSH key found: %s" % matching_ssh_key_found)


def user_details(gl):
    """Capture user details for various other usages."""
    current_user = gl.user
    user_attrs = current_user.attributes
    user_id = user_attrs['id']
    user_name = user_attrs['username']
    user_web_url = user_attrs['web_url']

    print("user_id: %s" % user_id)
    print("user_name: %s" % user_name)
    print("user_web_url: %s" % user_web_url)
    print("\n")
    return current_user


def user_home():
    """Capture users home directory."""
    home = expanduser("~")
    return home


if __name__ == "__main__":
    main()
