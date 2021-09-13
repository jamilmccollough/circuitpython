import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5

print("Make it r!")

while True:
    dot.fill((23, 11, 68))
