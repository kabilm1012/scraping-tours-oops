import smtplib, ssl
import os


class Email:
    def send(self, raw_message):
        host = "smtp.gmail.com"
        port = 465

        username = "guestkabil@gmail.com"
        password = os.getenv("PASSWORD")

        receiver = "kabilm1012@gmail.com"
        context = ssl.create_default_context()

        message = f"""\
    Subject: Hey, new event was found!

    Event details: {raw_message}
    """

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email was sent!")