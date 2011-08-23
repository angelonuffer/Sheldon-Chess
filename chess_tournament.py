import os
import pickle
from chesstournament.interface import Window

if os.path.isfile("window.pickle"):
    window = pickle.load(open("window.pickle"))
else:
    window = Window()
window.init()
del window.screen
del window.focus
del window.cursor_image
pickle.dump(window, open("window.pickle", "w"))
