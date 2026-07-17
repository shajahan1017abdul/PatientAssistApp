import threading
from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.metrics import sp, dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.utils import platform

try:
    from plyer import tts
except:
    tts = None

HC05_NAME = "HC-05"
UUID_STR = "00001101-0000-1000-8000-00805F9B34FB"

STATE_COLORS = {
    "HELP": (0.86, 0.08, 0.24, 1),
    "WATER": (0.05, 0.13, 0.45, 1),
    "FOOD": (0.9, 0.55, 0.02, 1),
    "RESTROOM": (0.29, 0.0, 0.51, 1),
    "IDLE": (0.4, 0.4, 0.42, 1),
}

class AppUI(App):

    def build(self):
        Window.clearcolor = (0.05, 0.05, 0.07, 1)

        self.socket = None
        self.connected = False

        root = BoxLayout(orientation="vertical", padding=dp(5))

        # STATUS CARD
        self.card = BoxLayout(size_hint_y=0.5)
        with self.card.canvas.before:
            self.color = Color(*STATE_COLORS["IDLE"])
            self.rect = Rectangle(pos=self.card.pos, size=self.card.size)
        self.card.bind(pos=self.update_rect, size=self.update_rect)

        self.label = Label(text="IDLE", font_size=sp(40))
        self.card.add_widget(self.label)
        root.add_widget(self.card)

        # BUTTON
        self.btn = Button(text="Connect Bluetooth", size_hint_y=0.1)
        self.btn.bind(on_press=self.connect_bt)
        root.add_widget(self.btn)

        # LOG
        self.log_box = GridLayout(cols=1, size_hint_y=None)
        self.log_box.bind(minimum_height=self.log_box.setter("height"))

        scroll = ScrollView(size_hint_y=0.4)
        scroll.add_widget(self.log_box)
        root.add_widget(scroll)

        return root

    def update_rect(self, *args):
        self.rect.pos = self.card.pos
        self.rect.size = self.card.size

    def log(self, msg):
        time = datetime.now().strftime("%H:%M:%S")
        lbl = Label(text=f"[{time}] {msg}", size_hint_y=None, height=30)
        self.log_box.add_widget(lbl)

    def connect_bt(self, instance):
        if platform != "android":
            self.log("Run on Android only")
            return

        threading.Thread(target=self.bt_thread, daemon=True).start()

    def bt_thread(self):
        try:
            from jnius import autoclass

            BluetoothAdapter = autoclass("android.bluetooth.BluetoothAdapter")
            UUID = autoclass("java.util.UUID")
            BufferedReader = autoclass("java.io.BufferedReader")
            InputStreamReader = autoclass("java.io.InputStreamReader")

            adapter = BluetoothAdapter.getDefaultAdapter()

            devices = adapter.getBondedDevices().toArray()
            device = None

            for d in devices:
                if HC05_NAME in d.getName():
                    device = d
                    break

            if not device:
                Clock.schedule_once(lambda dt: self.log("HC-05 not paired"))
                return

            socket = device.createRfcommSocketToServiceRecord(UUID.fromString(UUID_STR))
            socket.connect()

            self.socket = socket
            self.connected = True

            Clock.schedule_once(lambda dt: self.log("Connected"))

            reader = BufferedReader(InputStreamReader(socket.getInputStream()))

            while True:
                line = reader.readLine()
                if not line:
                    break
                cmd = line.strip().upper()
                Clock.schedule_once(lambda dt: self.update_ui(cmd))

        except Exception as e:
            Clock.schedule_once(lambda dt: self.log(f"Error: {e}"))

    def update_ui(self, cmd):
        if cmd not in STATE_COLORS:
            return

        self.label.text = cmd
        self.color.rgba = STATE_COLORS[cmd]
        self.log(f"Received: {cmd}")

        if tts:
            threading.Thread(target=lambda: tts.speak(cmd)).start()


if __name__ == "__main__":
    AppUI().run()