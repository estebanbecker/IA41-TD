not2(A):- A , !, fail.
not2(_).

sas(C,A,_):- C,!, A.
sas(_,_,B):- B.