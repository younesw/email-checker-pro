import imaplib
import smtplib
from config import PROVIDERS

class EmailChecker:
    def __init__(self):
        self.last_result = None

    def check_imap(self, email, password, provider_name):
        """
        Check IMAP login for email account
        Returns: dict with status, provider, message, inbox_count
        """
        provider = PROVIDERS.get(provider_name)
        if not provider:
            return {
                "status": "unsupported",
                "message": "Provider not supported"
            }

        try:
            imap = imaplib.IMAP4_SSL(
                provider["imap_server"],
                provider["imap_port"],
                timeout=20
            )
            imap.login(email, password)
            status, data = imap.select("INBOX")
            
            if status == "OK":
                count = len(data[0].split()) if data and data[0] else 0
                imap.close()
                imap.logout()
                
                return {
                    "status": "valid",
                    "provider": provider["display_name"],
                    "method": "IMAP",
                    "message": "Login successful via IMAP",
                    "inbox_count": count
                }
            else:
                imap.logout()
                return {
                    "status": "invalid",
                    "provider": provider["display_name"],
                    "method": "IMAP",
                    "message": "IMAP login failed"
                }
        except imaplib.IMAP4.error as e:
            return {
                "status": "invalid",
                "provider": provider["display_name"],
                "method": "IMAP",
                "message": f"IMAP Error: {str(e)[:100]}"
            }
        except Exception as e:
            return {
                "status": "error",
                "provider": provider["display_name"],
                "method": "IMAP",
                "message": f"Error: {str(e)[:100]}"
            }

    def check_smtp(self, email, password, provider_name):
        """
        Check SMTP login for email account
        Returns: dict with status, provider, message
        """
        provider = PROVIDERS.get(provider_name)
        if not provider:
            return {
                "status": "unsupported",
                "message": "Provider not supported"
            }

        try:
            if provider["smtp_port"] == 587:
                smtp = smtplib.SMTP(
                    provider["smtp_server"],
                    provider["smtp_port"],
                    timeout=20
                )
                smtp.starttls()
            else:
                smtp = smtplib.SMTP_SSL(
                    provider["smtp_server"],
                    provider["smtp_port"],
                    timeout=20
                )
            
            smtp.login(email, password)
            smtp.quit()
            
            return {
                "status": "valid",
                "provider": provider["display_name"],
                "method": "SMTP",
                "message": "Login successful via SMTP"
            }
        except smtplib.SMTPAuthenticationError:
            return {
                "status": "invalid",
                "provider": provider["display_name"],
                "method": "SMTP",
                "message": "SMTP Authentication failed"
            }
        except Exception as e:
            return {
                "status": "error",
                "provider": provider["display_name"],
                "method": "SMTP",
                "message": f"Error: {str(e)[:100]}"
            }

    def check_account(self, email, password, provider_name):
        """
        Check both IMAP and SMTP for email account
        Returns: dict with combined results
        """
        imap_result = self.check_imap(email, password, provider_name)
        smtp_result = self.check_smtp(email, password, provider_name)
        
        self.last_result = {
            "email": email,
            "provider": imap_result.get("provider", provider_name),
            "imap": imap_result,
            "smtp": smtp_result
        }
        
        return self.last_result
