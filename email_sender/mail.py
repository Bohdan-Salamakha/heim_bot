import smtplib

from core.settings import GMAIL_APP_LOGIN, GMAIL_APP_PASSWORD


class EmailSender:
    def __init__(self,
                 receivers: list[str],
                 message: str,
                 subject: str):
        self.__gmail_app_login = GMAIL_APP_LOGIN
        self.__gmail_app_password = GMAIL_APP_PASSWORD
        self.__sender = GMAIL_APP_LOGIN
        self.__receivers = receivers
        self.__message = f'Subject: {subject}\n{message}'

    def send_email(self):
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(self.__gmail_app_login, self.__gmail_app_password)
            server.sendmail(self.__sender,
                            self.__receivers,
                            self.__message)
        except smtplib.SMTPException as error:
            print(error)
        else:
            print("Successfully sent email")


if __name__ == '__main__':
    email_sender = EmailSender(receivers=['test1@gmail.com',
                                          'test2@yahoo.com'],
                               subject='Test Subject',
                               message='Test message body')
    email_sender.send_email()
