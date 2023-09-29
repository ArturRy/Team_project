import tkinter as tk
import tkinter.filedialog
from PIL import ImageTk, Image
from tkinter import ttk
import requests

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.user_info()
        self.title('VKinder')
        self.geometry('700x700')
        self.photo_images = []
        self.img_x = 27
        self.btn_x = 88
        self.url_list = exe['url_list']
        self.func()
        self.user()
        self.buttons()
        self.token = token_vk
    def func(self):
        for url in self.url_list:

            response = requests.get(url)
            image = Image.open(BytesIO(response.content)).resize((200, 200), PIL.Image.LANCZOS)
            photo_image = ImageTk.PhotoImage(image)
            self.photo_images.append(photo_image)

            tk.Label(self, image=photo_image).place(x=self.img_x)
            self.img_x += 220
            tk.Button(self, text="Поставить\nлайк", width=10, height=2).place(x=self.btn_x, y=220)
            self.btn_x += 220

    def user(self):
        data_text = f"{exe['name']}\nВозраст: {exe['age']}\nСхожие увлечения: {exe['hobby']}"
        label = ttk.Label(text=data_text, font=('Times', 18))
        label.place(x=0, y=300)

    def buttons(self):
        self.black_list = Button(self, text='Черный\nсписок').place(x=10, y=500)
        self.contact = Button(self, text='Добавить\nк себе').place(x=310, y=500)
        self.next = Button(self, text='Дальше\n ').place(x=610, y=500)
        self.more_users = Button(self, text='Найти больше пользователей').place(x=260, y=630)

    def user_info(self):
        params = {
            'count': 1000,
            'hometown': None,
            'sex': 1,
            'has_photo': True,
            'access_token': token_vk,
            'v': '5.131',
            'age_from': None,
            'age_to': None
        }

        window = Tk()
        window.title("VKinder")
        window.geometry("500x300")

        c = StringVar()
        self.user_city_text = ttk.Label(text='Введите город для поиска', font=('Times', 15)).place(x=142, y=0)
        self.user_city_insert = Entry(window, width=40, textvariable=c).place(x=135, y=35)

        s = StringVar()
        self.user_sex_text = ttk.Label(text='Кого ищем, парня или девушку\n     1 - девушка, 2 - парень',
                                  font=('Times', 15)).place(x=130, y=70)
        self.user_sex_insert = Entry(width=40, textvariable=s).place(x=135, y=120)

        af = StringVar()
        self.age_from_text = ttk.Label(text='Возраст от', font=('Times', 15)).place(x=92, y=155)
        self.age_from_insert = Entry(width=20, textvariable=af).place(x=85, y=190)

        at = StringVar()
        self.age_to_text = ttk.Label(text='Возраст до', font=('Times', 15)).place(x=300, y=155)
        self.age_to_insert = Entry(width=20, textvariable=at).place(x=300, y=190)

        self.close_button = ttk.Button(window, text="Продолжить", command=lambda: window.destroy()).place(x=400, y=250)
        window.mainloop()

        params['hometown'] = c.get()
        params['sex'] = s.get()
        params['age_from'] = af.get()
        params['age_to'] = at.get()
        self.params = params
        return self

if __name__ == "__main__":
    main = Main()
    main.mainloop()