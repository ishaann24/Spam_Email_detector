Automated Content Filtering Agent (Spam Detector)

Overview of the Project

This project is a basic "Intelligent Agent" designed for spam and phishing attempt detection in text messages. It is a useful tool since it allows the users to detect hazardous content among messages by looking for suspicious keywords and providing them with a calculated risk score. Therefore, it stands as the first line of protection against scams.

Features

Real-time Scanning: instantly analyzes any text input provided by the user.

Keyword Detection: Identifies more than 50+ common words used in spam, fraud, and phishing attacks.

Risk Scoring System: Calculates an overall "Risk Score" based on the threat.

Smart Alerts: categorizes messages into three safety levels:

SAFE (Low score)

WARN (Medium score)

DANGER (High score)

User-Friendly Interface: Simple command-line interaction that anyone can use.

Technologies/Tools Used

Programming Language: Python 3

Libraries: Standard Python libraries (no external installation required).

Concepts Used: String manipulation, List handling, Conditional logic, Knowledge Representation.

Steps to Install & Run the Project

Prerequisite: Make sure you have Python installed on your computer.

Download: Download the spam_filter.py file to your computer.

Run: Open a terminal or command prompt, change into the folder, and type

python spam_filter.py


Output: The program will begin to execute in the terminal. Follow the on-screen instructions.

Testing Instructions

You can test the accuracy of AI with messages of varying types:

Test 1 (Safe Message):

Q: "Hey, are we meeting for lunch tomorrow?

Expected Result: SAFE

Test 2 (Marketing Spam):

Click here to win a free iPhone now!

Expected Result: DANGER (Detects: 'click', 'win', 'free', 'now')

Test 3 (Phishing Attempt):

Your bank account is suspended. Please verify immediately.

Expected Result: DANGER Detects: 'bank', 'account', 'suspended', 'verify
