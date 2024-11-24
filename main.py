import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email details
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")

# Get the password from the environment variable
password = os.getenv("PASSWORD")

# Email subject
subject = "Low Budget Travel Guide for South African Students"

# HTML content (styled email body)
html_body = """
<html>
  <head>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        margin: 0;
        padding: 0;
      }
      .container {
        width: 100%;
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      }
      h1 {
        color: #4CAF50;
        text-align: center;
      }
      p {
        font-size: 16px;
        color: #333333;
        line-height: 1.5;
      }
      .cta-button {
        display: inline-block;
        padding: 15px 30px;
        margin-top: 20px;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        text-decoration: none;
        font-size: 18px;
        border-radius: 5px;
        width: 100%;
      }
      .cta-button:hover {
        background-color: #45a049;
      }
      .footer {
        text-align: center;
        font-size: 12px;
        color: #888888;
        margin-top: 30px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Explore South Africa on a Budget!</h1>
      <p>Dear Traveler,</p>
      <p>Are you a student eager to explore the beauty of South Africa but worried about the cost? Don't let a tight budget hold you back! We've put together a practical guide to help you travel the country without breaking the bank.</p>
      
      <p><strong>Here’s how you can travel on a budget:</strong></p>
      <ul>
        <li><strong>Affordable Transport:</strong> Take advantage of budget buses, carpooling, and local trains to get around.</li>
        <li><strong>Hostels & Backpacker Accommodation:</strong> Stay in affordable hostels or guesthouses – many offer student discounts!</li>
        <li><strong>Explore Nature:</strong> South Africa offers beautiful national parks, beaches, and mountains – and many are free or low-cost to visit.</li>
        <li><strong>Eat Like a Local:</strong> Save money by eating at local markets, street vendors, or cooking your own meals.</li>
        <li><strong>Discounted Attractions:</strong> Look for student discounts or special promotions for tourists on a budget.</li>
      </ul>

      <p>Don’t let finances stop you from experiencing the adventure of a lifetime! Check out our tips and start planning your next budget-friendly adventure today!</p>

      <a href="https://www.example.com/budget-travel-tips" class="cta-button">Get More Travel Tips</a>

      <div class="footer">
        <p>&copy; 2024 Budget Travel SA. All rights reserved.</p>
      </div>
    </div>
  </body>
</html>
"""

# Create the MIME message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the HTML body to the message
msg.attach(MIMEText(html_body, 'html'))

# Connect to Gmail's SMTP server (port 587)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  # Start TLS encryption

# Log in to your email account
server.login(sender_email, password)

# Send the email
server.sendmail(sender_email, receiver_email, msg.as_string())

# Close the server connection
server.quit()

print("Email sent successfully!")
