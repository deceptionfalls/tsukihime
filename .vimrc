" SETUP

" Mapping
let mapleader = ' '
let maplocalleader = ' '

set encoding=UTF-8
set term=screen-256color
set laststatus=2
set noshowmode
set number
set showcmd

" Highlight searched words
set showmatch
set hlsearch

" Line Break
set linebreak
set wrap
set wrapmargin=80

" Intellisense settings
set complete+=kspell
set completeopt=menuone,longest
set shortmess+=c

" Clipboard
set clipboard=unnamedplus

" No auto commenting
set formatoptions-=cro

" Casing settings
set mouse=a
set smartcase
set ignorecase

" Tab settings
set expandtab
set shiftwidth=2
set softtabstop=2
set tabstop=2

syntax on

" Lightline colorscheme
let g:lightline = { 'colorscheme': 'catppuccin_macchiato', }

" Make hidden directories shown by default
let g:NERDTreeShowHidden=1

if !has('gui_running')
  set t_Co=256
endif

" PLUGINS

call plug#begin('~/.vim/plugged')

" Colorscheme
Plug 'catppuccin/vim', { 'as': 'catppuccin' }
Plug 'dylanaraps/wal.vim'

" NERDtree for file browsing
Plug 'preservim/nerdtree' |
	\ Plug 'Xuyuanp/nerdtree-git-plugin'

" lightline for our statusbar
Plug 'itchyny/lightline.vim'

" vim-commentary
Plug 'tpope/vim-commentary'

" Intellisense
Plug 'vim-scripts/AutoComplPop'

" For typing brackets or single quotes
Plug 'Raimondi/delimitMate'

" Zen mode
Plug 'junegunn/goyo.vim'
Plug 'junegunn/limelight.vim'
Plug 'amix/vim-zenroom2'

" Javascript support
Plug 'pangloss/vim-javascript'
Plug 'w0rp/ale'
Plug 'yuezk/vim-js'

" Markdown support
Plug 'godlygeek/tabular'
Plug 'preservim/vim-markdown'

" HTML Snippets
Plug 'mattn/emmet-vim'

" Splash Screen
Plug 'mhinz/vim-startify'

" Highlight on yank
Plug 'machakann/vim-highlightedyank'

" Surround
Plug 'tpope/vim-surround'

" Discord RPC
Plug 'vbe0201/vimdiscord'

call plug#end()

" Colorscheme
colorscheme wal

" Quit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

" Close the tab if NERDTree is the only window remaining in it.
autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

" ESLint
let g:ale_sign_error = 'X'
let g:ale_sign_warning = '!'
highlight ALEErrorSign ctermbg=NONE ctermfg=red
highlight ALEWarningSign ctermbg=NONE ctermfg=yellow

" KEYBINDS

" Go to end/beginning of line
nnoremap <leader>l $
nnoremap <leader>h 0

" Reload config or Reload plugins
nnoremap <silent> <leader>r :source "~/.vimrc"<CR>
nnoremap <silent> <leader>q :PlugInstall<CR>

" Clear search highlight
map <leader>g :nohlsearch<CR>

" Write and Quit
map <leader>w :w<CR>
map <leader>c :q<CR>
nnoremap <SPACE> <Nop>

" Spellchecking
map <leader>s :setlocal spell! spelllang=en_au<CR>

" Lint current file
noremap <leader>u :make % <CR>:cwindow<CR>:redraw!<CR>
noremap <leader>ui :make --fix % <CR>:cwindow<CR>:redraw!<CR>

" Intellisense
inoremap <expr> <C-k> pumvisible() ? "<C-p>" :"<Up>"
inoremap <expr> <C-j> pumvisible() ? "<C-n>" :"<Down>"
inoremap <expr> <C-h> pumvisible() ? "<C-y>" :"<Right>"
inoremap <expr> <CR> pumvisible() ? "<C-y>" :"<CR>"
inoremap <expr> <C-l> pumvisible() ? "<C-e>" :"<Left>"

" Goyo
map <silent> <leader>z :Goyo<cr>

" NERDTree 
map <leader>e :NERDTreeToggle<CR>

" Pywal for lightline
set laststatus=2
let g:lightline = {
       \ 'colorscheme': 'wal',
       \ }
