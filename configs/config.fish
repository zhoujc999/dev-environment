function ls --wraps exa
    command exa -la --color=auto --group-directories-first $argv
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

contains /home/$USER/bin $fish_user_paths; or set -Ua fish_user_paths /home/$USER/bin/

starship init fish | source
