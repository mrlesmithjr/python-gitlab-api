# Usage

This guide shows some of the various usages of using this project. Functionality
will change over time. So, this is just a subset of use cases.

## Groups

The following is a list of supported functionalities for groups.

### All Groups

To view all of your GitLab groups:

```bash
python -m python_gitlab_api all-groups --token PersonalAccessToken
```

## Projects

The following are the currently supported functionalities for projects.

### All Projects

To view all of your GitLab projects:

```bash
python -m python_gitlab_api all-projects --token PersonalAccessToken
```

## Users

### All Users

> NOTE: If the GitLab instance is gitlab.com, this retrieves all users. Which
> could be a huge issue.

To get all users:

```bash
python -m python_gitlab_api all-users --token PersonalAccessToken
```

### Current User Attributes

To view your GitLab user attributes:

```bash
python -m python_gitlab_api user-attrs --token PersonalAccessToken
```
