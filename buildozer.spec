[app]
title = Tigreship
package.name = tigreship
package.domain = ca.deuxpi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_patterns = *_test.py
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py
requirements = kivy
orientation = landscape
fullscreen = 1
android.ndk_path = /home/phil/android-ndk-r10d
android.sdk_path = /home/phil/android-studio/sdk

[buildozer]
log_level = 1
warn_on_root = 1
