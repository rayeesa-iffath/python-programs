
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# Gmail details
sender_email = "sdafgASDfc@gmail.com"
receiver_email = "sdfGdsfgafh@gmail.com"
app_password = "your password"

# File path
file_path = r"C:\Users\C2C\Downloads\vac.pdf"

# Create email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Python Email with Attachment"

# Email body
body = "Hello! This email contains an attachment."
message.attach(MIMEText(body, "plain"))

# Attach file
with open(file_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file into base64
encoders.encode_base64(part)

# Get file name only
filename = os.path.basename(file_path)

# Add attachment header
part.add_header(
    "Content-Disposition",
    f'attachment; filename="{filename}"'
)

# Attach the file
message.attach(part)

try:
    # Connect to Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Login to Gmail
    server.login(sender_email, app_password)

    # Send email
    server.send_message(message)

    print("Email with attachment sent successfully!")

except Exception as e:
    print("Error:", e)

finally:
    server.quit()
