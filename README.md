Simple Practice Test Task Automation

📋 Project Overview

This repository contains an automated testing solution for SimplePractice that performs end-to-end task management validation. The automation script demonstrates testing practices for web application functionality.

🚀 Features
Secure Authentication: Login with validated credentials

Task Management: Create new tasks with verification

Task Completion: Mark tasks as completed with status validation

Comprehensive Testing: Workflow testing with assertions

⚙️ Prerequisites
Software Requirements
Python: 3.9.13

Google Chrome Browser: 140.0.7339.128

ChromeDriver: 140.0.7339.82

Python Dependencies
All required packages are listed in requirements.txt:

Selenium WebDriver

Unit testing framework

Additional testing utilities

📥 Installation & Setup
1. Clone the Repository
bash
git clone <https://github.com/fcoisn1/simplepractice_exam.git>

3. Create Virtual Environment
bash
# Using venv (recommended)
python -m venv venv

# Activate environment
# On Windows:
venv\Scripts\activate.bat

# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
bash
pip install -r requirements.txt

5. Configure Application Settings
Edit utils/config.py with your credentials and ChromeDriver path:
python

# Authentication credentials
email = "your_email@example.com"  # Replace with your SimplePractice email
pwd = "your_secure_password"      # Replace with your password

# ChromeDriver configuration
chromedriver = "C:/path/to/your/chromedriver.exe"  # Update with correct path

5. ChromeDriver Setup
Download ChromeDriver:

Visit ChromeDriver download page

Download version 140.0.7339.82

Extract and note the file path

Update chromedriver variable in config.py

Verification:

bash
# Check ChromeDriver version
chromedriver --version

# Should return: ChromeDriver 140.0.7339.82

🎯 Execution
Run the automation script:

bash
python main.py
Expected Output
The script will:

- Launch Chrome browser

- Navigate to SimplePractice login

- Authenticate with provided credentials

- Create a new task and verify creation

- Mark task as completed and verify status
  

🔧 Technical Implementation
Technologies Used
Python 3.9.13: Core programming language

Selenium WebDriver: Browser automation framework

unittest: Testing framework for validation

ChromeDriver: Browser controller for Chrome

Key Components
Authentication Module: Secure login handling

Task Management: Create and complete tasks

Verification System: Assertion-based validation

Configuration Management: Secure credential handling

🧪 Test Coverage
The automation validates:

✅ Successful user authentication

✅ Task creation functionality

✅ Task completion workflow

✅ UI element presence and interactivity

✅ Status verification mechanisms

🔒 Security Notes
Credentials are stored in config.py (excluded from version control)

Never commit sensitive information to repository

Consider using environment variables for production use

🐛 Troubleshooting
Common Issues
ChromeDriver Version Mismatch

bash
# Update Chrome browser or download matching ChromeDriver version
Authentication Failures

Verify credentials in config.py

Check internet connection

Element Not Found Errors

Ensure stable internet connection

Verify SimplePractice UI hasn't changed or verify version with development department


📊 Performance
Typical execution time: 1 minute

👨‍💻 Author
Francisco Israel Santillán Nolasco

📧 Email: fcoisn1@gmail.com

💼 LinkedIn: Santillan Francisco
