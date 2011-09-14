from rajesh.element import Button, Div
from rajesh import expr
from constants import CREDITS


class Screen(Div):

    def __init__(self, app, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.app = app

    @property
    def js(self):
        return getattr(self.app.js, self.parameters["id"])

    def on_put(self):
        self.js.style.setProperty("margin-left", expr("-%s.offsetWidth / 2" % self.parameters["id"]))
        self.js.style.setProperty("margin-top", expr("-%s.offsetHeight / 2" % self.parameters["id"]))
        self.js.style.setProperty("background", "#aaaaaa")
        self.js.style.setProperty("border-radius", 9)
        self.js.style.setProperty("border-style", "solid")
        self.js.style.setProperty("padding", 5)


class Menu(Screen):

    def __init__(self, app, buttons, **kwargs):
        super(Menu, self).__init__(app, **kwargs)
        self.buttons = buttons
        for button_name, action in buttons:
            button_id = button_name.lower().replace(" ", "_")
            button = Button(id=button_id, onclick="sock.send('%s')" % action.__name__)
            self.app.js._events[action.__name__] = action
            button.text = button_name
            self.put(button)


class MainMenu(Menu):

    def __init__(self, app, **kwargs):
        buttons = [
            ("New game", self.new_game),
            ("Options", self.options),
            ("Credits", self.credits),
        ]
        kwargs["id"] = "main_menu"
        super(MainMenu, self).__init__(app, buttons, **kwargs)

    def new_game(self):
        pass

    def options(self):
        pass

    def credits(self):
        self.app.js.alert(CREDITS)
