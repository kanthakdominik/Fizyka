# 28 — Mechanika analityczna (wstęp)

> **Status:** ✅ pełny · **Poziom:** 🔵 · **Odpowiednik:** Mechanika teoretyczna / klasyczna (pierwsza część) · **Czas:** 20–35 h od zera

## Cel modułu

Poznać sformułowanie mechaniki przez zasadę najmniejszego działania, równania Lagrange'a i Hamiltona oraz związek symetrii z prawami zachowania — język, w którym zapisuje się fizykę teoretyczną.

## Wymagania wstępne

- [00 Narzędzia matematyczne fizyka](../00-narzedzia-matematyczne/)
- [05 Pęd, środek masy i zderzenia](../05-ped-i-zderzenia/)
- [06 Bryła sztywna, statyka i sprężystość](../06-bryla-sztywna/)
- [09 Drgania](../09-drgania/)

## Tematy

| # | Temat | Poziom | OpenStax (PL) | Halliday — wyd. 2015 (paragraf, strona) · wyd. 1 (PDF) |
|---|---|---|---|---|
| 01 | [Rachunek wariacyjny i zasada najmniejszego działania](01-zasada-najmniejszego-dzialania.md) | 🔵 | — | — |
| 02 | [Więzy, współrzędne uogólnione i równania Lagrange'a](02-rownania-lagrangea.md) | 🔵 | — | — |
| 03 | [Symetrie i prawa zachowania — twierdzenie Noether](03-symetrie-i-prawa-zachowania.md) | 🔵 | — | — |
| 04 | [Funkcja Hamiltona, równania Hamiltona i przestrzeń fazowa](04-rownania-hamiltona.md) | 🔵 | — | — |
| 05 | [Małe drgania i drgania sprzężone — mody normalne](05-mody-normalne.md) | 🔵 | — | — |

🟢 matura rozszerzona · 🔵 studia (1. rok) · 🟢🔵 temat maturalny pogłębiany na studiach

Wszystkie wzory modułu na jednej stronie: **[ściąga](SCIAGA.md)**.

## Główne źródła modułu

| Źródło | Zakres |
|---|---|
| [phyphox](https://phyphox.org/) — pomiary smartfonem | doświadczenia w tematach 28.04, 28.05 |
| [S. Charzyński, K. Turzyński, *Mechanika analityczna*, „Delta” 9/2016](https://deltami-old.mimuw.edu.pl/temat/fizyka/mechanika/2016/09/03/1609delta-mechanika-analityczna.pdf) | popularne wprowadzenie do zasady najmniejszego działania, po polsku |
| [W. Wojtyński, *Matematyczne metody mechaniki*, skrypt MIMUW](https://mst.mimuw.edu.pl/wyklady/mmk/wyklad.pdf) | rachunek wariacyjny, równania Lagrange'a i Hamiltona, symetrie, po polsku |
| J. R. Taylor, *Mechanika klasyczna*, PWN | podręcznik z wieloma przykładami i zadaniami |
| L. D. Landau, E. M. Lifszyc, *Mechanika*, PWN | klasyczny, zwięzły wykład mechaniki teoretycznej |
| [R. Feynman, *The Feynman Lectures on Physics*, t. II, rozdz. 19 „The Principle of Least Action”](https://www.feynmanlectures.caltech.edu/II_19.html) | wykład o zasadzie najmniejszego działania (po angielsku; po polsku w *Feynmana wykładach z fizyki*, PWN) |

## Test wejściowy (diagnoza)

Rozwiąż bez notatek, około 30 minut.

1. Oblicz pochodne cząstkowe $f(x, y) = x^2y + \sin(xy)$ po $x$ i po $y$.
2. Scałkuj przez części $\displaystyle\int_0^\pi x\cos x\,dx$.
3. Zapisz energię kinetyczną punktu poruszającego się po okręgu o promieniu $R$ przez prędkość kątową $\dot\varphi$. Jak wygląda ona we współrzędnych biegunowych dla ruchu dowolnego?
4. Wahadło matematyczne o długości $l$ wychylono o kąt $\theta$. Zapisz jego energię potencjalną względem najniższego położenia.
5. Rozwiąż równanie $\ddot x = -\omega^2x$ z warunkami $x(0) = A$, $\dot x(0) = 0$.
6. Znajdź wartości własne macierzy $\begin{pmatrix}2 & -1\\ -1 & 2\end{pmatrix}$.

<details>
<summary>Odpowiedzi</summary>

1. $\partial_x f = 2xy + y\cos(xy)$, $\partial_y f = x^2 + x\cos(xy)$
2. $[x\sin x]_0^\pi - \int_0^\pi\sin x\,dx = -2$
3. $\tfrac12mR^2\dot\varphi^2$; ogólnie $\tfrac12m(\dot r^2 + r^2\dot\varphi^2)$
4. $mgl(1 - \cos\theta)$
5. $x = A\cos\omega t$
6. 1 i 3
</details>

## Projekt modułowy: od lagranżjanu do symulacji

- [ ] **Wahadło na wózku.** Wyprowadź równania Lagrange'a dla wahadła zawieszonego na wózku poruszającym się bez tarcia po poziomej szynie (2 stopnie swobody). Rozwiąż je numerycznie (25.02), sprawdź zachowanie energii i pędu poziomego, znajdź mody małych drgań.
- [ ] **Brachistochrona doświadczalnie.** Zbuduj dwa tory (prosty i cykloidalny) z tymi samymi końcami, zmierz czasy zjazdu kulki (nagranie w zwolnionym tempie) i porównaj z obliczeniami, uwzględniając toczenie kulki (06.04).
- [ ] **Przestrzeń fazowa wahadła tłumionego.** Zmierz w phyphox prędkość kątową wahadła, scałkuj do kąta i narysuj portret fazowy. Porównaj z rozwiązaniem numerycznym z tłumieniem.
- [ ] **Mody łańcucha.** Zbuduj łańcuch 3–5 wahadeł połączonych gumkami, wyznacz doświadczalnie częstości modów i porównaj z obliczeniami z macierzy sztywności.
- [ ] W sprawozdaniu porównaj nakład pracy przy wyprowadzaniu równań metodą sił i metodą Lagrange'a dla wybranego układu.

## Sprawdzian końcowy modułu

- [ ] Wyprowadzam równanie Eulera–Lagrange'a z warunku ekstremum funkcjonału; rozwiązuję zagadnienia najkrótszej drogi, brachistochrony i zasady Fermata.
- [ ] Wybieram współrzędne uogólnione, zapisuję lagranżjan i wyprowadzam równania ruchu dla wahadeł, maszyny Atwooda, klina, koralika na obracającym się okręgu.
- [ ] Rozpoznaję współrzędne cykliczne i wielkości zachowane; stosuję twierdzenie Noether i potencjał efektywny w polu centralnym.
- [ ] Przechodzę od lagranżjanu do hamiltonianu, zapisuję równania Hamiltona, rysuję i interpretuję portrety fazowe; wyjaśniam twierdzenie Liouville'a i znaczenie metod symplektycznych.
- [ ] Wyznaczam mody normalne i częstości małych drgań z równania $\det(K - \omega^2M) = 0$; opisuję dudnienia i przejście łańcucha mas w falę.
