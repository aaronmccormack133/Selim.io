apt-get install update
apt-get install espeak -y
apt-get install python3-dev -y
apt-get install pyaudio -y
apt-get install python-pyaudio python3-pyaudio portaudio19-dev python-all-dev python3-all-dev -y
apt-get install pulseaudio -y
apt-get install update

curl https://yt-dl.org/latest/youtube-dl -o /usr/local/youtube-dl
chmod a+rx /usr/local/bin/youtube-dl
youtube-dl -U

pip3 install requests
pip3 install youtube_dl
pip3 install --upgrade youtube_dl
pip3 install pyaudio
pip3 install pytube
pip3 install BeautifulSoup4
pip3 install pyttsx3
pip3 install SpeechRecognition
-H pip3 install --upgrade youtube-dl
pip3 install PyAudio

chmod +x scrape_cron.sh
chmod +x selim_init.py
./scrape_cron.sh
chmod +x youtube.sh