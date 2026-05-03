[app]
title = My Word
package.name = myword
package.domain = org.myword
source.dir = .
source.include_exts = py,kv
version = 1.3

requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0

android.minapi = 24
android.api = 33
android.ndk = 25b
android.ndk_api = 24

android.permissions = INTERNET
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.enable_androidx = True

# Mali GPU fix for Realme/ColorOS
android.add_jars =
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
