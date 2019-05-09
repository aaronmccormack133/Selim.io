apt-get install update
apt-get install espeak -y
apt-get install python3-dev -y
apt-get install pyaudio -y
apt-get install update 

pip3 install requests
pip3 install BeautifulSoup4
pip3 install pyttsx3
pip3 install SpeechRecognition
-H pip3 install --upgrade youtube-dl

chmod +x scrape_cron.sh
chmod +x selim_init.py
./scrape_cron.sh