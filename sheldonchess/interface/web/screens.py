from rajesh.element import Button, Div, Input
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
        self.center()
        self.js.style.setProperty("background", "#aaaaaa")
        self.js.style.setProperty("border-radius", 9)
        self.js.style.setProperty("border-style", "solid")
        self.js.style.setProperty("padding", 5)

    def center(self):
        self.js.style.setProperty("margin-left", expr("-%s.offsetWidth / 2" % self.parameters["id"]))
        self.js.style.setProperty("margin-top", expr("-%s.offsetHeight / 2" % self.parameters["id"]))


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
        self.js.parentElement.removeChild(expr("main_menu"))
        choose_name = ChooseName(self.app)
        self.app.put(choose_name, ("50%", "50%"))

    def options(self):
        pass

    def credits(self):
        self.js.parentElement.removeChild(expr("main_menu"))
        credits = Credits(self.app)
        self.app.put(credits, ("50%", "50%"))


class ChooseName(Screen):

    def __init__(self, app, **kwargs):
        kwargs["id"] = "choose_name"
        super(ChooseName, self).__init__(app, **kwargs)
        self.text = "Type your name:"
        name = Input(id="name_input", type="text", value=self.app.player.name)
        self.put(name)
        enter = Button(id="enter", onclick="sock.send('enter ' + name_input.value)")
        self.app.js._events["enter"] = self.enter
        enter.text = "enter"
        self.put(enter)
        back = Button(id="back", onclick="sock.send('back')")
        self.app.js._events["back"] = self.back
        back.text = "back"
        self.put(back)

    def enter(self, name):
        if name != "" and name not in NormalGameLobby.get_players_names():
            self.app.player.name = name
            self.js.parentElement.removeChild(expr("choose_name"))
            normal_game_lobby = NormalGameLobby(self.app)
            self.app.put(normal_game_lobby, ("50%", "50%"))

    def back(self):
        self.js.parentElement.removeChild(expr("choose_name"))
        main_menu = MainMenu(self.app)
        self.app.put(main_menu, ("50%", "50%"))


class NormalGameLobby(Screen):

    players = []
    messages = []

    def __init__(self, app, **kwargs):
        kwargs["id"] = "normal_game_lobby"
        super(NormalGameLobby, self).__init__(app, **kwargs)
        NormalGameLobby.players.append(self.app.player)
        message_box = Div(id="message_box")
        self.put(message_box)
        player_list = Div(id="player_list")
        self.put(player_list)
        message = Input(id="message_input", type="text")
        self.put(message)
        send = Button(id="send", onclick="sock.send('send ' + message_input.value)")
        self.app.js._events["send"] = self.send
        send.text = "send"
        self.put(send)
        back = Button(id="back", onclick="sock.send('back')")
        self.app.js._events["back"] = self.back
        back.text = "back"
        self.put(back)

    @classmethod
    def get_players_names(cls):
        return map(lambda player: player.name, cls.players)

    @classmethod
    def update_players(cls):
        for player in cls.players:
            player.app.js.player_list.innerHTML = "<p style=\"margin: 0\">%s</p>" % "<br>".join(cls.get_players_names())

    def update_messages(self, app):
        app.js.message_box.innerHTML = "<p style=\"margin: 0\">%s</p>" % "<br>".join(NormalGameLobby.messages)
        app.js.message_box.scrollTop = expr("message_box.scrollHeight - 300")

    def on_put(self):
        super(NormalGameLobby, self).on_put()
        NormalGameLobby.update_players()
        self.app.js.message_box.style.setProperty("overflow", "auto")
        self.app.js.message_box.style.setProperty("width", "400px")
        self.app.js.message_box.style.setProperty("height", "300px")
        self.app.js.message_box.style.setProperty("float", "left")
        self.app.js.player_list.style.setProperty("float", "left")
        self.app.js.message_input.style.setProperty("width", "307px")
        self.update_messages(self.app)
        self.center()

    def send(self, *words):
        message = " ".join(words)
        self.app.js.message_input.value = ""
        self.app.js.message_input.focus()
        NormalGameLobby.messages.append("%s: %s" % (self.app.player.name, message))
        if len(NormalGameLobby.messages) > 500:
            NormalGameLobby.messages.pop(0)
        for player in NormalGameLobby.players:
            self.update_messages(player.app)

    def back(self):
        NormalGameLobby.players.remove(self.app.player)
        NormalGameLobby.update_players()
        self.js.parentElement.removeChild(expr("normal_game_lobby"))
        main_menu = MainMenu(self.app)
        self.app.put(main_menu, ("50%", "50%"))


class Credits(Screen):

    def __init__(self, app, **kwargs):
        kwargs["id"] = "credits"
        super(Credits, self).__init__(app, **kwargs)
        self.text = "<p>%s<p>" % CREDITS.replace("\n", "<br>")
        back = Button(id="back", onclick="sock.send('back')")
        self.app.js._events["back"] = self.back
        back.text = "back"
        self.put(back)

    def back(self):
        self.js.parentElement.removeChild(expr("credits"))
        main_menu = MainMenu(self.app)
        self.app.put(main_menu, ("50%", "50%"))
