# 02.06 — Ruch po okręgu: jednostajny i niejednostajny

> **Moduł:** [02 — Kinematyka](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 4: [§4.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/4-4-ruch-po-okregu) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/4-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §4.5 (s. 95)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§4.7, s. 71](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=83), [§11.5, s. 268](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=280) — PDF z serwera AGH

← [Rzut poziomy i ukośny](05-rzuty.md) · [spis modułu](README.md) · [Ruch względny i transformacja Galileusza](07-ruch-wzgledny.md) →

## Po co to jest

Koła, wirówki, satelity, elektrony w modelu Bohra, ładunki w cyklotronie — ruch po okręgu jest wszędzie. Najważniejszy wniosek tego tematu jest nieintuicyjny: ciało poruszające się ze stałą szybkością po okręgu **przyspiesza**, bo zmienia się kierunek jego prędkości. Z tego przyspieszenia dośrodkowego wynikają siła dośrodkowa (03.04), prędkości orbitalne (07) i promień toru ładunku w polu magnetycznym (14).

## Teoria w pigułce

**Wielkości kątowe.** Położenie na okręgu o promieniu $R$ opisuje kąt $\varphi$ (w radianach). Długość łuku $s = R\varphi$.

- **Prędkość kątowa** $\omega = \dfrac{d\varphi}{dt}$ [rad/s].
- **Okres** $T$ — czas jednego obiegu, **częstotliwość** $f = 1/T$ [Hz]; $\omega = 2\pi f = 2\pi/T$.
- **Prędkość liniowa** (styczna do okręgu): $v = \omega R$.

**Ruch jednostajny po okręgu** — stała szybkość $v$, ale wektor prędkości stale obraca się. Przyspieszenie jest skierowane do środka okręgu (**dośrodkowe**):

$$a_d = \frac{v^2}{R} = \omega^2R.$$

**Skąd ten wzór (bez rachunku).** W krótkim czasie $\Delta t$ wektor prędkości obraca się o kąt $\Delta\varphi = \omega\Delta t$. Zmiana prędkości ma długość $\Delta v \approx v\Delta\varphi$ i jest skierowana do środka, więc $a = \Delta v/\Delta t = v\omega = v^2/R$.

**Ruch niejednostajny po okręgu** — szybkość się zmienia. Wtedy przyspieszenie ma dwie składowe:
- **styczną** $a_t = \dfrac{dv}{dt} = \varepsilon R$, gdzie $\varepsilon = \dfrac{d\omega}{dt}$ to przyspieszenie kątowe,
- **dośrodkową** $a_d = v^2/R$.

Całkowite przyspieszenie: $a = \sqrt{a_t^2 + a_d^2}$.

**Ruch po okręgu a drgania.** Rzut punktu poruszającego się jednostajnie po okręgu na średnicę wykonuje ruch harmoniczny $x = R\cos\omega t$ — to połączenie wróci w module 09.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\omega = 2\pi/T = 2\pi f$ | prędkość kątowa | ruch jednostajny po okręgu |
| $v = \omega R = 2\pi R/T$ | prędkość liniowa | $\omega$ w rad/s |
| $a_d = v^2/R = \omega^2R$ | przyspieszenie dośrodkowe | zawsze (także w ruchu niejednostajnym) |
| $a_t = dv/dt = \varepsilon R$ | przyspieszenie styczne | ruch niejednostajny |
| $a = \sqrt{a_t^2 + a_d^2}$ | przyspieszenie całkowite | składowe prostopadłe |
| $1\ \mathrm{obr/min} = \dfrac{2\pi}{60}\ \mathrm{rad/s}$ | przelicznik | — |

## Przykład rozwiązany

**Zadanie.** Oblicz prędkość i przyspieszenie dośrodkowe punktu na równiku wynikające z obrotu Ziemi ($R = 6371\ \mathrm{km}$, doba gwiazdowa $T = 86\,164\ \mathrm{s}$).

$$v = \frac{2\pi R}{T} = \frac{2\pi\cdot6{,}371\cdot10^6}{86\,164} \approx 465\ \mathrm{m/s}, \qquad a_d = \frac{v^2}{R} \approx 0{,}034\ \mathrm{m/s^2}.$$

To ok. 0,35% przyspieszenia ziemskiego — dlatego na równiku ważymy nieco mniej niż na biegunie.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Samochód rusza z miejsca na torze o promieniu $R = 50\ \mathrm{m}$ i zwiększa szybkość ze stałym przyspieszeniem stycznym $a_t = 2\ \mathrm{m/s^2}$. Po jakim czasie całkowite przyspieszenie osiągnie $5\ \mathrm{m/s^2}$ (granica przyczepności opon)? Jaka będzie wtedy prędkość?

$v = a_tt$, $a_d = \dfrac{(a_tt)^2}{R}$. Warunek: $a_t^2 + a_d^2 = 25$, czyli

$$a_d = \sqrt{25 - 4} \approx 4{,}58\ \mathrm{m/s^2} \Rightarrow (2t)^2 = 4{,}58\cdot50 \Rightarrow t \approx 7{,}57\ \mathrm{s},\ v \approx 15{,}1\ \mathrm{m/s}.$$

**Wyprowadzenie ogólne.** Prędkość piszemy jako $\vec{v} = v\,\hat{\tau}$, gdzie $\hat{\tau}$ to wersor styczny. Różniczkując iloczyn:

$$\vec{a} = \frac{dv}{dt}\hat{\tau} + v\frac{d\hat{\tau}}{dt} = a_t\hat{\tau} + \frac{v^2}{R}\hat{n},$$

bo wersor styczny obraca się z prędkością kątową $\omega = v/R$, a jego pochodna wskazuje do środka ($\hat{n}$).

## Typowe pułapki

- **„Stała prędkość, więc brak przyspieszenia”.** Stała jest szybkość, a nie wektor prędkości.
- **Stopnie zamiast radianów.** Wzór $v = \omega R$ działa tylko z $\omega$ w rad/s.
- **Obroty na minutę.** Przed liczeniem zamień obr/min na rad/s (mnóż przez $2\pi/60$).
- **Średnica zamiast promienia.** Wzory zawierają promień.
- **Siła odśrodkowa jako przyczyna ruchu.** W układzie inercjalnym nie ma siły odśrodkowej; jest wypadkowa siła dośrodkowa (więcej w 03.06).

## Doświadczenie / symulacja

**Pomiar z telefonem.** Połóż telefon na obracającym się krześle biurowym albo talerzu gramofonu, w znanej odległości $R$ od osi. W phyphox uruchom eksperyment *Centripetal Acceleration*: aplikacja mierzy jednocześnie $\omega$ (żyroskop) i przyspieszenie. Narysuj $a$ od $\omega^2$ i wyznacz $R$ z nachylenia prostej; porównaj z odległością zmierzoną linijką.

**Python:** przyspieszenie w ruchu niejednostajnym z przykładu.

```python
import numpy as np
import matplotlib.pyplot as plt

R, a_t = 50.0, 2.0
t = np.linspace(0, 10, 501)
v = a_t * t
a_d = v**2 / R
a = np.hypot(a_t, a_d)

i = np.argmax(a >= 5.0)
print(f"a = 5 m/s² po t = {t[i]:.2f} s przy v = {v[i]:.1f} m/s")

plt.plot(t, a_d, label="dośrodkowe v²/R")
plt.plot(t, np.full_like(t, a_t), label="styczne")
plt.plot(t, a, "k", label="całkowite")
plt.axhline(5, ls="--", color="gray")
plt.xlabel("t [s]"); plt.ylabel("a [m/s²]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Samochód jedzie z prędkością 72 km/h, koła mają średnicę 60 cm. Oblicz prędkość kątową koła, częstotliwość obrotów i liczbę obrotów na minutę.

<details>
<summary>Odpowiedź</summary>

$\omega = 20/0{,}3 \approx 66{,}7\ \mathrm{rad/s}$, $f \approx 10{,}6\ \mathrm{Hz}$, ok. 637 obr/min.
</details>

2. Wirówka laboratoryjna obraca się z prędkością 3000 obr/min. Oblicz przyspieszenie dośrodkowe próbki w odległości 10 cm od osi i porównaj je z $g$.

<details>
<summary>Odpowiedź</summary>

$\omega \approx 314\ \mathrm{rad/s}$, $a \approx 9870\ \mathrm{m/s^2} \approx 1000g$.
</details>

3. Księżyc obiega Ziemię po orbicie o promieniu $3{,}84\cdot10^8\ \mathrm{m}$ w czasie 27,3 doby. Oblicz jego prędkość i przyspieszenie dośrodkowe.

<details>
<summary>Odpowiedź</summary>

$v \approx 1{,}02\ \mathrm{km/s}$, $a \approx 2{,}7\cdot10^{-3}\ \mathrm{m/s^2}$. (Newton porównał tę wartość z $g/60^2$ — moduł 07.)
</details>

4. Ile razy większa jest prędkość kątowa wskazówki sekundowej od minutowej? Oblicz prędkość kątową wskazówki minutowej.

<details>
<summary>Odpowiedź</summary>

60 razy; $\omega = 2\pi/3600 \approx 1{,}75\cdot10^{-3}\ \mathrm{rad/s}$.
</details>

5. Jak zmieni się przyspieszenie dośrodkowe, gdy przy tym samym promieniu prędkość wzrośnie dwukrotnie? A gdy przy tej samej prędkości kątowej promień wzrośnie dwukrotnie?

<details>
<summary>Odpowiedź</summary>

Wzrośnie 4 razy; wzrośnie 2 razy.
</details>

### B. Poziom akademicki

1. Punkt porusza się po okręgu o promieniu $0{,}5\ \mathrm{m}$, a kąt zmienia się jak $\varphi(t) = 2t^2$ (rad, s). Oblicz prędkość, przyspieszenie styczne, dośrodkowe i całkowite w chwili $t = 1\ \mathrm{s}$.

<details>
<summary>Odpowiedź</summary>

$\omega = 4t = 4\ \mathrm{rad/s}$, $\varepsilon = 4\ \mathrm{rad/s^2}$; $v = 2\ \mathrm{m/s}$, $a_t = 2\ \mathrm{m/s^2}$, $a_d = 8\ \mathrm{m/s^2}$, $a \approx 8{,}25\ \mathrm{m/s^2}$.
</details>

2. Koło zamachowe zwalnia od 1200 obr/min do zatrzymania w ciągu 40 s ze stałym opóźnieniem kątowym. Ile obrotów wykona?

<details>
<summary>Odpowiedź</summary>

$\omega_0 = 125{,}7\ \mathrm{rad/s}$, $\varphi = \tfrac12\omega_0t = 2513\ \mathrm{rad} = 400$ obrotów.
</details>

3. Dla $\vec{r}(t) = R(\cos\varphi(t),\ \sin\varphi(t))$ z dowolną funkcją $\varphi(t)$ oblicz $\vec{a}$ i pokaż, że składowa styczna to $R\ddot{\varphi}$, a normalna $R\dot{\varphi}^2$.

<details>
<summary>Odpowiedź</summary>

$\vec{v} = R\dot{\varphi}(-\sin\varphi,\ \cos\varphi)$; $\vec{a} = R\ddot{\varphi}(-\sin\varphi,\ \cos\varphi) - R\dot{\varphi}^2(\cos\varphi,\ \sin\varphi)$ — pierwszy wyraz styczny, drugi skierowany do środka.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2026, zad. 2.1 — konstrukcja środka i promienia okręgu toru wahadła ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 4 — §4.4: ruch po okręgu jednostajny i niejednostajny.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §4.5; wyd. 1: t. 1, §4.7 i §11.5 (związek wielkości liniowych z kątowymi).
