import time
from twilio.rest import Client

# --- Client 1: Sends alert SMS ---
ACCOUNT_SID_1 = 'XXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN_1 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
TWILIO_PHONE_1 = '+1XXXXXXX'
TO_NUMBER_1 = '+91XXXXXXX'

client1 = Client(ACCOUNT_SID_1, AUTH_TOKEN_1)

def send_alert_sms(location="Rajajinagar", water_level_cm=48):
    route_link = "https://maps.app.goo.gl/EHLmJFhTc2SGstMk9"

    message = (
        f"Flood alert at {location}.\n"
        f"The Underpass is Flooded with Water level of: {water_level_cm}cm.\n"
        f"Choose Alternative route: {route_link}.\n\n"
        f"Warning! Please stay in your vehicle and wait until water is cleared. Do NOT attempt to cross. Stay safe!!"
    )

    try:
        sms = client1.messages.create(
            body=message,
            from_=TWILIO_PHONE_1,
            to=TO_NUMBER_1
        )
        print(f"✅ Alert sent by Client 1: {sms.sid}")
    except Exception as e:
        print(f"❌ Client 1 failed: {e}")

def send_safe_to_pass_sms(location="Rajajinagar"):
    message = (
        f"The water level at the {location} underpass is decreasing.\n"
        f"The underpass is now safe to pass. Proceed with caution."
    )
    try:
        sms = client1.messages.create(
            body=message,
            from_=TWILIO_PHONE_1,
            to=TO_NUMBER_1
        )
        print(f"✅ Safe-to-pass message sent by Client 1: {sms.sid}")
    except Exception as e:
        print(f"❌ Safe-to-pass message failed: {e}")

# --- Client 2: Sends general info SMS after 30 seconds ---
ACCOUNT_SID_2 = 'AC9XXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN_2 = 'XXXXXXXXXXXXXXX'
TWILIO_PHONE_2 = '+15XXXXXX5'
TO_NUMBER_2 = '+91XXXXXXXX'

client2 = Client(ACCOUNT_SID_2, AUTH_TOKEN_2)

def send_info_sms():
    message = (
        "URGENT: The underpass at RAJAJINAGAR is flooded and the system is not responding.\n"
        "Please dispatch a maintenance person immediately to attend to the problem and restore operation."
    )
    try:
        sms = client2.messages.create(
            body=message,
            from_=TWILIO_PHONE_2,
            to=TO_NUMBER_2
        )
        print(f"✅ Info sent by Client 2: {sms.sid}")
    except Exception as e:
        print(f"❌ Client 2 failed: {e}")

# Execute the flow
send_alert_sms()          # Immediate alert from Client 1
time.sleep(15)             # Wait 15 seconds
send_safe_to_pass_sms()   # Safe-to-pass update from Client 1
time.sleep(60)            # Wait remaining 25 seconds to total 30 seconds
send_info_sms()           # Info from Client 2
