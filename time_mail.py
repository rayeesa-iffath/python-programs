
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "rayeesaiffath@gmail.com"
receiver_email = "rayeesaizhan@gmail.com"
app_password = "bfnx mheb dbmd lbkq"

send_time = "14:42"   # HH:MM format

while True:
    current_time = time.strftime("%H:%M")

    if current_time == send_time:
        try:
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = "Automatic Email"

            body = "This email was sent automatically."
            message.attach(MIMEText(body, "plain"))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            server.login(sender_email, app_password)

            server.send_message(message)

            print("Email sent successfully!")

            server.quit()

            break

        except Exception as e:
            print("Error:", e)

    time.sleep(30)

