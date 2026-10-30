# 14.06 — Prawo Ampère'a, solenoid i toroid

> **Moduł:** [14 — Pole magnetyczne](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 12: [§12.5–12.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/12-5-prawo-amperea) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/12-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §29.3–29.4 (s. 303)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §30.3–30.4, s. 228 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Oddziaływanie przewodników z prądem](05-oddzialywanie-przewodnikow.md) · [spis modułu](README.md) · [Magnetyzm materii: dia-, para- i ferromagnetyki](07-magnetyzm-materii.md) →

## Po co to jest

Prawo Ampère'a jest dla pola magnetycznego tym, czym prawo Gaussa dla elektrycznego (12.04). Przy wysokiej symetrii daje pole w jednej linijce. Z niego wynika pole w zwojnicy (solenoidzie), czyli w elektromagnesach, przekaźnikach, zaworach elektromagnetycznych, cewkach indukcyjnych i tomografach MRI. Pole w toroidzie wyjaśnia, dlaczego rdzenie transformatorów robi się zamknięte. To kolejne z równań Maxwella (16), które w pełnej postaci uzupełnia prąd przesunięcia.

## Teoria w pigułce

**Prawo Ampère'a.** Całka z pola magnetycznego po dowolnej zamkniętej krzywej (konturze) jest proporcjonalna do prądu przepływającego przez powierzchnię rozpiętą na tym konturze:

$$\oint\vec B\cdot d\vec l = \mu_0I_{\text{obj}}.$$

Znak prądu wyznacza reguła prawej dłoni: palce wzdłuż kierunku obiegu, kciuk wskazuje dodatni kierunek prądu. Prądy płynące na zewnątrz konturu nie wnoszą wkładu do całki, choć wpływają na pole.

**Jak liczyć pole.** Wybierz kontur, na którym $B$ jest stałe i styczne (albo prostopadłe, wtedy $\vec B\cdot d\vec l = 0$):

| Układ | Kontur | Wynik |
|---|---|---|
| długi przewód | okrąg o promieniu $r$ | $B\cdot2\pi r = \mu_0I \Rightarrow B = \mu_0I/(2\pi r)$ |
| wnętrze przewodu (prąd jednorodny) | okrąg $r < R$ | $B = \dfrac{\mu_0Ir}{2\pi R^2}$, rośnie liniowo |
| długi solenoid ($n$ zwojów na metr) | prostokąt częściowo wewnątrz | $B = \mu_0nI$ wewnątrz, ≈ 0 na zewnątrz |
| toroid ($N$ zwojów) | okrąg o promieniu $r$ wewnątrz | $B = \dfrac{\mu_0NI}{2\pi r}$, 0 na zewnątrz |
| kabel koncentryczny | okrąg poza ekranem | $I_{\text{obj}} = 0 \Rightarrow B = 0$ |

**Solenoid.** Wewnątrz długiej zwojnicy pole jest jednorodne i nie zależy od średnicy ani od położenia (z dala od końców). Na końcach spada do połowy. Na zewnątrz linie się rozbiegają i pole jest słabe, dlatego solenoid przypomina magnes sztabkowy.

**Toroid** zamyka linie pola wewnątrz, więc pole na zewnątrz jest zerowe i cewka toroidalna nie zakłóca otoczenia.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\oint\vec B\cdot d\vec l = \mu_0I_{\text{obj}}$ | prawo Ampère'a | prądy stałe (w ogólnym przypadku + prąd przesunięcia, 16) |
| $B = \mu_0nI$ | solenoid | długość $\gg$ średnica, z dala od końców |
| $B = \mu_0NI/(2\pi r)$ | toroid | wewnątrz uzwojenia |
| $B = \mu_0Ir/(2\pi R^2)$ | wnętrze przewodu | prąd jednorodny |

## Przykład rozwiązany

**Zadanie 1.** Solenoid o długości 50 cm ma 1000 zwojów, a płynie przez niego prąd 2 A. Oblicz pole wewnątrz. Jakie $nI$ jest potrzebne dla pola 1,5 T w tomografie MRI?

$B = \mu_0\cdot\dfrac{1000}{0{,}5}\cdot2 \approx 5{,}0\ \mathrm{mT}$.

Dla 1,5 T: $nI = B/\mu_0 \approx 1{,}2\cdot10^6\ \mathrm{A/m}$, np. 2000 zwojów na metr i prąd 600 A. Zwykły miedziany drut by się stopił. Dlatego cewki MRI są nadprzewodzące, chłodzone ciekłym helem.

**Zadanie 2.** Toroid ma 500 zwojów, a prąd wynosi 1 A. Oblicz pole w odległości 10 cm od osi.

$B = \dfrac{\mu_0\cdot500\cdot1}{2\pi\cdot0{,}1} = 1\ \mathrm{mT}$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** W przewodzie o promieniu $R$ gęstość prądu rośnie od osi: $J(r) = J_0r/R$. Całkowity prąd wynosi $I$. Wyznacz $B(r)$ wewnątrz i na zewnątrz.

Prąd w kole o promieniu $r$: $I(r) = \displaystyle\int_0^rJ_0\frac{r'}{R}2\pi r'\,dr' = \frac{2\pi J_0r^3}{3R}$, a $I = \dfrac{2\pi J_0R^2}{3}$, więc $I(r) = I\dfrac{r^3}{R^3}$.

Z prawa Ampère'a: $B\cdot2\pi r = \mu_0I\dfrac{r^3}{R^3} \Rightarrow B = \dfrac{\mu_0Ir^2}{2\pi R^3}$ wewnątrz, a na zewnątrz $B = \dfrac{\mu_0I}{2\pi r}$. Oba wzory dają tę samą wartość na powierzchni.

## Typowe pułapki

- **Pole w solenoidzie zależy od średnicy.** Dla długiego solenoidu nie zależy. Liczy się tylko liczba zwojów na metr i prąd.
- **$n$ jako całkowita liczba zwojów.** We wzorze $\mu_0nI$ to zwoje **na metr**. W toroidzie $N$ to całkowita liczba zwojów.
- **Prawo Ampère'a daje $B = 0$ tam, gdzie $I_{\text{obj}} = 0$.** Zerowa całka nie oznacza zerowego pola w każdym punkcie. Wynik $B = 0$ wymaga symetrii (np. kabel koncentryczny).
- **Prawo Ampère'a dla krótkiego odcinka przewodu.** Działa dla zamkniętych obwodów prądu. Do pola krótkiego odcinka służy prawo Biota–Savarta.
- **Pole na końcu solenoidu.** Wynosi połowę pola w środku, bo to jak połowa nieskończonego solenoidu.

## Doświadczenie / symulacja

**Pole w zwojnicy telefonem.** Nawiń 100–200 zwojów drutu w lakierze na rurę PCV (np. średnicy 5 cm i długości 30 cm). Zasilaj przez opornik z zasilacza i mierz prąd. Telefon z magnetometrem włóż do środka (lub przyłóż do końca, jeśli się nie mieści) i zmierz pole dla kilku prądów. Sprawdź $B \propto I$ i porównaj z $\mu_0nI$. Pamiętaj o odjęciu pola Ziemi.

**Symulacja PhET:** *Laboratorium elektromagnetyczne Faradaya* — zakładka z elektromagnesem: zmieniaj liczbę zwojów i prąd.

**Python:** pole na osi solenoidu skończonej długości (suma pętli) w porównaniu z $\mu_0nI$.

```python
import numpy as np
import matplotlib.pyplot as plt

mu0 = 4e-7*np.pi
L, R, N, I = 0.5, 0.02, 1000, 2.0
n = N/L
zc = np.linspace(-L/2, L/2, N)                        # położenia zwojów

def B_os(z):                                           # suma pól pętli kołowych
    return np.sum(mu0*I*R**2/(2*((z - zc)**2 + R**2)**1.5))

def B_wzor(z):                                         # wzór zamknięty dla solenoidu skończonego
    return mu0*n*I/2*((z + L/2)/np.hypot(z + L/2, R) - (z - L/2)/np.hypot(z - L/2, R))

for z in (0, L/4, L/2, L/2 + 0.05):
    print(f"z = {z*100:5.1f} cm: suma pętli {B_os(z)*1e3:.3f} mT, wzór {B_wzor(z)*1e3:.3f} mT, μ0nI = {mu0*n*I*1e3:.3f} mT")
print(f"MRI 1,5 T: potrzebne nI = {1.5/mu0:.3e} A/m")

z = np.linspace(-0.4, 0.4, 400)
plt.plot(z*100, [B_os(v)*1e3 for v in z]); plt.axhline(mu0*n*I*1e3, ls="--", color="gray")
plt.axvline(-L/2*100, color="k", lw=0.5); plt.axvline(L/2*100, color="k", lw=0.5)
plt.xlabel("z [cm]"); plt.ylabel("B [mT]"); plt.title("pole na osi solenoidu"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Ile zwojów na centymetr musi mieć solenoid, żeby przy prądzie 0,5 A pole wynosiło 1 mT?

<details>
<summary>Odpowiedź</summary>

$n = B/(\mu_0I) \approx 1600\ \mathrm{m^{-1}} = 16$ zwojów na cm.
</details>

2. Jak zmieni się pole wewnątrz solenoidu, gdy rozciągniemy go dwukrotnie (ta sama liczba zwojów i prąd)?

<details>
<summary>Odpowiedź</summary>

Zmaleje dwukrotnie, bo $n$ maleje dwa razy.
</details>

3. Przewód o promieniu 1 mm przewodzi prąd 10 A rozłożony równomiernie. Oblicz pole na powierzchni i w odległości 0,5 mm od osi.

<details>
<summary>Odpowiedź</summary>

Na powierzchni $\mu_0I/(2\pi R) = 2\ \mathrm{mT}$. W połowie promienia 1 mT.
</details>

### B. Poziom akademicki

1. Wyprowadź pole solenoidu z prawa Ampère'a, używając prostokątnego konturu o boku $l$ wewnątrz solenoidu i drugim boku na zewnątrz.

<details>
<summary>Odpowiedź</summary>

Wkład daje tylko bok wewnątrz: $Bl$. Boki prostopadłe są prostopadłe do $\vec B$, a na zewnątrz $B \approx 0$. Przez kontur przechodzi $nl$ zwojów, czyli prąd $nlI$. Stąd $Bl = \mu_0nlI$ i $B = \mu_0nI$.
</details>

2. Kabel koncentryczny: wewnętrzny przewód o promieniu $a$ i ekran (cienka powłoka o promieniu $b$) przewodzą prądy $I$ w przeciwnych kierunkach. Wyznacz $B(r)$ we wszystkich obszarach.

<details>
<summary>Odpowiedź</summary>

$r < a$: $\mu_0Ir/(2\pi a^2)$; $a < r < b$: $\mu_0I/(2\pi r)$; $r > b$: 0.
</details>

3. Gęstość energii pola magnetycznego wynosi $B^2/(2\mu_0)$. Ile energii mieści się w 1 m³ pola tomografu 1,5 T? Dlaczego nagłe wyłączenie nadprzewodzącego magnesu (quench) jest groźne?

<details>
<summary>Odpowiedź</summary>

$w = 1{,}5^2/(2\mu_0) \approx 0{,}9\ \mathrm{MJ/m^3}$. Megadżule energii zamieniają się w ciepło w kilka sekund i gwałtownie odparowują ciekły hel, który musi zostać bezpiecznie odprowadzony na zewnątrz.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 12 — §12.5 (prawo Ampère'a) i §12.6 (solenoidy i toroidy).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §29.3–29.4; wyd. 1: t. 3, §30.3–30.4.
- Symulacja PhET *Laboratorium elektromagnetyczne Faradaya*.
