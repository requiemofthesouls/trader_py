import tkinter as tk


title = 'TRADE HELPER DEMO'


def makeWidgets():
    window = tk.Tk()
    # window.geometry('700x200')
    window.title(title)
    container = tk.Frame(window)
    container.pack()

    first_bet_label = tk.Label(container, text='Первая ставка')
    first_bet_field = tk.Entry(container)
    first_bet_label.grid(row=0, column=0)
    first_bet_field.grid(row=0, column=1)

    the_percentage_label = tk.Label(
        container, text='Процент выплат')
    the_percentage_field = tk.Entry(container)
    the_percentage_label.grid(row=1, column=0)
    the_percentage_field.grid(row=1, column=1)

    martingale_coefficient_label = tk.Label(
        container, text='Коэффициент мартингейла')
    martingale_coefficient_field = tk.Entry(container)
    martingale_coefficient_label.grid(row=2, column=0)
    martingale_coefficient_field.grid(row=2, column=1)

    win_label = tk.Label(container, text='Выигрышная ставка?')
    win_field = tk.Checkbutton(container)
    win_label.grid(row=3, column=0)
    win_field.grid(row=3, column=1)

    income_label = tk.Label(container, text='Доход')
    income_field = tk.Entry(container)
    income_label.grid(row=0, column=2)
    income_field.grid(row=0, column=3)

    safe_label = tk.Label(container, text='Сбереженная сумма')
    safe_field = tk.Entry(container)
    safe_label.grid(row=1, column=2)
    safe_field.grid(row=1, column=3)

    next_bet_label = tk.Label(container, text='Сумма следующей ставки')
    next_bet_field = tk.Entry(container)
    next_bet_label.grid(row=2, column=2)
    next_bet_field.grid(row=2, column=3)

    def calculate(): 
        """ Подсчёт полей """
        income_field.insert(0, int((int(first_bet_field.get()) +
                            (int(first_bet_field.get()) * (int(the_percentage_field.get()) / 100)))))

        safe_field.insert(0, int(float(income_field.get()) * 0.3))

        next_bet_field.insert(0, int(float(income_field.get()) * 0.7))


    def clear():
        first_bet_field.delete(1, tk.END)
        income_field.delete(0, tk.END)
        safe_field.delete(0, tk.END)
        next_bet_field.delete(0, tk.END)

    tk.Button(text="Calculate", command=calculate).pack()
    tk.Button(text="Clear", command=clear).pack()

    return window


window=makeWidgets()
window.mainloop()
