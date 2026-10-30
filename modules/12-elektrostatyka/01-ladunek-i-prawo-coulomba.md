# 12.01 — Ładunek elektryczny i prawo Coulomba

> **Moduł:** [12 — Elektrostatyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 5: [§5.1–5.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/5-1-ladunek-elektryczny) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/5-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §21.1–21.3 (s. 1)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: [§22.1–22.6, s. 2](https://home.agh.edu.pl/~czapli/Resnick_3.pdf#page=12) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Natężenie pola, linie pola i dipol](02-pole-elektryczne.md) →

## Po co to jest

Siły elektryczne trzymają w całości atomy, cząsteczki i wszystkie ciała stałe. Tarcie, sprężystość, nacisk podłoża i reakcje chemiczne to w gruncie rzeczy oddziaływania elektryczne. Prawo Coulomba jest punktem wyjścia całej elektryczności. Ma tę samą postać co prawo grawitacji (07.01), ale siła jest o ok. 39 rzędów wielkości silniejsza i może być odpychająca. Z elektryzowania korzystają kserografy, malowanie proszkowe, elektrofiltry kominowe i drukarki laserowe, a wyładowania elektrostatyczne potrafią zniszczyć elektronikę.

## Teoria w pigułce

**Ładunek elektryczny** występuje w dwóch rodzajach, dodatnim i ujemnym. Ładunki jednoimienne się odpychają, a różnoimienne przyciągają. Jednostką jest kulomb (C).

- **Kwantyzacja:** każdy ładunek swobodny jest całkowitą wielokrotnością ładunku elementarnego $e = 1{,}602\cdot10^{-19}\ \mathrm C$. Elektron ma $-e$, proton $+e$.
- **Zasada zachowania ładunku:** w układzie izolowanym suma ładunków jest stała. Elektryzowanie nie tworzy ładunku, tylko go przenosi (zwykle elektrony).

**Przewodniki i izolatory.** W metalach część elektronów porusza się swobodnie, a w izolatorach elektrony są związane z atomami. Ciało można naelektryzować:
- przez **pocieranie** (bursztyn, balon o włosy);
- przez **dotyk** naelektryzowanym ciałem;
- przez **indukcję**: zbliżony ładunek rozsuwa ładunki w przewodniku, a uziemienie odprowadza jedną ich część.

Nienaelektryzowany izolator też jest przyciągany przez naelektryzowane ciało, bo jego cząsteczki się **polaryzują** (07). Dlatego potarty balon przyczepia się do ściany.

**Prawo Coulomba.** Dwa ładunki punktowe działają na siebie siłą skierowaną wzdłuż łączącej je prostej:

$$F = k\frac{\lvert q_1q_2\rvert}{r^2}, \qquad k = \frac{1}{4\pi\varepsilon_0} \approx 8{,}99\cdot10^9\ \mathrm{\frac{N\cdot m^2}{C^2}},$$

gdzie $\varepsilon_0 = 8{,}854\cdot10^{-12}\ \mathrm{C^2/(N\cdot m^2)}$ to przenikalność elektryczna próżni. Wektorowo: $\vec F_{12} = k\dfrac{q_1q_2}{r^2}\hat r_{12}$, gdzie $\hat r_{12}$ to wektor jednostkowy od ładunku 1 do 2. Znak iloczynu decyduje o kierunku.

**Zasada superpozycji.** Siła wypadkowa działająca na ładunek to wektorowa suma sił od wszystkich pozostałych ładunków. Każda para działa niezależnie.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $q = Ne$ | kwantyzacja ładunku | $e = 1{,}602\cdot10^{-19}\ \mathrm C$ |
| $F = k\lvert q_1q_2\rvert/r^2$ | prawo Coulomba | ładunki punktowe (lub kule), spoczywające |
| $k = 1/(4\pi\varepsilon_0) \approx 9\cdot10^9\ \mathrm{N\,m^2/C^2}$ | stała elektryczna | próżnia (powietrze w przybliżeniu) |
| $\vec F = \sum_i\vec F_i$ | superpozycja | — |

## Przykład rozwiązany

**Zadanie 1.** W atomie wodoru elektron jest średnio w odległości $5{,}29\cdot10^{-11}\ \mathrm m$ od protonu. Porównaj siłę elektryczną z grawitacyjną.

$F_e = 8{,}99\cdot10^9\cdot\dfrac{(1{,}602\cdot10^{-19})^2}{(5{,}29\cdot10^{-11})^2} \approx 8{,}2\cdot10^{-8}\ \mathrm N$.

$F_g = \dfrac{Gm_em_p}{r^2} \approx 3{,}6\cdot10^{-47}\ \mathrm N$.

Stosunek wynosi ok. $2\cdot10^{39}$. W świecie atomów grawitacja nie gra żadnej roli. Dla planet jest odwrotnie, bo są elektrycznie obojętne.

**Zadanie 2.** Trzy ładunki po $1\ \mu\mathrm C$ leżą w wierzchołkach trójkąta równobocznego o boku 10 cm. Oblicz siłę działającą na jeden z nich.

Każda z dwóch sił ma wartość $k\cdot10^{-12}/0{,}01 \approx 0{,}90\ \mathrm N$, a kąt między nimi wynosi $60^\circ$. Wypadkowa $F = 2\cdot0{,}90\cos30^\circ \approx 1{,}56\ \mathrm N$, skierowana od środka trójkąta.

## Typowe pułapki

- **Odległość nie do kwadratu.** Siła maleje jak $1/r^2$. Dwa razy dalej to cztery razy słabiej.
- **Dodawanie wartości sił.** Siły od kilku ładunków dodaje się wektorowo.
- **Mikro- i nanokulomby.** $1\ \mu\mathrm C = 10^{-6}\ \mathrm C$, $1\ \mathrm{nC} = 10^{-9}\ \mathrm C$. Ładunki z elektryzowania przez pocieranie to zwykle nanokulomby.
- **Naelektryzowanie = dodanie protonów.** Ciało elektryzuje się dodatnio przez **utratę elektronów**.
- **Prawo Coulomba dla ciał rozciągłych.** Dla kul jednorodnie naładowanych działa jak dla punktów (wynika to z prawa Gaussa, 12.04). Dla innych kształtów trzeba całkować (12.03).

## Doświadczenie / symulacja

**Elektroskop z puszki.** Przyklej dwa paski folii aluminiowej do drutu wbitego w korek słoika. Zbliżaj potarty balon albo plastikową linijkę. Paski rozchylają się już przy zbliżaniu (indukcja), a przy dotknięciu ładunek przechodzi na elektroskop.

**Dwa balony na nitkach.** Naelektryzuj dwa jednakowe balony i zawieś je obok siebie. Z masy, długości nici i odległości balonów oszacuj ich ładunek (zadanie B1).

**Symulacje PhET:** *Prawo Coulomba* (*Coulomb's Law*), *Balony i elektryczność statyczna* (*Balloons and Static Electricity*), *John Travoltage* — [phet.colorado.edu/pl](https://phet.colorado.edu/pl/).

**Python:** siła wypadkowa w układzie kilku ładunków (superpozycja wektorowa).

```python
import numpy as np

k = 8.9875e9
q = np.array([1e-6, 1e-6, 1e-6])                     # ładunki [C]
r = np.array([[0, 0], [0.1, 0], [0.05, 0.1*np.sqrt(3)/2]])   # trójkąt równoboczny 10 cm

def sila_na(i):
    F = np.zeros(2)
    for j in range(len(q)):
        if j != i:
            d = r[i] - r[j]
            F += k*q[i]*q[j]*d/np.linalg.norm(d)**3
    return F

for i in range(3):
    F = sila_na(i)
    print(f"ładunek {i}: F = ({F[0]:+.3f}, {F[1]:+.3f}) N, |F| = {np.linalg.norm(F):.3f} N")
print("suma wszystkich sił (III zasada dynamiki):", np.round(sum(sila_na(i) for i in range(3)), 12))
```

## Zadania

### A. Poziom maturalny

1. Ile elektronów trzeba zabrać z kulki, żeby uzyskała ładunek $+1\ \mu\mathrm C$?

<details>
<summary>Odpowiedź</summary>

$N = 10^{-6}/1{,}602\cdot10^{-19} \approx 6{,}2\cdot10^{12}$.
</details>

2. Dwa ładunki punktowe po $1\ \mu\mathrm C$ są odległe o 1 m. Oblicz siłę. Jak się zmieni, gdy odległość zmaleje do 10 cm?

<details>
<summary>Odpowiedź</summary>

$F \approx 9\cdot10^{-3}\ \mathrm N$; przy 10 cm wzrośnie 100 razy, do ok. 0,9 N.
</details>

3. Dwie jednakowe metalowe kulki mają ładunki $+5\ \mathrm{nC}$ i $-1\ \mathrm{nC}$. Zetknięto je i rozsunięto na poprzednią odległość. Jak zmieniła się siła?

<details>
<summary>Odpowiedź</summary>

Po zetknięciu każda ma $+2\ \mathrm{nC}$. Siła zmieniła się z przyciągającej o wartości $\propto 5$ na odpychającą o wartości $\propto 4$, czyli zmalała do 0,8 poprzedniej i zmieniła zwrot.
</details>

4. Ładunek $q$ leży w punkcie $x = 0$, a ładunek $4q$ w punkcie $x = L$ (oba dodatnie). Gdzie na odcinku między nimi trzeci ładunek będzie w równowadze?

<details>
<summary>Odpowiedź</summary>

$\dfrac{q}{x^2} = \dfrac{4q}{(L - x)^2} \Rightarrow L - x = 2x \Rightarrow x = L/3$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Dwie kulki o masie 1 g wiszą na niciach o długości 1 m zaczepionych w jednym punkcie. Po naelektryzowaniu jednakowym ładunkiem rozsunęły się na 10 cm. Oblicz ładunek.

<details>
<summary>Odpowiedź</summary>

$\sin\theta = 0{,}05$, $F = mg\tan\theta \approx 4{,}9\cdot10^{-4}\ \mathrm N$, $q = r\sqrt{F/k} \approx 23\ \mathrm{nC}$.
</details>

2. Ładunek $Q$ jest rozłożony równomiernie na pręcie o długości $L$. Oblicz całkowaniem siłę działającą na ładunek punktowy $q$ leżący na przedłużeniu pręta w odległości $a$ od jego końca. Sprawdź granicę $a \gg L$.

<details>
<summary>Odpowiedź</summary>

$F = \displaystyle\int_a^{a+L}\frac{kq(Q/L)\,dx}{x^2} = \frac{kqQ}{L}\left(\frac1a - \frac{1}{a + L}\right) = \frac{kqQ}{a(a + L)}$. Dla $a \gg L$ wychodzi $kqQ/a^2$, jak dla ładunku punktowego.
</details>

3. Ile wynosi ładunek wszystkich elektronów w 1 g wody? Oszacuj siłę, z jaką przyciągałyby się dwa takie zbiory ładunku w odległości 1 m, gdyby nie było protonów.

<details>
<summary>Odpowiedź</summary>

1 g wody to $1/18$ mola, a cząsteczka ma 10 elektronów: $N \approx 3{,}3\cdot10^{23}$, $q \approx 5{,}4\cdot10^4\ \mathrm C$. Siła $kq^2 \approx 2{,}6\cdot10^{19}\ \mathrm N$, czyli tyle, ile ważyłaby na Ziemi skalista planetoida o średnicy ok. 130 km. Materia jest neutralna z ogromną dokładnością.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 5 — §5.1 (ładunek elektryczny), §5.2 (przewodniki, izolatory i elektryzowanie przez indukcję), §5.3 (prawo Coulomba).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §21.1–21.3; wyd. 1: t. 3, §22.1–22.6.
- Symulacje PhET *Prawo Coulomba* i *Balony i elektryczność statyczna*.
