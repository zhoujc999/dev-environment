# fish is from the official .pkg (/usr/local), so it doesn't know Homebrew's completion dir
contains /opt/homebrew/share/fish/vendor_completions.d $fish_complete_path
or set -p fish_complete_path /opt/homebrew/share/fish/vendor_completions.d

set -gx EDITOR fresh
set -gx VISUAL fresh

# Added by OrbStack: command-line tools and integration
# This won't be added again if you remove it.
source ~/.orbstack/shell/init2.fish 2>/dev/null || :

# ---------- Interactive only ----------
if status is-interactive
    function ls --wraps eza
        command eza -la --group-directories-first $argv
    end

    function cat --wraps bat
        command bat $argv
    end

    function vim --wraps fresh
        command fresh $argv
    end

    function grep --wraps rg
        command rg $argv
    end

    function find --wraps fd
        command fd $argv
    end

    function mv
        command mv -i $argv
    end

    function cp
        command cp -i $argv
    end

    function rm
        command rm -I $argv
    end

    function cs --wraps cd
        cd $argv && ls
    end

    function ds
        cd .. && ls
    end

    starship init fish | source
end
