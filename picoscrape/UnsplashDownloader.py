#import necessary packages
import selenium
from selenium import webdriver
import os
import time
from datetime import datetime
import urllib.request
import logging

#set the logging configuration to info (will show info on console)
logging.basicConfig(level = logging.INFO)

class UnsplashDownloader:
	"""An image scraper for Unsplash.

	This downloader depends on selenium and an appropriate browser-driver.exe
	should be used with it. Refer to selenium webpage for more info.

	https://selenium-python.readthedocs.io/

	selenium and selenium driver must be imported before crating an instance
	of this class.

	Attributes
	----------
	driver : selenium webdriver object
		(Use appropriate driver for your browser and version)

	outputFolder : str
		(the path of the folder where files will be downloaded.
		Will default to current directory if incorrect path or not given.)

	Methods
	-------
	download : (keyword, num_images, imageWidth)
		Parameters :
			keyword : str (default = 'Dog')
				(what you want to search for - dog, cat, etc.)
			num_imges : int (default = 10)
				(Number of images you want to download.)
			imageWidth : int (default = 640)
				(The width of all images which will be downloaded.)

	Use Example:
		import selenium
		from selenium import webdriver
		from picoscrape import UnsplashDownloader

		browser = webdriver.Chrome(chromedriver.exe)

		unsplash = UnsplashDownloader(browser, <OUTPUT-FOLDER-PATH>)
		unsplash.download('dog', 10, 640)
	"""


	def __init__(self, driver, outputFolder = None):
		"""
		Parameters
		----------
		driver : selenium webdriver object
			(Use appropriate driver for your browser and version)

		outputFolder : str
			(the path of the folder where files will be downloaded.
			Will default to current directory if incorrect path or not given.)
		"""
		self.driver = driver
		self.outputFolder = outputFolder

		if self.outputFolder == None or not os.path.exists(self.outputFolder):
			self.outputFolder = os.getcwd()
			logging.info('Output folder changed to current directory.')


	def download(self, keyword='Dog', num_images=10, imageWidth=640):
		"""
		Parameters
		----------
			keyword : str (default = 'Dog')
				(what you want to search for - dog, cat, etc.)
			num_imges : int (default = 10)
				(Number of images you want to download.)
			imageWidth : int (default = 640)
				(The width of all images which will be downloaded.)
		"""

		if not os.path.exists(self.outputFolder + '/'+keyword):
			os.makedirs(self.outputFolder + '/'+keyword)

		scrolls = num_images // 6
		downloadString = '/download?force=true&w='+str(imageWidth)

		url = 'https://unsplash.com/s/photos/' + keyword
		self.driver.get(url)

		for _ in range(scrolls):
				self.driver.execute_script("window.scrollBy(0, 1000)")
				time.sleep(1)

		#find the  html elements which contaion link to image
		imgLinks = self.driver.find_elements_by_class_name('_2Mc8_')
		#generate actual link from the link stored in href tag of html elements
		imgLinks = [sublink.get_attribute('href') + downloadString for sublink in imgLinks]

		logging.info('Total Image Links Retreived (Not Max Limit) : {}'.format(len(imgLinks)))
		logging.info('Total Images to Download : {}'.format(num_images))

		for i,link in enumerate(imgLinks):
			if i == num_images:
				break
			#name the images based on current time
			curtime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')

			try:
				#download each image
				urllib.request.urlretrieve(link, self.outputFolder+'/'+keyword+'/'+keyword+'-'+curtime+'.jpg')
				logging.info('Downloaded {}/{}'.format(i+1, num_images))
			except:
				logging.info('Unable to Download {}/{}'.format(i+1,num_images))
				continue
