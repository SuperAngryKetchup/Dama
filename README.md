# Python Dámajáték
Ez egy dámajáték megvalósítva Pythonban.

A programot az ezt_indítsd.py file-t futtatva kell használni. A futtatáshoz szükséges a pygame (https://www.pygame.org/news) csomag.

Lehetőség van 2 emberi játékos egymás elleni játékára az "uj jatek 2 jatekos" menüpontot választva.

Illetve lehet játszani a számítógép ellen az "uj jatek AI ellen" menüpontot választva. Az AI egy MIN-MAX algoritmus szerint működik.

A játékban a klasszikus dáma szabályai érvényesek, ütéskényszer nincs. Döntetlen esetén, avagy amikor az egyik fél nem tud szabályosan lépni, automatikusan az ellenfél nyer.

Az alábbi képen látható a játék felülete. Itt a piros játékos jön, a kék hátterű mezőn lévő bábuját választotta ki, ekkor a megjelenő kék hátterű üres mezők a lépési lehetőségei (ezek között van lépés, ütés, illetve ütéssorozat is). Ha másik bábuval szeretne lépni, akkor arra kattintva megjelennek a lehetőségek. Ha üres mezőre kattint, akkor eltűnnek az aktuális lehetőségek.
![dama](https://github.com/SuperAngryKetchup/damajatek/assets/113912999/ba0c6726-34b9-4e0f-be60-aa31d4efc22d)
