sport(tennis).
sport(badminton).
sport(natation).
sport(jogging).
sport(football).
sport(basketball).
sport(athletisme).
sport(escalade).
sport(volleyball).
sport(rugby).
sport(escrime).

musique(jazz).
musique(rock).
musique(pop).
musique(classique).
musique(reggae).
musique(rap).
musique(techno).
musique(metal).
musique(blues).
musique(soul).
musique(folk).

livre(aventures).
livre(policiers).
livre(sciencefiction).

taille(petit).
taille(moyenne).
taille(grand).

homme(paul,grand,brun,mur).
homme(pierre,moyenne,blond,jeune).
homme(pean,petit,brun,mur).

femme(marie,moyenne,blond,moyen).
femme(eva,petit,blond,jeune).
femme(lea,petit,brun,mur).

aime(paul,classique,aventures,natation).
aime(pierre,rock,sciencefiction,tennis).
aime(jean,jazz,policiers,tennis).
aime(marie,X,aventures,natation):- musique(X).
aime(eva,rock,sciencefiction,X):- sport(X) , X\=jogging.
aime(lea,classique,aventures,natation).

cherche(paul,grand,rousse,jeune).
cherche(pierre,X,blond,jeune):- taille(X), X\=grand.
cherche(jean,petit,blond,moyen).
cherche(marie,grand,brun,moyen).
cherche(eva,moyenne,blond,jeune).
cherche(lea,moyenne,brun,mur).

convient_physiquement(X,Y):- homme(X,A,B,C), femme(Y,_,_,_), cherche(Y,A,B,C).
convient_physiquement(X,Y):- femme(X,A,B,C), homme(Y,_,_,_), cherche(Y,A,B,C).

ont_meme_gout(X,Y):- aime(X,A,B,C), aime(Y,A,B,C), X\=Y.

convient(X,Y):- convient_physiquement(X,Y), ont_meme_gout(X,Y), convient_physiquement(Y,X), homme(X,_,_,_), femme(Y,_,_,_).
