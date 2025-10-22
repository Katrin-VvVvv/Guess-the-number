import random

secret = random.randint(1, 100)
attempt = 0

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
