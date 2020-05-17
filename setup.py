from distutils.core import setup

setup(
  name = 'picoscrape',
  packages = ['picoscrape'],
  version = '1.0',
  license='MIT License',
  description = 'This library enables the user to easily scrape images from various websites like unsplash, pexels. This library is dependent on selenium and other pre-installed packages.',
  author = 'Anurag Gupta',
  author_email = 'anuraggupta29@outlook.com',
  url = 'https://github.com/anuraggupta29/picoscrape',
  download_url = 'https://github.com/anuraggupta29/picoscrape/archive/v1.0.tar.gz',
  keywords = ['scrape', 'image scraper', 'unsplash scraper', 'image dataset', 'unsplash'],
  install_requires=['selenium'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
