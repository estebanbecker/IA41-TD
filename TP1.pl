homme(odilon).
homme(roger).
homme(vincent).
homme(arnaud).
homme(marcel).
homme(blaise).
homme(edouard).
homme(marius).

femme(pauline).
femme(genevieve).
femme(melanie).
femme(roseline).
femme(agnes).
femme(paule).
femme(martine).
femme(tatiana).
femme(prisca).

couple(1,odilon, genevieve).
couple(2,roger, melanie).
couple(3,vincent, roseline).
couple(4,marcel,paule).
couple(5,edouard,tatiana).

enfant(pauline, 1).
enfant(melanie, 1).
enfant(edouard, 1).
enfant(roseline, 2).
enfant(marcel, 2).
enfant(agnes, 3).
enfant(arnaud, 3).
enfant(martine, 4).
enfant(blaise, 4).
enfant(marius, 5).
enfant(prisca, 5).

pere(X,Y) :- homme(X), couple(A,X,_), enfant(Y,A).
mere(X,Y) :- femme(X), couple(A,_,X), enfant(Y,A).
parent(X,Y) :- pere(X,Y).
parent(X,Y) :- mere(X,Y).
soeur(X,Y) :- femme(X), enfant(X,A), enfant(Y,A), X\=Y.
frere(X,Y) :- homme(X), enfant(X,A), enfant(Y,A), X\=Y.
frere_ou_soeur(X,Y) :- frere(X,Y). 
frere_ou_soeur(X,Y) :- soeur(X,Y).
grand_parent(X,Y) :- parent(X,A), parent(A,Y).
oncle(X,Y) :- homme(X), frere_ou_soeur(X,A), parent(A,Y).
tante(X,Y) :- femme(X), frere_ou_soeur(X,A), parent(A,Y).
cousin(X,Y) :- homme(X), oncle(A,X), parent(A,Y).
cousin(X,Y) :- homme(X), tante(A,X), parent(A,Y).
cousine(X,Y) :- femme(X), oncle(A,X), parent(A,Y).
cousine(X,Y) :- femme(X), tante(A,X), parent(A,Y).