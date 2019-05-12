# Selim.io

The code is located at https://github.com/aaronmccormack15533/Selim.io

Selim.io is a personal assistant which interprets the user's speech and uses natural language processing to construct 
the appropriate responses to users regarding their music preferences. The responses contain information on upcoming
events in their area, upcoming new releases from all of their favourite artists and recommendations on new artists
based on their preferences.

Selim.io is developed for linux distributions and can easily be incorporated into a raspberry pi system with 
microphone and speaker capabilities.

To install Selim, run the 'install.sh' in a unix terminal with sudo privilages. This will install all the dependencies 
that are needed to run the application

There are known issues involved with Selim such as 

    A channel error when the application does not close the audio output channel. This issue is resolved by running the application again

    The speech recognition is a finicky service. Sometimes it does not pick up the correct input from the user, or sometimes it won't pickup
    input at all. Please speak in a clear voice and wait a moment after the prompt to make sure that the microphone picks up your voice.

    Selim must be run in a linux environment with the dependencies in the install.sh file installed. ./install.sh in the directory will install 
    the dependencies for you. This script must be run with sudo privilages.

    The youtube.sh script can only be run a certain number of times a day. If the script is run too many times, the IP will be blocked and 
    the command line will show a 403: Permission Denied error.

    
