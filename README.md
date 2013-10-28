hallowedhue
===========

This repo has a few handy scripts for spooking up your environment using the IP-controllable Phillips Hue series of lights.

These scripts assume you have a Hue starter pack of 3 lights. Adjustments will be required if you have more than/less than 3 lights.

This isn't the best packaging or the best Python but it's good enough for a quick Halloween bodge.

Installation
============

* Clone: `git clone git@github.com:JamesHarrison/hallowedhue.git; cd hallowedhue`
* Setup Python environment: `pip install virtualenv; virtualenv venv; source venv/bin/activate; pip install -r requirements.txt`

Usage
=====

* (First run only) Push the button on the Hue bridge, then immediately...
* Run `spooky.py ip-of-bridge`, eg `spooky.py 192.168.0.213`

Pair with a theatrical haze generator for best results. hallowedhue is known to look damn good with an Antari X-310PRO.

