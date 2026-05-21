
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Gmail details
sender_email = "sedgsdfhgs@gmail.com"
receiver_email = "etgwreetr@gmail.com"
app_password = "your password"

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Mail from Python"

body = "Hello! This email is sent using Python and Gmail SMTP."
message.attach(MIMEText(body, "plain"))

try:
    # Connect to Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Login using app password
    server.login(sender_email, app_password)

    # Send email
    server.send_message(message)

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)

finally:
    server.quit()
