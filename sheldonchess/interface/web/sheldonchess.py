from rajesh import Application, run
from rajesh.element import Img, Button


class SheldonChess(Application):

    def begin(self):
        background = Img(id="background", src="images/Image_chessSound.jpg", width=800, height=600)
        self.put(background, (0, 0))

        new_game = Button(id="new_game")
        new_game.text = "New game"
        self.put(new_game, (300, 420))
        self.js.new_game.onclick = self.new_game

        options = Button(id="options")
        options.text = "Options"
        self.put(options, (340, 420))
        self.js.options.onclick = self.options

        credits = Button(id="credits")
        credits.text = "Credits"
        self.put(credits, (380, 420))
        self.js.credits.onclick = self.credits

    def new_game(self):
        pass

    def options(self):
        pass

    def credits(self):
        pass


if __name__ == "__main__":
    run()
