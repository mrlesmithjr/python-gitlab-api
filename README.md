# python-gitlab-api

## Requirements

-   Set up API token in GitLab

## Usage

### Display all of your groups in JSON or YAML output

```bash
python gitlab-management.py get_all_groups --token mysupersecrettoken -o {json,yaml}
```

### Display all of your groups in JSON or YAML output and filter on names only

```bash
python gitlab-management.py get_all_groups --token mysupersecrettoken -o {json,yaml} -f namesonly
```

### Display all of your groups details in JSON or YAML output

```bash
python gitlab-management.py get_group_details --token mysupersecrettoken -o {json,yaml}
```

### Display all issues in JSON or YAML output

```bash
python gitlab-management.py get_issues --token mysupersecrettoken -o {json,yaml}
```

### Display all issues in JSON or YAML output and filter on either opened or closed

```bash
python gitlab-management.py get_issues --token mysupersecrettoken -o {json,yaml} -f {opened,closed}
```

### Display all of your projects in JSON or YAML output

```bash
python gitlab-management.py get_projects --token mysupersecrettoken -o {json,yaml}
```

### Display all of your projects in JSON or YAML output and filter on names only

```bash
python gitlab-management.py get_projects --token mysupersecrettoken -o {json,yaml} -f namesonly
```

### Manage Runners (**Limited for now**)

```bash
python gitlab-management.py manage_runners --token mysupersecrettoken
```

### Manage SSH Keys (**Limited for now**)

```bash
python gitlab-management.py manage_ssh_keys --token mysupersecrettoken
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   <mailto:mrlesmithjr@gmail.com>
