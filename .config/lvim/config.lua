-- Read the docs: https://www.lunarvim.org/docs/configuration
-- Video Tutorials: https://www.youtube.com/watch?v=sFA9kX-Ud_c&list=PLhoH5vyxr6QqGu0i7tt_XoVK9v-KvZ3m6
-- Forum: https://www.reddit.com/r/lunarvim/
-- Discord: https://discord.com/invite/Xb9B4Ny

lvim.plugins = {
  "jaeheonji/catppuccin-nvim",
  {
    "Pocco81/auto-save.nvim",
    config = function()
      require("auto-save").setup()
    end,
  },
  -- You must install glow globally
  -- https://github.com/charmbracelet/glow
  -- yay -S glow
  {
    "npxbr/glow.nvim",
    ft = {"markdown"}
    -- build = "yay -S glow"
  },
  {
    "ethanholz/nvim-lastplace",
    event = "BufRead",
    config = function()
     require("nvim-lastplace").setup({
      lastplace_ignore_buftype = { "quickfix", "nofile", "help" },
      lastplace_ignore_filetype = {
       "gitcommit", "gitrebase", "svn", "hgcommit",
      },
      lastplace_open_folds = true,
     })
    end,
  },

}

lvim.colorscheme = 'catppuccin'

