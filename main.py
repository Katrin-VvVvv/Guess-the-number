import tkinter as tk
from tkinter import messagebox
import random

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Угадай число")
    new_window.geometry("400x400")
  
    secret = random.randint(1, 100)
    attempt = 0
  
    label = tk.Label(new_window, text="Угадай число от 1 до 100!", font=("Arial", 16))
    label.pack(pady=20)
    
    entry = tk.Entry(new_window, font=("Arial", 14), width=10)
    entry.pack(pady=10)
    
    result_label = tk.Label(new_window, text="", font=("Arial", 12))
    result_label.pack(pady=10)
    
    attempts_label = tk.Label(new_window, text=f"Попыток: {attempt}", font=("Arial", 12))
    attempts_label.pack(pady=5)

    def check_guess():
      nonlocal attempt
      try:
        num = int(entry.get())
        attempt += 1
        attempts_label.config(text=f"Попыток: {attempt}")
        
        if num == secret:
          result_label.config(text=f"Поздравляем! Вы угадали число {secret} за {attempt} попыток.")
          check_button.config(state="disabled")
        elif num < secret:
          result_label.config(text="Загаданное число больше!")
        else:
          result_label.config(text="Загаданное число меньше!")
                
        entry.delete(0, tk.END)
          
      except ValueError:
        result_label.config(text="Пожалуйста, введите целое число от 1 до 100.")
        entry.delete(0, tk.END)

    check_button = tk.Button(new_window, text="Проверить", command=check_guess, font=("Arial", 14))
    check_button.pack(pady=10)

def exit_app():
    if messagebox.askokcancel("Выход", "Точно выйти?"):
        root.destroy()

root = tk.Tk()
root.title("Угадай число")
root.geometry("500x400")

main_frame = tk.Frame(root)
main_frame.pack(expand=True)

label = tk.Label(main_frame, text="Привет, Давай сыграем в игру угадай число", font=("Arial", 14))
label.pack()

tk.Button(main_frame,text="Давай",command=open_new_window,font=("Arial", 16, "bold"),width=15,height=2,bg="#4CAF50",fg="white").pack(pady=20)

tk.Button(main_frame,text="Выход",command=exit_app,font=("Arial", 16, "bold"),width=15,height=2,bg="#f44336",fg="white").pack(pady=20)

root.mainloop()
