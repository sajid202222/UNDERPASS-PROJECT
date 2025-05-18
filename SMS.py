import serial
from twilio.rest import Client

# Twilio credentials
ACCOUNT_SID = 'ACdc8f0d8acd73d47741c6745f8b89ebf0'
AUTH_TOKEN = '492cb98c3e3049d6a04c9925900b9084'
TWILIO_PHONE_NUMBER = '+16087057947'
TO_PHONE_NUMBER = '+918088845950'


UNDERPASS_LAT = "12.9716"
UNDERPASS_LON = "77.5946"


print("Serial module is working!")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)


sms_sent_water = False
sms_sent_rain = False

def send_sms(alert_message):
    try:
        message = client.messages.create(
            body=alert_message,
            from_=TWILIO_PHONE_NUMBER,
            to=TO_PHONE_NUMBER
        )
        print(f"SMS sent: SID {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

print("Listening for alerts...")

while True:
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        print(f"Received from Arduino: {line}")

        try:

            if "Distance:" in line:
                distance = float(line.split(":")[1].strip())

                if distance <= 7:
                    if not sms_sent_water:
                        alert_message = (
                            f"Alert: Water level is high in the underpass! "
                            f"Water Level: {distance} cm. "
                            f"Location: https://www.google.com/maps?q={UNDERPASS_LAT},{UNDERPASS_LON}"
                        )
                        send_sms(alert_message)
                        sms_sent_water = True
                else:
                    sms_sent_water = False

            elif "Humidity:" in line:
                humidity = float(line.split(":")[1].strip().split("%")[0])

                if humidity > 80:
                    if not sms_sent_rain:
                        alert_message = f"Alert: Humidity exceeds 80%! Rain might occur. Humidity: {humidity}%."
                        send_sms(alert_message)
                        sms_sent_rain = True
                else:
                    sms_sent_rain = False

        except ValueError:
            print("Invalid data received; ignoring.")
