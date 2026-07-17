[app]

title = My App

package.name = myapp
package.domain = org.test

source.dir = .

source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,kivymd,pyjnius

orientation = portrait

fullscreen = 0


android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_SCAN,BLUETOOTH_CONNECT


android.api = 35
android.minapi = 23
android.ndk = 25c


p4a.bootstrap = sdl2


log_level = 2


[buildozer]

log_level = 2
warn_on_root = 1