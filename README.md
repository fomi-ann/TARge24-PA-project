# TARge24-PA-projekt
 TARge24 / THK / Group Project

# Grupp 5
- Anna Fomina
- Kati Koppel
- Kevin Randla

# Idee
Menüü kalkulaator

# Jira projekti link
https://katikoppel95.atlassian.net/jira/software/projects/TEAM/boards/3?atlOrigin=eyJpIjoiOWNlNmUxN2ZiMzUxNGY1YTk5OWRiNmJkYjM1MGJlZGYiLCJwIjoiaiJ9

# Nõuded
Python 3.12 ja pandas package

# Kasutusjuhend
1. Programm küsib kas sa tahad sisse logida, registreerida või jätkata.
 - L või login(case insensitive) laseb sisse logida oma kasutaja ID-ga mida genereeritakse sulle
 - R või register inputiga laseb programm sul registreerida kontot
 - C või continue inputiga laseb programm sul jätkata
 - Kasutaja registreerimisel ja niisama jätkamisel küsib programm nime ja pangakontot.
 - Nimi peab olema eraldatud tühikuga ja numbreid ei tohi hoida.
 - Pangakonto peab sisaldama 16 numbrit ja mitte ühtegi tähte.
 - Registreerimise lõpus prinditakse välja uus kasutaja ID
2. Programm laeb ette menüü ning kasutaja peab sisestama pitsa järjenumbri, et seda valida
3. Programm küsib kas kasutaja tahab peenikese või paksu põhjaga pitsat. thick ja thin(case insensitive) on aktsepteeritavad inputtid
4. Programm küsib mis suurust kasutaja tahab ja aktsepteeritavad inputtid on 25 ja 30
5. Programm küsib kas kasutaja tahab veel midagi lisada, aktsepteeritavad inputtid on y, yes, n ja no
6. Programm küsib kas kasutaja tahab orderit kinnitada. Aktsepteeritavad inputtid on y ja n.
-- kui on valitud n:
- küsib kas kasutaja tahab lisada, muuta või kustutada orderit. inputtid on add/change/delete
- change valimisel laeb praeguse orderi pitsad ja küsib järjenumbrit kustutamiseks
- delete valimisel ütleb programm et order on kustutatud ja lõpetab programmi
-- kui on valitud y siis programm prindib välja orderi summary juhul kui order ei ole tühi ning lõpetab programmi
