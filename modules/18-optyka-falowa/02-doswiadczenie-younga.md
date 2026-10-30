# 18.02 — Doświadczenie Younga

> **Moduł:** [18 — Optyka falowa](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 3: [§3.1–3.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/3-1-doswiadczenie-younga-z-dwiema-szczelinami) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/3-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §35.2–35.3 (s. 104)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§36.4–36.6, s. 81](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=96) — PDF z serwera AGH

← [Zasada Huygensa dla światła](01-zasada-huygensa.md) · [spis modułu](README.md) · [Interferencja na wielu szczelinach i siatka dyfrakcyjna](03-siatka-dyfrakcyjna.md) →

## Po co to jest

W 1801 r. Thomas Young przepuścił światło przez dwie wąskie szczeliny i na ekranie zobaczył jasne i ciemne prążki. To rozstrzygnęło, że światło jest falą, i pozwoliło po raz pierwszy zmierzyć jego długość fali. To samo doświadczenie wykonane z pojedynczymi fotonami i elektronami stało się najsłynniejszym pokazem dziwności mechaniki kwantowej (20.05). Prawo położenia prążków jest proste i jest stałym elementem matury rozszerzonej.

## Teoria w pigułce

**Układ.** Spójne światło o długości fali $\lambda$ pada na dwie szczeliny odległe o $d$. Na ekranie w odległości $L \gg d$ fale z obu szczelin się nakładają. Do punktu widzianego pod kątem $\theta$ fala z dalszej szczeliny ma do przebycia dłuższą drogę o

$$\Delta r = d\sin\theta.$$

**Warunki:**

$$\text{jasne prążki: } d\sin\theta = m\lambda, \qquad \text{ciemne: } d\sin\theta = \left(m + \tfrac12\right)\lambda, \qquad m = 0, \pm1, \pm2, \dots$$

Dla małych kątów $\sin\theta \approx \tan\theta = y/L$, więc jasne prążki leżą w punktach $y_m = m\lambda L/d$, a ich odstęp to

$$\Delta y = \frac{\lambda L}{d}.$$

Prążki są równo rozłożone. Szersze dla większej długości fali i mniejszej odległości szczelin.

**Natężenie.** Fale o amplitudzie $E_0$ i różnicy faz $\phi = \dfrac{2\pi}{\lambda}d\sin\theta$ dają (09.06):

$$I = 4I_0\cos^2\frac\phi2.$$

W maksimach natężenie jest cztery razy większe niż od jednej szczeliny, w minimach zero, a średnio dwa razy większe. Energia nie ginie, tylko się przerzuca z minimów do maksimów. W rzeczywistości prążki są dodatkowo modulowane obrazem dyfrakcyjnym pojedynczej szczeliny (18.05).

**Światło białe** daje biały prążek środkowy ($m = 0$ dla wszystkich barw) i kolorowe prążki boczne, z fioletem bliżej środka.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $d\sin\theta = m\lambda$ | jasne prążki | źródło spójne |
| $d\sin\theta = (m + \tfrac12)\lambda$ | ciemne prążki | — |
| $y_m = m\lambda L/d$, $\ \Delta y = \lambda L/d$ | położenie prążków na ekranie | małe kąty, $L \gg d$ |
| $I = 4I_0\cos^2(\pi d\sin\theta/\lambda)$ | natężenie | wąskie szczeliny |

## Przykład rozwiązany

**Zadanie 1.** Laser He-Ne (633 nm) oświetla dwie szczeliny odległe o 0,25 mm. Ekran stoi 1 m dalej. Oblicz odstęp prążków.

$\Delta y = 633\cdot10^{-9}\cdot1/0{,}25\cdot10^{-3} \approx 2{,}5\ \mathrm{mm}$.

**Zadanie 2.** Przy szczelinach odległych o 0,30 mm i ekranie w odległości 1 m odstęp prążków wynosi 2,0 mm. Jaka jest długość fali?

$\lambda = d\Delta y/L = 0{,}3\cdot10^{-3}\cdot2\cdot10^{-3}/1 = 600\ \mathrm{nm}$ (światło pomarańczowe).

## Typowe pułapki

- **$d$ to szerokość szczeliny.** $d$ to odległość między szczelinami (środek–środek).
- **Wzór $y = m\lambda L/d$ dla dużych kątów.** Działa tylko dla małych kątów. Ogólnie trzeba liczyć $\theta$ z $d\sin\theta = m\lambda$.
- **W minimum energia znika.** Przesuwa się do maksimów. Średnie natężenie to suma natężeń od obu szczelin.
- **Prążek zerowy jest ciemny.** W środku różnica dróg wynosi zero i prążek jest jasny.

## Doświadczenie / symulacja

**Young w domu.** Na zaczernionym nad świecą szkiełku (lub kawałku folii aluminiowej na szkle) zrób żyletką dwie równoległe rysy bardzo blisko siebie (mniej niż 0,5 mm). Oświetl wskaźnikiem laserowym i obserwuj prążki na ścianie 2–3 m dalej. Zmierz odstęp prążków, a odległość szczelin pod mikroskopem lub lupą z linijką, i wyznacz $\lambda$ lasera. Nie patrz w wiązkę.

**Symulacja PhET:** *Interferencja fal* — zakładka *Szczeliny* (*Slits*): zmieniaj $d$ i $\lambda$, obserwuj prążki.

**Python:** natężenie na ekranie dla dwóch szczelin (ze skończoną szerokością szczelin).

```python
import numpy as np
import matplotlib.pyplot as plt

lam, d, a, L = 633e-9, 0.25e-3, 0.05e-3, 1.0
y = np.linspace(-0.02, 0.02, 4001)                     # nieparzysta liczba punktów: y = 0 jest w siatce
th = np.arctan(y/L)
beta = np.pi*a*np.sin(th)/lam
I = np.cos(np.pi*d*np.sin(th)/lam)**2*np.sinc(beta/np.pi)**2     # interferencja × dyfrakcja
print(f"odstęp prążków λL/d = {lam*L/d*1e3:.2f} mm")
# odczyt odstępu z wykresu: maksima lokalne blisko środka
k = np.where((I[1:-1] > I[:-2]) & (I[1:-1] > I[2:]) & (I[1:-1] > 0.5))[0] + 1
print(f"odstęp z symulacji: {np.diff(y[k]).mean()*1e3:.2f} mm")
plt.plot(y*1e3, I); plt.xlabel("y [mm]"); plt.ylabel("I / I_max"); plt.title("dwie szczeliny"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Jak zmieni się odstęp prążków, gdy (a) ekran odsuniemy dwa razy dalej, (b) szczeliny zbliżymy dwa razy, (c) światło czerwone zamienimy na niebieskie?

<details>
<summary>Odpowiedź</summary>

(a) wzrośnie 2 razy, (b) wzrośnie 2 razy, (c) zmaleje.
</details>

2. Szczeliny są odległe o 0,1 mm, a $\lambda = 500\ \mathrm{nm}$. Pod jakim kątem widać drugi jasny prążek?

<details>
<summary>Odpowiedź</summary>

$\sin\theta = 2\cdot500\cdot10^{-9}/10^{-4} = 0{,}01$, czyli $\theta \approx 0{,}57^\circ$.
</details>

3. Całe doświadczenie zanurzono w wodzie ($n = 1{,}33$). Co stanie się z prążkami?

<details>
<summary>Odpowiedź</summary>

Długość fali w wodzie jest 1,33 razy mniejsza, więc prążki zbliżą się do siebie 1,33 razy.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź wzór $I = 4I_0\cos^2(\phi/2)$, dodając dwa pola $E_0\sin\omega t$ i $E_0\sin(\omega t + \phi)$ i uśredniając kwadrat w czasie.

<details>
<summary>Odpowiedź</summary>

Suma: $2E_0\cos(\phi/2)\sin(\omega t + \phi/2)$. Średni kwadrat: $\tfrac12\cdot4E_0^2\cos^2(\phi/2)$, a dla jednej fali $\tfrac12E_0^2$. Stosunek $4\cos^2(\phi/2)$.
</details>

2. Jedną ze szczelin przykryto folią o grubości $t$ i $n = 1{,}5$. Środkowy prążek przesunął się na miejsce piątego. Oblicz $t$ dla $\lambda = 600\ \mathrm{nm}$.

<details>
<summary>Odpowiedź</summary>

$(n - 1)t = 5\lambda \Rightarrow t = 6\ \mu\mathrm m$.
</details>

3. Pokaż, że średnia z natężenia $4I_0\cos^2(\phi/2)$ po wielu prążkach wynosi $2I_0$.

<details>
<summary>Odpowiedź</summary>

Średnia z $\cos^2$ to $\tfrac12$, więc $4I_0\cdot\tfrac12 = 2I_0$, czyli suma natężeń od obu szczelin.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 3 — §3.1 (doświadczenie Younga) i §3.2 (matematyczny opis interferencji).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §35.2–35.3; wyd. 1: t. 4, §36.4–36.6.
- Symulacja PhET *Interferencja fal*.
