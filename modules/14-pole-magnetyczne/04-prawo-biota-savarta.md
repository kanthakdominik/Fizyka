# 14.04 — Prawo Biota–Savarta

> **Moduł:** [14 — Pole magnetyczne](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 12: [§12.1–12.2 i §12.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/12-1-prawo-biota-savarta) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/12-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §29.1 (s. 293), §29.5 (s. 312)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §30.1, s. 219, §30.5, s. 235 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Efekt Halla, spektrometr masowy, cyklotron](03-hall-cyklotron-spektrometr.md) · [spis modułu](README.md) · [Oddziaływanie przewodników z prądem](05-oddzialywanie-przewodnikow.md) →

## Po co to jest

Prąd elektryczny wytwarza pole magnetyczne. Tak Ørsted w 1820 r. odkrył związek elektryczności z magnetyzmem, a dziś działają na tym elektromagnesy, przekaźniki, cewki, głowice zapisujące i tomografy MRI. Prawo Biota–Savarta pozwala obliczyć pole od dowolnego przewodu, tak jak prawo Coulomba z całkowaniem pozwala obliczyć pole elektryczne (12.03). Pole w środku i na osi pętli to podstawa cewek Helmholtza, które dają jednorodne pole w laboratoriach.

## Teoria w pigułce

**Prawo Biota–Savarta.** Element przewodu $d\vec l$ z prądem $I$ wytwarza w punkcie odległym o $\vec r$ pole

$$d\vec B = \frac{\mu_0}{4\pi}\frac{I\,d\vec l\times\hat r}{r^2}, \qquad \mu_0 = 4\pi\cdot10^{-7}\ \mathrm{T\cdot m/A}.$$

$\mu_0$ to przenikalność magnetyczna próżni. Od 2019 r. jest wyznaczana doświadczalnie, ale z dokładnością do $10^{-10}$ ma tę wartość. Pole jest prostopadłe zarówno do $d\vec l$, jak i do $\vec r$, i maleje jak $1/r^2$. Całkowite pole to całka po całym obwodzie.

**Przewód prosty.** Odcinek przewodu widziany z punktu w odległości $d$ pod kątami $\theta_1$ i $\theta_2$ (mierzonymi od prostopadłej):

$$B = \frac{\mu_0I}{4\pi d}(\sin\theta_2 - \sin\theta_1).$$

Dla przewodu nieskończonego ($\theta = \pm90^\circ$):

$$B = \frac{\mu_0I}{2\pi d}.$$

Linie pola to okręgi wokół przewodu. Zwrot wyznacza **reguła prawej dłoni**: kciuk wzdłuż prądu, a zgięte palce pokazują zwrot pola.

**Pętla kołowa** o promieniu $R$:
- w środku: $B = \dfrac{\mu_0I}{2R}$;
- na osi, w odległości $z$: $B = \dfrac{\mu_0IR^2}{2(z^2 + R^2)^{3/2}}$;
- daleko na osi: $B \approx \dfrac{\mu_0}{2\pi}\dfrac{\mu}{z^3}$, gdzie $\mu = I\pi R^2$. Pętla to **dipol magnetyczny**, a pole ma tę samą postać co pole dipola elektrycznego (12.02).

Łuk o kącie $\varphi$ daje w środku krzywizny pole $\dfrac{\mu_0I\varphi}{4\pi R}$.

**Cewki Helmholtza** to dwie współosiowe pętle o promieniu $R$ odległe o $R$. W środku dają bardzo jednorodne pole $B = \left(\tfrac45\right)^{3/2}\dfrac{\mu_0NI}{R}$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $d\vec B = \dfrac{\mu_0}{4\pi}\dfrac{I\,d\vec l\times\hat r}{r^2}$ | prawo Biota–Savarta | prąd stały |
| $B = \mu_0I/(2\pi d)$ | nieskończony przewód prostoliniowy | $d \ll$ długość |
| $B = \mu_0I/(2R)$ | środek pętli kołowej | — |
| $B = \mu_0IR^2/[2(z^2 + R^2)^{3/2}]$ | oś pętli | — |
| $B = (4/5)^{3/2}\mu_0NI/R$ | cewki Helmholtza (środek) | odległość cewek $= R$ |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Wyprowadź pole na osi pętli kołowej. Oblicz je w środku i w odległości $z = R$ dla $I = 10\ \mathrm A$, $R = 5\ \mathrm{cm}$.

Każdy element $d\vec l$ jest prostopadły do wektora $\vec r$ do punktu na osi, a $r^2 = z^2 + R^2$. Składowe prostopadłe do osi znoszą się parami. Składowa wzdłuż osi to $dB\cdot\dfrac{R}{r}$:

$$B = \oint\frac{\mu_0I\,dl}{4\pi r^2}\cdot\frac Rr = \frac{\mu_0IR}{4\pi r^3}\cdot2\pi R = \frac{\mu_0IR^2}{2(z^2 + R^2)^{3/2}}.$$

W środku: $B = \mu_0I/(2R) \approx 1{,}26\cdot10^{-4}\ \mathrm T = 126\ \mu\mathrm T$. Dla $z = R$: $B = \dfrac{\mu_0I}{2^{5/2}R} \approx 44\ \mu\mathrm T$.

**Zadanie 2.** Wyprowadź pole przewodu nieskończonego, całkując po kącie.

Element w położeniu $x$ widziany pod kątem $\theta$: $x = d\tan\theta$, $dx = d\,d\theta/\cos^2\theta$, $r = d/\cos\theta$, a $\lvert d\vec l\times\hat r\rvert = dx\cos\theta$:

$$B = \frac{\mu_0I}{4\pi}\int_{-\pi/2}^{\pi/2}\frac{\cos\theta\,d\theta}{d} = \frac{\mu_0I}{2\pi d}.$$

Dla $I = 10\ \mathrm A$ i $d = 5\ \mathrm{cm}$: $B = 40\ \mu\mathrm T$, porównywalnie z polem Ziemi. Dlatego kompas obok przewodu z prądem wyraźnie się odchyla (doświadczenie Ørsteda).

## Typowe pułapki

- **Pole przewodu skierowane wzdłuż niego.** Linie pola to okręgi wokół przewodu, prostopadłe do prądu.
- **Pole przewodu maleje jak $1/d^2$.** Pojedynczy element daje $1/r^2$, ale całkowite pole nieskończonego przewodu maleje jak $1/d$.
- **Wzór na nieskończony przewód blisko końca.** Przy końcu długiego przewodu pole jest o połowę mniejsze (pół przewodu). Trzeba użyć wzoru z kątami.
- **Mylenie $\mu_0I/(2R)$ i $\mu_0I/(2\pi R)$.** Pierwszy wzór dotyczy środka pętli, drugi przewodu prostego.
- **Pole w środku pętli z $N$ zwojami.** Trzeba pomnożyć przez $N$.

## Doświadczenie / symulacja

**Doświadczenie Ørsteda z telefonem.** Długi przewód (np. przedłużacz rozdzielony na dwie żyły albo drut z baterią i opornikiem mocy) połóż prosto na stole. Magnetometrem telefonu zmierz pole w odległościach 1–10 cm przy znanym prądzie (miernik). Odejmij pole Ziemi (pomiar bez prądu) i sprawdź $B \propto 1/d$. Uwaga: prąd z baterii przez sam drut to zwarcie. Użyj opornika lub żarówki samochodowej.

**Symulacja PhET:** *Laboratorium elektromagnetyczne Faradaya* (*Faraday's Electromagnetic Lab*) — pole cewki z prądem i jej wpływ na kompas.

**Python:** prawo Biota–Savarta numerycznie — pole pętli z sumy elementów i porównanie ze wzorem.

```python
import numpy as np
import matplotlib.pyplot as plt

mu0 = 4e-7*np.pi
I, R, N = 10.0, 0.05, 2000
phi = np.linspace(0, 2*np.pi, N, endpoint=False)
pts = np.stack([R*np.cos(phi), R*np.sin(phi), np.zeros(N)], axis=1)          # pętla w płaszczyźnie xy
dl = np.stack([-R*np.sin(phi), R*np.cos(phi), np.zeros(N)], axis=1)*(2*np.pi/N)

def B_biot(P):
    r = P - pts
    rn = np.linalg.norm(r, axis=1)[:, None]
    return mu0*I/(4*np.pi)*np.sum(np.cross(dl, r)/rn**3, axis=0)

for z in (0.0, 0.05, 0.2):
    Bz = B_biot(np.array([0, 0, z]))[2]
    wzor = mu0*I*R**2/(2*(z**2 + R**2)**1.5)
    print(f"z = {z:.2f} m: numerycznie {Bz*1e6:8.3f} µT, wzór {wzor*1e6:8.3f} µT")

z = np.linspace(-0.2, 0.2, 200)
plt.plot(z*100, mu0*I*R**2/(2*(z**2 + R**2)**1.5)*1e6, label="pętla")
Bh = sum(mu0*I*R**2/(2*((z - s*R/2)**2 + R**2)**1.5) for s in (-1, 1))   # cewki Helmholtza, po 1 zwoju
plt.plot(z*100, Bh*1e6, label="para Helmholtza")
plt.xlabel("z [cm]"); plt.ylabel("B [µT]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Oblicz pole w odległości 2 cm od długiego przewodu z prądem 5 A.

<details>
<summary>Odpowiedź</summary>

$B = \mu_0I/(2\pi d) = 50\ \mu\mathrm T$.
</details>

2. Kompas leży 5 cm od pionowego przewodu z prądem 10 A. Pozioma składowa pola Ziemi wynosi ok. 20 μT. O jaki kąt odchyli się igła, jeśli pole przewodu jest prostopadłe do ziemskiego?

<details>
<summary>Odpowiedź</summary>

$B_{\text{przew}} = 40\ \mu\mathrm T$, $\tan\alpha = 40/20 \Rightarrow \alpha \approx 63^\circ$.
</details>

### B. Poziom akademicki

1. Pętla kwadratowa o boku $a$ przewodzi prąd $I$. Oblicz pole w jej środku, sumując cztery odcinki. Porównaj z pętlą kołową o tym samym obwodzie.

<details>
<summary>Odpowiedź</summary>

Każdy bok: $d = a/2$, $\sin\theta = \pm1/\sqrt2$, więc $B_1 = \dfrac{\mu_0I}{4\pi(a/2)}\sqrt2$. Razem $B = \dfrac{2\sqrt2\mu_0I}{\pi a}$. Okrąg o obwodzie $4a$ ma $R = 2a/\pi$ i $B = \mu_0I\pi/(4a)$. Stosunek kwadrat/okrąg $= 8\sqrt2/\pi^2 \approx 1{,}15$.
</details>

2. Pokaż, że daleko na osi pętli pole wynosi $\dfrac{\mu_0}{2\pi}\dfrac{\mu}{z^3}$, gdzie $\mu = I\pi R^2$.

<details>
<summary>Odpowiedź</summary>

Dla $z \gg R$: $B \approx \dfrac{\mu_0IR^2}{2z^3} = \dfrac{\mu_0}{2\pi}\dfrac{I\pi R^2}{z^3}$.
</details>

3. Oblicz pole w środku cewek Helmholtza o promieniu 10 cm, po 100 zwojów, z prądem 1 A. Pokaż, że w środku $dB/dz = 0$ i $d^2B/dz^2 = 0$.

<details>
<summary>Odpowiedź</summary>

$B = (4/5)^{3/2}\mu_0NI/R \approx 0{,}90\ \mathrm{mT}$. Pierwsza pochodna znika z symetrii. Druga pochodna pola jednej pętli, $\propto (4z^2 - R^2)$, znika w $z = \pm R/2$, czyli dokładnie w środku pary.
</details>

4. Łuk o promieniu $R$ i kącie $90^\circ$ połączony jest z dwoma prostymi przewodami biegnącymi promieniście (wzdłuż promieni łuku). Oblicz pole w środku krzywizny.

<details>
<summary>Odpowiedź</summary>

Odcinki promieniste dają zero ($d\vec l \parallel \hat r$). Łuk: $B = \dfrac{\mu_0I}{4\pi R}\cdot\dfrac\pi2 = \dfrac{\mu_0I}{8R}$.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2025, zad. 8 — pole magnetyczne przewodnika prostoliniowego ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 12 — §12.1 (prawo Biota–Savarta), §12.2 (pole magnetyczne prostoliniowego przewodnika z prądem), §12.4 (pole magnetyczne pętli z prądem).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §29.1, §29.5; wyd. 1: t. 3, §30.1, §30.5.
- Symulacja PhET *Laboratorium elektromagnetyczne Faradaya*.
