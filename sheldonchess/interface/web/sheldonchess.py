from rajesh import Application, run, expr
from rajesh.element import Img
from screens import MainMenu


class SheldonChess(Application):

    def begin(self):
        background = Img(id="background", src="images/sheldonchess_background.png", width="100%", height="100%")
        self.put(background, (0, 0))
        main_menu = MainMenu(self)
        self.put(main_menu, ("50%", "50%"))


if __name__ == "__main__":
    run()
