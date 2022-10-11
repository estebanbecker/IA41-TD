premier(A,[A|_]).

dernier(A,[_|B]) :- dernier(A,B).
dernier(A,[A]).

ajout_debut(A,B,[A|B]).

ajout_fin(A,[],[A]).
ajout_fin(A,[B|C],[B|D]) :- ajout_fin(A,C,D).

incluse([],_).
incluse([A|B],C) :- member(A,C), incluse(B,C).

cons_list_npaire([],[]).
cons_list_npaire([A|B],[A|C]) :- paire(A), cons_list_npaire(B,C), !.
cons_list_npaire([_|B],C) :- cons_list_npaire(B,C).

paire(A) :- A mod 2 =:= 0.


cons_liste_pn(N,L) :- cons_liste_pn(N,1,L).
cons_liste_pn(N,N,[N]) :- !.
cons_liste_pn(N,A,[A|B]) :-A1 is A+1, cons_liste_pn(N,A1,B).

cons_liste_ordonnee([],B,B).
cons_liste_ordonnee(A,[],A).
cons_liste_ordonnee([A|B],[C|D],[A|E]) :- A =< C, cons_liste_ordonnee(B,[C|D],E), !.
cons_liste_ordonnee(A,[C|D],[C|E]) :- cons_liste_ordonnee(A,D,E).