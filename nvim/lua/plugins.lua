return {
  {
    -- Colorscheme
    "AlphaTechnolog/pywal.nvim",
  },
  {
    -- File Explorer
    "luukvbaal/nnn.nvim",
  },
  {
    -- Dashboard
    'glepnir/dashboard-nvim',
    event = 'VimEnter',
    config = function()
      require('dashboard').setup {
        -- config
      }
    end,
    dependencies = { {'nvim-tree/nvim-web-devicons'}}
  },
  {
    -- Statusline
    "nvim-lualine/lualine.nvim",
  },
  {
    "utilyre/barbecue.nvim",
    name = "barbecue",
    version = "*",
    dependencies = {
      "SmiteshP/nvim-navic",
      "nvim-tree/nvim-web-devicons", -- optional dependency
    },
    opts = {
      -- configurations go here
    },
  },
  {
    "yamatsum/nvim-cursorline",
  },
}
