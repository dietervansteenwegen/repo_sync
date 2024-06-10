#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99


__author__ = 'Dieter Vansteenwegen'
__project__ = 'RepoSync'
__project_link__ = 'https://www.boxfish.be'

import logging
import pathlib
import subprocess

STRIP_FOR_LOGS = '\n\t\r '
log = logging.getLogger()


class LocalRepo:
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = pathlib.Path(path)
        self.errors = []
        self.pull_message = ''

    @property
    def is_valid(self) -> bool:
        dir_exists = self.path.is_dir()
        is_repo = dir_exists and pathlib.Path.joinpath(self.path, '.git').is_dir()
        return dir_exists and is_repo

    @property
    def has_remote(self) -> bool:
        rtn = subprocess.run(['git', '-C', self.path, 'remote'], capture_output=True, text=True)  # noqa: S603, S607
        return rtn.stdout != ''

    def pull_repo(self) -> bool:
        log.debug(f'Pulling {self}')
        success = False
        rtn = subprocess.run(['git', '-C', self.path, 'pull'], capture_output=True, text=True)  # noqa: S603, S607
        if rtn.returncode == 0:
            success = True
            if rtn.stdout.strip(STRIP_FOR_LOGS) != 'Already up to date.':
                log.info(rtn.stdout.strip(STRIP_FOR_LOGS))
        else:
            msg = rtn.stderr.strip().replace('\n', '---')
            log.error(f'Issue during pull: {msg}')
            self.errors.append(rtn.stderr)
        return success

    def push_repo(self) -> bool:
        log.debug(f'Pushing {self}')
        success = False
        rtn = subprocess.run(['git', '-C', self.path, 'push'], capture_output=True, text=True)  # noqa: S603, S607
        if rtn.returncode == 0:
            success = True
            if rtn.stdout.strip(STRIP_FOR_LOGS) != '':
                log.info(rtn.stdout.strip(STRIP_FOR_LOGS))
        else:
            msg = rtn.stderr.strip().replace('\n', '---')
            log.error(f'Issue during push: {msg}')
            self.errors.append(rtn.stderr)
        return success

    def __str__(self) -> str:
        return f'Repository "{self.name}" at {self.path.__str__()}'
