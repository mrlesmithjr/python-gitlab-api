# Usage

This guide shows some of the various usages of using this project. Functionality
will change over time. So, this is just a subset of use cases.

## Help

```bash
python -m gitlab_api --help
...
usage: __main__.py [-h] [--netrcfile NETRCFILE] [--search SEARCH]
                   [--token TOKEN] [--url URL]
                   {all-groups,all-groups-members,all-projects,all-projects-members,all-users,current-user-attrs}

Manage GitLab via API.

positional arguments:
  {all-groups,all-groups-members,all-projects,all-projects-members,all-users,current-user-attrs}
                        Define action to take.

optional arguments:
  -h, --help            show this help message and exit
  --netrcfile NETRCFILE
                        Path to Netrc file
  --search SEARCH       Filter objects.
  --token TOKEN         Your GitLab API private token.
  --url URL             Your GitLab API Url.
```

## Groups

The following is a list of supported functionalities for groups.

### All Groups

To view all of your GitLab groups:

```bash
python -m gitlab_api all-groups --token PersonalAccessToken
```

#### All Groups - Searching

To search for a specific group.

```bash
python -m gitlab_api all-groups --search group --token PersonalAccessToken
```

### All Group Members

To get a list of all groups with group members for each group.

```bash
python -m gitlab_api all-groups-members --token PersonalAccessToken
```

## Projects

The following are the currently supported functionalities for projects.

### All Projects

To view all of your GitLab projects:

```bash
python -m gitlab_api all-projects --token PersonalAccessToken
```

#### All Projects - Searching

To search for a specific project.

```bash
python -m gitlab_api all-projects --search project --token PersonalAccessToken
```

### All Project Members

To get a list of all projects with members for each project.

```bash
python -m gitlab_api all-projects-members --token PersonalAccessToken
```

## Users

### All Users

> NOTE: If the GitLab instance is gitlab.com, this retrieves all users. Which
> could be a huge issue.

To get all users:

```bash
python -m gitlab_api all-users --token PersonalAccessToken
```

#### All Users - Searching

To search for a specific user.

```bash
python -m gitlab_api all-users --search user --token PersonalAccessToken
```

### Current User Attributes

To view your GitLab user attributes:

```bash
python -m gitlab_api user-attrs --token PersonalAccessToken
```
