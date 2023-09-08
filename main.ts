let num_a = 0
let num_b = 0
// defs
input.onGesture(Gesture.ScreenDown, function () {
    num_a = 0
    num_b = 0
    basic.showString("nollattu")
    basic.pause(2000)
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    num_a += 1
    basic.showNumber(num_a)
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(num_a + num_b)
})
input.onButtonPressed(Button.B, function () {
    num_b += 1
    basic.showNumber(num_b)
})
