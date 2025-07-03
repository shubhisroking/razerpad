import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.rgb import RGB
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

key_pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
]

keyboard.matrix = MatrixScanner(
    rows=key_pins,
    columns=[],
    pins_are_direct=True
)

rgb = RGB(
    pixel_pin=board.GP6,
    num_pixels=6,
    hue_default=180,
    sat_default=255,
    val_default=50,
    animation_speed=2,
)
keyboard.modules.append(rgb)

keyboard.keymap = [
    [
        KC.LEFT, KC.W, KC.RIGHT,
        KC.A, KC.S, KC.D
    ]
]

if __name__ == '__main__':
    keyboard.go()
