# ProjectGeorgeMichael

NOTE: I am using Python 3.7.3 on raspberry pi

First you need to make sure you pip install the following: bottle, RPi.GPIO, pygame, and time

Next you need to create a folder where your project will be. I named my folder GeorgeMichael. Put both the server.py and CarelessWhisper.wav in that folder

Edit server.py with the ip address of your pi and the location of the .wav file. I added comments so it should be easy.

Follow link provided for installation and signup of ngrok (https://www.dexterindustries.com/howto/access-your-raspberry-pi-from-outside-your-home-or-local-network/)

Install IFTTT from google on your phone.

Open Terminal on your pi, cd to your server.py folder, and run server.py

Open another terminal on your pi and run "./ngrok http 'whatever your ip address is':1234" (ex: ./ngrok http 192.168.1.1:1234). In the terminal you will see two "Forwarding" lines, one for http and one for https, we will use the top one for http.

Open IFTTT on your phone. Tap on "Create". Tap on "This". Scroll to and tap on "Google Assistant". Tap on "Say a simple phrase". Under "What do you want to say?" I put "I'm feeling sexy today". Under "What do you want the Assistant to say?" I put "ok, I have just the thing". Language "English" for me. Another way to say it is blank, and another way is also blank. Tap Continue. Tap on "That". Go to search and type in "web". Tap on "Webhooks", then tap on "make a web request". "URL" is the forwarding http shown in the ngrok terminal but with an added '/relay/1' at the end. So an example would be "http://8772f4208858.ngrok.io/relay/1". "Method" is GET. "Content type" is text/plain. Tap Continue, then finish.

There is an oder this needs to go in. Open server.py first, then nrgok from terminal, then finish on ifttt.
EACH TIME YOU OPEN NGROK THE FORWARDING ADDRESS CHANGES. So keep that in mind.

WIRING:
You're gonna have to google what the pin layout is for your board, i have no idea if they are different.

Raspi 5v power -> relay input power
Raspi GND -> relay input GND
Raspi GPIO 17 -> relay input signal

Batt +  -> breadboard -> relay -> fan connector
Batt -  -> Fan GND
