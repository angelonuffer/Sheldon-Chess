from rajesh import Application, run, expr
from rajesh.element import Img, Div
from screens import MainMenu, NormalGameLobby


class Player(object):

    def __init__(self, app):
        self.app = app
        self.name = ""


class SheldonChess(Application):

    def begin(self):
        self.player = Player(self)
        background = Img(id="background", src="images/sheldonchess_background.png", width="100%", height="100%")
        self.put(background, (0, 0))
        main_menu = MainMenu(self)
        self.put(main_menu, ("50%", "50%"))
        info_box = Div(id="info_box")
        self.put(info_box, ("50%", 0))

    def connectionLost(self, reason):
        for player in NormalGameLobby.players:
            if player == self.player:
                NormalGameLobby.players.remove(player)
                NormalGameLobby.update_players()


if __name__ == "__main__":
    run()
