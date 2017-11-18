#! /usr/bin/python3

import os, sys

if __name__ == '__main__':

    dotfiles = ['gitconfig',
                'gitignore',
                'tmux.conf',
                'vimrc',
                'zshrc']

    # cd into HOME directory.
    os.chdir(os.path.expanduser('~'))

    for dotfile in ['.' + dotfile for dotfile in dotfiles]:
        if os.path.lexists(dotfile + '.bak'):
            os.replace(dotfile + '.bak', dotfile)

