# USCWebRegAuto

This is a simple Python script that automates your course registration checkout process on USC WebReg system.

## Dependencies

- [Python 3.x](https://www.python.org/) 
    Please make sure that pip is installed with Python, and Python directory is added to the `$PATH` environment variable.
    Open a terminal and type `python --version` and `pip --version`to check installation.
- [Selenium](https://www.selenium.dev/): 
    In terminal type `pip install selenium` to install and `pip show selenium` to check installation.
- [Google Chrome](https://www.google.com/chrome/)
    Or other available browsers listed on [this page](https://chromedriver.storage.googleapis.com/index.html).
- [Chrome WebDriver](https://chromedriver.chromium.org/)
    Please select the correct version corresponding to the version of your browser. Also available on [this page](https://chromedriver.storage.googleapis.com/index.html).
    Make sure the path of chromedriver executable is added to the `$PATH` environment variable.
    To test installation, run `chromedriver` in a terminal to see if it can be successfully started.
    For WebDrivers of other browsers, check [this page](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/). 
- [Duo Two-Factor Authentication](https://itservices.usc.edu/duo/)
    Duo Mobile should be installed on your mobile device and should be able to receive push.

## Run the script

- Login to WebReg system and add the course you want to register into your course bin.
- Open `script.py` using a text editor and edit line 6-8 with your own myUSC username, email, the term you want to register, and the browser you are using.
- Open a terminal and change directory into this folder, then type `python script.py` to run the script.
- Approve the login action on your DUO mobile client.
- Leave it running to keep monitoring available spots 24/7, or run script just before 9:00 am MWF [when seats of your favorite GE classes will be released]([https://dornsife.usc.edu/2015ge/gesm-registration/](https://dornsife.usc.edu/ge/registration/)).
