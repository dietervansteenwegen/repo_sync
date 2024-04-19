#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__project__ = 'RepoSync'
__project_link__ = 'https://www.boxfish.be'

from config.config import Config
from log.log import add_rotating_file, setup_logger
from repo_sync import RepoSyncer


def _setup_log():
    log = setup_logger()
    add_rotating_file(log)


def main():
    conf = Config.get_config()

    repo_syncer = RepoSyncer(conf)
    repo_syncer.sync_repos()


if __name__ == '__main__':
    _setup_log()
    main()
