from rajesh import Application, run, expr
from rajesh.element import Img, Div
from rajesh.widget import Box
from screens import MainMenu, NormalGameLobby


class Player(object):

    def __init__(self, app):
        self.app = app
        self.name = ""


class SheldonChess(Application):

    def begin(self):
        self.player = Player(self)
        self.title = "Sheldon Chess"
        self.background = "images/sheldonchess_background.png"
        self.info_box = self.new_box("info_box", ("50%", 0))
        main_menu = MainMenu(self)
        self.put(main_menu, ("50%", "50%"))

    def connectionLost(self, reason):
        for player in NormalGameLobby.players:
            if player == self.player:
                NormalGameLobby.players.remove(player)
                NormalGameLobby.update_players()


if __name__ == "__main__":
    run()
