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
    elif args.action == "get_group_details":
        get_all_groups(args, gl)
    elif args.action == "get_issues":
        get_issues(args, gl)
    elif args.action == "get_projects":
        get_projects(args, gl, current_user)
    elif args.action == "manage_ssh_keys":
        ssh_keys(args, current_user)


def get_all_groups(args, gl):
    """Get all groups that exist in account."""
    # Capture a list of groups
    all_groups_list = gl.groups.list()
    # Create an array to collect group(s) attributes
    all_groups = []

    # Iterate over list of groups
    for group in all_groups_list:
        group_attrs = group.attributes
        if args.filter and args.action != "get_group_details":
            if args.filter == "namesonly":
                all_groups.append(group_attrs['name'])
        else:
            all_groups.append(group_attrs)

    if args.action == "get_group_details":
        get_group_details(all_groups, args, gl)
    else:

        # Check if output flag has been defined to print in either json or yaml
        if args.output:
            if args.output == "yaml":
                print(yaml.dump(yaml.load(json.dumps(all_groups)),
                                default_flow_style=False))
            elif args.output == "json":
                print(json.dumps(all_groups, indent=4))
        else:
            print(all_groups)


def get_group_details(all_groups, args, gl):
    """Get group projects."""
    for group in all_groups:
        group_id = group['id']
        group_attrs = gl.groups.get(group_id).attributes

        # Check if output flag has been defined to print in either json or yaml
        if args.output:
            if args.output == "yaml":
                print(yaml.dump(yaml.load(json.dumps(group_attrs)),
                                default_flow_style=False))
            elif args.output == "json":
                print(json.dumps(group_attrs, indent=4))
        else:
            print(gl.groups.get(group_id))


def get_issues(args, gl):
    """Get a list of issues."""
    # Check if filter has been passed as an argument and
    # set appropriately if so
    if args.filter:
        if args.filter == "closed":
            issues = gl.issues.list(state="closed")
        elif args.filter == "opened":
            issues = gl.issues.list(state="opened")
    else:
        issues = gl.issues.list()

    # Iterate over list of issues
    for issue in issues:
        issue_attrs = issue.attributes
        # Check if output flag has been defined to print in either json or yaml
        if args.output:
            if args.output == "yaml":
                print(yaml.dump(yaml.load(json.dumps(issue_attrs)),
                                default_flow_style=False))
            elif args.output == "json":
                print(json.dumps(issue_attrs, indent=4))
        else:
            print(issue_attrs)


def get_projects(args, gl, current_user):
    """Get users projects."""
    # Defines users attributes
    user_attrs = current_user.attributes
    # Defines users user variable to use for capturing users projects
    user_name = gl.users.list(
        username=user_attrs['username'])[0]
    # Captures users projects
    projects = user_name.projects.list(all=True)
    # Defines an array to collect all of users projects
    user_projects = []
    # Iterate over each of users projects
    for project in projects:
        project_attrs = project.attributes
        if args.filter:
            if args.filter == "namesonly":
                user_projects.append(project_attrs['name'])
        else:
            user_projects.append(project_attrs)

    user_projects = sorted(user_projects)
    # Check if output flag has been defined to print in either json or yaml
    if args.output:
        if args.output == "yaml":
            print(yaml.dump(yaml.load(json.dumps(user_projects)),
                            default_flow_style=False))
        elif args.output == "json":
            print(json.dumps(user_projects, indent=4))
    else:
        print(user_projects)
    return user_projects


def parse_args(home):
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Manage GitLab via API.")
    parser.add_argument("action", help="Define action to take.", choices=[
        "get_all_groups", "get_group_details", "get_issues", "get_projects",
        "manage_ssh_keys"])
    parser.add_argument(
        "-f", "--filter", help="Filter output.",
        choices=["closed", "namesonly", "opened"])
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
