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
   * `L` või `login` laseb sisse logida oma kasutaja ID-ga mida genereeritakse sulle
   * `R` või `register` inputiga laseb programm sul registreerida kontot
   * `C` või `continue` inputiga laseb programm sul jätkata
   * Kasutaja registreerimisel ja niisama jätkamisel küsib programm nime ja pangakontot.
   * Nimi peab olema eraldatud tühikuga ja numbreid ei tohi hoida.
   * Pangakonto peab sisaldama 16 numbrit ja mitte ühtegi tähte.
   * Registreerimise lõpus prinditakse välja uus kasutaja ID
2. Programm laeb ette menüü ning kasutaja peab sisestama pitsa järjenumbri, et seda valida
3. Programm küsib kas kasutaja tahab peenikese või paksu põhjaga pitsat. `thick` ja `thin` on aktsepteeritavad inputtid
4. Programm küsib mis suurust kasutaja tahab ja aktsepteeritavad inputtid on `25` ja `30`
5. Programm küsib kas kasutaja tahab veel midagi lisada, aktsepteeritavad inputtid on `y`, `yes`, `n` ja `no`
6. Programm küsib, kas kasutaja tahab tellimust kinnitada. Aktsepteeritavad sisendid on `y` ja `n`.

    **Kui on valitud "**n**":**

    * Programm küsib, kas kasutaja soovib tellimust **lisada**, **muuta** või **kustutada**.
        * Lubatud sisendid on: `add`, `change`, `delete`.
    * **"change"** valiku korral:
        * Programm laeb praeguse tellimuse pitsad.
        * Seejärel küsib programm **järjenumbrit**, mida kasutaja soovib muuta või kustutada.
    * **"delete"** valiku korral:
        * Programm kuvab teate: "**Tellimus on kustutatud**" ja lõpetab töö.

    **Kui on valitud "**y**":**

    * Programm prindib välja tellimuse **kokkuvõtte** (summary) **juhul, kui tellimus ei ole tühi**.
    * Seejärel programm lõpetab töö.
