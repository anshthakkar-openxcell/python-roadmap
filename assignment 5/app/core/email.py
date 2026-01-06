import time

def send_welcome_email(email: str):
    """
    Simulate slow email provider
    """
    time.sleep(10)  # simulate delay
    print(f"Welcome email sent to {email}")
