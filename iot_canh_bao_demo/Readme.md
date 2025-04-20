# Hệ thống cảnh báo cửa mở - IoT Project

##  Yêu cầu
- Python 3.10+
- Môi trường ảo: `python -m venv counterfit_env`
- Kích hoạt: `counterfit_env\Scripts\activate`
- Cài đặt module:
    pip install -r requirements.txt

##  Thiết bị mô phỏng (CounterFit)
- LED cảnh báo (D4)
- Grove Light Sensor (A0)
- Grove Button (D2)

## ▶ Cách chạy
1. Bật CounterFit: `counterfit`
2. Gán cảm biến đúng chân trên giao diện web (http://localhost:5000)
3. Chạy code:
    python main.py

##  Tích hợp hệ thống
- Platform: Mainflux (chạy Docker đã setup ổn)
- Giao tiếp: Có thể tích hợp thêm HTTP/MQTT gửi dữ liệu đến Mainflux hoặc hiển thị dashboard riêng (tuỳ nâng cấp).

## Mô tả:

Mô phỏng hệ thống cảnh báo cửa mở sử dụng CounterFit (giả lập thiết bị) và hiển thị dữ liệu thời gian thật qua Docker + MQTT + Telegraf + InfluxDB + Grafana.

 Công nghệ sử dụng:

CounterFit (mô phỏng thiết bị Grove)

Python + Paho MQTT

Mosquitto MQTT broker (container)

Telegraf (thu thập dữ liệu)

InfluxDB 1.8

Grafana (dashboard)

 Thiết bị giả lập:

Grove Button (cửa mở)

Grove LED (loa cảnh báo)

Grove Light Sensor (môi trường)

 Cách chạy hệ thống

# B1: Clone repo và vào thư mục
cd iot-canhbaomocua

# B2: Khởi chạy Docker
docker-compose up -d

# B3: Kết nối CounterFit
python main.py

# B4: Truy cập dashboard:
http://localhost:3000 (user/pass: admin)

💡 Một số lệnh MQTT hỗ trợ:

# Tắt cảnh báo
mosquitto_pub -h localhost -t iot/control -m "disable_alert"

# Bật cảnh báo
mosquitto_pub -h localhost -t iot/control -m "enable_alert"

# Tham khảo
Dự án gốc Mainflux: https://github.com/hieu079/LT_IOT
CounterFit: https://github.com/CounterFit-IoT/CounterFit

> ✅ Tình trạng hiện tại: Hoàn thành chức năng cảnh báo + bật/tắt từ xa + dashboard. Có thể demo hoạt động thực tế trên localhost hoặc quay video minh hoạ.