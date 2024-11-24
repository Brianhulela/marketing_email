# Budget Travel Email Guide

This Python script sends a styled email promoting a low-budget travel guide for South African students. The email includes tips and suggestions for affordable travel within South Africa.

## Requirements

You can install the required external libraries with the following command:

```bash
pip install -r requirements.txt
```

## Setup
Clone this repository or download the main.py file.

Create a .env file in the same directory as main.py with the following content:

```bash
SENDER_EMAIL=your_email@gmail.com
RECEIVER_EMAIL=recipient_email@gmail.com
PASSWORD=your_email_password
```

Replace your_email@gmail.com with the sender's email address.
Replace recipient_email@gmail.com with the recipient's email address.
Replace your_email_password with your email account password (or an application-specific password if using Gmail with 2FA).

## Run the script:

```bash
python main.py
```

The script will send an email to the provided recipient with a styled HTML body promoting the low-budget travel guide for South African students.
