import os
import io
import time

# Настройки через переменные окружения
SEND_INTERVAL = int(os.getenv("SEND_INTERVAL", 2))  # Интервал отправки сообщений (по умолчанию 2 сек)
LOG_FILE = os.getenv("LOG_FILE", "log.txt")  # Файл логов

class FakeSerial(io.StringIO):
    def __init__(self):
        super().__init__()
        self.buffer = ""

    def write(self, data):
        print(f"➡️ Отправлено: {data.strip()}")
        with open(LOG_FILE, "a") as f:
            f.write(f"➡️ Отправлено: {data.strip()}\n")
        self.buffer = data

    def readline(self):
        time.sleep(1)
        if self.buffer:
            print(f"📥 Читаем: {self.buffer.strip()}")
            with open(LOG_FILE, "a") as f:
                f.write(f"📥 Читаем: {self.buffer.strip()}\n")
            return self.buffer
        return ""

fake_serial = FakeSerial()

def writer():
    while True:
        fake_serial.write("Hello from Python!\n")
        time.sleep(SEND_INTERVAL)

def reader():
    while True:
        data = fake_serial.readline().strip()
        if data:
            print(f"📩 Принято: {data}")
        time.sleep(1)

import threading
threading.Thread(target=writer, daemon=True).start()
reader()
