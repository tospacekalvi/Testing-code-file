from mfrc522 import MFRC522
import utime

# Your same initialization (SPI0 pins)
reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)

print("\n📡 RFID Continuous Detection Mode")
print("Show card to reader...\n")

while True:
    try:
        reader.init()  # keep reinitializing for clone stability

        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card = int.from_bytes(bytes(uid), "little", False)
                print("✅ CARD DETECTED:", card)
            else:
                print("❌ NO CARD DETECTED")
        else:
            print("❌ NO CARD DETECTED")

        utime.sleep_ms(400)  # loop delay

    except Exception as e:
        print("⚠️ Error:", e)
        utime.sleep(1)
