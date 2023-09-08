num_a = 0
num_b = 0
# defs

def on_gesture_screen_down():
    global num_a, num_b
    num_a = 0
    num_b = 0
    basic.show_string("nollattu")
    basic.pause(2000)
    basic.clear_screen()
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_a():
    global num_a
    num_a += 1
    basic.show_number(num_a)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(num_a + num_b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global num_b
    num_b += 1
    basic.show_number(num_b)
input.on_button_pressed(Button.B, on_button_pressed_b)
