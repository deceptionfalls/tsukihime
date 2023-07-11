-- Legacy Vim settings, includes vimscript stuff

vim.cmd [[
  " you would normally use `set termguicolors` here but it breaks my pywal theme
  map <leader>g :nohlsearch<CR>
  map <leader>w :w<CR>
  map <leader>c :q<CR>
  nnoremap <SPACE> <Nop>
  map <leader>s :setlocal spell! spelllang=en_au<CR>
]]
