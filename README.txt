Before the execution of the program can be done on your system, the following packages needs to be installed. The installation instructions are given for any UNIX operating system. Windows installation instructions can be obtained from the links provided. The commands following the '$' symbol are to be executed from the terminal.

1. Python 2.7 installation:
   (https://www.python.org/downloads/release/python-2713/)

2. MongoDB installation:
   $ brew update
   $ brew install mongodb
   $ mkdir -p /data/db
   (http://treehouse.github.io/installation-guides/)

3. PyMongo module:
   $ python -m pip install pymongo

4. TextBlob module installation:
   $ pip install -U textblob
   $ python -m textblob.download_corpora

5. Tweepy API installation:
   $ pip install tweepy

Once the following packages are installed, the following is to be run to access the application:

1. Host the web application using an open source host like MAMP and then navigate to the www folder and click on 'index.html'. Enter your search term.

2. Open a terminal and type in the following:
2.1. $ mongod //to be running till the end
2.2. $ mongo //to be running till the end
2.3. Phase 1 - Data Collection - $ python data_collection.py
2.4. Phase 2 - Data Processing - $ python data_processing.py
2.5. Phase 3 - Bot Processing:
	 Modify line 27 and 28 according to your marketing strategy.
	 $ python yolobot.py

NOTE: before you run Phase1, Phase2 and Phase3 enter your twitter credentials.
