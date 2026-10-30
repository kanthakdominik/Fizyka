# 08.01 — Ciśnienie, prawo Pascala, ciśnienie hydrostatyczne

> **Moduł:** [08 — Mechanika płynów](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 14: [§14.1–14.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-1-plyny-gestosc-i-cisnienie) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §14.1–14.4 (s. 78)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§15.1–15.6, s. 61](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=77) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Prawo Archimedesa i pływanie ciał](02-prawo-archimedesa.md) →

## Po co to jest

Ciśnienie wyjaśnia, dlaczego nurek musi wynurzać się powoli, jak działa hamulec samochodu i podnośnik hydrauliczny, dlaczego zapora jest grubsza u dołu i jak barometr przewiduje pogodę. Ciśnienie gazu wróci w teorii kinetycznej (11.04), a pojęcie ciśnienia jako energii na jednostkę objętości — w równaniu Bernoulliego (08.03).

## Teoria w pigułce

**Płyn** to ciecz lub gaz — substancja, która nie ma własnego kształtu i płynie pod działaniem sił stycznych. W spoczynku płyn działa na ścianki tylko siłami prostopadłymi.

**Ciśnienie** to siła nacisku na jednostkę powierzchni:

$$p = \frac{F_\perp}{S}, \qquad [p] = \mathrm{Pa} = \mathrm{N/m^2}.$$

Inne jednostki: $1\ \mathrm{bar} = 10^5\ \mathrm{Pa}$, $1\ \mathrm{atm} = 101\,325\ \mathrm{Pa} = 760\ \mathrm{mmHg}$, $1\ \mathrm{hPa} = 100\ \mathrm{Pa}$ (prognozy pogody).

**Ciśnienie hydrostatyczne.** W cieczy o gęstości $\rho$ ciśnienie rośnie z głębokością, bo każda warstwa dźwiga ciężar warstw nad nią:

$$p = p_0 + \rho gh,$$

gdzie $p_0$ — ciśnienie na powierzchni (zwykle atmosferyczne). Ciśnienie zależy tylko od głębokości, a nie od kształtu naczynia (**paradoks hydrostatyczny**). Stąd **naczynia połączone**: ciecz jednorodna ustawia się w nich na tej samej wysokości.

**Prawo Pascala.** Ciśnienie wywierane z zewnątrz na ciecz w zamkniętym naczyniu przenosi się bez zmian na każdy punkt cieczy. Na tym działa **prasa hydrauliczna**:

$$\frac{F_2}{F_1} = \frac{S_2}{S_1}.$$

Siła rośnie, ale praca nie: mały tłok przesuwa się odpowiednio więcej ($F_1s_1 = F_2s_2$).

**Ciśnienie atmosferyczne** to ciężar słupa powietrza nad jednostką powierzchni. Barometr rtęciowy (Torricelli, 1643): słup rtęci o wysokości 760 mm równoważy ciśnienie atmosfery. Słup wody musiałby mieć ponad 10 m — dlatego pompa ssąca nie podniesie wody wyżej.

**Ciśnienie bezwzględne a nadciśnienie.** Manometr (np. do opon) pokazuje zwykle nadciśnienie $p - p_{\text{atm}}$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $p = F/S$ | ciśnienie | siła prostopadła do powierzchni |
| $p = p_0 + \rho gh$ | ciśnienie hydrostatyczne | ciecz nieściśliwa, $g$ stałe |
| $F_2/F_1 = S_2/S_1$ | prasa hydrauliczna | prawo Pascala, ciecz w spoczynku |
| $\rho_1h_1 = \rho_2h_2$ | dwie ciecze w rurce U | ciecze się nie mieszają, poziomy od granicy cieczy |
| $p = p_0e^{-h/H}$, $\ H = RT/(Mg)$ | wzór barometryczny | atmosfera izotermiczna |

## Przykład rozwiązany

**Zadanie 1.** Jakie ciśnienie działa na nurka na głębokości 20 m w wodzie słodkiej?

$p = 101\,325 + 1000\cdot9{,}81\cdot20 \approx 2{,}98\cdot10^5\ \mathrm{Pa} \approx 2{,}9\ \mathrm{atm}$. Co 10 m głębokości ciśnienie rośnie o ok. 1 atm.

**Zadanie 2.** Podnośnik hydrauliczny ma tłoki o polach $2\ \mathrm{cm^2}$ i $200\ \mathrm{cm^2}$. Jaką siłą trzeba działać na mały tłok, żeby podnieść samochód o masie 1500 kg? O ile trzeba przesunąć mały tłok, żeby podnieść samochód o 10 cm?

$F_1 = mg\cdot\dfrac{S_1}{S_2} = 14\,715\cdot\dfrac{2}{200} \approx 147\ \mathrm{N}$. Objętość cieczy się nie zmienia: $s_1 = s_2S_2/S_1 = 10\ \mathrm{m}$ (w praktyce wiele ruchów pompki).

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1 — siła na zaporę.** Pionowa zapora ma szerokość 100 m, a woda sięga do wysokości 50 m. Oblicz wypadkową siłę parcia wody (bez ciśnienia atmosferycznego, które działa z obu stron).

Pasek zapory na głębokości $y$ o wysokości $dy$: $dF = \rho gy\cdot w\,dy$.

$$F = \int_0^H\rho gyw\,dy = \tfrac12\rho gwH^2 = \tfrac12\cdot1000\cdot9{,}81\cdot100\cdot2500 \approx 1{,}2\cdot10^9\ \mathrm{N}.$$

Siła rośnie z kwadratem głębokości, a przyłożona jest na głębokości $\tfrac23H$ — dlatego zapory są najgrubsze u podstawy.

**Zadanie 2 — atmosfera.** Ciśnienie w powietrzu też spełnia $dp = -\rho g\,dh$, ale gęstość gazu zależy od ciśnienia: $\rho = pM/(RT)$. Dla stałej temperatury:

$$\frac{dp}{p} = -\frac{Mg}{RT}dh \Rightarrow p = p_0e^{-h/H}, \qquad H = \frac{RT}{Mg} \approx \frac{8{,}314\cdot288}{0{,}029\cdot9{,}81} \approx 8{,}4\ \mathrm{km}.$$

Na wysokości 5 km ciśnienie to ok. 55% ciśnienia na poziomie morza.

## Typowe pułapki

- **Ciśnienie zależy od ilości wody.** Zależy tylko od głębokości (paradoks hydrostatyczny).
- **Zapomniane ciśnienie atmosferyczne.** Pytanie o ciśnienie „całkowite” wymaga dodania $p_0$; o różnicę ciśnień — nie.
- **Prasa hydrauliczna daje darmową energię.** Daje większą siłę kosztem drogi.
- **Jednostki pola.** $1\ \mathrm{cm^2} = 10^{-4}\ \mathrm{m^2}$.
- **Głębokość w rurce U.** Wysokości liczymy od wspólnego poziomu granicy cieczy.

## Doświadczenie / symulacja

**Barometr w telefonie.** Większość smartfonów ma czujnik ciśnienia. W phyphox uruchom eksperyment *Pressure* i przejdź z telefonem kilka pięter po schodach (albo przejedź windą). Zmiana ciśnienia o ok. 12 Pa odpowiada 1 m wysokości. Wyznacz wysokość budynku i porównaj z pomiarem taśmą lub liczbą stopni.

**Symulacja PhET:** *Pod ciśnieniem* (*Under Pressure*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)) — ciśnienie w naczyniach o różnych kształtach i w różnych cieczach.

**Python:** ciśnienie w atmosferze — model izotermiczny i model z temperaturą malejącą z wysokością (atmosfera standardowa do 11 km).

```python
import numpy as np
import matplotlib.pyplot as plt

p0, T0, M, R, g, L = 101325, 288.15, 0.029, 8.314, 9.81, 0.0065
h = np.linspace(0, 11000, 200)
H = R*T0/(M*g)
p_iso = p0*np.exp(-h/H)
p_std = p0*(1 - L*h/T0)**(g*M/(R*L))            # temperatura maleje 6,5 K/km
for hh in (0, 1000, 5000, 8849):
    print(f"h = {hh:5d} m: izotermiczny {p0*np.exp(-hh/H)/100:6.0f} hPa, standardowy {p0*(1 - L*hh/T0)**(g*M/(R*L))/100:6.0f} hPa")
print(f"zmiana ciśnienia na 1 m przy ziemi: {p0*M*g/(R*T0):.1f} Pa")
plt.plot(p_iso/100, h/1000, label="izotermiczny"); plt.plot(p_std/100, h/1000, label="atmosfera standardowa")
plt.xlabel("p [hPa]"); plt.ylabel("h [km]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Jak wysoki musiałby być słup wody, żeby zrównoważyć ciśnienie atmosferyczne 1013 hPa?

<details>
<summary>Odpowiedź</summary>

$h = p/(\rho g) \approx 10{,}3\ \mathrm{m}$.
</details>

2. Kobieta o masie 60 kg stoi na jednym obcasie o polu $1\ \mathrm{cm^2}$. Jakie ciśnienie wywiera na podłogę? Porównaj ze słoniem (5 t na czterech stopach po $0{,}1\ \mathrm{m^2}$).

<details>
<summary>Odpowiedź</summary>

$5{,}9\ \mathrm{MPa}$; słoń: $5000\cdot9{,}81/0{,}4 \approx 0{,}12\ \mathrm{MPa}$ — obcas wywiera 50 razy większe ciśnienie.
</details>

3. W rurce w kształcie litery U jest woda. Do jednego ramienia wlano olej ($\rho = 800\ \mathrm{kg/m^3}$) tworzący słup o wysokości 10 cm. O ile poziom wody w drugim ramieniu jest wyżej niż granica olej–woda?

<details>
<summary>Odpowiedź</summary>

$\rho_wh_w = \rho_oh_o \Rightarrow h_w = 8\ \mathrm{cm}$.
</details>

4. Prasa hydrauliczna ma tłoki o średnicach 2 cm i 20 cm. Jaką siłą działa duży tłok, gdy na mały działamy siłą 100 N?

<details>
<summary>Odpowiedź</summary>

Stosunek pól $= 100$: $F = 10\ \mathrm{kN}$.
</details>

5. Dlaczego zatyka uszy przy szybkiej jeździe windą w wysokim budynku albo w samolocie?

<details>
<summary>Odpowiedź</summary>

Ciśnienie zewnętrzne zmienia się (ok. 12 Pa na metr), a w uchu środkowym zostaje dawne ciśnienie, dopóki nie wyrówna się przez trąbkę Eustachiusza; różnica ciśnień wygina błonę bębenkową.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Oblicz moment siły parcia wody na zaporę z przykładu względem jej podstawy i pokaż, że siła wypadkowa działa na wysokości $H/3$ nad dnem.

<details>
<summary>Odpowiedź</summary>

$\tau = \displaystyle\int_0^H\rho gw y(H - y)\,dy = \rho gw\frac{H^3}{6}$; ramię $\tau/F = H/3$ nad dnem.
</details>

2. Na jakiej wysokości (model izotermiczny, $H = 8{,}4\ \mathrm{km}$) ciśnienie spada do połowy? Porównaj z wysokością Mount Everestu.

<details>
<summary>Odpowiedź</summary>

$h = H\ln2 \approx 5{,}8\ \mathrm{km}$; na Evereście (8,85 km) ciśnienie jest ok. 3 razy mniejsze niż na poziomie morza.
</details>

3. Naczynie z wodą przyspiesza pionowo w górę z przyspieszeniem $a$. Jak zmienia się ciśnienie na głębokości $h$?

<details>
<summary>Odpowiedź</summary>

$p = p_0 + \rho(g + a)h$ — jak w polu o „efektywnym” $g + a$ (03.06).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 14 — §14.1 (płyny, gęstość, ciśnienie), §14.2 (pomiar ciśnienia), §14.3 (prawo Pascala i układy hydrauliczne).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §14.1–14.4; wyd. 1: t. 2, §15.1–15.6.
- Symulacja PhET *Pod ciśnieniem*.
