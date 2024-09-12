import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox


def download_tracks():
    name = entry.get()
    if not name:
        messagebox.showwarning("Внимание", "Введите название группы!")
        return

    url = f'https://rus.hitmotop.com/search?q={name}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    try:
        data = requests.get(url, headers=headers).text
        block = BeautifulSoup(data, 'lxml')
        heads = block.find_all('div', class_='track__info-r')

        if not heads:
            messagebox.showinfo("Информация", "Треки не найдены!")
            return

        count = 1
        for head in heads:
            if count > 48:  # Ограничение на 48 треков
                break
            w = head.find('a', href=True)
            link = w['href']
            vois = requests.get(link, headers=headers).content
            with open(f'{name}_{count}.mp3', 'wb') as f:
                f.write(vois)
            count += 1

        messagebox.showinfo("Успех", "Треки успешно загружены!")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


# Создание окна
app = tk.Tk()
app.title("Загрузка музыкальных треков")
app.geometry("400x200")

# Метка
label = tk.Label(app, text="Введите название группы:")
label.pack(pady=10)

# Поле ввода
entry = tk.Entry(app, width=50)
entry.pack(pady=10)

# Кнопка для загрузки треков
button = tk.Button(app, text="Загрузить треки", command=download_tracks)
button.pack(pady=20)

# Запуск приложения
app.mainloop()
