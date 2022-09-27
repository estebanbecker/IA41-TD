member(X,[A|R]):-member(X,R).
member(A,[A|_]).

entree_liste([foie_gras, salade_gourmande, crudites, tomates_mozzarella]).

entree(X):-entree_liste(L),member(X,L).

viande_liste([entrecote, magret_de_canard, dinde_fermiere]).

viande(X):-viande_liste(L),member(X,L).

poisson_liste([truite_meuniere, brochet_de_loire, cube_de_bar_en_dret]).

poisson(X):-poisson_liste(L),member(X,L).

dessert_liste([mousse_au_chocolat, sorbet, ile_flottante, poire_belle_helene]).

dessert(X):-dessert_liste(L),member(X,L).

plat(X):-viande(X).
plat(X):-poisson(X).

menu(X,Y,Z):-entree(X),plat(Y),dessert(Z).

calories_liste([[foie_gras,208],[salade_gourmande,154],[crudites,81],[tomates_mozzarella,109],[entrecote,537],[magret_de_canard,405],[dinde_fermiere,382],[truite_meuniere,260],[brochet_de_loire,256],[cube_de_bar_en_dret,292],[mousse_au_chocolat,136],[sorbet,60],[ile_flottante,95],[poire_belle_helene,114]]).
calories(X,Y):-calories_liste(L),member([X,Y],L).

menu_kc(X,Y,Z,K):-menu(X,Y,Z),calories(X,A),calories(Y,B),calories(Z,C),K is A+B+C.