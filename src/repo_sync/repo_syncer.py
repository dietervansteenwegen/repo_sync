#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__project__ = 'RepoSync'
__project_link__ = 'https://www.boxfish.be'

import logging
import pathlib

from repo_sync.config import Config
from repo_sync.local_repo import LocalRepo

log = logging.getLogger(__name__)


class RepoSyncer:
    def __init__(self, config: Config):
        log.debug(f'RepoSyncer initialized. Config: {config}')
        self._config = config
        self.issues: list[str] = []

    def _sync_repo(self, repo: LocalRepo):
        log.debug(f'Handling {repo}')
        if repo.is_valid and repo.has_remote:
            repo.pull_repo()
            repo.push_repo()
        else:
            msg = (
                f'{repo} does not exist, is no repository or has no remote. ' 'Ignoring this entry.'
            )
            log.warning(msg)

    def _sync_individual_repos(self) -> None:
        for repo_name, repo_path in self._config.config['repos'].items():
            repo = LocalRepo(name=repo_name, path=repo_path)
            self._sync_repo(repo)

    def sync_repos(self) -> None:
        log.info('Syncing repos...')
        if self._config.config.has_section('repos'):
            self._sync_individual_repos()
        if self._config.config.has_section('repo_directories'):
            self._sync_repo_directories()
        log.info('Done.')

    def _sync_repo_directories(self) -> None:
        for _, repo_dir_path in self._config.config['repo_directories'].items():
            src_dir = pathlib.Path(repo_dir_path)
            if src_dir.is_dir():
                for subdir in [subdir for subdir in src_dir.iterdir() if subdir.is_dir()]:
                    self._sync_repo(LocalRepo(name=subdir.stem, path=subdir))
