[app]

# App info
title = My App
package.name = myapp
package.domain = org.test

# Source
source.dir = .
source.include_exts = py,png,jpg,kv

# Version
version = 1.0

# Requirements (ONLY ONE LINE!)
requirements = python3,kivy,kivymd

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Permissions (optional)
android.permissions = INTERNET

# Android API
android.api = 31
android.minapi = 21

# Bootstrap
android.bootstrap = sdl2

# Log level
log_level = 2


[buildozer]

# Log level
log_level = 2

# Warn on root
warn_on_root = 1
