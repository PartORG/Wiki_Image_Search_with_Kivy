import wikipedia
import requests

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def get_image_link(self):
        # get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text

        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        req = requests.get(self.get_image_link())
        image_path = 'files/image.jpg'
        print(req.content)
        with open(image_path, 'wb') as file:
            file.write(req.content)

        return image_path

    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
