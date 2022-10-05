" Nvim config file by MF14

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Leader stuff
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let mapleader = ","

nnoremap <leader>s :%s///g<Left><Left><Left>
nnoremap <leader>n :NERDTree<CR>
nnoremap <leader>N :NERDTreeClose<CR>
nnoremap <leader>r :bro ol<CR>
nnoremap <leader>a ggVG 

map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l

" Buffer stuff
map <leader>bd :Bclose<cr>:tabclose<cr>gT
map <leader>ba :bufdo bd<cr>
map gb :bnext<cr>
map gB :bprevious<cr>

" Tab stuff
map <leader>tn :tabnew<cr>
map <leader>to :tabonly<cr>
map <leader>tc :tabclose<cr>
map <leader>tm :tabmove
map <leader>t<leader> :tabnext

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Plugins
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
call plug#begin('~/AppData/Local/nvim/autoload/plugged')
    Plug 'folke/tokyonight.nvim', { 'branch': 'main' }
    Plug 'ryanoasis/vim-devicons'
    Plug 'SirVer/ultisnips'
    Plug 'honza/vim-snippets'
    Plug 'scrooloose/nerdtree'
    Plug 'mhinz/vim-startify'
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes' " tomorrow theme

    Plug 'tpope/vim-commentary'
    Plug 'tpope/vim-surround'
    Plug 'easymotion/vim-easymotion'
call plug#end()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => More stuff
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set nocompatible            " disable compatibility to old-time vi
set showmatch               " show matching 
set ignorecase              " case insensitive 
set mouse=v                 " middle-click paste with 
set hlsearch                " highlight search 
set incsearch               " incremental search
set tabstop=4               " number of columns occupied by a tab 
set softtabstop=4           " see multiple spaces as tabstops so <BS> does the right thing
set expandtab               " converts tabs to white space
set shiftwidth=4            " width for autoindents
set autoindent              " indent a new line the same amount as the line just typed
set signcolumn=yes
set scrolloff=10
set relativenumber
set nowrap
set number                  " add line numbers
set wildmode=longest,list   " get bash-like tab completions

set wildmenu
set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx

" open new split panes to right and below
set splitright
set splitbelow

set cc=100                 
filetype plugin indent on   "allow auto-indenting depending on file type
syntax on                   " syntax highlighting
set mouse=a                 " enable mouse click
filetype plugin on
set cursorline              " highlight current cursorline
set ttyfast                 " Speed up scrolling in Vim
" set spell                 " enable spell check (may need to download language package)
" set noswapfile            " disable creating swap file
" set backupdir=~/.cache/vim " Directory to store backup files.

set clipboard=unnamedplus   " using system clipboard
vnoremap <C-c> "+y
map <C-p> "+P

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Colors and Fonts
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Enable syntax highlighting
syntax enable

" Enable 256 colors palette in Gnome Terminal
if $COLORTERM == 'gnome-terminal'
    set t_Co=256
endif
set background=dark
" Set extra options when running in GUI mode
if has("gui_running")
    set guioptions-=T
    set guioptions-=e
    set t_Co=256
    set guitablabel=%M\ %t
endif
set encoding=utf8
" Use Unix as the standard file type
set ffs=unix,dos,mac
" plugin colorschemes needs to be after plugins btw 
colorscheme tokyonight-moon 
let g:airline_theme='tomorrow' " Statusbar Theme from Airline



" ###########################################
" Quick Install in Windows Vim Plug Github (winget install Neovim.Neovim)
" 1. Install with Powershell (use neovim)
" https://github.com/junegunn/vim-plug
"
" 2. Create the folders & 3. Create the init.vim in AppData/Local/nvim/init.vim
" mkdir ~\AppData\Local\nvim\autoload\plugged
" New-Item -Name init.vim -ItemType File
"
" Then run nvim and :PlugInstall
"
" ###########################################
"
" Quick Install in Linux Vim Plug Github
" 1. Install with Powershell (use neovim)
" https://github.com/junegunn/vim-plug
"
" 2. Create the folders & 3. Create the init.vim in AppData/Local/nvim/init.vim
" mkdir -p ~/.config/nvim/autoload/plugged ;  ; 
" touch ~/.config/nvim/init.vim
"
" Then run nvim and :PlugInstall
" ###########################################
