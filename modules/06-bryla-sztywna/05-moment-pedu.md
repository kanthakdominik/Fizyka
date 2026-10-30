# 06.05 — Moment pędu i zasada jego zachowania

> **Moduł:** [06 — Bryła sztywna, statyka i sprężystość](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 11: [§11.2–11.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/11-2-moment-pedu) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/11-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §11.4–11.8 (s. 384)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§12.5–12.10, s. 303](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=315) — PDF z serwera AGH

← [Toczenie bez poślizgu](04-toczenie.md) · [spis modułu](README.md) · [Precesja żyroskopu](06-precesja.md) →

## Po co to jest

Moment pędu to obrotowy odpowiednik pędu — i tak jak pęd, jest zachowany, gdy nic go nie zmienia z zewnątrz. Dzięki temu łyżwiarka przyspiesza piruet, kot ląduje na łapach, gwiazda neutronowa obraca się setki razy na sekundę, a planety zakreślają równe pola w równych czasach (II prawo Keplera, 07.04). W fizyce atomowej moment pędu jest skwantowany i wyznacza strukturę atomu (21).

## Teoria w pigułce

**Moment pędu punktu** względem punktu O:

$$\vec{L} = \vec{r}\times\vec{p} = m\,\vec{r}\times\vec{v}, \qquad L = mvd,$$

gdzie $d$ to odległość O od prostej, wzdłuż której porusza się ciało. Nawet ciało lecące po prostej ma moment pędu względem punktu, który nie leży na tej prostej. Jednostka: $\mathrm{kg\cdot m^2/s}$.

**Moment pędu bryły** obracającej się wokół osi symetrii:

$$\vec{L} = I\vec{\omega}.$$

**Zasada dynamiki dla momentu pędu:**

$$\sum\vec{\tau}_{\text{zewn}} = \frac{d\vec{L}}{dt}.$$

Dla stałego $I$ daje to $\tau = I\varepsilon$ (06.03), ale jest ogólniejsze — obowiązuje także, gdy moment bezwładności się zmienia.

**Zasada zachowania momentu pędu.** Jeśli wypadkowy moment sił zewnętrznych jest zerowy:

$$\vec{L} = \text{const}, \qquad I_1\omega_1 = I_2\omega_2.$$

Przykłady:
- **piruet**: łyżwiarka przyciąga ręce, $I$ maleje, $\omega$ rośnie; jej energia kinetyczna rośnie (praca mięśni ramion);
- **skoczek do wody** zwija się w kłębek, żeby obrócić się szybciej;
- **zapadanie się gwiazdy**: zmniejszenie promienia tysiące razy przyspiesza obrót miliony razy;
- **siła centralna** (grawitacja, siła Coulomba) nie daje momentu względem centrum — stąd stały moment pędu planet i II prawo Keplera.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec{L} = \vec{r}\times m\vec{v}$, $\ L = mvd$ | moment pędu punktu | względem wybranego punktu |
| $L = I\omega$ | moment pędu bryły | obrót wokół osi symetrii |
| $\sum\vec{\tau} = d\vec{L}/dt$ | zasada dynamiki | momenty względem tego samego punktu |
| $I_1\omega_1 = I_2\omega_2$ | zachowanie momentu pędu | $\sum\tau_{\text{zewn}} = 0$ |
| $E_k = \dfrac{L^2}{2I}$ | energia przy danym $L$ | — |

## Przykład rozwiązany

**Zadanie 1 — piruet.** Łyżwiarka z rozłożonymi rękami ma moment bezwładności $3{,}5\ \mathrm{kg\cdot m^2}$ i wykonuje 1 obrót na sekundę. Przyciąga ręce, zmniejszając moment bezwładności do $1{,}0\ \mathrm{kg\cdot m^2}$. Z jaką prędkością się obraca? Ile razy wzrosła jej energia kinetyczna?

$\omega_2 = \omega_1\cdot3{,}5/1{,}0 = 3{,}5\ \mathrm{obr/s}$. Energia $E = L^2/(2I)$ przy stałym $L$ rośnie jak $1/I$ — **3,5 razy**. Różnica pochodzi z pracy, którą wykonują mięśnie, przyciągając ręce wbrew „sile odśrodkowej”.

**Zadanie 2 — karuzela.** Karuzela ($I = 200\ \mathrm{kg\cdot m^2}$) obraca się z prędkością 1 rad/s. Dziecko o masie 40 kg wskakuje na jej brzeg ($R = 2\ \mathrm{m}$), biegnąc wzdłuż promienia. Jak zmieni się prędkość obrotu?

$I' = 200 + 40\cdot4 = 360\ \mathrm{kg\cdot m^2}$, $\omega' = 200/360 \approx 0{,}56\ \mathrm{rad/s}$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Pocisk o masie 10 g lecący z prędkością 200 m/s uderza prostopadle w koniec pręta (masa 1 kg, długość 1 m) zamocowanego obrotowo w środku i grzęźnie w nim. Oblicz prędkość kątową pręta.

Moment pędu względem osi (siły w osi nie dają momentu): przed — $L = mv\frac{L_p}{2} = 0{,}01\cdot200\cdot0{,}5 = 1\ \mathrm{kg\cdot m^2/s}$; po — $(I_p + m(L_p/2)^2)\omega$.

$I = \tfrac1{12}\cdot1\cdot1 + 0{,}01\cdot0{,}25 \approx 0{,}0858\ \mathrm{kg\cdot m^2}$, $\omega = 1/0{,}0858 \approx 11{,}7\ \mathrm{rad/s}$.

Pęd **nie** jest tu zachowany — oś pręta działa siłą zewnętrzną. Moment pędu względem osi — tak.

**Wyprowadzenie $\tau = dL/dt$ dla punktu.**

$$\frac{d\vec{L}}{dt} = \frac{d\vec{r}}{dt}\times m\vec{v} + \vec{r}\times m\frac{d\vec{v}}{dt} = \underbrace{\vec{v}\times m\vec{v}}_{0} + \vec{r}\times\vec{F} = \vec{\tau}.$$

## Typowe pułapki

- **Moment pędu tylko w ruchu obrotowym.** Ciało w ruchu prostoliniowym też ma moment pędu względem punktu poza torem.
- **Zachowanie energii przy piruecie.** Energia kinetyczna się zmienia; zachowany jest moment pędu.
- **Zachowanie pędu przy osi.** Gdy bryła jest zamocowana na osi, oś działa siłą zewnętrzną — pęd nie jest zachowany, moment pędu względem tej osi tak.
- **Różne punkty odniesienia.** Momenty sił i moment pędu liczymy względem tego samego punktu.

## Doświadczenie / symulacja

**Krzesło obrotowe.** Usiądź na obrotowym krześle z ciężkimi przedmiotami (butelki z wodą) w wyciągniętych rękach i poproś kogoś o rozkręcenie. Przyciągnij ręce — obrót przyspieszy. Telefon w kieszeni z phyphox (*Gyroscope*) zmierzy $\omega$ przed i po; oszacuj stosunek momentów bezwładności.

**Python:** zapadanie się gwiazdy — prędkość obrotu w zależności od promienia (zachowanie $L$ dla jednorodnej kuli).

```python
import numpy as np
import matplotlib.pyplot as plt

R0, T0 = 7.0e8, 25*86400               # promień i okres obrotu gwiazdy typu Słońca
R = np.logspace(np.log10(R0), 4, 200)  # od 7·10⁵ km do 10 km
T = T0*(R/R0)**2                       # I ∝ R², L = const ⇒ T ∝ R²
print(f"gwiazda neutronowa (R = 10 km): T = {T[-1]*1000:.2f} ms")
plt.loglog(R/1000, T); plt.gca().invert_xaxis()
plt.xlabel("promień [km]"); plt.ylabel("okres obrotu [s]"); plt.grid(True, which="both"); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Ile razy wzrośnie prędkość obrotu łyżwiarki, która zmniejszy moment bezwładności z $4\ \mathrm{kg\cdot m^2}$ do $1{,}6\ \mathrm{kg\cdot m^2}$?

<details>
<summary>Odpowiedź</summary>

$2{,}5$ razy.
</details>

2. Dlaczego skoczek do wody wykonujący salto zwija się w kłębek?

<details>
<summary>Odpowiedź</summary>

W locie moment pędu jest zachowany (ciężar nie daje momentu względem środka masy). Zwinięcie zmniejsza moment bezwładności, więc zwiększa prędkość obrotu.
</details>

3. Oblicz moment pędu Ziemi w ruchu obrotowym. Przyjmij $I = 0{,}33MR^2$ (Ziemia nie jest jednorodna), $M = 5{,}97\cdot10^{24}\ \mathrm{kg}$, $R = 6{,}37\cdot10^6\ \mathrm{m}$.

<details>
<summary>Odpowiedź</summary>

$L = I\omega \approx 0{,}33\cdot5{,}97\cdot10^{24}\cdot(6{,}37\cdot10^6)^2\cdot7{,}29\cdot10^{-5} \approx 5{,}8\cdot10^{33}\ \mathrm{kg\cdot m^2/s}$.
</details>

4. Samochód o masie 1000 kg jedzie z prędkością 20 m/s po prostej drodze. Oblicz jego moment pędu względem drzewa stojącego 10 m od drogi.

<details>
<summary>Odpowiedź</summary>

$L = mvd = 2\cdot10^5\ \mathrm{kg\cdot m^2/s}$ — stały, choć samochód jedzie po prostej.
</details>

### B. Poziom akademicki

1. Gwiazda o promieniu $7\cdot10^5\ \mathrm{km}$ obraca się raz na 25 dni. Zapada się do gwiazdy neutronowej o promieniu 10 km, zachowując masę i moment pędu (model kuli jednorodnej). Jaki będzie jej okres obrotu?

<details>
<summary>Odpowiedź</summary>

$T_2 = T_1(R_2/R_1)^2 \approx 2{,}16\cdot10^6\ \mathrm{s}/4{,}9\cdot10^9 \approx 0{,}44\ \mathrm{ms}$. (Obserwowane pulsary mają okresy od ok. 1 ms do kilku sekund — część momentu pędu jest tracona.)
</details>

2. Pokaż, że dla planety w polu grawitacyjnym Słońca prędkość polowa $dA/dt$ (pole zakreślane przez promień w jednostce czasu) jest stała i równa $L/(2m)$.

<details>
<summary>Odpowiedź</summary>

$dA = \tfrac12\lvert\vec{r}\times d\vec{r}\rvert$, więc $\dfrac{dA}{dt} = \dfrac12\lvert\vec{r}\times\vec{v}\rvert = \dfrac{L}{2m}$. Siła centralna nie daje momentu, więc $L$ jest stały — to II prawo Keplera.
</details>

3. Dwa koła na wspólnej osi: pierwsze ($I_1 = 2\ \mathrm{kg\cdot m^2}$) obraca się z $\omega_1 = 10\ \mathrm{rad/s}$, drugie ($I_2 = 3\ \mathrm{kg\cdot m^2}$) spoczywa. Sprzęgamy je. Oblicz wspólną prędkość i utraconą energię.

<details>
<summary>Odpowiedź</summary>

$\omega = 20/5 = 4\ \mathrm{rad/s}$; $E$ z 100 J spada do 40 J — strata 60 J (obrotowy odpowiednik zderzenia doskonale niesprężystego).
</details>

4. Kulka na nici krąży po poziomym gładkim stole wokół otworu, przez który przechodzi nić. Wciągając nić, zmniejszamy promień z 0,5 m do 0,25 m. Prędkość kulki wynosiła 2 m/s. Jaka jest teraz? Jaką pracę wykonano?

<details>
<summary>Odpowiedź</summary>

$mvr = \text{const} \Rightarrow v = 4\ \mathrm{m/s}$; praca $= \tfrac12m(16 - 4) = 6m$ (J, dla $m$ w kg).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 11 — §11.2 (moment pędu) i §11.3 (zasada zachowania momentu pędu).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §11.4–11.8; wyd. 1: t. 1, §12.5–12.10.
