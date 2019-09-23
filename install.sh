#!/bin/bash
set -exou pipefail
cd $(dirname $0)

# Initialization
sudo apt-get update && sudo apt-get install -y curl

function setup_config {
	mv --backup=numbered ~/.$1 ~/.$1.bak || true # TODO: Ignore links
	ln -s $PWD/sources/$1 ~/.$1
}

# zsh # TODO: Should check the existence of oh-my-zsh
sudo apt-get install -y zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" || true # oh-my-zsh
setup_config zshrc
chsh -s $(which zsh)

# vim
sudo apt-get install -y vim
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim # vim-plug
setup_config vimrc
vim +PlugInstall

# tmux
sudo apt-get install -y tmux
setup_config tmux.conf

# git
sudo apt-get install -y git
setup_config gitconfig
setup_config gitignore
