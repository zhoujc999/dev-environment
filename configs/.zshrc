# Set vim as default editor
export EDITOR=vim

# Enable colors and change prompt
autoload -U colors && colors
PS1="%{$fg[blue]%}%T %n:%~/ %B>%b %{$reset_color%}"

# History in cache directory
HISTSIZE=2000
HISTFILESIZE=2000

# Enable auto cd
setopt autocd

# Basic auto/tab complete
autoload -Uz compinit promptinit
zstyle ":completion:*" menu select
zmodload zsh/complist
compinit
promptinit

# Include hidden files
_comp_options+=(globdots)

# vi mode
bindkey -v
export KEYTIMEOUT=1

# Use vim keys in tab complete menu
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history
bindkey -v '^?' backward-delete-char

# Change cursor shape for different vi modes
function zle-keymap-select {
  if [[ ${KEYMAP} == vicmd ]] ||
     [[ $1 = 'block' ]]; then
    echo -ne '\e[1 q'
  elif [[ ${KEYMAP} == main ]] ||
       [[ ${KEYMAP} == viins ]] ||
       [[ ${KEYMAP} = '' ]] ||
       [[ $1 = 'beam' ]]; then
    echo -ne '\e[5 q'
  fi
}
zle -N zle-keymap-select
# Initiate `vi insert` as keymap (can be removed if `bindkey -V` has been set elsewhere)
zle-line-init() {
    zle -K viins
    echo -ne "\e[1 q"
}
zle -N zle-line-init

# Edit line in vim with ctrl-e
autoload edit-command-line; zle -N edit-command-line
bindkey '^e' edit-command-line


alias ls="ls -FGAlh --color=auto"
alias dc="cd .."

cs() { cd "$@" && ls; }
ds() { cd .. && ls; }

alias mv="mv -i"

alias rm="rm -I"

alias zshrc="vim $HOME/.zshrc"

# File finder
alias s="rg --files | fzf | xargs -r -o $EDITOR"

# mnemonic: [K]ill [P]rocess
# show output of "ps -ef", use [tab] to select one or multiple entries
# press [enter] to kill selected processes and go back to the process list.
# or press [escape] to go back to the process list. Press [escape] twice to exit completely.

kp() {
  local pid=$(ps -ef | sed 1d | eval "fzf ${FZF_DEFAULT_OPTS} -m --header='[kill:process]'" | awk '{print $2}')
  if [ "x$pid" != "x" ]
    then
    echo $pid | xargs kill -${1:-9}
    kp
  fi
}

########## TEMP ALIAS ##########################


# Load zsh-syntax-highlighting; should be last.
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null
# End of lines added by compinstall

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh"  ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm

# PATH
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:$HOME/.cargo/bin"
