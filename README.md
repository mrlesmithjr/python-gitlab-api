# python-gitlab-api

This project provides the ability to manage GitLab functionality using python
and the GitLab API.

## Build Status

### GitHub Actions

![Python Test](https://github.com/mrlesmithjr/python-gitlab-api/workflows/Python%20Test/badge.svg)

### Travis CI

[![Build Status](https://travis-ci.org/mrlesmithjr/python-gitlab-api.svg?branch=master)](https://travis-ci.org/mrlesmithjr/python-gitlab-api)

## Requirements

- [requirements.txt](requirements.txt)
- [requirements-dev.txt](requirements-dev.txt)

### GitLab API Personal Token

You will need to create a [GitLab API Personal Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) in order to authenticate.

To use your token you will either need to use `--token PersonalAccessToken` or
create/edit a `~/.netrc`.

The `~/.netrc` file should look like:

```bash
machine gitlab.com
password = PersonalAccessToken
```

## Dependencies

## Usage

To view the different usages available checkout the [usage](USAGE.md) guide.

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://twitter.com/mrlesmithjr)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
- [http://everythingshouldbevirtual.com](http://everythingshouldbevirtual.com)

> NOTE: Repo has been created/updated using [https://github.com/mrlesmithjr/cookiecutter-python-project](https://github.com/mrlesmithjr/cookiecutter-python-project) as a template.
