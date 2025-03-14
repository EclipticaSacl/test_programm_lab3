import io
import time

class FakeSerial(io.StringIO):
    def __init__(self):
        super().__init__()
        self.buffer = ""

    def write(self, data):
        print(f"➡️ Отправлено: {data.strip()}")
        with open("log.txt", "a") as f:
            f.write(f"➡️ Отправлено: {data.strip()}\n")
        self.buffer = data

    def readline(self):
        time.sleep(1)
        if self.buffer:
            print(f"📥 Читаем: {self.buffer.strip()}")
            with open("log.txt", "a") as f:
                f.write(f"📥 Читаем: {self.buffer.strip()}\n")
            return self.buffer
        print("⌛ Ожидание данных...")
        return ""

# Создаём "виртуальный порт"
fake_serial = FakeSerial()

def writer():
    while True:
        fake_serial.write("Hello from Python!\n")
        time.sleep(2)

def reader():
    while True:
        data = fake_serial.readline().strip()
        if data:
            print(f"📩 Принято: {data}")
        time.sleep(1)

import threading
threading.Thread(target=writer, daemon=True).start()
reader()
