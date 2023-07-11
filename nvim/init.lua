-- Init.lua :moon:
-- This config is meant to be fragmented and separated into multiple files, so customizing it and switching out parts and pieces becomes easier

require("core.conf")        -- main config
require("core.conf-legacy") -- legacy vim settings
require("core.keys")        -- keybinds
require("plugin.lazy")      -- lazy
require("plugin.themes")    -- colorschemes + ui
require("plugin.lsp")       -- lsps

vim.g.mapleader = ' ' -- Leader key

-- Plugin setup
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end

vim.opt.rtp:prepend(lazypath)

require("lazy").setup("plugins")

-- KEYBINDS

-- W to save and C to quit
vim.api.nvim_set_keymap('n', '<leader>w', ':w<CR>', {noremap = true})
vim.api.nvim_set_keymap('n', '<leader>c', ':q<CR>', {noremap = true})

-- Go to end/beginning of line
vim.api.nvim_set_keymap('n', '<leader>l', '$', {noremap = true})
vim.api.nvim_set_keymap('n', '<leader>h', '0', {noremap = true})

-- Clear search highlight
vim.api.nvim_set_keymap('n', '<leader>g', ':nohlsearch<CR>', {noremap = true})

-- Spellchecking
vim.api.nvim_set_keymap('n', '<leader>s', ':setlocal spell! spelllang=en_au<CR>', {noremap = true})

-- MISC
vim.cmd('set number') -- Line numbers
vim.cmd('set showmatch') -- Show matched words
vim.cmd('set hlsearch') -- Show matched letters
vim.cmd('set showcmd') -- Show command

vim.cmd('set linebreak')
vim.cmd('set wrap')
vim.cmd('set wrapmargin=80')

-- Intellisense
vim.cmd('set complete+=kspell')
vim.cmd('set completeopt=menuone,longest')
vim.cmd('set shortmess+=c')

-- No auto commenting
vim.cmd('set formatoptions-=cro')

-- Casing settings
vim.cmd('set mouse=a')
vim.cmd('set smartcase')
vim.cmd('set ignorecase')

-- Tab settings
vim.cmd('set expandtab')
vim.cmd('set shiftwidth=2')
vim.cmd('set softtabstop=2')
vim.cmd('set tabstop=2')

-- Syntax highlighting
vim.cmd('syntax on')

-- Clipboard
vim.cmd('set clipboard=unnamedplus')

-- PLUGIN CONFIG

-- Pywal
local pywal = require('pywal')
pywal.setup()

-- Lualine
require('lualine').setup()
local lualine = require('lualine')

lualine.setup {
  options = {
    theme = 'pywal-nvim',
  },
}

-- Barbecue
require("barbecue.ui").toggle(true)
vim.opt.updatetime = 200

require("barbecue").setup({
  create_autocmd = false, -- prevent barbecue from updating itself automatically
})

vim.api.nvim_create_autocmd({
  "WinScrolled", -- or WinResized on NVIM-v0.9 and higher
  "BufWinEnter",
  "CursorHold",
  "InsertLeave",
}, {
  group = vim.api.nvim_create_augroup("barbecue.updater", {}),
  callback = function()
    require("barbecue.ui").update()
  end,
})

-- Cursorline
require('nvim-cursorline').setup {
  cursorline = {
    enable = true,
    timeout = 1000,
    number = false,
  },
  cursorword = {
    enable = true,
    min_length = 3,
    hl = { underline = true },
  }
}
