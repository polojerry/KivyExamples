from kivy.app import App
from kivy.uix.widget import Widget


class MyGrid(Widget):

    def button_press(self):
        print("First Name: ", self.firstName.text, "Last Name: ", self.lastName.text, "Email: ", self.emailAddress.text)
        self.firstName.text = ""
        self.lastName.text = ""
        self.emailAddress.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
