from tkinter import *
import ast 

root = Tk()
root.title("Calculadora")

# input
display = Entry(root)

#input style
display.grid(row=1, columnspan=6, sticky=W+E)

index = 0

# 5

def get_numbers(n):
    global index
    display.insert(index, n)
    index += 1

def get_operations(operator):
    global index
    operator_length = len(operator)
    display.insert(index, operator)
    index += operator_length


def clear_display():
    global index
    display.delete(0, END)

def undo():
    display_state  = display.get()
    if len(display_state) :
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, "Error")

def calculate():
    display_state = display.get()
    try:
    # math_expression = parser.expr(display_state).compile()
    # res = eval(math_expression)

      math_expression = ast.parse(display_state, mode="eval")
      result  = eval(compile(math_expression, '', mode="eval"))
      clear_display()

      display.insert(0, result)
    except Exception as e:
        clear_display()
        display.insert(0, 'Error')
       

# def createButton(textContent, row, col):
#     Button(root, text=textContent).grid(row=row, col=col, sticky=W+E)
# Buttons
Button(root, text="1", command=lambda: get_numbers(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda: get_numbers(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda: get_numbers(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda: get_numbers(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda: get_numbers(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda: get_numbers(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda: get_numbers(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda: get_numbers(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda: get_numbers(9)).grid(row=4, column=2, sticky=W+E)

# Buttons part 2

Button(root, text="AC", command=lambda: clear_display()).grid(
    row=5, column=0, sticky=W+E)
Button(root, text="0", command=lambda: get_numbers(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text="%", command=lambda: get_operations("%")).grid(row=5, column=2, sticky=W+E)


Button(root, text="+", command=lambda: get_operations("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda: get_operations("-")).grid(row=3, column=3,  sticky=W+E)
Button(root, text="*", command=lambda: get_operations("*")).grid(row=4, column=3,  sticky=W+E)
Button(root, text="/", command=lambda: get_operations("/")).grid(row=5, column=3, sticky=W+E)


Button(root, text="⇽", command=lambda: undo()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="exp", command=lambda: get_operations("**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="^2", command=lambda: get_operations("**2")).grid(row=3, column=5, sticky=W+E)
Button(root, text="(", command=lambda: get_operations("(")).grid(row=4, column=4, sticky=W+E)
Button(root, text=")", command=lambda: get_operations(")")).grid(row=4, column=5, sticky=W+E)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=4, sticky=W+E, columnspan=2)


root.mainloop()
