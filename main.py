import time
from pywintrace import ETW, ProviderInfo, GUID

def callback(event):
    print("Yangi sysmon log")
    print("🆔 Event ID:", event)

provider = ProviderInfo(
    "Microsoft-Windows-Sysmon",
    GUID("{5770385f-c22a-43e0-bf4c-06f5698ffbd9}")
)
etw = ETW(providers=[provider], event_callback=callback)
print("🔍 Sysmon tinglanmoqda... (Ctrl+C to'xtatadi)")
etw.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("⛔ To‘xtatildi.")
    etw.stop()
