import tkinter

root = tkinter.Tk()
root.title('calculator coding challenge')
root.geometry('700x600')
root.tk_setPalette('black')

my_canvas = tkinter.Canvas(root, height=400, width=400, bg='blue')
my_canvas.pack()

resultfield = tkinter.Text(root, height=3.4, width=16, font=('arial', 24))
resultfield.place(x=165, y=10)

math = " "

def toCalculation(data):
    global math
    math += str(data)
    resultfield.delete(1.0, "end")
    resultfield.insert(1.0, math)

def doTheMath():
    global math
    try:
        math = str(eval(math))
        resultfield.delete(1.0, "end")
        resultfield.insert(1.0, math)
    except:
            cleanSlate()
            resultfield.insert(1.0, "Math error")
            pass

def cleanSlate():
    global math
    math = " "
    resultfield.delete(1.0, "end") 


button1 = tkinter.Button(root, text='1', bg='grey', width='7', height='3', command =lambda:toCalculation(1))
button2 = tkinter.Button(root, text='2', bg='grey', width='7', height='3', command = lambda:toCalculation(2))
button3 = tkinter.Button(root, text='3', bg='grey', width='7', height='3', command = lambda:toCalculation(3))
button4 = tkinter.Button(root, text='X', bg='grey', width='7', height='3',command = lambda:toCalculation('*'))
button5 = tkinter.Button(root, text='4', bg='grey', width='7', height='3',command = lambda:toCalculation(4))
button6 = tkinter.Button(root, text='5', bg='grey', width='7', height='3',command = lambda:toCalculation(5))
button7 = tkinter.Button(root, text='6', bg='grey', width='7', height='3',command = lambda:toCalculation(6))
button8 = tkinter.Button(root, text='-', bg='grey', width='7', height='3',command = lambda:toCalculation('-'))
button9 = tkinter.Button(root, text='7', bg='grey', width='7', height='3',command = lambda:toCalculation(7))
button10 = tkinter.Button(root, text='8', bg='grey', width='7', height='3',command = lambda:toCalculation(8))
button11 = tkinter.Button(root, text='9', bg='grey', width='7', height='3',command = lambda:toCalculation(9))
button12 = tkinter.Button(root, text='+', bg='grey', width='7', height='3',command = lambda:toCalculation('+'))
button13 = tkinter.Button(root, text='clear', bg='grey', width='7', height='3',command = cleanSlate)
button14 = tkinter.Button(root, text='0', bg='grey', width='7', height='3',command = lambda:toCalculation(0))
button15 = tkinter.Button(root, text='=', bg='grey', width='7', height='3',command = doTheMath)
button16 = tkinter.Button(root, text='/', bg='grey', width='7', height='3',command = lambda:toCalculation('/'))


button1.place(x=155,y=150,)
button2.place(x=215,y=150)
button3.place(x=275,y=150)
button4.place(x=335,y=150)
button5.place(x=155,y=205)
button6.place(x=215,y=205)
button7.place(x=275,y=205)
button8.place(x=335,y=205)
button9.place(x=155,y=260)
button10.place(x=215,y=260)
button11.place(x=275,y=260)
button12.place(x=335,y=260)
button13.place(x=155,y=310)
button14.place(x=215,y=310)
button15.place(x=275,y=310)
button16.place(x=335,y=310)
root.mainloop()