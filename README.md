# RepoSync

> Automated synchronisation of multiple local GIT repositories.

Reads location of repos on your local machine from a config file and pulls latest versions from the remote.

## Usage

Call with `-c INI_FILE_LOCATION`:

`python -m repo_sync -c c:/users/username/repo_sync.ini`

Or after installation using pip (`python -m pip install .`):

`repo_sync -c c:/users/username/repo_sync.ini`

## Ini file

The ini file can have two sections.

* `[repos]`: directories that are git repositories
* `[repo_directories]`: directories that contain git repositories as subdirectories. Useful if all your repos are in one directory.

Example:

```ini
[repos]
my_site = /mnt/external_drive/my_site

[repo_directories]
my_repos = ~/repos
```

## Release History

See [CHANGELOG.md](https://github.com/dietervansteenwegen/repo_sync/blob/master/CHANGELOG.md)

## Meta

Author: Dieter Vansteenwegen

[Github profile](https://github.com/dietervansteenwegen/)

Distributed under the GNU GPLv3 license. See [LICENSE](LICENSE) for more information.
