
import smtplib
import os
import time
import zipfile
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Gmail details
sender_email = "rayeesaiffath@gmail.com"
receiver_email = "rayeesaizhan@gmail.com"
app_password = "bfnx mheb dbmd lbkq"

# Folder path
folder_path = r"C:\Users\C2C\Desktop\vac prog"

# Daily sending time
send_time = "15:00"

print("Waiting for scheduled time...")

while True:

    current_time = time.strftime("%H:%M")

    if current_time == send_time:

        # Today's date
        today = date.today().strftime("%d-%m-%Y")

        # ZIP file name
        zip_filename = f"backup_{today}.zip"
        zip_path = os.path.join(folder_path, zip_filename)

        # Create ZIP automatically
        with zipfile.ZipFile(
            zip_path,
            "w",
            zipfile.ZIP_DEFLATED
        ) as zipf:

            # Read all files in folder
            for file in os.listdir(folder_path):

                file_full_path = os.path.join(folder_path, file)

                # Skip zip itself
                if (
                    os.path.isfile(file_full_path)
                    and file != zip_filename
                ):

                    # Check today's modified files
                    modified_date = date.fromtimestamp(
                        os.path.getmtime(file_full_path)
                    )

                    if modified_date == date.today():

                        # Add file to ZIP
                        zipf.write(
                            file_full_path,
                            arcname=file
                        )

                        print("Added:", file)

        print("ZIP file created successfully!")

        # Create email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Daily Automatic Backup"

        body = "Today's files are attached in ZIP format."
        message.attach(MIMEText(body, "plain"))

        # Attach ZIP file
        with open(zip_path, "rb") as attachment:

            part = MIMEBase("application", "zip")
            part.set_payload(attachment.read())

        # Encode ZIP
        encoders.encode_base64(part)

        # Add attachment header
        part.add_header(
            "Content-Disposition",
            f'attachment; filename="{zip_filename}"'
        )

        # Attach ZIP to email
        message.attach(part)

        try:
            # Gmail SMTP
            server = smtplib.SMTP(
                "smtp.gmail.com",
                587
            )

            server.starttls()

            # Login
            server.login(
                sender_email,
                app_password
            )

            # Send email
            server.send_message(message)

            print("Email sent successfully!")

            server.quit()

        except Exception as e:
            print("Error:", e)

        # Prevent duplicate sending
        time.sleep(60)

    # Check every 30 seconds
    time.sleep(30)
