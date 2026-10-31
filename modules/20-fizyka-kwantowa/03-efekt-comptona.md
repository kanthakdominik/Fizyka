# 20.03 — Efekt Comptona

> **Moduł:** [20 — Podstawy fizyki kwantowej](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6: [§6.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-3-efekt-comptona) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §38.3 (s. 8)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§39.4, s. 8](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=24) — PDF z serwera AGH

← [Efekt fotoelektryczny](02-efekt-fotoelektryczny.md) · [spis modułu](README.md) · [Fale materii de Broglie'a i dualizm korpuskularno-falowy](04-fale-materii.md) →

## Po co to jest

W 1923 r. Compton rozpraszał promieniowanie rentgenowskie na elektronach i stwierdził, że rozproszone ma dłuższą falę, tym dłuższą, im większy kąt. Klasycznie to niemożliwe. Zjawisko wyjaśnia zderzenie fotonu z elektronem jak dwóch kul bilardowych, z zachowaniem energii i pędu. To dowód, że foton niesie nie tylko energię, ale i pęd. Efekt Comptona decyduje o oddziaływaniu promieniowania rentgenowskiego i gamma z tkankami (radiologia, radioterapia, osłony) i jest wykorzystywany w detektorach i kamerach gamma.

## Teoria w pigułce

**Pęd fotonu.** Foton nie ma masy, więc z $E^2 = (pc)^2 + (mc^2)^2$ (19.05):

$$p = \frac Ec = \frac h\lambda.$$

**Zderzenie fotonu z elektronem.** Foton o długości fali $\lambda$ uderza w swobodny (lub słabo związany) spoczywający elektron i rozprasza się pod kątem $\theta$. Elektron odskakuje. Z zasad zachowania energii (relatywistycznej) i pędu (wektorowo) wynika **wzór Comptona**:

$$\Delta\lambda = \lambda' - \lambda = \frac{h}{m_ec}(1 - \cos\theta).$$

$\lambda_C = h/(m_ec) \approx 2{,}43\ \mathrm{pm}$ to **komptonowska długość fali** elektronu.
- Przesunięcie nie zależy od długości fali padającej, tylko od kąta.
- Największe jest dla rozproszenia wstecz ($\theta = 180^\circ$): $2\lambda_C \approx 4{,}85\ \mathrm{pm}$.
- Dla światła widzialnego (500 nm) przesunięcie jest znikomo małe w stosunku do $\lambda$. Dla promieniowania rentgenowskiego (dziesiątki pm) jest dobrze mierzalne.

W widmie rozproszonym obok linii przesuniętej występuje też linia nieprzesunięta. Pochodzi z rozproszeń na elektronach mocno związanych, gdzie pęd przejmuje cały atom o masie tysiące razy większej.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $p = h/\lambda = E/c$ | pęd fotonu | — |
| $\Delta\lambda = \lambda_C(1 - \cos\theta)$ | wzór Comptona | elektron swobodny, spoczywający |
| $\lambda_C = h/(m_ec) = 2{,}43\ \mathrm{pm}$ | komptonowska długość fali | — |
| $E_{k,e} = hc/\lambda - hc/\lambda'$ | energia odrzutu elektronu | — |

## Przykład rozwiązany

**Zadanie.** Promieniowanie rentgenowskie o długości fali 71 pm (linia Mo Kα) rozprasza się na graficie. Oblicz długość fali rozproszonej pod kątem $90^\circ$ i $180^\circ$ oraz energię odrzutu elektronu dla $90^\circ$.

$90^\circ$: $\lambda' = 71 + 2{,}43 = 73{,}4\ \mathrm{pm}$. $180^\circ$: $\lambda' = 75{,}9\ \mathrm{pm}$.

Energia fotonu: $E = 1240\ \mathrm{eV\cdot nm}/0{,}071\ \mathrm{nm} \approx 17{,}5\ \mathrm{keV}$. Po rozproszeniu pod $90^\circ$: $\approx 16{,}9\ \mathrm{keV}$. Elektron dostaje ok. 0,58 keV.

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie wzoru Comptona.** Oznaczmy pęd fotonu przed i po zderzeniu $\vec p$, $\vec p\,'$, a pęd elektronu po zderzeniu $\vec p_e$.

Pęd: $\vec p_e = \vec p - \vec p\,'$, więc $p_e^2 = p^2 + p'^2 - 2pp'\cos\theta$.

Energia: $pc + mc^2 = p'c + \sqrt{p_e^2c^2 + m^2c^4}$. Przenosząc i podnosząc do kwadratu:

$$(pc - p'c + mc^2)^2 = p_e^2c^2 + m^2c^4.$$

Rozwijając i wstawiając $p_e^2$: $-2pp'c^2 + 2(p - p')mc^3 = -2pp'c^2\cos\theta$, czyli

$$\frac{1}{p'} - \frac1p = \frac{1 - \cos\theta}{mc} \Rightarrow \lambda' - \lambda = \frac{h}{mc}(1 - \cos\theta).$$

## Typowe pułapki

- **Przesunięcie zależy od długości fali padającej.** $\Delta\lambda$ zależy tylko od kąta. Względna zmiana $\Delta\lambda/\lambda$ jest jednak duża tylko dla krótkich fal.
- **Foton po rozproszeniu ma większą energię.** Ma mniejszą (dłuższą falę), bo część energii przejął elektron.
- **Pęd fotonu $mv$.** Foton nie ma masy. Jego pęd to $h/\lambda$.
- **Efekt Comptona dla światła widzialnego.** Jest tak mały względem $\lambda$, że praktycznie niemierzalny.

## Doświadczenie / symulacja

**Pęd światła w praktyce.** Efekt Comptona to zderzenia pojedynczych fotonów. Pęd światła w dużej skali widać jako ciśnienie promieniowania (16.03). Przelicz, ile fotonów 550 nm na sekundę daje siłę 1 μN po pochłonięciu.

**Python:** długość fali i energia fotonu rozproszonego w funkcji kąta, energia elektronu odrzutu.

```python
import numpy as np
import matplotlib.pyplot as plt

h, c, me, e = 6.62607015e-34, 2.99792458e8, 9.1093837e-31, 1.602176634e-19
lamC = h/(me*c)
th = np.radians(np.linspace(0, 180, 181))
for lam0 in (71e-12, 500e-9):
    lam1 = lam0 + lamC*(1 - np.cos(th))
    print(f"λ = {lam0:.3g} m: Δλ/λ przy 180° = {2*lamC/lam0:.2e}")
lam0 = 71e-12
lam1 = lam0 + lamC*(1 - np.cos(th))
Ee = h*c*(1/lam0 - 1/lam1)/e/1e3
print(f"λ_C = {lamC*1e12:.3f} pm; 90°: λ' = {(lam0 + lamC)*1e12:.2f} pm, E_e = {Ee[90]:.3f} keV")
print(f"fotony 550 nm na 1 µN (pochłanianie): {1e-6/(h/550e-9):.2e} na sekundę")
plt.plot(np.degrees(th), lam1*1e12)
plt.xlabel("kąt rozproszenia [°]"); plt.ylabel("λ' [pm]"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Oblicz pęd fotonu światła zielonego (550 nm) i fotonu promieniowania rentgenowskiego 0,1 nm.

<details>
<summary>Odpowiedź</summary>

$p = h/\lambda$: $1{,}2\cdot10^{-27}$ i $6{,}6\cdot10^{-24}\ \mathrm{kg\cdot m/s}$.
</details>

2. Pod jakim kątem rozproszenia przesunięcie Comptona jest równe $\lambda_C$?

<details>
<summary>Odpowiedź</summary>

$1 - \cos\theta = 1 \Rightarrow \theta = 90^\circ$.
</details>

### B. Poziom akademicki

1. Foton gamma o energii 662 keV (cez-137) rozprasza się wstecz na elektronie. Oblicz energię fotonu rozproszonego i energię elektronu (krawędź Comptona w widmie detektora).

<details>
<summary>Odpowiedź</summary>

$\dfrac{1}{E'} = \dfrac1E + \dfrac{2}{m_ec^2}$: $E' = \dfrac{662}{1 + 2\cdot662/511} \approx 184\ \mathrm{keV}$. Elektron dostaje ok. 478 keV.
</details>

2. Pokaż, że energia fotonu po rozproszeniu wynosi $E' = \dfrac{E}{1 + (E/m_ec^2)(1 - \cos\theta)}$. Kiedy przesunięcie jest istotne?

<details>
<summary>Odpowiedź</summary>

Z $\lambda' = \lambda + \lambda_C(1 - \cos\theta)$ i $E = hc/\lambda$: $\dfrac{1}{E'} = \dfrac1E + \dfrac{1 - \cos\theta}{m_ec^2}$. Istotne, gdy $E$ jest porównywalne z $m_ec^2 = 511\ \mathrm{keV}$.
</details>

3. Wyznacz kąt, pod jakim odskakuje elektron, gdy foton 17,5 keV rozprasza się pod $90^\circ$.

<details>
<summary>Odpowiedź</summary>

Pęd elektronu = $\vec p - \vec p\,'$. Przy $\theta = 90^\circ$: $\tan\varphi = p'/p = \lambda/\lambda' = 71/73{,}4$, więc elektron odskakuje pod kątem $\varphi \approx 44^\circ$ od kierunku padania, po przeciwnej stronie niż foton.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6 — §6.3: efekt Comptona.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §38.3; wyd. 1: t. 5, §39.4.
