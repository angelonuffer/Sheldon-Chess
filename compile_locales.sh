#! /bin/bash

cd sheldonchess/interface/locales
cd pt_BR/LC_MESSAGES
msgfmt menu.po -o menu.mo
cd -
cd en/LC_MESSAGES
msgfmt menu.po -o menu.mo
