import tkinter as tk
from shamsicalendar import ShamsiCalendar


WIDTH, HEIGHT = 500, 500

def show_value():
    lbl_show_date.configure(text=f'Date: {str(date_entry.get())}')

app = tk.Tk()

x = ((app.winfo_screenwidth() // 2) - (WIDTH//2))
y = ((app.winfo_screenheight() // 2) - (HEIGHT//2))

app.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
app.resizable(False, False)
app.title('Shamsi Calander App')


tk.Label(text='Hello Welcome', font=('Arial', 25, 'bold')).pack(pady=20)
tk.Label(text='Select Date', font=('Arial', 15, 'bold')).pack()

date_entry = ShamsiCalendar.ShamsiDateEntry(app)
date_entry.pack(pady=5)

lbl_show_date = tk.Label(text='Date:                      ', font=('Arial', 30, 'bold'), foreground='red')
lbl_show_date.pack(pady=20)

btn_show = tk.Button(app, text="show Date", command=show_value)
btn_show.pack(pady=10)

app.mainloop()