Selenium
WEBSITE: https://selenium-python.readthedocs.io/installation.html

Install Chromedriver
	Windows: update to have latest stable version of chromedriver
	Mac: install homebrew brew.sh
		Run on term:
			brew tap homebrew/cask
			Brew cask install chromedriver
				Didnt work, used “ brew install chromedriver ”  instead
		If you have but need to update:
			Brew cask upgrade chromedriver

Setting up selenium
	Create your project folder
		In the folder, create a blank file called “requirements.txt”. Open the file and type in the following line. Afterwords, save the file
			selenium==3.141.0
	Open your terminal, Cd to project folder install selenium ver on term
		Pip install -r requirements.txt
		

Demo
	CD to project folder
	Run: python3 starter.py
	
	If you get the error: “chromedriver” cannot be opened because the developer cannot be verified.
		Find a path to chromedriver binary:
			which chromedriver
		You should get something like /usr/local/bin/chromedriver
		
		Now tell MacOS to trust this binary by lifting the quarantine via the following command:
			xattr -d com.apple.quarantine /usr/local/bin/chromedriver


