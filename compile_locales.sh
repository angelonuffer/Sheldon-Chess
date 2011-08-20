#! /bin/bash

cd chesstournament/interfaces/locales
cd pt_BR/LC_MESSAGES
msgfmt menu.po -o menu.mo
cd -
cd en/LC_MESSAGES
msgfmt menu.po -o menu.mo
