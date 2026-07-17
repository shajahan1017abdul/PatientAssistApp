[app]

title = Gesture Communication
package.name = gestureapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,kivymd

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b

android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,INTERNET

# IMPORTANT: Fix Bluetooth for Android 12+
android.enable_androidx = True

# Reduce errors
log_level = 2

# Skip problematic builds
android.gradle_dependencies = 

# Faster builds
p4a.branch = stable
requirements = python3,kivy,plyer

android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,INTERNET

android.gradle_dependencies = 'androidx.core:core:1.9.0'

android.minapi = 21
android.api = 33
android.ndk = 25b
