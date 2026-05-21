
import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Gmail details
sender_email = "rayeesaiffath@gmail.com"
receiver_email = "rayeesaizhan@gmail.com"
app_password = "bfnx mheb dbmd lbkq"

# Time to send mail (24-hour format)
send_time = "15:00"

# File attachment path
file_path = r"C:\Users\C2C.ITPG21.000\Desktop\vac.pdf"

print("Program started... Waiting for scheduled time.")

while True:
    current_time = time.strftime("%H:%M")

    if current_time == send_time:
        try:
            # Create email
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = "Automatic Email with Attachment"

            # Email body
            body = "Hello! This email was sent automatically with attachment."
            message.attach(MIMEText(body, "plain"))

            # Open and attach file
            with open(file_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode attachment
            encoders.encode_base64(part)

            # Get file name
            filename = os.path.basename(file_path)

            # Add header
            part.add_header(
                "Content-Disposition",
                f'attachment; filename="{filename}"'
            )

            # Attach file to email
            message.attach(part)

            # Connect to Gmail SMTP
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            # Login
            server.login(sender_email, app_password)

            # Send email
            server.send_message(message)

            print("Email sent successfully!")

            # Close server
            server.quit()

            break

        except Exception as e:
            print("Error:", e)

    # Check every 30 seconds
    time.sleep(30)
