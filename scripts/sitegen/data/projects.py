# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Open-source projects, grouped. Gitea links where Gitea is canonical."""
from .models import Group, Item

GT = "https://git.rootiest.dev/rootiest/"
GH = "https://github.com/rootiest/"

# ╭──────────────────────────────────────────────────────────╮
# │                    Terminal and editor                   │
# ╰──────────────────────────────────────────────────────────╯
TERMINAL = Group("Terminal &amp; editor", "peach", (
    Item("Fish Config", GT + "fish-config", "fish",
         "A modular, guard-railed Fish shell configuration with full documentation.", ("Shell", "Gitea")),
    Item("Neovim Config", GT + "neovim-config", "square-terminal",
         "The Rootiest Neovim setup, tuned for everyday development, with a printable cheatsheet.",
         ("Editor", "Gitea")),
    Item("Dotfiles", GT + "dotfiles", "package",
         "Brings a fresh Linux machine to a working state with chezmoi, cloning each Rootiest config into place.",
         ("chezmoi", "Gitea")),
    Item("Tmux Config", GT + "tmux-config", "panels-top-left", "The Rootiest tmux configuration.",
         ("Terminal", "Gitea")),
    Item("Kitty Config", GT + "kitty-config", "cat", "The Rootiest kitty terminal configuration.",
         ("Terminal", "Gitea")),
    Item("Ghostty Config", GT + "ghostty-config", "ghost", "The Rootiest Ghostty terminal configuration.",
         ("Terminal", "Gitea")),
    Item("WezTerm Config", GT + "wezterm-config", "terminal", "The Rootiest WezTerm configuration.",
         ("Terminal", "Gitea")),
    Item("Lazygit Config", GT + "lazygit-config", "git-commit-horizontal",
         "Catppuccin theme, difftastic diffs and a Conventional Commits form for lazygit.", ("Git", "Gitea")),
    Item("Hyprland Config", GT + "hypr-config", "app-window", "Hyprland desktop configuration (work in progress).",
         ("Desktop", "Gitea")),
    Item("Rootiest Iosevka", GT + "rootiest-iosevka", "type",
         "A custom Iosevka font variant built for terminals and editors.", ("Font", "Gitea")),
))

# ╭──────────────────────────────────────────────────────────╮
# │                       Tools and apps                     │
# ╰──────────────────────────────────────────────────────────╯
TOOLS = Group("Tools &amp; apps", "mauve", (
    Item("Rootiest AI Plugins", GT + "rootiest-ai", "sparkles",
         "Plugins and skills for Claude Code and other AI coding agents.", ("Agent plugins", "Gitea")),
    Item("Claude Tokenization Proxy", GT + "claude-tokenization-proxy", "shield-check",
         "Masks secrets locally before they reach the Claude API, then restores them in replies.",
         ("Tool", "Gitea")),
    Item("Rootiest Status for Android", GT + "rootiest-status-android", "smartphone",
         "Native Android client for status.rootiest.dev, with a widget and notifications.", ("Android", "Gitea")),
    Item("Color Tool", GT + "color-tool", "pipette",
         "Portable CLI for picking, converting and formatting colours on KDE Plasma and Wayland.", ("CLI", "Gitea")),
    Item("Icon Color Tool", GT + "icon-color-tool", "palette",
         "GTK4 app for editing the colour scheme embedded in Breeze icon SVGs.", ("Desktop app", "Gitea")),
    Item("nvim-updater.nvim", GH + "nvim-updater.nvim", "refresh-cw",
         "Build and update Neovim from source, from inside Neovim.", ("Neovim plugin", "GitHub")),
    Item("NeoTerm", GH + "neoterm", "terminal", "Use Neovide as a traditional terminal emulator.",
         ("Tool", "GitHub")),
    Item("Obsidian AI Image OCR", GH + "obsidian-ai-image-ocr", "scan-text",
         "Obsidian plugin for AI-powered text extraction from images.", ("Obsidian plugin", "GitHub")),
))

# ╭──────────────────────────────────────────────────────────╮
# │                   Keyboards and hardware                 │
# ╰──────────────────────────────────────────────────────────╯
HARDWARE = Group("Keyboards &amp; hardware", "lavender", (
    Item("QMK Cheatsheet", "https://qmk.rootiest.fyi", "keyboard",
         "Layer and shortcut reference for the Rootiest QMK keyboards.", ("qmk.rootiest.fyi",)),
    Item("Heartbeat 60Hz", GT + "heartbeat-60hz", "radar",
         "ESPHome config for a 60 GHz mmWave presence and vital-signs sensor, built for Home Assistant.",
         ("ESPHome", "Gitea")),
    Item("CANBurner", GH + "CANburner", "cpu", "A CAN bus adapter PCB for 3D printers.", ("Hardware", "GitHub")),
))

# ╭──────────────────────────────────────────────────────────╮
# │                    Klipper and printing                  │
# ╰──────────────────────────────────────────────────────────╯
KLIPPER = Group("Klipper &amp; 3D printing", "sky", (
    Item("PrintCFG", GH + "printcfg", "settings", "A suite of macros to enhance the Klipper experience.",
         ("Klipper macros", "GitHub")),
    Item("Zippy Klipper Config", GH + "zippy-klipper_config", "printer",
         "Klipper configurations, macros and tuning.", ("Klipper config", "GitHub")),
    Item("Zippy Guides", GH + "zippy_guides", "book-open", "Guides for all things Klipper.", ("Docs", "GitHub")),
    Item("Klipper Scripts", GH + "klipper-scripts", "scroll-text",
         "Scripts that simplify userspace modification of Klipper.", ("Scripts", "GitHub")),
), "Older projects from the Klipper community, kept online for the people who still use them.")

GROUPS = (TERMINAL, TOOLS, HARDWARE, KLIPPER)

# Shown on the home page, in this order.
FEATURED = ("Fish Config", "Neovim Config", "Rootiest AI Plugins", "Claude Tokenization Proxy",
            "Dotfiles", "Rootiest Status for Android")
