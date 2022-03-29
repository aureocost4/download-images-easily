A simple project to download multiple images from https://www.freepik.com/ using
the Google Chrome browser.


1° step: Download ChromeDriver according to the version of your google chrome installed.

- ChromeDriver -> https://chromedriver.chromium.org/home


2° step: Additional libraries.

- WebDriver Manager
```bash 
pip install webdriver-manager
```

- Selenium
```bash
pip install selenium
```

- Pillow
```bash
pip install Pillow
```

3° step: Put the chromedriver's path that you downloaded in step 1 in the variable
CHROMEDRIVER_PATH, located in script/files.py file

for linux/mac users:

you should put the chromedriver's folder in the PATH of your operating system.

for example, on linux(ubuntu) it should look like this:

/usr/local/bin/chromedriver_linux64/chromedriver

in files.py CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver_linux64/chromedriver"


4° step: Execute main.py file.

More information about using the Selenium library with Python

https://selenium-python.readthedocs.io/
