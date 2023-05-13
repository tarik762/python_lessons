# recursion
import time
import graphics as gr
import self_modules.Memoize

window = gr.GraphWin("Recursion test", 1000, 1000)
alpha = 0.1
window.setBackground('white')

__count = 0


@Memoize(5)
def draw_fractal_rectangle(A, B, C, D, dept=200):
    global __count
    if dept < 1:
        return
    time.sleep(.01)
    for M, N in ((A, B), (B, C), (C, D), (D, A)):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)

    A_next = (A[0]*(1 - alpha) + B[0] * alpha, A[1]*(1 - alpha) + B[1] * alpha)
    B_next = (B[0]*(1 - alpha) + C[0] * alpha, B[1]*(1 - alpha) + C[1] * alpha)
    C_next = (C[0]*(1 - alpha) + D[0] * alpha, C[1]*(1 - alpha) + D[1] * alpha)
    D_next = (D[0]*(1 - alpha) + A[0] * alpha, D[1]*(1 - alpha) + A[1] * alpha)
    __count += 1
    draw_fractal_rectangle(A_next, B_next, C_next, D_next, dept - 1)


draw_fractal_rectangle((50, 50), (600, 50), (600, 600), (50, 600))
print("Count = ", __count)
window.getMouse()
window.close()
