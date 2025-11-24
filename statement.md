Problem Statement

Unsolicited spam messages, phishing scams, and fraudulent offers are a major issue for internet and mobile phone users. These messages are not just annoying; they pose a serious security risk, often leading to financial loss or identity theft. Manual filtering by humans is inefficient and prone to error, as people may easily miss subtle signs of fraud.

Scope of the Project

The scope of this project is to develop a lightweight, text-based "Intelligent Agent" that automates the process of message filtering.

In Scope: Detection of common English spam keywords, financial fraud terms, and urgent phishing threats in short text messages (SMS/Email subjects).

Out of Scope: Image analysis, complex deep learning, or checking the validity of URLs (links).

Target Users

General Public: Anyone who receives SMS or emails and wants to double-check if a message is safe.

Elderly or Non-Tech Savvy Users: People who are more vulnerable to scams and need a tool to warn them about suspicious language.

Small Business Owners: To filter out spam inquiries from legitimate customer messages.

High-Level Features

Pattern Matching Engine: A core logic component that compares input text against a known database of "bad words."

Weighted Scoring: Not all words are equal; the system aggregates matches to decide if a message is truly dangerous or just marketing.

Interactive Feedback: The system explains why a message was flagged by showing the detected words to the user.