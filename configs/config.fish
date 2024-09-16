function ls --wraps exa
    command eza -la --color=auto --group-directories-first $argv
end

function vim --wraps nvim
    command nvim $argv
end

function cat --wraps batcat
    command batcat $argv
end

function grep --wraps rg
    command rg $argv
end

function find --wraps fdfind
    command fdfind $argv
end

function cs --wraps ls
    cd $argv && ls
end

function ds --wraps ls
    cd .. && ls
end

function mv --wraps mv
    command mv -i $argv
end

function rm --wraps rm
    command rm -I $argv
end

contains /home/$USER/.local/bin/ $fish_user_paths; or set -Ua fish_user_paths /home/$USER/.local/bin/

starship init fish | source
