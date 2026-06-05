[app]

# Application name
title = GhostForge IDE

# Package name (must be unique)
package.name = ghostforge

# Package domain
package.domain = com.ghostforge

# Source directory
source.dir = .

# Source includes
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,ttf,otf,json,yaml,yml,csv

# Version
version = 1.0.0

# Python requirements
requirements = python3,kivy

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Icon (optional)
icon.filename = %(source.dir)s/icon.png

# Presplash (optional)
presplash.filename = %(source.dir)s/presplash.png

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# Features
android.features = 

# Android API levels
android.api = 31
android.minapi = 21
android.ndk = 21c

# Android archs
android.archs = arm64-v8a,armeabi-v7a

# Gradle
android.gradle_dependencies = 

# AndroidX
android.enable_androidx = True

# Copy libs
android.copy_libs = 1

# Java classes
android.add_src = 

# Log level
log_level = 2

# Warn on root
warn_on_root = 1

[buildozer]

# Log level
log_level = 2

# Warn on root
warn_on_root = 1

# Build directory
# build_dir = .buildozer

# Bin directory
# bin_dir = ./bin
