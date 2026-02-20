# Incandescent Binary Clock

Crazy idea for a binary clock using small incandescent bulbs

Bulb count (20):

* (2) 10 Hours: 0-2 
* (4) 1 Hours 0-9
* (3) 10 minutes 0-5
* (4) 1 minutes 0-9
* (3) 10 seconds 0-5
* (4) 1 secondss 0-9

To make it more interesting, let's build all the logic
out of discrete NPN and PNP transistors!

There's a schematic of a working 4-bit binary counter
with count=9 carry output and reset in `Spice/couter-4bit.asc`
(LTspice XVII format).

It requires "only" 18 transistors, 30 resistors, 12 capacitors.
So something like 150, 250, 100 total.

