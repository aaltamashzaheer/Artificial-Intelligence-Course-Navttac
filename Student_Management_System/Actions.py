# import subprocess

# def send_email(sender, recipient, subject, message):
#     # Construct the email headers and body
#     email = f"From: {sender}\nTo: {recipient}\nSubject: {subject}\n\n{message}"
    
#     try:
#         # Use the sendmail command to send the email
#         subprocess.run(['sendmail', '-t'], input=email, encoding='utf-8', check=True)
#         print("Email sent successfully!")
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to send email. Error: {e}")

# # Usage example
# sender_email = 'altamashzaheerofficial@gmail.com'
# recipient_email = 'hassan.ad.mehtab@gmail.com'
# email_subject = 'Code Test'
# email_body = 'Hello Sr! Sending this message to you via My Code.'

# send_email(sender_email, recipient_email, email_subject, email_body)



# import yagmail

# def send_email(sender, recipient, subject, message):
#     try:
#         # Create a yagmail.SMTP object with your email credentials
#         yag = yagmail.SMTP(sender)

#         # Send the email
#         yag.send(to=recipient, subject=subject, contents=message)
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email. Error: {e}")

# # Usage example
# sender_email = 'altamashzaheer@outlook.com'
# recipient_email = 'hassan.ad.mehtab@gmail.com'
# email_subject = 'Code Test'
# email_body = 'Hello Sr! Sending this message to you via My Code.'

# send_email(sender_email, recipient_email, email_subject, email_body)




# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# def send_whatsapp_message(contact_name, message):
#     # Provide the path to your Chrome WebDriver executable
#     driver = webdriver.Chrome('path/to/chromedriver')

#     # Open WhatsApp Web
#     driver.get('https://web.whatsapp.com')
#     input("Scan the QR code and press Enter to continue...")

#     # Search for the contact
#     search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
#     search_box.send_keys(contact_name)
#     time.sleep(2)  # Add a short delay to allow search results to load
#     search_box.send_keys(Keys.ENTER)

#     # Send the message
#     message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
#     message_box.send_keys(message)
#     message_box.send_keys(Keys.ENTER)

#     # Close the browser
#     driver.quit()
#     print("WhatsApp message sent successfully!")

# # Usage example
# contact = "John Doe"  # Replace with the name of your contact
# message = "Hello, this is a test message."  # Replace with your desired message

# send_whatsapp_message(contact, message)


import pywhatkit

def send_whatsapp_message(phone_number, message, hour, minute):
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

# Usage example
phone_number = "+923024691807"  # Replace with the recipient's phone number including the country code
message = "Hello, this is a test message."
hour = 22  # Replace with the desired hour (24-hour format)
minute = 34  # Replace with the desired minute

send_whatsapp_message(phone_number, message, hour, minute)
