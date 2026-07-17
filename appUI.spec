[app]

title = Gesture Communication
package.name = gestureapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,plyer,pyjnius

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