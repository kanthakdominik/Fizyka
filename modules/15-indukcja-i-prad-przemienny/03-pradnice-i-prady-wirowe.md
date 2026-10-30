# 15.03 — Prądy wirowe, prądnice i SEM wsteczna

> **Moduł:** [15 — Indukcja elektromagnetyczna i prąd przemienny](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 13: [§13.5–13.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/13-5-prady-wirowe) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/13-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §30.2 (s. 338)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §31.5, s. 256 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [SEM ruchu i indukowane pole elektryczne](02-sem-ruchu-i-pole-indukowane.md) · [spis modułu](README.md) · [Indukcyjność własna i wzajemna, energia pola magnetycznego](04-indukcyjnosc.md) →

## Po co to jest

Prawie cała energia elektryczna na świecie pochodzi z prądnic: wirników obracanych parą, wodą lub wiatrem w polu magnetycznym. Silnik elektryczny to prądnica pracująca odwrotnie i podczas pracy sam też indukuje napięcie (SEM wsteczną). To wyjaśnia, dlaczego silnik pobiera ogromny prąd przy rozruchu i dlaczego zablokowany może się spalić. Prądy wirowe grzeją garnek na kuchence indukcyjnej, hamują pociągi i kolejki górskie, wykrywają metal na lotnisku. W rdzeniach transformatorów są szkodliwe i trzeba je ograniczać.

## Teoria w pigułce

**Prądnica prądu przemiennego.** Ramka o $N$ zwojach i polu $A$ obraca się z prędkością kątową $\omega$ w polu $B$. Kąt między normalną a polem rośnie jak $\theta = \omega t$, więc

$$\Phi = NBA\cos\omega t, \qquad \varepsilon = -\frac{d\Phi}{dt} = NBA\omega\sin\omega t = \varepsilon_0\sin\omega t.$$

Powstaje napięcie sinusoidalne o amplitudzie $\varepsilon_0 = NBA\omega$ i częstotliwości obrotów. W Europie sieć ma 50 Hz. W elektrowniach ramka zwykle stoi (stojan), a obraca się elektromagnes (wirnik). Trzy uzwojenia przesunięte o 120° dają prąd trójfazowy (09.06).

Prądnica prądu stałego ma komutator, który co pół obrotu odwraca połączenia. Napięcie jest wtedy jednokierunkowe, ale tętniące.

**Siła elektromotoryczna wsteczna w silniku.** Wirnik silnika obraca się w polu, więc działa też jak prądnica. Indukuje SEM $\varepsilon_w$ przeciwną do napięcia zasilania. Prąd wynosi

$$I = \frac{U - \varepsilon_w}{R}.$$

Przy rozruchu $\varepsilon_w = 0$ i prąd jest największy. Gdy silnik się rozpędza, $\varepsilon_w$ rośnie i prąd maleje. Zablokowany silnik przegrzewa się, bo stale płynie przez niego prąd rozruchowy.

**Prądy wirowe.** W masywnym przewodniku poruszającym się w polu albo umieszczonym w zmiennym polu indukują się zamknięte prądy krążące wewnątrz metalu:
- grzeją go: **kuchenka indukcyjna** (pole zmienia się z częstotliwością 20–100 kHz, w zwykłych płytach garnek musi być ferromagnetyczny, bo aluminium czy miedź mają za mały opór i nie wchodzą w histerezę), piece indukcyjne do topienia metali;
- hamują ruch: **hamulce wiroprądowe** w pociągach, kolejkach górskich i trenażerach rowerowych (bez tarcia i zużycia);
- zmieniają indukcyjność cewki w pobliżu metalu: **wykrywacze metali**;
- w rdzeniach transformatorów i silników są stratą. Ogranicza się je, składając rdzeń z cienkich, izolowanych blach (laminowanie) albo stosując ferryty.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\varepsilon = NBA\omega\sin\omega t$ | SEM prądnicy | stała prędkość, pole jednorodne |
| $\varepsilon_0 = NBA\omega$ | amplituda SEM | — |
| $I = (U - \varepsilon_w)/R$ | prąd silnika | silnik prądu stałego |
| $P_{\text{wir}} \propto B^2f^2d^2$ | straty na prądy wirowe | $d$ — grubość blachy |

## Przykład rozwiązany

**Zadanie 1.** Ramka prądnicy ma 100 zwojów o wymiarach 10 cm × 10 cm i obraca się 50 razy na sekundę w polu 0,5 T. Oblicz amplitudę i wartość skuteczną SEM (15.06).

$\varepsilon_0 = 100\cdot0{,}5\cdot0{,}01\cdot2\pi\cdot50 \approx 157\ \mathrm V$, wartość skuteczna $\varepsilon_0/\sqrt2 \approx 111\ \mathrm V$.

**Zadanie 2.** Silnik 12 V ma opór uzwojenia 1 Ω. Podczas pracy SEM wsteczna wynosi 10 V. Oblicz prąd w pracy i przy rozruchu oraz moc mechaniczną.

W pracy $I = (12 - 10)/1 = 2\ \mathrm A$. Przy rozruchu $I = 12\ \mathrm A$, sześć razy więcej.

Moc mechaniczna to $\varepsilon_wI = 20\ \mathrm W$, a straty w uzwojeniu $I^2R = 4\ \mathrm W$. Sprawność wynosi $20/24 \approx 83\%$.

## Typowe pułapki

- **Prądnica wytwarza energię.** Zamienia pracę mechaniczną na elektryczną. Im większy pobór prądu, tym trudniej obracać wirnik (reguła Lenza).
- **SEM największa, gdy strumień największy.** SEM jest największa, gdy strumień przechodzi przez zero, czyli gdy płaszczyzna ramki jest równoległa do pola. Wtedy strumień zmienia się najszybciej.
- **Prądy wirowe w izolatorach.** Płyną tylko w przewodnikach. Dlatego na kuchence indukcyjnej szklany garnek się nie grzeje.
- **Silnik zawsze pobiera prąd nominalny.** Prąd zależy od obciążenia, bo obciążony silnik zwalnia i SEM wsteczna maleje.

## Doświadczenie / symulacja

**Silnik jako prądnica.** Mały silnik prądu stałego (np. z zabawki) podłącz do diody LED albo do miernika i zakręć wałem palcami lub wiertarką. Zmierz napięcie w funkcji prędkości obrotowej (obrotomierz aplikacją z mikrofonem lub stroboskopem). Sprawdź $\varepsilon \propto \omega$.

**Prąd rozruchowy.** Miernikiem w szereg z małym silnikiem zmierz prąd, gdy silnik pracuje swobodnie i gdy palcem przytrzymasz wał (krótko!). Oblicz SEM wsteczną.

**Symulacja PhET:** *Prądnica* (*Generator*) — część *Laboratorium elektromagnetycznego Faradaya*.

**Python:** SEM prądnicy jedno- i trójfazowej.

```python
import numpy as np
import matplotlib.pyplot as plt

N, B, A, f = 100, 0.5, 0.01, 50
w = 2*np.pi*f
t = np.linspace(0, 2/f, 1000)
eps0 = N*B*A*w
print(f"amplituda SEM = {eps0:.1f} V, wartość skuteczna = {eps0/np.sqrt(2):.1f} V")
faz = [eps0*np.sin(w*t - k*2*np.pi/3) for k in range(3)]
print(f"maksymalna suma trzech faz: {np.abs(sum(faz)).max():.2e} V (zrównoważony układ trójfazowy)")
U, R, eps_w = 12.0, 1.0, 10.0
print(f"silnik: prąd w pracy {(U - eps_w)/R:.0f} A, przy rozruchu {U/R:.0f} A, sprawność {eps_w/U*100:.0f} %")
for k, e in enumerate(faz):
    plt.plot(t*1e3, e, label=f"faza {k + 1}")
plt.xlabel("t [ms]"); plt.ylabel("ε [V]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Jak zmieni się amplituda SEM prądnicy, gdy prędkość obrotów wzrośnie dwukrotnie? A częstotliwość?

<details>
<summary>Odpowiedź</summary>

Obie wzrosną dwukrotnie.
</details>

2. Dlaczego na kuchence indukcyjnej nie nagrzewa się płyta ceramiczna, a nagrzewa się stalowy garnek?

<details>
<summary>Odpowiedź</summary>

Zmienne pole indukuje prądy wirowe tylko w przewodniku (garnku). Ceramika jest izolatorem. Grzeje się dopiero od gorącego garnka.
</details>

3. Dlaczego rdzenie transformatorów składa się z cienkich, izolowanych blach?

<details>
<summary>Odpowiedź</summary>

Izolacja przerywa drogi prądów wirowych. W cienkich blachach indukowane prądy są małe, a straty maleją z kwadratem grubości blachy.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Prądnica (amplituda $\varepsilon_0$, opór wewnętrzny pomijalny) zasila opornik $R$. Oblicz średnią moc i średni moment siły potrzebny do obracania wirnika.

<details>
<summary>Odpowiedź</summary>

$\bar P = \overline{\varepsilon^2}/R = \varepsilon_0^2/(2R)$, $\bar\tau = \bar P/\omega = \dfrac{(NBA)^2\omega}{2R}$.
</details>

2. Silnik zasilany napięciem $U$ ma opór $R$, a SEM wsteczna to $\varepsilon_w$. Pokaż, że moc mechaniczna jest największa, gdy $\varepsilon_w = U/2$. Jaka jest wtedy sprawność?

<details>
<summary>Odpowiedź</summary>

$P_{\text{mech}} = \varepsilon_w(U - \varepsilon_w)/R$, maksimum dla $\varepsilon_w = U/2$. Sprawność to $\varepsilon_w/U = 50\%$ (analogia z dopasowaniem, 13.04).
</details>

3. Dysk przewodzący o promieniu $R$ i grubości $d$ znajduje się w jednorodnym polu $B = B_0\sin\omega t$ prostopadłym do dysku. Oszacuj moc traconą na prądy wirowe, rozważając pierścienie o promieniu $r$ i szerokości $dr$ (opór właściwy $\rho$).

<details>
<summary>Odpowiedź</summary>

$\varepsilon(r) = \pi r^2\dot B$, opór pierścienia $\rho\dfrac{2\pi r}{d\,dr}$, moc $\dfrac{\varepsilon^2}{R_r} = \dfrac{\pi r^3d\dot B^2}{2\rho}dr$. Całka daje $P = \dfrac{\pi R^4d}{8\rho}\dot B^2$, a średnio $\dfrac{\pi R^4dB_0^2\omega^2}{16\rho}$. Straty rosną jak $\omega^2$ i jak $R^4$, stąd dzielenie rdzeni na cienkie elementy.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 13 — §13.5 (prądy wirowe), §13.6 (prądnice elektryczne i SEM wsteczna), §13.7 (zastosowania indukcji).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §30.2; wyd. 1: t. 3, §31.5.
- Symulacja PhET *Laboratorium elektromagnetyczne Faradaya*.
