" Basic stuff
set encoding=UTF-8
set term=screen-256color
set termguicolors
set laststatus=2
set noshowmode
set number
if !has('gui_running')
  set t_Co=256
endif

call plug#begin('~/.vim/plugged')

" Colorscheme
Plug 'catppuccin/vim', { 'as': 'catppuccin' }

" NERDtree for file browsing
Plug 'preservim/nerdtree' |
	\ Plug 'Xuyuanp/nerdtree-git-plugin' |
	\ Plug 'ryanoasis/vim-devicons'

" lightline for a statusbar
Plug 'itchyny/lightline.vim'

" vim-commentary
Plug 'tpope/vim-commentary'

" Zen mode
Plug 'junegunn/goyo.vim'
Plug 'amix/vim-zenroom2'

" Intellisense setup
Plug 'ncm2/ncm2'
Plug 'roxma/nvim-yarp'
Plug 'ncm2/ncm2-bufword'
Plug 'ncm2/ncm2-path'
Plug 'prabirshrestha/vim-lsp'
Plug 'ncm2/ncm2-vim-lsp'

" Javascript support
Plug 'pangloss/vim-javascript'
Plug 'ncm2/ncm2-tern',  {'do': 'npm install'}

" HTML Snippets
Plug 'mattn/emmet-vim'

" Emojis
Plug 'subnut/ncm2-github-emoji'

" Splash Screen
Plug 'mhinz/vim-startify'

call plug#end()

colorscheme catppuccin_macchiato

" Lightline settings
let g:lightline = { 'colorscheme': 'catppuccin_macchiato', }

nnoremap <SPACE> <Nop>

" Keybinds
let mapleader = ' '
map <leader>w :w<CR>
map <leader>c :q<CR>
map <leader>e :NERDTreeToggle<CR>
map <silent> <leader>z :Goyo<cr>
map <C-h> :NERDTreeFocus<CR>
