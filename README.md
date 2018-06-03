# A short Raspberry Pi Presentation for Santa Cruz PyLadies

*I had mentioned a Raspberry Pi project at a [Santa Cruz PyLadies](https://www.meetup.com/PyLadiesSC/) meetup last 
month, and some people who weren't familiar with the Raspberry Pi asked me about it. I volunteered to demonstrate some 
Raspberry Pi stuff at the upcoming [Speaker Night](https://www.meetup.com/PyLadiesSC/events/250555271/), and the 
following is basically my script, with links and code.*

## Introduction to the Raspberry Pi

The [Raspberry Pi](https://www.raspberrypi.org/) is a single-board Linux computer which was first released in 2012, and 
over 19 million of them have been sold. The most common models are the size of a credit card, and cost around $35, but 
there are also smaller Raspberry Pi Zero models that only cost $5 and $10. You *can* use them as general purpose 
computers -- [Idea Fab Labs](http://santacruz.ideafablabs.com/) has two of them as dedicated print servers for 3D 
printers -- but at those prices, as you can imagine they're pretty low-end and slow compared to mass-market laptop and 
desktop computers. But what makes them particularly special and popular (in addition to the price) is that they have a 
lot of input/output pins that your programs can use to talk to and control hardware, making them well-suited for use in 
robotics, home-automation, art, etc.

Being Linux computers, you can write and run programs on them using any language you like, but the Raspberry Pi 
community mostly revolves around Python -- Raspberry Pis come with Python 2 and 3 installed, including the Python 
[Rpi.GPIO](https://pypi.org/project/RPi.GPIO/) library that makes it easy for your programs to control the Raspberry 
Pi's GPIO (General Purpose Input/Output) pins. They also come with the 
[IDLE](https://docs.python.org/3/library/idle.html) Python IDE installed, but you can use other IDEs (or text editors) 
too, such as the [PyCharm](https://www.jetbrains.com/pycharm/) free Community Edition, which I'm using here.

## Hello World!

When you're getting started with a Raspberry Pi (or Arduino, or Android Things), the "Hello World" equivalent is to 
connect and blink an LED. A [breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) is a tool that 
lets you easily make circuits and connections by poking wires and components into it -- everything is reusable, and you 
don't need to do any soldering. Adafruit has a product called the [Cobbler](https://www.adafruit.com/product/914) which 
I have here, and which connects to the Raspberry Pi with a cable, and then plugs into a breadboard, to make all 
Raspberry Pi pins labeled and easily accessible from the breadboard, but you can also just use jumper wires to connect 
individual Raspberry Pi pins one at a time to a breadboard.

For the hardware part of this example we're using a jumper wire to connect one of the Raspberry Pi's Ground pins to one 
end of this 330-ohm resistor, then we're connecting the other end of the 330-ohm resistor to the negative pin of this 
LED, and then using another jumper wire to connect the Raspberry Pi's GPIO20 pin to the positive pin of the LED. (I 
didn't choose GPIO pin 20 for any particular reason - you can use whichever GPIO pin or pins you like so long as you 
use the same pins in your software.) 

For the software part of this example we have 
[hello_world_blink.py](https://github.com/tachyonlabs/raspberry_pi_pyladies_presentation/blob/master/hello_world_blink.py).
*(I do a walk-through of [the code](https://github.com/tachyonlabs/raspberry_pi_pyladies_presentation/blob/master/hello_world_blink.py) and run it.)*

## [Raspberry Pi Instagram Slide and Video Show](https://github.com/tachyonlabs/raspberry_pi_slide_and_video_show)

I'm a volunteer at the [Idea Fab Labs](https://santacruz.ideafablabs.com/) maker/hacker/artspace here in Santa Cruz, 
and I was asked to set up a Raspberry Pi for our weekly open house and for IFL booths at events, so that all you 
had to do was plug it into a large monitor and it would start running a slideshow of 
[Idea Fab Labs' Instagram feed](https://www.instagram.com/ideafablabs/) of photos of projects, facilities, and events.

I had written my original 
[Raspberry Pi Instagram Slideshow](https://github.com/tachyonlabs/raspberry_pi_instagram_slideshow) version in Python 
using the [Tkinter](https://wiki.python.org/moin/TkInter) GUI, but when I was asked to update it to include Instagram 
videos as well as photos, I [rewrote it](https://github.com/tachyonlabs/raspberry_pi_slide_and_video_show) (still in 
Python) using the cross-platform (you can run your same Python application on Windows, OS X, Android, and iOS, in 
addition to Raspberry Pi/Linux) [Kivy](https://kivy.org/) Framework. *(I demonstrate the application.)*

## HATs

In addition to building your own circuits or prototypes as we did with the blinking LED example, you can also buy 
pre-built add-on boards called "HAT"s ("Hardware Attached on Top") that plug onto the Raspberry Pi's pins and extend 
your Raspberry Pi's functionality with components like sensors, buttons, displays, etc. At both of the most recent 
Google I/O and droidconSF conferences I got free 
[Android Things Starter Kits](https://androidthings.withgoogle.com/#!/kits/starter-kit), 
featuring the NXP i.MX7D Android Things development board, which among other things is pin-compatible with the 
Raspberry Pi, so I can use the included [Rainbow Hat](https://shop.pimoroni.com/products/rainbow-hat-for-android-things) 
with the Raspberry Pi as well.

## Free Giant Amazing Project Books

There are three official Raspberry Pi project books that are free online, each one 200 lavishly-illustrated pages of 
projects and articles (including beginner's guides). You'll see projects for gaming, music, robotics, Lego, telescope 
control, high-altitude photography, terrarium lighting control, etc. etc. etc.

* [The Official Raspberry Pi Projects Book](https://www.raspberrypi.org/magpi-issues/Projects_Book_v1.pdf)
* [The Official Raspberry Pi Projects Book Volume 2](https://www.raspberrypi.org/magpi-issues/Projects_Book_v2.pdf)
* [The Official Raspberry Pi Projects Book Volume 3](https://www.raspberrypi.org/magpi-issues/Projects_Book_v3.pdf)
