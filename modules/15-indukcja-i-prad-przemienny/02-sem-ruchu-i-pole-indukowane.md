# 15.02 — SEM ruchu i indukowane pole elektryczne

> **Moduł:** [15 — Indukcja elektromagnetyczna i prąd przemienny](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 13: [§13.3–13.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/13-3-sila-elektromotoryczna-wywolana-ruchem) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/13-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §30.2–30.3 (s. 338)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §31.5–31.6, s. 256 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Prawo Faradaya i reguła Lenza](01-prawo-faradaya-i-lenza.md) · [spis modułu](README.md) · [Prądy wirowe, prądnice i SEM wsteczna](03-pradnice-i-prady-wirowe.md) →

## Po co to jest

Przewodnik poruszający się w polu magnetycznym staje się źródłem napięcia. To najprostszy model prądnicy, a także podstawa hamulców magnetycznych w pociągach i kolejkach górskich, przepływomierzy elektromagnetycznych (krew, woda w wodociągach) i napięcia między końcami skrzydeł samolotu. Drugie oblicze indukcji jest głębsze: zmienne pole magnetyczne wytwarza **pole elektryczne o zamkniętych liniach**, nawet w pustej przestrzeni. Ta obserwacja prowadzi wprost do fal elektromagnetycznych (16).

## Teoria w pigułce

**SEM ruchu.** Pręt o długości $L$ porusza się z prędkością $v$ prostopadle do pola $B$. Na elektrony w pręcie działa siła Lorentza $evB$ wzdłuż pręta, która rozdziela ładunki. Powstaje SEM:

$$\varepsilon = BLv.$$

To samo daje prawo Faradaya: pręt ślizgający się po szynach powiększa pole obwodu w tempie $Lv$, więc $d\Phi/dt = BLv$.

**Pręt na szynach z opornikiem $R$:**
- prąd $I = BLv/R$;
- na pręt działa siła hamująca $F = BIL = \dfrac{B^2L^2v}{R}$ (reguła Lenza);
- żeby utrzymać stałą prędkość, trzeba ciągnąć z mocą $Fv = \dfrac{(BLv)^2}{R} = I^2R$, czyli dokładnie tyle, ile wydziela się w oporniku. Praca mechaniczna zamienia się w energię elektryczną.

**Indukowane pole elektryczne.** Gdy zmienia się pole magnetyczne, a przewodnik stoi, siła Lorentza nie działa (bo $v = 0$). Mimo to powstaje SEM. Faraday i Maxwell wyjaśnili to tak: zmienne pole magnetyczne wytwarza pole elektryczne

$$\oint\vec E\cdot d\vec l = -\frac{d\Phi_B}{dt}.$$

To pole ma **zamknięte linie** (wiry), w odróżnieniu od pola elektrostatycznego. Nie jest zachowawcze, więc nie da się dla niego określić potencjału. Istnieje także w próżni, bez żadnego przewodnika. W betatronie przyspiesza ono elektrony krążące w komorze.

W obszarze o promieniu $R$ z jednorodnym, zmiennym polem (np. wnętrze solenoidu):

$$E = \frac r2\frac{dB}{dt}\ (r < R), \qquad E = \frac{R^2}{2r}\frac{dB}{dt}\ (r > R).$$

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\varepsilon = BLv$ | SEM ruchu | $\vec L$, $\vec v$, $\vec B$ wzajemnie prostopadłe |
| $F = B^2L^2v/R$ | siła hamująca pręt | obwód o oporze $R$ |
| $\oint\vec E\cdot d\vec l = -d\Phi_B/dt$ | prawo Faradaya (postać całkowa) | zawsze |
| $E = \dfrac r2\dfrac{dB}{dt}$ | pole indukowane w solenoidzie | $r < R$, symetria osiowa |

## Przykład rozwiązany

**Zadanie 1.** Pręt o długości 0,5 m ślizga się z prędkością 2 m/s po szynach połączonych opornikiem 2 Ω, w polu 0,4 T. Oblicz SEM, prąd, siłę hamującą i moc.

$\varepsilon = 0{,}4\cdot0{,}5\cdot2 = 0{,}4\ \mathrm V$, $I = 0{,}2\ \mathrm A$, $F = BIL = 0{,}04\ \mathrm N$, $P = Fv = 0{,}08\ \mathrm W = I^2R$.

**Zadanie 2.** Samolot o rozpiętości skrzydeł 60 m leci poziomo z prędkością 250 m/s. Pionowa składowa pola Ziemi wynosi 45 μT. Jakie napięcie powstaje między końcami skrzydeł?

$\varepsilon = 45\cdot10^{-6}\cdot60\cdot250 \approx 0{,}68\ \mathrm V$. Nie da się go wykorzystać, bo przewód podłączony do woltomierza na pokładzie porusza się razem z samolotem i ma w sobie tę samą SEM.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Pręt z zadania 1 (masa 0,1 kg) puszczono z prędkością 2 m/s i nikt go nie ciągnie. Wyznacz $v(t)$ i drogę do zatrzymania.

$m\dfrac{dv}{dt} = -\dfrac{B^2L^2}{R}v \Rightarrow v = v_0e^{-t/\tau}$, $\tau = \dfrac{mR}{B^2L^2} = \dfrac{0{,}1\cdot2}{0{,}04} = 5\ \mathrm s$.

Droga: $s = \displaystyle\int_0^\infty v\,dt = v_0\tau = 10\ \mathrm m$. Cała energia kinetyczna $\tfrac12mv_0^2 = 0{,}2\ \mathrm J$ wydziela się w oporniku.

**Pole indukowane.** Wewnątrz solenoidu pole rośnie w tempie 0,1 T/s. Na okręgu o promieniu $r = 5\ \mathrm{cm}$ (wewnątrz): $E\cdot2\pi r = \pi r^2\dfrac{dB}{dt} \Rightarrow E = \dfrac r2\dfrac{dB}{dt} = 2{,}5\ \mathrm{mV/m}$.

## Typowe pułapki

- **SEM ruchu przy ruchu wzdłuż pręta lub wzdłuż pola.** SEM powstaje, gdy pręt „przecina” linie pola. Przy ruchu wzdłuż linii pola SEM wynosi zero.
- **Indukowane pole elektryczne ma potencjał.** Nie ma. Całka po zamkniętej drodze nie jest zerowa, więc napięcie między dwoma punktami zależy od drogi, po której mierzymy.
- **Pręt sam się rozpędza.** Siła indukowana zawsze hamuje ruch (reguła Lenza).
- **Moc mechaniczna ≠ elektryczna.** Przy stałej prędkości są równe.

## Doświadczenie / symulacja

**Wahadło z hamulcem magnetycznym.** Płytka aluminiowa zawieszona jako wahadło przechodzi przez szczelinę między dwoma magnesami neodymowymi. Drgania gasną w kilku wahnięciach. Z płytką ponacinaną jak grzebień tłumienie jest dużo słabsze, bo prądy wirowe nie mogą płynąć.

**Symulacja PhET:** *Laboratorium elektromagnetyczne Faradaya* — zakładka z prądnicą.

**Python:** pręt na szynach — hamowanie indukcyjne (numerycznie i analitycznie) i bilans energii.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, trapezoid

B, L, R, m, v0 = 0.4, 0.5, 2.0, 0.1, 2.0
k = B**2*L**2/R
sol = solve_ivp(lambda t, s: [s[1], -k/m*s[1]], (0, 30), [0, v0], max_step=0.01, dense_output=True)
t = np.linspace(0, 30, 600)
x, v = sol.sol(t)
tau = m/k
print(f"τ = {tau:.1f} s, droga: numerycznie {x[-1]:.3f} m, v0·τ = {v0*tau:.3f} m")
Q = trapezoid((B*L*v)**2/R, t)
print(f"ciepło w oporniku: {Q:.4f} J, energia kinetyczna: {0.5*m*v0**2:.4f} J")
plt.plot(t, v); plt.plot(t, v0*np.exp(-t/tau), "--")
plt.xlabel("t [s]"); plt.ylabel("v [m/s]"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Samochód o rozstawie kół 1,6 m jedzie z prędkością 30 m/s. Pionowa składowa pola Ziemi wynosi 45 μT. Oblicz napięcie między końcami osi.

<details>
<summary>Odpowiedź</summary>

$\varepsilon = BLv \approx 2{,}2\ \mathrm{mV}$.
</details>

2. Pręt na szynach (z zadania 1) ciągnięto z prędkością 4 m/s zamiast 2 m/s. Jak zmieniły się SEM, prąd, siła i moc?

<details>
<summary>Odpowiedź</summary>

SEM, prąd i siła wzrosły 2 razy, a moc 4 razy.
</details>

3. Ramka spada pionowo w poziome pole magnetyczne, które zajmuje obszar pod pewną linią. Kiedy płynie w niej prąd indukowany: gdy wchodzi w pole, gdy jest cała w polu, gdy z niego wychodzi?

<details>
<summary>Odpowiedź</summary>

Gdy wchodzi i gdy wychodzi (w przeciwnych kierunkach). Gdy jest cała w jednorodnym polu, strumień się nie zmienia i prądu nie ma.
</details>

### B. Poziom akademicki

1. Ramka z prętem z zadania 1 spada pionowo pod wpływem ciężaru $mg$ (szyny pionowe, pole poziome). Wyznacz prędkość graniczną.

<details>
<summary>Odpowiedź</summary>

$mg = B^2L^2v_{\text{gr}}/R \Rightarrow v_{\text{gr}} = \dfrac{mgR}{B^2L^2} \approx 49\ \mathrm{m/s}$ dla danych z zadania.
</details>

2. Pręt o długości $L$ obraca się z prędkością kątową $\omega$ wokół jednego końca w płaszczyźnie prostopadłej do pola $B$. Oblicz SEM między końcami (dysk Faradaya).

<details>
<summary>Odpowiedź</summary>

$d\varepsilon = B\,v(r)\,dr = B\omega r\,dr$, więc $\varepsilon = \tfrac12B\omega L^2$.
</details>

3. Pole w długim solenoidzie o promieniu $R$ maleje w tempie $dB/dt$. Wyznacz $E(r)$ na zewnątrz solenoidu i narysuj wykres $E(r)$ dla wszystkich $r$.

<details>
<summary>Odpowiedź</summary>

Na zewnątrz strumień jest równy $\pi R^2B$: $E\cdot2\pi r = \pi R^2\lvert dB/dt\rvert \Rightarrow E = \dfrac{R^2}{2r}\left\lvert\dfrac{dB}{dt}\right\rvert$. Wykres rośnie liniowo do $r = R$, potem maleje jak $1/r$. Pole elektryczne istnieje poza solenoidem, choć tam $B \approx 0$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 13 — §13.3 (SEM ruchu) i §13.4 (indukowane pole elektryczne).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §30.2–30.3; wyd. 1: t. 3, §31.5–31.6.
- Symulacja PhET *Laboratorium elektromagnetyczne Faradaya*.
