import pywhatkit

def send_whatsapp_message(phone_number, message, hour, minute):
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

# Usage example
phone_number = "+923024691807"  # Replace with the recipient's phone number including the country code
message = "Hello, this is a test message sent to me."
hour = 10  # Replace with the desired hour (24-hour format)
minute = 22  # Replace with the desired minute

send_whatsapp_message(phone_number, message, hour, minute)
