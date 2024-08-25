import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(subject, to_email, attachment=None, url="", link_text=""):
    msg = MIMEMultipart('alternative')
    msg['From'] = 'john@microsoft-support.zapto.org'
    msg['To'] = to_email
    msg['Subject'] = subject

    # Plain Text Body
    plain_text_body = """Hello Diya,

I hope this email finds you well. We would like to inform you that security updates regarding vulnerabilities for the month of April from Microsoft have been shared with you as an attachment.

Please review the attached file for detailed information about the security updates.

If you have any questions or need further assistance, please feel free to contact us at john@microsoft-support.zapto.org.

Best regards,
John
Microsoft Support"""

    # HTML Body
    html_body = f"""\
<html>
    <head></head>
    <body>
        <p>Hello Diya,</p>
        <p>I hope this email finds you well. We would like to inform you that security updates regarding vulnerabilities for the month of April from Microsoft have been shared with you as an attachment.</p>
        <p>Please review the attached file for detailed information about the security updates.</p>
        <p>If you have any questions or need further assistance, please feel free to contact us at <a href="mailto:john@microsoft-support.zapto.org">john@microsoft-support.zapto.org</a>.</p>
        <p>Best regards,<br><strong>John</strong><br>Microsoft Support</p>
	<p>Attachments Password: infected  </p>
        {f'<p><a href="{url}"><img src="http://localhost/folder.png" alt="File Icon" style="vertical-align:middle; margin-right: 5px;">{link_text}</a></p>' if url and link_text else ''}
    </body>
</html>
"""

    # Attach both plain text and HTML versions
    msg.attach(MIMEText(plain_text_body, 'plain'))
    msg.attach(MIMEText(html_body, 'html'))

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

# Call the function with parameters
send_email('Security Update Notification', 'diya@example.com', '/var/www/html/client.zip', 'http://localhost/client.zip', 'Click here for more details')

