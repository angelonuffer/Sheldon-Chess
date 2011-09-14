from rajesh.element import Button, Div
from rajesh import expr
from constants import CREDITS


class Screen(Div):

    def __init__(self, app, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.app = app


class Menu(Screen):

    def __init__(self, app, buttons, **kwargs):
        super(Menu, self).__init__(app, **kwargs)
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
