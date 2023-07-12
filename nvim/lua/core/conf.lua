-- Legacy Vim settings, includes vimscript stuff

vim.cmd [[
  " you would normally use `set termguicolors` here but it breaks my pywal theme
  map <leader>g :nohlsearch<CR>
  map <leader>w :w<CR>
  map <leader>c :q<CR>
  nnoremap <SPACE> <Nop>
  map <leader>s :setlocal spell! spelllang=en_au<CR>
]]

-- Lua options

vim.g.mapleader = " "                   -- leader key
vim.o.hlsearch = true                   -- highlight search
vim.o.sh = "zsh"                        -- default shell
vim.wo.number = true                    -- line numbers
vim.o.mouse = 'a'                       -- mouse
vim.o.clipboard = 'unnamedplus'         -- clipboard
vim.o.breakindent = true                -- break indentation
vim.o.undofile = true                   -- saving undo history
vim.wo.signcolumn = 'yes'               -- signcolumn off
vim.o.completeopt = 'menuone,noselect'  -- autocompletion

-- Case insensitive searching
vim.o.ignorecase = true
vim.o.smartcase = true

-- Update time
vim.o.updatetime = 250  
vim.o.timeout = true
vim.o.timeoutlen = 250  

-- Tab behavior
vim.o.tabstop = 4
vim.o.shiftwidth = 4
vim.o.softtabstop = 4
vim.o.expandtab = true

vim.keymap.set({ 'n', 'v' }, '<Space>', '<Nop>', { silent = true })

-- Word wrap remap
vim.keymap.set('n', 'k', "v:count == 0 ? 'gk' : 'k'", { expr = true, silent = true })
vim.keymap.set('n', 'j', "v:count == 0 ? 'gj' : 'j'", { expr = true, silent = true })

-- Highlighting when yanking
local highlight_group = vim.api.nvim_create_augroup('YankHighlight', { clear = true })
vim.api.nvim_create_autocmd('TextYankPost', {
  callback = function()
    vim.highlight.on_yank()
  end,
  group = highlight_group,
  pattern = '*',
})
