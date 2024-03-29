" => General
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Sets how many lines of history VIM has to remember
set history=500
" Enable filetype plugins
filetype off
filetype plugin on
filetype indent on
" Set to auto read when a file is changed from the outside
set autoread
" Fast saving
command W w !sudo tee % > /dev/null
" Automatically save before commands like :next and :make"
set autowrite
" Enable mouse usage (all modes)"
set mouse=a
" Highlight line which cursor is on
set cursorline
nnoremap j gj
nnoremap k gk
" Disable automatic commenting on new line
autocmd Filetype * setlocal formatoptions-=c formatoptions-=r formatoptions-=o
" Splits open windows bottom and right
set splitbelow splitright
" Don't increment numbers in octal notation
set nrformats-=octal
" Use OS clipboard by default
set clipboard^=unnamed,unnamedplus
" Set utf8 as standard encoding and en_US as the standard language
set encoding=utf8
" Use Unix as the standard file type
set fileformats=unix,dos,mac

" => Plugins
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
call plug#begin('~/.vim/plugged')
  Plug 'morhetz/gruvbox'
  Plug 'itchyny/lightline.vim'
  Plug 'neoclide/coc.nvim', {'branch': 'release'}
  Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
  Plug 'jremmen/vim-ripgrep'
  Plug 'sheerun/vim-polyglot'
  Plug 'ap/vim-buftabline'
  Plug 'scrooloose/nerdtree'
  Plug 'scrooloose/nerdcommenter'
  Plug 'jiangmiao/auto-pairs'
  Plug 'Yggdroot/indentLine'
  Plug 'ntpeters/vim-better-whitespace'
call plug#end()

" => VIM user interface
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Set 1 line to the cursor - when moving vertically using j/k
set scrolloff=1
" Avoid garbled characters in Chinese language windows OS
let $LANG='en'
set langmenu=en
source $VIMRUNTIME/delmenu.vim
source $VIMRUNTIME/menu.vim
" Turn on the Wild menu
set wildmenu
set wildmode=longest:full,full
" Ignore compiled files
set wildignore=*.o,*~,*.pyc
if has("win16") || has("win32")
    set wildignore+=.git\*,.hg\*,.svn\*
else
    set wildignore+=*/.git/*,*/.hg/*,*/.svn/*,*/.DS_Store
endif
"Always show current position
set ruler
" Height of the command bar
set cmdheight=2
" A buffer becomes hidden when it is abandoned
set hidden
" Configure backspace so it acts as it should act
set backspace=eol,start,indent
set whichwrap+=<,>,h,l
" Ignore case when searching
set ignorecase
" When searching try to be smart about cases
set smartcase
" Highlight search results
set hlsearch
" Makes search act like search in modern browsers
set incsearch
" Don't redraw while executing macros (good performance config)
set lazyredraw
" For regular expressions turn magic on
set magic
" Show matching brackets when text indicator is over them
set showmatch
" How many tenths of a second to blink when matching brackets
set mat=2
" No annoying sound on errors
set noerrorbells visualbell t_vb=
" Properly disable sound on errors on MacVim
if has("gui_macvim")
    autocmd GUIEnter * set vb t_vb=
endif
" Add a bit extra margin to the left
" set foldcolumn=1
" Hide -- INSERT --
set noshowmode

" => Colors and Fonts
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
silent! colorscheme gruvbox
set background=dark
" Enable syntax highlighting
if !exists("g:syntax_on")
    syntax enable
endif
let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'cocstatus', 'readonly', 'filename', 'modified' ] ]
      \ },
      \ 'component_function': {
      \   'cocstatus': 'coc#status'
      \ },
      \ }
" Enable 256 colors palette in Gnome Terminal
if $COLORTERM == 'gnome-terminal'
    set t_Co=256
endif
hi cCustomFunc  gui=bold guifg=yellowgreen
hi cCustomClass gui=reverse guifg=#00FF00
" Set extra options when running in GUI mode
if has("gui_running")
    set guioptions-=T
    set guioptions-=e
    set guitablabel=%M\ %t
endif
set t_Co=256
" Allow color schemes to do bright colors without forcing bold.
if &t_Co == 8 && $TERM !~# '^linux\|^Eterm'
  set t_Co=16
endif

" => Files, backups and undo
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Turn backup off, since most stuff is in SVN, git et.c anyway...
set nobackup
set nowritebackup
set noswapfile

" => Text, tab and indent related
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Use spaces instead of tabs
set autoindent
set smartindent
set expandtab
" Be smart when using tabs ;)
set smarttab
" 1 tab == 4 spaces
set formatoptions=tcqrn1
set shiftwidth=4
set tabstop=4 softtabstop=4
set noshiftround
" Linebreak on 500 characters
set linebreak
set textwidth=500
" Wrap lines
set wrap
" Wrap-broken line prefix
set showbreak=<->
" Show line numbers
set number
" Show relative numbers
set relativenumber
" Show command in bottom bar
set showcmd
" enable folding
set foldenable
" Open most folds by default
set foldlevelstart=10
" 10 nested fold max
set foldnestmax=10
set foldmethod=indent

" => Polyglot
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:go_highlight_build_constraints = 1
let g:go_highlight_extra_types = 1
let g:go_highlight_fields = 1
let g:go_highlight_functions = 1
let g:go_highlight_methods = 1
let g:go_highlight_operators = 1
let g:go_highlight_structs = 1
let g:go_highlight_types = 1
let g:go_highlight_function_parameters = 1
let g:go_highlight_function_calls = 1
let g:go_highlight_generate_tags = 1
let g:go_highlight_format_strings = 1
let g:go_highlight_variable_declarations = 1
let g:go_auto_sameids = 1

" => FZF
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:fzf_colors =
\ { 'fg':      ['fg', 'Normal'],
  \ 'bg':      ['bg', 'Normal'],
  \ 'hl':      ['fg', 'Comment'],
  \ 'fg+':     ['fg', 'CursorLine', 'CursorColumn', 'Normal'],
  \ 'bg+':     ['bg', 'CursorLine', 'CursorColumn'],
  \ 'hl+':     ['fg', 'Statement'],
  \ 'info':    ['fg', 'PreProc'],
  \ 'border':  ['fg', 'Ignore'],
  \ 'prompt':  ['fg', 'Conditional'],
  \ 'pointer': ['fg', 'Exception'],
  \ 'marker':  ['fg', 'Keyword'],
  \ 'spinner': ['fg', 'Label'],
  \ 'header':  ['fg', 'Comment'] }

function! s:find_git_root()
    return system('git rev-parse --show-toplevel 2> /dev/null')[:-2]
endfunction
command! ProjectFiles execute 'FZF' s:find_git_root()
nnoremap <C-p> :ProjectFiles<CR>

" => COC
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Install language servers
let g:coc_global_extensions = [
    \ 'coc-tsserver',
    \ ]

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction
inoremap <silent><expr> <TAB>
    \ pumvisible() ? "\<C-n>" :
    \ <SID>check_back_space() ? "\<TAB>" :
    \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

" => Ripgrep
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:rg_command = 'rg --vimgrep -S'
let g:rg_root_types = ['.git']
if executable('rg')
    let g:rg_derive_root='true'
endif

" => Status line
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Always show the status line
set laststatus=2
function! HasPaste()
    if &paste
        return 'PASTE MODE  '
    endif
    return ''
endfunction
let g:NERDSpaceDelims = 1
let g:NERDCustomDelimiters = { 'c': { 'left': '//','right': ''  }  }
map <C-f> :NERDTreeToggle<CR>
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
highlight ColorColumn ctermbg=058
fun! ToggleCC()
  if &cc == ''
    set cc=80
  else
    set cc=
  endif
endfun
nnoremap <C-i> :call ToggleCC()<CR>

" => Leader Key Bindings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let mapleader = ","
nnoremap <leader>c   <Plug>NERDCommenterToggle
vnoremap <leader>c   <Plug>NERDCommenterToggle<CR>gv
" Use <leader>s to search on selected text
vnoremap <leader>s    y/<C-r>"<CR>
" Use <leader>s to clear search highlighting
if maparg('<leader>s', 'n') ==# ''
  nnoremap <silent> <leader>s :nohlsearch<C-R>=has('diff')?'<Bar>diffupdate':''<CR><CR><leader>s
endif
" Buffers
nnoremap <leader>n :bnext<CR>
nnoremap <leader>p :bprev<CR>

" => Vim Startup Commands
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" autocmd VimEnter * PlugInstall

" => Specific Directories Bindings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
