[app]
title = My Word
package.name = myword
package.domain = org.myword
source.dir = .
source.include_exts = py,kv,json,png,jpg,ttf
version = 1.1

# KivyMD 1.1.1 requires exactly Kivy 2.2.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1,plyer,pillow

orientation = portrait
fullscreen = 0

android.minapi = 24
android.api = 33
android.ndk = 25b
android.ndk_api = 24

# Android 16 / ColorOS needs these intent declarations
android.manifest.intent_filters = <intent-filter><action android:name="android.intent.action.VIEW"/><category android:name="android.intent.category.DEFAULT"/><category android:name="android.intent.category.BROWSABLE"/></intent-filter>

# Scoped storage for Android 13+ compatibility
android.permissions = INTERNET, READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, READ_MEDIA_AUDIO

android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
