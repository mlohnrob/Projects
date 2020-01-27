import tkinter as tk
import matplotlib.pyplot as plt


root = tk.Tk()

root.title("Andengradsligning")

root.geometry("300x400")



def plot():
    a = float(a_input.get())
    b = float(b_input.get())
    c = float(c_input.get())

    d = b**2-4*a*c

    

    x_T = -b/(2*a)
    y_T = -d/(4*a)

    a_list = []
    b_list = []

    for x in range(-10,10,1):
        y = (a*(x**2))+(b*x)+c
        a_list.append(x)
        b_list.append(y)
    
    print(a_list, b_list)
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(a_list, b_list)

    if d>0:
        x_1 = (-b+d**0.5)/(2*a)
        x_2 = (-b-d**0.5)/(2*a)
        plt.scatter(x_1, 0)
        plt.scatter(x_2, 0)
    elif d==0:
        x_1 = (-b)/(2*a)
        plt.scatter(x_1)

    


    plt.show()

a_lbl = tk.Label(root, text="a:")
a_lbl.grid(row=0, column=1)

a_input = tk.Entry(root, width=25)
a_input.grid(row=1, column=2)

b_lbl = tk.Label(root, text="b:")
b_lbl.grid(row=2, column=1)

b_input = tk.Entry(root, width=25)
b_input.grid(row=3, column=2)

c_lbl = tk.Label(root, text="c:")
c_lbl.grid(row=4, column=1)

c_input = tk.Entry(root, width=25)
c_input.grid(row=5, column=2)


plot_btn = tk.Button(root, text="Plot", command=plot)
plot_btn.grid(row=6, column=1)


root.mainloop()