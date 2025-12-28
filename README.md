# Le Mot (Le Pack)

## Présentation du jeu

Le Mot est un jeu de devinette simpliste.

Le but de ce jeu est de trouver un mot choisi aléatoirement parmi une liste de mots prédéfinie. Le joueur a le choix entre des mots de 3, 4, 5 ou 6 lettres, en langue française et sans accents.\
Le joueur dispose pour cela de 6 essais. À chaque essai, des informations sont données sur chaque lettre du mot renseignée :
- si le fond de la lettre est vert : cela signifie que la lettre est présente au bon endroit dans le mot à deviner
- si le fond est orange : cela signifie que la lettre est dans le mot mais placé à un autre endroit\
Prend en compte les cas particuliers des lettres présentes en double.
- si le fond est gris foncé, cela signifie que la lettre n'apparaît pas dans le mot.
- si un mot n'existe pas (= n'est pas présent dans la liste de mots), l'essai n'est pas comptabilisé et le message "Mot non reconnu" apparaît en bas de l'écran. Il faut attendre une seconde avant de pouvoir modifier le mot écrit.

La partie se termine lorsque le joueur a trouvé le mot ou lorsque les six essais n'ont pas été concluants. Après trois secondes, le joueur est renvoyé sur le menu pour pouvoir lancer une autre partie.

## Comment jouer ?

Ce jeu fonctionne uniquement avec Python : il est nécessaire de télécharger le code source pour pouvoir y jouer.\
Version PC uniquement.

Deux moyens existent pour télécharger le code source.

### Depuis la Release GitHub

Rendez-vous dans la section [Releases](https://github.com/HiAbdounour/le_mot_le_pack/releases) et sélectionnez la version qui vous intéresse (la première est la plus récente).\
Vous trouverez après un message descriptif de la Release un dossier .zip et un dossier .rar contenant tous les fichiers du repo. Il vous suffit de télécharger l'un des dossiers, de le dézipper puis de lancer le fichier main.py (depuis le terminal en tapant `python main.py` ou depuis un IDE (VS Code, PyCharm, Spyder, etc)).

### Depuis le terminal

Ouvrez le terminal et déplacez-vous dans le dossier où vous souhaitez télécharger le code source.\
Ensuite, tapez :
```git
    git clone https://github.com/HiAbdounour/le_mot_le_pack
```

Cette instruction va directement télécharger le code source sur votre machine.

Pour lancer le jeu, il suffit de taper
```bash
    cd le_mot_le_pack
    python main.py
```

### Requis

Python version 3.12 ou ultérieure\
pygame version 2.6.1 ou ultérieure

## Sources

Le Mot est une version revisitée à ma sauce du [Wordle](https://github.com/louanben/wordle-fr). 

Les mots utilisés dans ce jeu sont tirés de la version 6 (2012) du Dictionnaire Officiel du Scrabble. Tous les mots utilisés dans le jeu ont une longueur comprise entre 3 et 6 lettres et sont conservés dans les fichiers .txt du repo.\
Par exemple, le fichier *mots4.txt* contient tous les mots valides de 4 lettres.




