# UNDERPASS-PROJECT

 Overview
The IoT-Enabled Underpass Water Monitoring System is a smart solution designed to tackle the issue of waterlogging in urban underpasses. The system continuously monitors water levels using sensors and takes real-time actions such as sending SMS alerts to commuters, notifying municipal authorities, suggesting alternative routes via Google Maps, and predicting rainfall using weather data.

By integrating IoT technology, automation, and communication APIs, this project enhances public safety, minimizes traffic disruption, and promotes efficient civic management.

💡 Features
🚨 Real-time Water Level Monitoring

📲 Automatic SMS Alerts via Twilio

🗺️ Alternative Route Suggestions using Google Maps API

🌦️ Weather Prediction Integration

🧠 Threshold-based Emergency Notifications to Municipal Authorities

🌐 Web Dashboard for Underpass Monitoring

🔧 Live Pump Activation for Water Ejection

🔧 Technologies Used
Hardware:

Arduino UNO

Ultrasonic Sensor / Water Level Sensor

Pump Module

Software:

Arduino IDE (Embedded C for hardware logic)

Python (PyCharm for backend logic)

Twilio API for SMS alerts

Google Maps API for route suggestions

Flask/Django for web-based monitoring dashboard (choose the one you used)

Frontend:

HTML, CSS, JavaScript (for dashboard UI)

🖥️ Web Dashboard
Monitor all underpasses with current water levels

Visualize alerts and emergency status

Control water pumps remotely

🚀 Installation and Setup
Prerequisites
Arduino UNO IDE installed

Python 3.x installed

Twilio account and credentials

Google Maps API key

Flask or Django environment set up

Steps
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/your-username/iot-underpass-monitoring.git
cd iot-underpass-monitoring
Upload Arduino Code:

Open water_monitor.ino in Arduino IDE.

Connect the hardware and upload the code to Arduino.

Install Python Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure API Keys:

Add Twilio credentials and Google Maps API key in config.py.

Run Python Script:

bash
Copy
Edit
python main.py
Run Web Dashboard (Optional):

If using Flask:

bash
Copy
Edit
flask run
If using Django:

bash
Copy
Edit
python manage.py runserver
📸 Screenshots
(Insert screenshots of the dashboard, alert SMS, and circuit here)

📬 SMS Alert Sample
ruby
Copy
Edit
ALERT: Water logging detected at MG Road Underpass!
Please take an alternative route: https://maps.google.com/?q=alternative+route
👥 Authors
Your Name – sajidsjd873@gmail.com , Mohamed Sajid B

Project for B.E. Information Science – Visvesvaraya Technological University

📜 License
This project is open-source and available under the MIT License.
