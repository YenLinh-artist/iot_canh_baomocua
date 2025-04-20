from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_button import GroveButton
import time
import paho.mqtt.client as mqtt
import json

# Kết nối CounterFit
CounterFitConnection.init("127.0.0.1", 5000)

# Khai báo thiết bị
light_sensor = GroveLightSensor(0)
button = GroveButton(2)
led = GroveLed(4)

# Biến trạng thái cảnh báo
alert_enabled = True

# Hàm xử lý lệnh điều khiển từ hệ thống
def on_message(client, userdata, msg):
    global alert_enabled
    message = msg.payload.decode().lower()
    print(f"[MQTT] Nhận lệnh: {message}")

    if message == "disable_alert":
        alert_enabled = False
        print("[MQTT] Cảnh báo đã bị tắt từ hệ thống.")

    elif message == "enable_alert":
        alert_enabled = True
        print("[MQTT] Cảnh báo đã được bật từ hệ thống.")

# Kết nối MQTT Broker
mqtt_client = mqtt.Client()
def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Kết nối broker: {rc}")
    if rc == 0:
        print("[MQTT] Kết nối thành công.")
        client.subscribe("iot/control")
        print("[MQTT] Đã subscribe topic iot/control")
    else:
        print("[MQTT] Kết nối thất bại.")
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.loop_start()


print("Hệ thống cảnh báo cửa mở đang chạy...\n")

while True:
    # Đọc dữ liệu từ cảm biến
    light = light_sensor.light
    door_opened = button.is_pressed()

    # Hiển thị trạng thái
    print(f"Ánh sáng: {light:.2f} lux | Cửa mở: {'Có' if door_opened else 'Không'} | Cảnh báo: {'Bật' if alert_enabled else 'Tắt'}")

    # Xử lý cảnh báo nếu được bật
    if door_opened and alert_enabled:
        print("\n>>> CẢNH BÁO: CỬA ĐANG MỞ! <<<\n")
        led.on()
    else:
        led.off()

    # Gửi dữ liệu qua MQTT
    payload = {
    "light": round(light, 2),
    "door_open": int(door_opened),         # true → 1, false → 0
    "alert_enabled": int(alert_enabled)    # true → 1, false → 0
}
    mqtt_client.publish("iot/canhbao", json.dumps(payload))
    time.sleep(1)


