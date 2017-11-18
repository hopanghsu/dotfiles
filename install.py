#! /usr/bin/python3

import os, sys

if __name__ == '__main__':

    dotfiles = ['gitconfig',
                'gitignore',
                'tmux.conf',
                'vimrc',
                'zshrc']

    # cd into the directory of the python script.
    os.chdir((os.path.dirname(os.path.abspath(__file__))))

    # Check the existence of the dotfiles.
    existing_dotfiles     = []
    existing_dotfiles_bak = []

    for dotfile in dotfiles:
        if os.path.lexists(os.path.expanduser('~/.' + dotfile)):
            existing_dotfiles.append(dotfile)

        if os.path.lexists(os.path.expanduser('~/.' + dotfile + '.bak')):
            existing_dotfiles_bak.append(dotfile)

    existing_files = existing_dotfiles + existing_dotfiles_bak
    if existing_files and len(sys.argv) == 1 or sys.argv[1] != '-f':
        raise NameError('There already are ' + str(existing_files) + '.')

    # Backup the existing dotfiles
    for dotfile in existing_dotfiles:
        # TODO: Deal with the cases when the inode is a directory.
        os.replace(os.path.expanduser('~/.' + dotfile),
                   os.path.expanduser('~/.' + dotfile + '.bak'))

    # Install the dotfiles
    for dotfile in dotfiles:
        os.symlink(os.path.abspath('sources/' + dotfile),
                   os.path.expanduser('~/.' + dotfile))
