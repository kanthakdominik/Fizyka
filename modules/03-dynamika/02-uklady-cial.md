# 03.02 — Diagramy sił i układy ciał (równia, bloczki, więzy)

> **Moduł:** [03 — Dynamika punktu materialnego](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 5: [§5.7 i §6.1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/5-7-rozklady-sil-dzialajacych-na-ciala) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/5-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §5.3 (s. 134)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§5.8, s. 101](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=113) — PDF z serwera AGH

← [Zasady dynamiki Newtona i rodzaje sił](01-zasady-dynamiki.md) · [spis modułu](README.md) · [Tarcie statyczne i kinetyczne](03-tarcie.md) →

## Po co to jest

Zadania z równią pochyłą, bloczkami i połączonymi klockami to klasyka matury i pierwszego kolokwium z fizyki. Same zasady Newtona są proste — trudność polega na tym, żeby poprawnie zobaczyć wszystkie siły i zapisać równania. Metoda z tego tematu (rysunek sił dla każdego ciała osobno, wybór osi, więzy) działa w każdym zadaniu z dynamiki.

## Teoria w pigułce

**Procedura rozwiązywania.**

1. **Wyodrębnij każde ciało** i narysuj dla niego osobny **diagram sił** (rozkład sił): tylko siły działające *na to ciało*, każda z podanym źródłem.
2. **Wybierz osie** dla każdego ciała — najlepiej jedną wzdłuż kierunku ruchu (na równi: wzdłuż równi i prostopadle do niej).
3. **Zapisz II zasadę** dla każdej osi każdego ciała: $\sum F_x = ma_x$, $\sum F_y = ma_y$.
4. **Dopisz więzy** — związki wynikające z połączeń: ciała połączone nierozciągliwą nicią mają przyspieszenia o tej samej wartości; nieważka nić przez nieważki bloczek bez tarcia ma jednakowy naciąg po obu stronach.
5. **Rozwiąż układ równań** i sprawdź wynik (znak, jednostki, przypadki graniczne).

**Równia pochyła o kącie $\alpha$.** Ciężar rozkładamy na składową wzdłuż równi $mg\sin\alpha$ i prostopadłą $mg\cos\alpha$. Bez tarcia i bez innych sił: $N = mg\cos\alpha$, $a = g\sin\alpha$.

**Maszyna Atwooda** — dwa ciężarki $m_1 > m_2$ na nici przerzuconej przez bloczek:

$$a = \frac{m_1 - m_2}{m_1 + m_2}\,g, \qquad T = \frac{2m_1m_2}{m_1 + m_2}\,g.$$

Naciąg jest pośredni między ciężarami obu ciał: $m_2g < T < m_1g$.

**Układ jako całość.** Gdy interesuje nas tylko przyspieszenie, możemy potraktować połączone ciała jak jedno o masie $m_1 + m_2$ — siły wewnętrzne (naciągi, siły nacisku między klockami) się znoszą. Żeby obliczyć siłę wewnętrzną, trzeba wrócić do diagramu jednego ciała.

## Wzory i założenia

| Wzór | Znaczenie | Założenia |
|---|---|---|
| $a = g\sin\alpha$, $\ N = mg\cos\alpha$ | równia bez tarcia | jedyne siły: ciężar i reakcja |
| $a = \dfrac{m_1 - m_2}{m_1 + m_2}g$ | maszyna Atwooda | nić nieważka i nierozciągliwa, bloczek nieważki bez tarcia |
| $a = \dfrac{m_2}{m_1 + m_2}g$, $\ T = m_1a$ | klocek $m_1$ na stole, $m_2$ wiszący | stół bez tarcia |
| $a = \dfrac{F}{m_1 + m_2}$, $\ F_{12} = m_2a$ | siła pchająca dwa klocki | siła $F$ przyłożona do $m_1$ |

## Przykład rozwiązany

**Zadanie 1 — równia.** Klocek o masie 2 kg zsuwa się z gładkiej równi nachylonej pod kątem $30^\circ$. Oblicz przyspieszenie i siłę nacisku na równię.

Osie: $x$ w dół równi, $y$ prostopadle. $x$: $mg\sin30^\circ = ma \Rightarrow a = 4{,}9\ \mathrm{m/s^2}$. $y$: $N - mg\cos30^\circ = 0 \Rightarrow N \approx 17{,}0\ \mathrm{N}$.

**Zadanie 2 — klocek i ciężarek.** Klocek $m_1 = 4\ \mathrm{kg}$ leży na gładkim stole i jest połączony nicią przerzuconą przez bloczek na krawędzi stołu z wiszącym ciężarkiem $m_2 = 1\ \mathrm{kg}$. Oblicz przyspieszenie i naciąg nici.

Diagramy sił:
- $m_1$ (poziomo): tylko naciąg $T$ → $T = m_1a$.
- $m_2$ (pionowo, oś w dół): $m_2g - T = m_2a$.

Dodając równania: $m_2g = (m_1 + m_2)a \Rightarrow a = \dfrac{1}{5}g \approx 1{,}96\ \mathrm{m/s^2}$, $T = 4\cdot1{,}96 \approx 7{,}85\ \mathrm{N}$.

**Sprawdzenie.** $T < m_2g = 9{,}81\ \mathrm{N}$ — gdyby naciąg był równy ciężarowi, ciężarek nie przyspieszałby. Dla $m_1 \to 0$: $a \to g$ (swobodny spadek). Zgadza się.

## Typowe pułapki

- **Wspólny diagram dla kilku ciał.** Każde ciało ma własny rysunek sił.
- **Naciąg równy ciężarowi wiszącego ciała.** Tylko gdy układ jest w spoczynku lub porusza się jednostajnie.
- **$N = mg$ na równi.** Na równi $N = mg\cos\alpha$ (bez innych sił prostopadłych).
- **Siła „dośrodkowa”, „wypadkowa” lub „ma” na diagramie.** Na diagramie rysujemy tylko siły rzeczywiste; $m\vec{a}$ jest po drugiej stronie równania.
- **Niespójne zwroty osi.** Dla ciał połączonych nicią wybierz osie tak, żeby dodatni ruch jednego odpowiadał dodatniemu ruchowi drugiego.

## Doświadczenie / symulacja

**Maszyna Atwooda z telefonem.** Przewieś przez gładki pręt (np. drążek do zasłon) sznurek z dwoma woreczkami o masach różniących się o kilkadziesiąt gramów. Do cięższego przywiąż telefon z phyphox (*Acceleration (without g)*) albo nagraj ruch i przeanalizuj w Trackerze. Porównaj zmierzone przyspieszenie ze wzorem — różnicę wyjaśnij tarciem sznurka.

**Symulacja PhET:** *Rampa: siły i ruch* (*The Ramp: Forces and Motion*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)) — rozkład sił na równi.

**Python:** przyspieszenie układu „klocek na równi + ciężarek” w funkcji kąta nachylenia.

```python
import numpy as np
import matplotlib.pyplot as plt

g, m1, m2 = 9.81, 4.0, 3.0              # m1 na gładkiej równi, m2 wiszący
alpha = np.radians(np.linspace(0, 90, 181))
a = g * (m2 - m1*np.sin(alpha)) / (m1 + m2)   # dodatnie: m2 opada
T = m2 * (g - a)

i0 = np.argmin(abs(a))
print(f"równowaga dla α ≈ {np.degrees(alpha[i0]):.1f}° (sin α = m2/m1 = {m2/m1:.2f})")
print(f"α = 30°: a = {g*(m2 - m1*0.5)/(m1 + m2):.3f} m/s²")

plt.plot(np.degrees(alpha), a, label="a [m/s²]")
plt.plot(np.degrees(alpha), T/10, label="T/10 [N]")
plt.axhline(0, color="gray"); plt.xlabel("kąt równi [°]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Dwa stykające się klocki o masach 3 kg i 2 kg leżą na gładkim stole. Na klocek 3 kg działa pozioma siła 20 N, pchając oba klocki. Oblicz przyspieszenie i siłę, z jaką klocki naciskają na siebie.

<details>
<summary>Odpowiedź</summary>

$a = 4\ \mathrm{m/s^2}$; $F_{12} = 2\cdot4 = 8\ \mathrm{N}$.
</details>

2. Lampa o masie 5 kg wisi na dwóch linkach, każda nachylona pod kątem $30^\circ$ do poziomu. Oblicz naciąg każdej linki.

<details>
<summary>Odpowiedź</summary>

$2T\sin30^\circ = mg \Rightarrow T = mg \approx 49\ \mathrm{N}$.
</details>

3. Klocek zsuwa się z gładkiej równi o długości 3 m nachylonej pod kątem $30^\circ$. Z jaką prędkością dociera na dół?

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{2\cdot4{,}9\cdot3} \approx 5{,}4\ \mathrm{m/s}$.
</details>

4. Maszyna Atwooda: $m_1 = 3\ \mathrm{kg}$, $m_2 = 2\ \mathrm{kg}$. Oblicz przyspieszenie i naciąg nici.

<details>
<summary>Odpowiedź</summary>

$a = g/5 \approx 1{,}96\ \mathrm{m/s^2}$; $T = 2\cdot3\cdot2\cdot9{,}81/5 \approx 23{,}5\ \mathrm{N}$.
</details>

5. Lokomotywa ciągnie dwa wagony o masach 20 t każdy z przyspieszeniem $0{,}5\ \mathrm{m/s^2}$. Oblicz siłę w sprzęgu między lokomotywą a pierwszym wagonem i między wagonami (pomiń opory).

<details>
<summary>Odpowiedź</summary>

$20\ \mathrm{kN}$ i $10\ \mathrm{kN}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Klocek $m_1 = 4\ \mathrm{kg}$ na gładkiej równi o kącie $30^\circ$ jest połączony nicią przez bloczek na szczycie równi z wiszącym ciężarkiem $m_2 = 3\ \mathrm{kg}$. Oblicz przyspieszenie i naciąg.

<details>
<summary>Odpowiedź</summary>

$a = g\dfrac{m_2 - m_1\sin\alpha}{m_1 + m_2} \approx 1{,}40\ \mathrm{m/s^2}$ ($m_2$ opada); $T = m_2(g - a) \approx 25{,}2\ \mathrm{N}$.
</details>

2. Jednorodna lina o długości $L$ i masie $M$ wisi pionowo. Wyznacz naciąg w odległości $y$ od dolnego końca.

<details>
<summary>Odpowiedź</summary>

Odcinek poniżej punktu ma masę $My/L$, więc $T(y) = Mgy/L$; na górze $T = Mg$.
</details>

3. Z jakim poziomym przyspieszeniem musi poruszać się gładka równia o kącie $\alpha$, żeby leżący na niej klocek nie zsuwał się względem niej?

<details>
<summary>Odpowiedź</summary>

$N\cos\alpha = mg$, $N\sin\alpha = ma \Rightarrow a = g\tan\alpha$, skierowane poziomo w stronę niższego końca równi — tak, żeby jej powierzchnia napierała na klocek.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1 — §5.7 (rozkłady sił działających na ciała) i §6.1 (rozwiązywanie zadań z zasadami dynamiki).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §5.3; wyd. 1: t. 1, §5.8 (jak stosować zasady dynamiki Newtona — wiele przykładów rozwiązanych).
- Symulacja PhET *Rampa: siły i ruch*.
