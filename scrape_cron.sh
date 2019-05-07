chmod +x scraper.py
touch selim-scrape
echo "#!/bin/sh

set -e

/home/pi/Documents/Selim.io/scraper.py" >> selim-scrape
chmod +x selim-scrape
mv selim-scrape /etc/cron.weekly/
