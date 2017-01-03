# Overview

This repository is mainly for backing up the dotfiles of my daily applications
which include zsh, vim, git and tmux. Being created, applied and tested on
Ubuntu systems, the dotfiles in this repository might not be able to be directly
applied to other systems, but I believe they still can be good references.

In addition to the dotfiles, there are experimental installer and uninstaller
coming with this repository. With the installer, you can apply the dotfiles
easily on Linux systems without worrying too much, since it's designed to work
conservatively. To make the using of the repository even safer, you can restore
your settings once you find out something become weird after applying the
dotfiles of this repository.

# Prerequisites

**zsh**

- zsh
- [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
- [Powerline fonts](https://github.com/powerline/fonts) (for agnoster theme)

**vim**

- vim
- [vim-plug](https://github.com/junegunn/vim-plug)

**git**

- git

**tmux**

- tmux

# Usage

The installer is extremely conservative by design. Before taking any action, it
checks whether there already are dotfiles and whether it's possible to backup
them. The installer only operates after properly saving the well configured
dotfiles. That is, you can always restore your previous settings if anything
unexpected happens right applying the dotfiles from this repository.

```
./install.py
```

Since the installer backs up the original dotfiles automatically, we can easily
restore them by the following command.

```
./uninstall.py
```

# More detailss

~/.zshrc
~/.vimrc
~/.gitconfig and ~/.gitignore
~/.tmux.conf.

