# 17.01 — Rozchodzenie się światła i prawo odbicia

> **Moduł:** [17 — Optyka geometryczna](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1: [§1.1–1.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-1-rozchodzenie-sie-swiatla) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §33.5 (s. 23)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§34.7, s. 21](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=36) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Załamanie światła i całkowite wewnętrzne odbicie](02-zalamanie-i-calkowite-odbicie.md) →

## Po co to jest

Gdy przeszkody są dużo większe od długości fali światła (ok. 0,5 μm), światło można opisywać promieniami biegnącymi po liniach prostych. To optyka geometryczna. Wystarcza do zrozumienia cieni, zaćmień, lusterek, peryskopów, odblasków rowerowych, retroreflektorów zostawionych na Księżycu przez misje Apollo i aparatu otworkowego, od którego zaczęła się fotografia.

## Teoria w pigułce

**Promień światła** to linia wskazująca kierunek rozchodzenia się energii, prostopadła do czoła fali (10.04). W ośrodku jednorodnym promienie są prostymi. Na tym opierają się cienie i półcienie oraz zaćmienia Słońca i Księżyca.

**Prędkość światła** w próżni wynosi $c = 299\,792\,458\ \mathrm{m/s}$ (dokładnie, z definicji metra). W ośrodkach jest mniejsza: $v = c/n$ (17.02).

**Aparat otworkowy (camera obscura).** Przez mały otwór promienie od każdego punktu przedmiotu trafiają w jeden punkt ekranu. Powstaje obraz odwrócony, a powiększenie wynosi $h'/h = b/a$ (odległość ekranu przez odległość przedmiotu). Mniejszy otwór daje ostrzejszy, ale ciemniejszy obraz. Przy bardzo małym otworze ostrość psuje dyfrakcja (18).

**Odbicie.**
- **Prawo odbicia:** promień padający, odbity i normalna leżą w jednej płaszczyźnie, a kąt odbicia równa się kątowi padania (mierzonym od normalnej).
- **Odbicie zwierciadlane** od gładkiej powierzchni daje obrazy. **Odbicie rozproszone** od chropowatej (kartka, ściana) rozsyła światło we wszystkich kierunkach, dzięki czemu widzimy przedmioty z każdej strony.

**Zwierciadło płaskie** daje obraz:
- pozorny (promienie się nie przecinają, przecinają się ich przedłużenia),
- prosty, tej samej wielkości,
- symetryczny względem lustra, tak samo daleko za lustrem jak przedmiot przed nim,
- odwrócony „przód–tył”, co postrzegamy jako zamianę lewej i prawej strony.

**Retroreflektor (kątownik).** Trzy wzajemnie prostopadłe lustra odbijają promień dokładnie w kierunku, z którego przyszedł, niezależnie od kąta padania. Tak działają odblaski rowerowe, znaki drogowe i reflektory na Księżycu, od których odbija się światło laserów z Ziemi przy pomiarze odległości.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\theta_{\text{odb}} = \theta_{\text{pad}}$ | prawo odbicia | gładka powierzchnia |
| $h'/h = b/a$ | aparat otworkowy | mały otwór |
| obraz w lustrze: $y = -x$, $m = 1$ | zwierciadło płaskie | — |
| $\delta = 2\alpha$ | obrót promienia po obrocie lustra o $\alpha$ | — |

## Przykład rozwiązany

**Zadanie 1.** Drzewo o wysokości 10 m stoi w odległości 20 m od aparatu otworkowego o głębokości 10 cm. Jak duży jest obraz?

$h' = 10\cdot0{,}1/20 = 5\ \mathrm{cm}$, odwrócony.

**Zadanie 2.** Jak wysokie musi być lustro, żeby człowiek o wzroście 1,8 m zobaczył się w nim cały? Czy zależy to od odległości od lustra?

Promień od stóp odbija się w połowie wysokości między oczami a stopami, a od czubka głowy w połowie między oczami a czubkiem. Lustro musi mieć więc połowę wzrostu, 0,9 m, odpowiednio zawieszone. Wynik nie zależy od odległości.

## Typowe pułapki

- **Kąty od powierzchni.** Kąt padania i odbicia mierzy się od normalnej.
- **Obraz w lustrze jest na powierzchni lustra.** Jest za lustrem, w tej samej odległości co przedmiot. Aparat ustawiamy na tę odległość.
- **Lustro zamienia lewo z prawo.** Lustro zamienia przód z tyłem (kierunek prostopadły do lustra). „Zamianę stron” odczytujemy, bo wyobrażamy sobie, że obróciliśmy się do lustra.
- **Większe lustro z daleka pokaże więcej siebie.** Potrzebna wysokość lustra to zawsze połowa wzrostu.
- **Obraz pozorny nie istnieje.** Obrazu pozornego nie zobaczymy na ekranie, ale oko i aparat go widzą, bo soczewka oka skupia rozbieżne promienie.

## Doświadczenie / symulacja

**Camera obscura z pudełka.** W ciemnym pomieszczeniu zasłoń okno kartonem z otworem kilkumilimetrowym. Na przeciwległej ścianie lub kalce pojawi się kolorowy, odwrócony obraz ulicy. Zmierz powiększenie i porównaj z $b/a$. Sprawdź, jak ostrość i jasność zależą od średnicy otworu.

**Prawo odbicia z laserem.** Wskaźnik laserowy, lusterko i kątomierz na kartce. Zmierz kąty odbicia dla kilku kątów padania. Uwaga: nie kieruj wiązki w oczy.

**Symulacja PhET:** *Załamanie światła* (*Bending Light*) — pokazuje też odbicie ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** wektorowe prawo odbicia i retroreflektor z trzech luster.

```python
import numpy as np

def odbij(d, n):
    n = n/np.linalg.norm(n)
    return d - 2*np.dot(d, n)*n                     # d' = d − 2 (d·n) n

d = np.array([1.0, -1.0, 0]); d /= np.linalg.norm(d)
print("odbicie od podłogi:", odbij(d, np.array([0, 1.0, 0])))

rng = np.random.default_rng(0)
for _ in range(3):                                  # trzy prostopadłe lustra: kątownik
    d = -np.abs(rng.normal(size=3)); d /= np.linalg.norm(d)
    d2 = d.copy()
    for n in np.eye(3):
        d2 = odbij(d2, n)
    print(f"wchodzi {np.round(d, 3)}, wychodzi {np.round(d2, 3)} (dokładnie odwrócony)")

h, x_oczu = 1.8, 1.7                                # wzrost i wysokość oczu
print(f"lustro: od {x_oczu/2:.2f} m do {(x_oczu + h)/2:.2f} m, wysokość {h/2:.2f} m")
```

## Zadania

### A. Poziom maturalny

1. Promień pada na lustro pod kątem $35^\circ$ do jego powierzchni. Ile wynosi kąt między promieniem padającym a odbitym?

<details>
<summary>Odpowiedź</summary>

Kąt padania od normalnej to $55^\circ$, więc kąt między promieniami $110^\circ$.
</details>

2. Stoisz 2 m przed lustrem. Jak daleko od ciebie jest twój obraz? Jeśli podejdziesz 0,5 m, o ile zbliży się obraz do ciebie?

<details>
<summary>Odpowiedź</summary>

4 m. Obraz zbliży się o 1 m, bo przesuwa się razem z tobą względem lustra.
</details>

3. Ile obrazów powstaje między dwoma lustrami ustawionymi pod kątem $60^\circ$?

<details>
<summary>Odpowiedź</summary>

$360^\circ/60^\circ - 1 = 5$ (zasada kalejdoskopu).
</details>

4. Lustro obrócono o $10^\circ$. O jaki kąt obrócił się promień odbity?

<details>
<summary>Odpowiedź</summary>

O $20^\circ$. Wykorzystuje się to w lusterkowych galwanometrach i do pomiaru małych obrotów.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź prawo odbicia z zasady Fermata: promień z punktu $A = (0, a)$ do $B = (d, b)$ przez lustro $y = 0$ wybiera najkrótszą drogę.

<details>
<summary>Odpowiedź</summary>

$s(x) = \sqrt{x^2 + a^2} + \sqrt{(d - x)^2 + b^2}$; $s'(x) = 0$ daje $\dfrac{x}{\sqrt{x^2 + a^2}} = \dfrac{d - x}{\sqrt{(d - x)^2 + b^2}}$, czyli $\sin\theta_{\text{pad}} = \sin\theta_{\text{odb}}$.
</details>

2. Pokaż wektorowo, że odbicie od trzech wzajemnie prostopadłych luster zmienia wektor kierunku $\vec d$ na $-\vec d$.

<details>
<summary>Odpowiedź</summary>

Odbicie od lustra prostopadłego do osi $x$ zmienia znak składowej $d_x$, i analogicznie dla $y$ i $z$. Po trzech odbiciach wszystkie składowe zmieniają znak, niezależnie od kolejności.
</details>

3. Retroreflektor na Księżycu zwraca impuls laserowy po ok. 2,56 s. Oblicz odległość. Z jaką dokładnością trzeba mierzyć czas, żeby znać odległość z dokładnością do 1 cm?

<details>
<summary>Odpowiedź</summary>

$d = ct/2 \approx 384\,000\ \mathrm{km}$. $\Delta t = 2\cdot0{,}01/c \approx 67\ \mathrm{ps}$.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 9.1 — bieg promienia odbitego i załamanego w krążku szklanym (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1 — §1.1 (rozchodzenie się światła) i §1.2 (prawo odbicia).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §33.5; wyd. 1: t. 4, §34.7.
- Symulacja PhET *Załamanie światła*.
