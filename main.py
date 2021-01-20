def on_button_pressed_a():
    radio.send_string("Ciao!")
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_leds("""
    # . . . #
    # # . # #
    # . # . #
    # . . . #
    # . . . #
    """)
radio.set_group(1)

def on_forever():
    for index in range(4):
        basic.show_icon(IconNames.HEART)
        basic.pause(100)
        basic.show_icon(IconNames.SMALL_HEART)
        basic.pause(100)
basic.forever(on_forever)
