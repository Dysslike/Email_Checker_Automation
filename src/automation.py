import imaplib
import email
import pprint
import unicodedata
import re
from email.header import decode_header
import logging

logging.basicConfig(level=logging.INFO)

class Email_Credentials:
    def __init__(self, server, email, password):
        self.server = server
        self.email = email
        self.password = password
        self.imap = self._connect_to_server()

    def _connect_to_server(self):
        try:
            imap = imaplib.IMAP4_SSL(self.server)
            imap.login(self.email, self.password)
            logging.info("Logged in!~")
            return imap
        except Exception as e:
            logging.error("failed to load Credentials: {}".format(e))
            raise


