#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__project__ = 'RepoSync'
__project_link__ = 'https://www.boxfish.be'

from repo_sync.config import Config
from repo_sync.log import setup_logger
from repo_sync.repo_syncer import RepoSyncer

setup_logger()


def main():
    conf = Config.get_config()

    repo_syncer = RepoSyncer(conf)
    repo_syncer.sync_repos()


if __name__ == '__main__':
    main()
