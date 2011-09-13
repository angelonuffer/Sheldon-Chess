from rajesh import Application, run, expr
from rajesh.element import Img, Button


class SheldonChess(Application):

    def begin(self):
        background = Img(id="background", src="images/sheldonchess_background.png", width="100%", height="100%")
        self.put(background, (0, 0))

        new_game = Button(id="new_game")
        new_game.text = "New game"
        self.put(new_game, (expr("document.width / 2 - new_game.offsetWidth / 2"), expr("document.height / 2 + 20")))
        self.js.new_game.onclick = self.new_game

        options = Button(id="options")
        options.text = "Options"
        self.put(options, (expr("document.width / 2 - options.offsetWidth / 2"), expr("document.height / 2 + 60")))
        self.js.options.onclick = self.options

        credits = Button(id="credits")
        credits.text = "Credits"
        self.put(credits, (expr("document.width / 2 - credits.offsetWidth / 2"), expr("document.height / 2 + 100")))
        self.js.credits.onclick = self.credits

    def new_game(self):
        pass

    def options(self):
        pass

    def credits(self):
        pass


if __name__ == "__main__":
    run()
