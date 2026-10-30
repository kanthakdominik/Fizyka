# 14.02 — Siła elektrodynamiczna i moment sił na ramkę z prądem

> **Moduł:** [14 — Pole magnetyczne](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 11: [§11.4–11.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/11-4-sila-magnetyczna-dzialajaca-na-przewodnik-z-pradem) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/11-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §28.6–28.8 (s. 272)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §29.7–29.9, s. 202 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Pole magnetyczne, siła Lorentza i ruch ładunku](01-sila-lorentza.md) · [spis modułu](README.md) · [Efekt Halla, spektrometr masowy, cyklotron](03-hall-cyklotron-spektrometr.md) →

## Po co to jest

Przewodnik z prądem w polu magnetycznym jest popychany. To zasada działania każdego silnika elektrycznego, od wibracji w telefonie po napęd tramwaju i samochodu elektrycznego, a także głośnika, mierników wskazówkowych i dysku twardego (głowica). Ramka z prądem zachowuje się jak igła kompasu, czyli jak magnes. Pojęcie momentu magnetycznego łączy więc prądy z magnesami trwałymi i z magnetyzmem atomów (14.07).

## Teoria w pigułce

**Siła elektrodynamiczna.** Prąd to poruszające się ładunki, więc na przewodnik w polu działa suma sił Lorentza. Na prosty odcinek o długości $L$ z prądem $I$:

$$\vec F = I\vec L\times\vec B, \qquad F = BIL\sin\alpha.$$

Wektor $\vec L$ ma kierunek prądu. Zwrot wyznacza reguła lewej dłoni (dla prądu) albo równoważna reguła iloczynu wektorowego. Dla przewodnika dowolnego kształtu: $d\vec F = I\,d\vec l\times\vec B$, $\vec F = \int I\,d\vec l\times\vec B$.

**Ramka z prądem w polu jednorodnym.** Siły na przeciwległe boki mają równe wartości i przeciwne zwroty. Wypadkowa wynosi zero, ale tworzą **parę sił**, która obraca ramkę:

$$\tau = NIAB\sin\theta, \qquad \vec\tau = \vec\mu\times\vec B,$$

gdzie $\theta$ to kąt między normalną do ramki a polem. **Moment magnetyczny** ramki to

$$\vec\mu = NI\vec A,$$

skierowany prostopadle do ramki zgodnie z regułą prawej dłoni (palce wzdłuż prądu, kciuk wskazuje $\vec\mu$). Energia potencjalna wynosi $U = -\vec\mu\cdot\vec B$, jak dla dipola elektrycznego (12.02). Ramka obraca się tak, by $\vec\mu$ ustawił się zgodnie z $\vec B$, tak jak igła kompasu.

**Silnik prądu stałego.** Moment siły obraca ramkę (wirnik). Komutator co pół obrotu odwraca kierunek prądu, więc moment ma stale ten sam zwrot. W silnikach bezszczotkowych prąd przełącza elektronika.

**Miernik wskazówkowy** (magnetoelektryczny): moment siły od prądu równoważy moment sprężynki, $NIAB = \kappa\varphi$. Wychylenie jest proporcjonalne do prądu (13.05).

**Głośnik:** cewka w szczelinie magnesu, połączona z membraną, jest popychana w przód i w tył w rytm zmian prądu.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec F = I\vec L\times\vec B$, $F = BIL\sin\alpha$ | siła na prosty przewodnik | pole jednorodne na długości $L$ |
| $d\vec F = I\,d\vec l\times\vec B$ | siła na element | dowolny kształt i pole |
| $\vec\mu = NI\vec A$ | moment magnetyczny ramki | ramka płaska, $N$ zwojów |
| $\vec\tau = \vec\mu\times\vec B$, $\tau = NIAB\sin\theta$ | moment siły na ramkę | pole jednorodne |
| $U = -\vec\mu\cdot\vec B$ | energia ramki w polu | — |

## Przykład rozwiązany

**Zadanie 1.** Przewód o długości 1 m z prądem 10 A leży prostopadle do pola 0,5 T. Oblicz siłę.

$F = 0{,}5\cdot10\cdot1 = 5\ \mathrm N$.

**Zadanie 2.** Kwadratowa cewka o boku 5 cm ma 100 zwojów, płynie przez nią prąd 0,2 A. Jest w polu 0,1 T. Oblicz moment magnetyczny i największy moment siły. Ile pracy trzeba wykonać, żeby obrócić cewkę z położenia równowagi o $180^\circ$?

$\mu = NIA = 100\cdot0{,}2\cdot0{,}0025 = 0{,}05\ \mathrm{A\cdot m^2}$. $\tau_{\max} = \mu B = 5\cdot10^{-3}\ \mathrm{N\cdot m}$.

$W = \Delta U = \mu B - (-\mu B) = 2\mu B = 0{,}01\ \mathrm J$.

## Typowe pułapki

- **Przewód równoległy do pola.** Siła wynosi zero dla $\alpha = 0$.
- **Wypadkowa siła na ramkę w polu jednorodnym.** Wynosi zero. Działa tylko moment siły. W polu niejednorodnym pojawia się też siła wypadkowa (magnes przyciąga ramkę lub ją odpycha).
- **Kąt $\theta$ w $\tau = NIAB\sin\theta$.** To kąt między **normalną** do ramki a polem, a nie między płaszczyzną ramki a polem. Moment jest największy, gdy płaszczyzna ramki jest **równoległa** do pola.
- **Mylenie reguł dłoni.** Wybierz jedną regułę i sprawdzaj ją iloczynem wektorowym.
- **Moment zależy od kształtu ramki.** Zależy tylko od pola powierzchni $A$, nie od kształtu.

## Doświadczenie / symulacja

**Najprostszy silnik (homopolarny).** Bateria AA, magnes neodymowy przyłożony do bieguna ujemnego i kawałek drutu miedzianego wygiętego tak, by dotykał bieguna dodatniego i boku magnesu. Drut zaczyna się kręcić. Wyjaśnij kierunek obrotu siłą $I\vec L\times\vec B$. Uwaga: drut i bateria szybko się nagrzewają.

**Huśtawka z prądem.** Drut zawieszony między dwoma podporami w szczelinie magnesu podkowiastego, zasilany z baterii przez opornik, wychyla się w jedną lub drugą stronę zależnie od kierunku prądu.

**Symulacja PhET:** *Laboratorium elektromagnetyczne Faradaya* (*Faraday's Electromagnetic Lab*) — elektromagnes i kompas ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** moment siły na ramkę w funkcji kąta i ruch obrotowy ramki (wahadło magnetyczne).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

N, I, a, B = 100, 0.2, 0.05, 0.1
mu = N*I*a**2
th = np.linspace(0, 2*np.pi, 300)
print(f"μ = {mu:.3f} A·m², τ_max = {mu*B*1e3:.1f} mN·m, praca obrotu o 180° = {2*mu*B*1e3:.1f} mJ")

Iw = 2e-5                                           # moment bezwładności ramki [kg·m²]
sol = solve_ivp(lambda t, s: [s[1], -mu*B*np.sin(s[0])/Iw], (0, 0.5), [0.3, 0], max_step=1e-4)
T_num = 2*sol.t[np.where(np.diff(np.sign(sol.y[1])) != 0)[0][1]]
print(f"okres drgań ramki: numerycznie {T_num*1e3:.1f} ms, 2π√(I/μB) = {2*np.pi*np.sqrt(Iw/(mu*B))*1e3:.1f} ms (amplituda 0,3 rad)")
plt.plot(np.degrees(th), mu*B*np.sin(th)*1e3)
plt.xlabel("kąt między μ a B [°]"); plt.ylabel("τ [mN·m]"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Przewód o długości 20 cm z prądem 5 A jest w polu 0,3 T pod kątem $30^\circ$ do linii pola. Oblicz siłę.

<details>
<summary>Odpowiedź</summary>

$F = BIL\sin30^\circ = 0{,}15\ \mathrm N$.
</details>

2. Pręt miedziany o masie 10 g i długości 20 cm leży na poziomych szynach w pionowym polu 0,2 T. Jaki prąd musi przez niego płynąć, żeby siła zrównała się z tarciem ($\mu = 0{,}2$)?

<details>
<summary>Odpowiedź</summary>

$BIL = \mu mg \Rightarrow I = 0{,}2\cdot0{,}01\cdot9{,}81/(0{,}2\cdot0{,}2) \approx 0{,}49\ \mathrm A$.
</details>

3. W jakim położeniu ramki z prądem moment siły jest największy, a w jakim równy zeru?

<details>
<summary>Odpowiedź</summary>

Największy, gdy płaszczyzna ramki jest równoległa do pola ($\vec\mu \perp \vec B$). Zero, gdy płaszczyzna jest prostopadła do pola ($\vec\mu \parallel \vec B$), w położeniu równowagi.
</details>

4. Do czego służy komutator w silniku prądu stałego?

<details>
<summary>Odpowiedź</summary>

Co pół obrotu odwraca kierunek prądu w ramce, żeby moment siły stale obracał ją w tę samą stronę.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Przewód w kształcie półokręgu o promieniu $R$ z prądem $I$ leży w płaszczyźnie prostopadłej do jednorodnego pola $B$. Oblicz całkowaniem siłę i porównaj z siłą na prosty odcinek łączący końce.

<details>
<summary>Odpowiedź</summary>

$dF = IB\,R\,d\theta$, składowe wzdłuż średnicy się znoszą, a prostopadła: $F = \displaystyle\int_0^\pi IBR\sin\theta\,d\theta = 2IBR$. To samo co dla odcinka $2R$. W polu jednorodnym liczą się tylko końce przewodu.
</details>

2. Pokaż, że na zamkniętą pętlę dowolnego kształtu w polu jednorodnym działa zerowa siła wypadkowa.

<details>
<summary>Odpowiedź</summary>

$\vec F = I\left(\oint d\vec l\right)\times\vec B = 0$, bo $\oint d\vec l = 0$ dla zamkniętej krzywej.
</details>

3. Ramka o momencie magnetycznym $\mu$ i momencie bezwładności $I$ wychylona o mały kąt z położenia równowagi drga harmonicznie. Wyznacz okres. Jak można tak zmierzyć pole $B$?

<details>
<summary>Odpowiedź</summary>

$I\ddot\theta = -\mu B\theta \Rightarrow T = 2\pi\sqrt{I/(\mu B)}$. Mierząc okres przy znanych $I$ i $\mu$, wyznacza się $B$. Tak Gauss mierzył pole Ziemi, używając drgającej igły magnetycznej.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 11 — §11.4 (siła magnetyczna działająca na przewodnik z prądem) i §11.5 (siła i moment siły działające na ramkę z prądem).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §28.6–28.8; wyd. 1: t. 3, §29.7–29.9.
- Symulacja PhET *Laboratorium elektromagnetyczne Faradaya*.
