# 18.05 — Dyfrakcja na szczelinie i zdolność rozdzielcza

> **Moduł:** [18 — Optyka falowa](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 4: [§4.1–4.3 i §4.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/4-1-dyfrakcja-na-pojedynczej-szczelinie) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/4-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §36.1–36.4 (s. 141)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§37.1–37.6, s. 111](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=126) — PDF z serwera AGH

← [Interferencja w cienkich warstwach, interferometr Michelsona](04-cienkie-warstwy-i-michelson.md) · [spis modułu](README.md) · [Polaryzacja światła: prawo Malusa i kąt Brewstera](06-polaryzacja.md) →

## Po co to jest

Światło przechodzące przez wąską szczelinę lub mały otwór rozchodzi się na boki. Ta dyfrakcja wyznacza nieprzekraczalną granicę ostrości każdego przyrządu optycznego: oka, aparatu, mikroskopu, teleskopu, a także drobność ścieżek nagrywanych laserem na płytach i rozdzielczość litografii w produkcji procesorów. Dlatego teleskopy buduje się coraz większe, płyty Blu-ray używają lasera niebieskiego, a fabryki chipów skrajnego nadfioletu.

## Teoria w pigułce

**Pojedyncza szczelina** o szerokości $a$. Dzielimy szczelinę na pół. Fale z odpowiadających sobie punktów obu połówek znoszą się, gdy różnica ich dróg wynosi $\lambda/2$. Stąd minima:

$$a\sin\theta = m\lambda, \qquad m = \pm1, \pm2, \dots$$

($m = 0$ to jasne maksimum środkowe.) Maksimum środkowe jest **dwa razy szersze** od pozostałych i zawiera większość energii. Na ekranie w odległości $L$ ma szerokość $2L\lambda/a$. Węższa szczelina daje szerszy obraz.

**Natężenie** (z sumowania wskazów fal cząstkowych):

$$I = I_0\left(\frac{\sin\beta}{\beta}\right)^2, \qquad \beta = \frac{\pi a\sin\theta}{\lambda}.$$

Boczne maksima są słabe: pierwsze ma ok. 4,7% natężenia środkowego.

**Otwór kołowy** o średnicy $D$ daje jasną plamkę (krążek Airy'ego) otoczoną pierścieniami. Pierwsze minimum leży pod kątem

$$\sin\theta \approx 1{,}22\frac\lambda D.$$

**Kryterium Rayleigha.** Dwa punkty (gwiazdy, szczegóły preparatu) są rozróżnialne, gdy maksimum obrazu jednego wypada w pierwszym minimum drugiego:

$$\theta_{\min} = 1{,}22\frac\lambda D.$$

To graniczna rozdzielczość kątowa przyrządu o aperturze $D$. Większa średnica i krótsza fala dają ostrzejszy obraz.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $a\sin\theta = m\lambda$, $m \ne 0$ | minima pojedynczej szczeliny | dyfrakcja Fraunhofera (ekran daleko) |
| $I = I_0(\sin\beta/\beta)^2$, $\beta = \pi a\sin\theta/\lambda$ | natężenie | j.w. |
| szerokość maksimum środkowego $2L\lambda/a$ | — | małe kąty |
| $\theta_{\min} = 1{,}22\lambda/D$ | kryterium Rayleigha | otwór kołowy |

## Przykład rozwiązany

**Zadanie 1.** Laser 633 nm oświetla szczelinę o szerokości 0,1 mm. Jak szerokie jest maksimum środkowe na ekranie odległym o 2 m?

$2L\lambda/a = 2\cdot2\cdot633\cdot10^{-9}/10^{-4} \approx 25\ \mathrm{mm}$.

**Zadanie 2.** Źrenica oka w dzień ma ok. 3 mm. Jaka jest graniczna rozdzielczość kątowa oka dla światła 550 nm? Z jakiej odległości można rozróżnić dwa reflektory samochodu odległe o 1,5 m?

$\theta_{\min} = 1{,}22\cdot550\cdot10^{-9}/3\cdot10^{-3} \approx 2{,}2\cdot10^{-4}\ \mathrm{rad} \approx 0{,}8'$. Odległość: $1{,}5/2{,}2\cdot10^{-4} \approx 6{,}7\ \mathrm{km}$ (w praktyce mniej, bo ogranicza też siatkówka i atmosfera).

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie natężenia dla szczeliny.** Każdy pasek szczeliny o szerokości $dx$ w położeniu $x$ wysyła falę o amplitudzie $\propto dx$ i fazie $kx\sin\theta$. Suma (całka) daje:

$$E(\theta) \propto \int_{-a/2}^{a/2}e^{ikx\sin\theta}dx = a\frac{\sin\beta}{\beta}, \qquad \beta = \frac{ka\sin\theta}{2} = \frac{\pi a\sin\theta}{\lambda}.$$

Natężenie $I \propto \lvert E\rvert^2 = I_0(\sin\beta/\beta)^2$. Zera wypadają dla $\beta = m\pi$, czyli $a\sin\theta = m\lambda$. To transformata Fouriera kształtu szczeliny. Ogólnie obraz dyfrakcyjny w dużej odległości jest transformatą Fouriera przesłony.

**Teleskop Hubble'a** ($D = 2{,}4\ \mathrm m$): $\theta_{\min} = 1{,}22\cdot550\cdot10^{-9}/2{,}4 \approx 2{,}8\cdot10^{-7}\ \mathrm{rad}$. Na Księżycu daje to szczegóły ok. 110 m, więc ani Hubble, ani żaden teleskop z Ziemi nie zobaczy lądowników Apollo.

## Typowe pułapki

- **Wzór na minima pojedynczej szczeliny jak na maksima siatki.** Ten sam zapis $a\sin\theta = m\lambda$ oznacza tu **minima**, a w siatce i przy dwóch szczelinach maksima.
- **Węższa szczelina daje węższy obraz.** Daje szerszy: $\theta \propto \lambda/a$.
- **Większe powiększenie pokona dyfrakcję.** Rozdzielczość zależy od średnicy obiektywu i długości fali, a nie od powiększenia.
- **Czynnik 1,22 dla szczeliny.** Dotyczy otworu kołowego. Dla szczeliny pierwsze minimum jest przy $\lambda/a$.

## Doświadczenie / symulacja

**Dyfrakcja na włosie.** Włos rozciągnięty w świetle lasera daje taki sam obraz jak szczelina o tej samej szerokości (zasada Babineta). Zmierz odległość między minimami na ścianie 2–3 m dalej i oblicz grubość włosa. Typowo wychodzi 50–100 μm.

**Dyfrakcja w szczelinie palców.** Patrz na lampę przez wąską szczelinę między dwoma palcami. Widać ciemne prążki równoległe do szczeliny.

**Symulacja PhET:** *Interferencja fal* — zakładka *Dyfrakcja* (*Diffraction*), szczelina i otwór kołowy.

**Python:** obraz dyfrakcyjny szczeliny z całki numerycznej porównany ze wzorem $(\sin\beta/\beta)^2$.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

lam, a, L = 633e-9, 0.1e-3, 2.0
k = 2*np.pi/lam
y = np.linspace(-0.04, 0.04, 1500)
s = np.sin(np.arctan(y/L))
x = np.linspace(-a/2, a/2, 801)                          # punkty szczeliny (fale cząstkowe Huygensa)
E = trapezoid(np.exp(1j*k*np.outer(s, x)), x, axis=1)
I_num = np.abs(E)**2/np.abs(E).max()**2
beta = np.pi*a*s/lam
I_wz = np.sinc(beta/np.pi)**2
print(f"maks. różnica całka − wzór: {np.abs(I_num - I_wz).max():.1e}")
print(f"szerokość maksimum środkowego: {2*L*lam/a*1e3:.1f} mm")
print(f"oko 3 mm: θ_min = {1.22*550e-9/3e-3:.2e} rad; Hubble: {1.22*550e-9/2.4:.2e} rad")
plt.plot(y*1e3, I_num, label="całka Huygensa"); plt.plot(y*1e3, I_wz, "--", label="(sin β / β)²")
plt.xlabel("y [mm]"); plt.ylabel("I / I0"); plt.legend(); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Szczelina o szerokości 0,05 mm jest oświetlona światłem 500 nm. Pod jakim kątem leży pierwsze minimum?

<details>
<summary>Odpowiedź</summary>

$\sin\theta = 0{,}01$, $\theta \approx 0{,}57^\circ$.
</details>

2. Dlaczego radioteleskopy muszą być ogromne (dziesiątki do setek metrów), a i tak mają gorszą rozdzielczość niż małe teleskopy optyczne?

<details>
<summary>Odpowiedź</summary>

Rozdzielczość $\propto\lambda/D$, a fale radiowe są miliony razy dłuższe od światła. Dlatego łączy się radioteleskopy z całej Ziemi w interferometr (VLBI), co daje efektywne $D$ rzędu średnicy Ziemi.
</details>

3. Dlaczego płyta Blu-ray (laser 405 nm) mieści więcej danych niż DVD (650 nm)?

<details>
<summary>Odpowiedź</summary>

Plamka lasera ma rozmiar $\propto\lambda$, więc krótsza fala pozwala zapisać mniejsze i gęściej upakowane ślady. Pomaga też większa apertura numeryczna soczewki.
</details>

### B. Poziom akademicki

1. Teleskop amatorski ma obiektyw 10 cm. Oblicz jego rozdzielczość w sekundach łuku. Czy rozdzieli gwiazdę podwójną o separacji 2″?

<details>
<summary>Odpowiedź</summary>

$\theta = 1{,}22\cdot550\cdot10^{-9}/0{,}1 \approx 6{,}7\cdot10^{-6}\ \mathrm{rad} \approx 1{,}4''$. Tak, rozdzieli (jeśli pozwoli atmosfera, która zwykle rozmywa obraz do ok. 1–2″).
</details>

2. Pokaż, że pierwsze boczne maksimum szczeliny leży w przybliżeniu przy $\beta \approx 1{,}43\pi$ (rozwiązanie $\tan\beta = \beta$) i ma natężenie ok. 4,7% maksimum środkowego.

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{d\beta}\left(\dfrac{\sin\beta}{\beta}\right) = 0 \Rightarrow \tan\beta = \beta$, pierwszy niezerowy pierwiastek $\beta \approx 4{,}493 = 1{,}43\pi$. $(\sin\beta/\beta)^2 \approx 0{,}047$.
</details>

3. Dwie szczeliny o szerokości $a$ i odległości $d = 4a$. Które prążki interferencyjne nie będą widoczne?

<details>
<summary>Odpowiedź</summary>

Maksima interferencyjne $d\sin\theta = m\lambda$ pokrywają się z minimami dyfrakcyjnymi $a\sin\theta = m'\lambda$ dla $m = 4m'$. Brakuje prążków $m = \pm4, \pm8, \dots$
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 4 — §4.1 (dyfrakcja na pojedynczej szczelinie), §4.2 (natężenie), §4.3 (dyfrakcja na dwóch szczelinach), §4.5 (otwory kołowe i rozdzielczość).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §36.1–36.4; wyd. 1: t. 4, §37.1–37.6.
- Symulacja PhET *Interferencja fal*.
