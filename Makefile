default:
	more info.txt

start:
	python3 bot.py

install:
	pip3 install -r requirements.txt
	echo BOT_TOKEN=31313173843:ADFciRddsTestTokEN >> .env
	echo Installing .env file...
	echo Please put your bot TOKEN at the .env file.

win-install:
	pip install -r requirements.txt
	echo BOT_TOKEN=31313173843:ADFciRddsTestTokEN >> .env
	echo Installing .env file...
	echo Please put your bot TOKEN at the .env file.

win-start:
	python bot.py