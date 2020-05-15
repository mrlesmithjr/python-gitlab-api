commit 6895522e938022d2d0254664bcf76c8b017713bb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 17 00:37:35 2020 -0400

    Renamed package to drop python_

commit d26ea282ccd739ac21e69ef0e673c2af0573e2d8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 7 00:09:18 2020 -0500

    WIP: Searching by group
    
    Currently returns more than a single group
    
    Hoping to get a narrower search figured out

commit b4349a5eb7690a1f76569a1f95d00888d7dc74a1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 8 17:21:31 2020 -0400

    Enhancement: Added netrc auth functionality
    
    Removed tokenfile option in favor of standardizing on netrc

commit c3025d3aa0ea67e96317b585b11ea61baed9e27a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 23:18:29 2020 -0500

    Enhancement: Changed project members list
    
    Now includes recursive member inheritance

commit cc1b1171b347edd192aab2779da3299e80464b45
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 22:57:21 2020 -0500

    Enhancement: Enhanced users, groups, and projects
    
    user/member lookup by id for attributes

commit bf91779e7b4e992ea7614130bb52fd4d48fcf548
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 21:21:58 2020 -0500

    Added: Option to define --tokenfile
    
    - This will allow you to pass a gitlab.cfg file which contains token

commit b23a6fc01c7f74ed1f51ec944054b093b44d7c68
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 18:54:46 2020 -0500

    Added: Searching functionality
    
    Now --search will leverage the builtin search feature of python-gitlab

commit 130996891c3832a0abe74be9ca8b88a755bac30f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 16:30:40 2020 -0500

    Archived: Archived old script to /old

commit 0265cc1a47dbe7b3dca58348bed3d0f07079a462
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 16:22:15 2020 -0500

    Added: Get members of projects
    
    - Adds ability to get all of a users projects along with members of each project

commit 9894a8a9b1c5ac5691a5865102ab7303bdc8525b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 15:56:15 2020 -0500

    Changed: Only testing Python 3.7

commit fffcf52620c355032728616ebe53640156bbca7e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 15:52:27 2020 -0500

    Fixed: CI testing
    
    - This fixes issues with original CI testing names, etc.

commit be85a42f3f9080b4f069a3de16ca092781b40c7f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 15:42:05 2020 -0500

    Added: Return list of member for each group
    
    - This adds the ability to retrieve all groups including members

commit 74ed42aed4ea4379baff6e91edd9dd84f317b44a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 15:00:22 2020 -0500

    Added: Retrieve all users
    
    This will retrieve all users from a GitLab instance

commit a3c5a1ed1a3316716869046ecdb73afacbbbb44a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 14:27:56 2020 -0500

    Changed: user attributues to current user attributes
    
    This change will allow for other user functionality

commit 66cd3cd9da062a5b048892a91faf45b6408a1509
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 14:13:18 2020 -0500

    Changed: all_projects to all_owned_projects
    
    This will help with clarification

commit 47819f2738deb81e9ee9a78316d2732e7d6b7ede
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 14:11:08 2020 -0500

    Updated: changelog

commit 0003d279b4048836670ceb0181b04b0e1423452f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 14:10:44 2020 -0500

    Fixed: Pylint issues
    
    This fixes the majority of the initial Pylint issues.

commit cf143e0e453b8cab269aef50dfa53ea43181f5b3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 13:56:33 2020 -0500

    First commit of initial refactoring
    
    This is the beginning of changes to come

commit d1e044a909bfc7e0b218f8edac3b52e2ad7f2c5c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 6 13:55:26 2020 -0500

    Updated files, etc. after new structure
    
    This aligns to cookiecutter template

commit 576f83df86f9e70c06991ecba4039cf6e6577ec9
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 7 16:44:05 2020 -0500

    Lingering changes

commit ae96ab94821c516ea900c75c7b8e139f63d60209
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 20:27:28 2018 -0400

    Added usage of getting group projects

commit 282ea6b7c652fb527bc29de65abc7d4b966ee27f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 20:27:13 2018 -0400

    Updated for sorting of group projects

commit 9919e450f6840b3a5efb5c574e03773259160b99
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 14:15:57 2018 -0400

    Added initial functionality to get all groups projects

commit 7ed2e811975acd30a966a3f56ae5ce9e44d0faaf
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 12:56:58 2018 -0400

    Changed get_project to get_user_projects
    
    This will prepare for getting group based projects.

commit 3f3190be4a3e0eb169d63212643328754d1d58d9
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 10:44:41 2018 -0400

    Added initial functionality to manage runners

commit 7fd4840af293d3bb73c717086528ee4f3af17c8a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 08:59:01 2018 -0400

    Added API version flag.

commit 5cc6d96adbe1ed47928289e3d4fc08085b588acf
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 00:50:25 2018 -0400

    Added ability to get all issues and also to filter on opened/closed

commit df76d27f6ba3fa6ef66c7ee22077720685ea1fe5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 00:20:45 2018 -0400

    Added functionality to filter on names only for groups and updated usage

commit 0a02ec8649d3a734f1024ea842e00a311b8fc10e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 00:12:38 2018 -0400

    Added example of filter projects on name only

commit 19bdf2b233183a052d9910884bff816f55caa9ed
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 00:11:18 2018 -0400

    Added filtering capabilities to getting projects for user.

commit c68053d1e5f470588b33da3c8d7be9fd3bcea5ef
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 00:10:31 2018 -0400

    Added filter argument to be used in returning objects.

commit 9180969038cce432d72b3996847b84f88f648c56
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 15 00:09:05 2018 -0400

    Projects list being returned was not complete. This fixes that.

commit 73b5b1e3af2ded9359710f90ff3d4166804c9c73
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jun 14 23:42:43 2018 -0400

    Create LICENSE

commit d5626967bec3ffef70edb5873ed63a3862ae0f97
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jun 14 23:29:07 2018 -0400

    Added functionality to get all of your user projects

commit 610d14fe455b2a25fc6fe65cc6fcafc322c09269
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jun 14 23:28:44 2018 -0400

    Updated repo info with usage and owner info

commit 0acaa9506697dcf5d794ec7b0bace27166b8fb7b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jun 14 20:16:01 2018 -0400

    Added functionality to get group details

commit 54c3648920fda62dcca11585bb2caceb3dff289c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jun 14 01:04:26 2018 -0400

    Added functionality to get all of a users groups and display them.
    
    Future functionality will include using the JSON data to further take
    action(s).

commit bfefa2f5c2d5f109e7aea1b9512bec3e297f2aad
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Jun 13 22:43:46 2018 -0400

    Added positional argument for action. First one is manage_ssh_keys

commit 76803d0ac67362b4af1361b39efb4a9406b849d0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Jun 13 21:19:18 2018 -0400

    first commit
