# ShamsiCalendar

**ShamsiCalendar** یک پکیج پایتون برای نمایش و انتخاب تاریخ شمسی (Persian / Jalali) در رابط کاربری Tkinter است. این پکیج شامل یک تقویم شمسی و یک ویجت ورودی تاریخ است که استفاده از آن برای برنامه‌های GUI ساده و سریع است.

---

## ویژگی‌ها

- تقویم شمسی با قابلیت انتخاب روز
- دکمه "امروز" برای انتخاب سریع تاریخ فعلی
- تغییر ماه و سال به راحتی
- رنگ‌بندی مخصوص روز جاری و جمعه‌ها
- ورودی تاریخ شمسی با Popup تقویم
- فارسی‌سازی کامل نام ماه‌ها و روزهای هفته

---

## نصب

```bash
pip install ShamsiCalendar
```

> برای تست قبل از انتشار اصلی، می‌توانید از Test PyPI استفاده کنید:

```bash
pip install --index-url https://test.pypi.org/simple/ ShamsiCalendar
```

---

## استفاده از ShamsiCalendar

```python
import tkinter as tk
from shamsicalendar import ShamsiCalendar
import jdatetime

def on_date_selected(date):
    print("Selected date:", date)

root = tk.Tk()
root.title("Persian Shamsi Calendar")

cal = ShamsiCalendar(root, year=1404, month=6, select_callback=on_date_selected)
cal.pack(padx=10, pady=10)

root.mainloop()
```

---

## استفاده از ShamsiDateEntry

```python
import tkinter as tk
from shamsicalendar import ShamsiDateEntry

root = tk.Tk()
root.title("Persian Date Entry")

date_entry = ShamsiDateEntry(root)
date_entry.pack(padx=10, pady=10)

def show_date():
    print("Selected date:", date_entry.get())

btn = tk.Button(root, text="Show Date", command=show_date)
btn.pack(pady=5)

root.mainloop()
```

---

## مجوز

این پروژه تحت **MIT License** منتشر شده است.

---

## لینک‌ها

- GitHub Repository: [https://github.com/p7deli/ShamsiCalendar](https://github.com/p7deli/ShamsiCalendar)
- PyPI: [https://pypi.org/project/ShamsiCalendar/](https://pypi.org/project/ShamsiCalendar/)

---

## Keywords

Persian calendar, Shamsi calendar, Jalali date, Tkinter date picker, Python GUI, Persian date entry, Python ShamsiCalendar, تاریخ شمسی
