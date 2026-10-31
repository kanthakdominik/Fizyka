# 18.04 — Interferencja w cienkich warstwach, interferometr Michelsona

> **Moduł:** [18 — Optyka falowa](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 3: [§3.4–3.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/3-4-interferencja-w-cienkich-warstwach) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/3-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §35.4–35.5 (s. 117)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§36.7–36.8, s. 91](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=106) — PDF z serwera AGH

← [Interferencja na wielu szczelinach i siatka dyfrakcyjna](03-siatka-dyfrakcyjna.md) · [spis modułu](README.md) · [Dyfrakcja na szczelinie i zdolność rozdzielcza](05-dyfrakcja-i-rozdzielczosc.md) →

## Po co to jest

Barwy bańki mydlanej, plamy oleju na mokrym asfalcie i piór pawia to interferencja w cienkich warstwach. To samo zjawisko wykorzystują powłoki antyrefleksyjne na okularach i obiektywach, filtry interferencyjne, lustra laserowe i kontrola płaskości powierzchni optycznych. Interferometr Michelsona dzieli wiązkę na dwie i porównuje ich drogi z dokładnością do ułamka długości fali. Pozwolił obalić hipotezę eteru (19), a w gigantycznej wersji LIGO wykrywa fale grawitacyjne, zmiany długości mniejsze od rozmiaru protonu.

## Teoria w pigułce

**Cienka warstwa.** Światło pada na warstwę o grubości $t$ i współczynniku $n$. Odbija się od górnej i dolnej powierzchni, a dwie odbite fale interferują. Różnica dróg optycznych (przy padaniu prawie prostopadłym) wynosi $2nt$. Do tego dochodzą zmiany fazy przy odbiciach (18.01): o $\pi$ przy odbiciu od ośrodka o większym $n$.

**Warstwa w powietrzu** (bańka mydlana, $n_{\text{pow}} < n > n_{\text{pow}}$): przesunięcie o $\pi$ ma tylko odbicie od górnej powierzchni.

$$\text{wzmocnienie: } 2nt = \left(m + \tfrac12\right)\lambda, \qquad \text{wygaszenie: } 2nt = m\lambda.$$

Bardzo cienka warstwa ($t \ll \lambda$) jest w odbiciu **ciemna**. Tak wygląda czarna plama u góry bańki tuż przed pęknięciem.

**Powłoka antyrefleksyjna** na szkle ($n_{\text{pow}} < n_{\text{powł}} < n_{\text{szkło}}$): oba odbicia zmieniają fazę o $\pi$, więc liczy się tylko $2nt$. Wygaszenie zachodzi dla

$$2nt = \left(m + \tfrac12\right)\lambda \Rightarrow t_{\min} = \frac{\lambda}{4n}$$

(warstwa ćwierćfalowa). Idealnie, gdy $n_{\text{powł}} = \sqrt{n_{\text{szkło}}}$. Wtedy oba odbicia mają tę samą amplitudę i znoszą się całkowicie.

**Klin powietrzny i pierścienie Newtona.** Grubość warstwy zmienia się płynnie, więc prążki to linie stałej grubości. Każdy prążek odpowiada zmianie grubości o $\lambda/2$. Tak sprawdza się płaskość szkieł optycznych z dokładnością do ułamka mikrometra.

**Interferometr Michelsona.** Półprzepuszczalne lustro dzieli wiązkę na dwa prostopadłe ramiona. Wiązki odbijają się od luster i wracają. Przesunięcie jednego lustra o $d$ zmienia różnicę dróg o $2d$, a przez pole widzenia przechodzi

$$N = \frac{2d}{\lambda}$$

prążków. Tak można mierzyć długości w jednostkach długości fali, współczynnik załamania gazów i drgania.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| różnica dróg $2nt$ | cienka warstwa | padanie prawie prostopadłe |
| $2nt = (m + \tfrac12)\lambda$ | jasne odbicie, warstwa w powietrzu | jedno odbicie z przesunięciem $\pi$ |
| $t = \lambda/(4n)$ | powłoka antyrefleksyjna | $n_{\text{pow}} < n_{\text{powł}} < n_{\text{szkło}}$ |
| $N = 2d/\lambda$ | prążki w interferometrze Michelsona | przesunięcie lustra o $d$ |

## Przykład rozwiązany

**Zadanie 1.** Jaka jest najmniejsza grubość błony mydlanej ($n = 1{,}33$), która w świetle odbitym wydaje się jasnozielona (550 nm)?

Warstwa w powietrzu: $2nt = \tfrac12\lambda \Rightarrow t = \dfrac{\lambda}{4n} \approx 103\ \mathrm{nm}$.

**Zadanie 2.** Obiektyw pokryto warstwą $\mathrm{MgF_2}$ ($n = 1{,}38$), żeby nie odbijał światła 550 nm. Jaka grubość?

Oba odbicia zmieniają fazę o $\pi$, więc wygaszenie przy $2nt = \lambda/2$: $t = \lambda/(4n) \approx 100\ \mathrm{nm}$. Dla czerwieni i fioletu wygaszenie jest niepełne, stąd fioletowy połysk powłok.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** W interferometrze Michelsona z laserem 633 nm przesunięto lustro o 0,1 mm. Ile prążków przeszło? Następnie w jednym ramieniu umieszczono komorę o długości 5 cm i powoli wypompowano z niej powietrze. Przeszło 48 prążków. Oblicz współczynnik załamania powietrza.

$N = 2d/\lambda = 2\cdot10^{-4}/633\cdot10^{-9} \approx 316$.

Wiązka przechodzi przez komorę dwa razy, więc zmiana drogi optycznej wynosi $2L(n - 1) = N\lambda$:

$$n - 1 = \frac{N\lambda}{2L} = \frac{48\cdot633\cdot10^{-9}}{0{,}1} \approx 3{,}0\cdot10^{-4}.$$

Wynik $n \approx 1{,}0003$ zgadza się z tablicami.

## Typowe pułapki

- **Pomijanie zmiany fazy przy odbiciu.** To najczęstszy błąd. Sprawdź oba odbicia osobno.
- **Długość fali w powietrzu zamiast w warstwie.** We wzorach jest $2nt$, czyli długość fali w warstwie to $\lambda/n$.
- **Przesunięcie lustra o $\lambda$ daje jeden prążek.** Daje dwa: droga zmienia się o $2d$, więc jeden prążek odpowiada przesunięciu o $\lambda/2$.
- **Powłoka antyrefleksyjna zatrzymuje światło.** Nie zatrzymuje go. Światło, które się nie odbiło, przechodzi przez szkło.

## Doświadczenie / symulacja

**Bańka mydlana w pionowej ramce.** Ramkę z drutu zanurz w płynie do baniek i ustaw pionowo w świetle lampy. Woda spływa w dół, więc warstwa jest klinem. Pojawiają się poziome kolorowe prążki, a u góry czarny pas tuż przed pęknięciem.

**Pierścienie Newtona.** Połóż soczewkę wypukłą (np. z lupy) na płaskiej szybie i oświetl lampą sodową lub światłem przez kolorowy filtr. Wokół punktu styku widać pierścienie.

**Python:** barwa błony mydlanej w funkcji grubości (widmo odbite od cienkiej warstwy).

```python
import numpy as np
import matplotlib.pyplot as plt

n = 1.33
lam = np.linspace(400e-9, 700e-9, 301)
t = np.linspace(0, 1000e-9, 400)
# natężenie odbite (dwie fale, przesunięcie π na górnej powierzchni): ~ sin²(2π n t / λ)
R = np.sin(2*np.pi*n*t[:, None]/lam[None, :])**2
for tt in (50e-9, 103e-9, 200e-9):
    i = np.argmin(abs(t - tt))
    print(f"t = {tt*1e9:.0f} nm: najsilniej odbijana λ = {lam[np.argmax(R[i])]*1e9:.0f} nm")
print(f"powłoka MgF2 dla 550 nm: t = {550e-9/(4*1.38)*1e9:.1f} nm")
print(f"Michelson: 0,1 mm → {2*0.1e-3/633e-9:.0f} prążków; n − 1 powietrza = {48*633e-9/(2*0.05):.2e}")
plt.imshow(R.T, aspect="auto", extent=[0, 1000, 700, 400], cmap="viridis")
plt.xlabel("grubość warstwy [nm]"); plt.ylabel("λ [nm]"); plt.title("odbicie od błony mydlanej"); plt.colorbar(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Plama oleju ($n = 1{,}45$) leży na wodzie ($n = 1{,}33$). Czy przy odbiciu od dolnej powierzchni oleju faza się zmienia? Jaka najmniejsza grubość daje wzmocnienie dla 600 nm?

<details>
<summary>Odpowiedź</summary>

Nie, bo woda ma mniejsze $n$ niż olej. Zmienia się tylko przy górnej powierzchni, jak w bańce: $t = \lambda/(4n) \approx 103\ \mathrm{nm}$.
</details>

2. Dlaczego bańka mydlana tuż przed pęknięciem staje się u góry czarna?

<details>
<summary>Odpowiedź</summary>

Warstwa jest dużo cieńsza od długości fali, więc różnica dróg jest prawie zerowa, a jedno z odbić zmienia fazę o $\pi$. Fale odbite się znoszą dla wszystkich barw.
</details>

3. O ile przesunięto lustro w interferometrze Michelsona (światło 500 nm), jeśli przeszło 1000 prążków?

<details>
<summary>Odpowiedź</summary>

$d = N\lambda/2 = 0{,}25\ \mathrm{mm}$.
</details>

### B. Poziom akademicki

1. Klin powietrzny utworzono z dwóch płytek szklanych o długości 10 cm, rozdzielonych na jednym końcu włosem. W świetle 600 nm widać 40 ciemnych prążków na całej długości. Oblicz grubość włosa.

<details>
<summary>Odpowiedź</summary>

Kolejne prążki odpowiadają zmianie grubości o $\lambda/2$: $t = 40\cdot300\ \mathrm{nm} = 12\ \mu\mathrm m$ (z dokładnością do jednego prążka). To raczej cienki włos lub nić.
</details>

2. Pokaż, że dla powłoki ćwierćfalowej o $n_1$ na szkle o $n_2$ odbicie znika całkowicie, gdy $n_1 = \sqrt{n_2}$. Współczynnik odbicia amplitudy na granicy to $r = (n_a - n_b)/(n_a + n_b)$.

<details>
<summary>Odpowiedź</summary>

Wygaszenie całkowite wymaga równych amplitud: $\dfrac{n_1 - 1}{n_1 + 1} = \dfrac{n_2 - n_1}{n_2 + n_1}$, co daje $n_1^2 = n_2$. Dla szkła 1,52 idealne byłoby $n_1 = 1{,}23$. $\mathrm{MgF_2}$ (1,38) jest najbliższym trwałym materiałem.
</details>

3. LIGO ma ramiona o długości 4 km i wykrywa zmiany długości rzędu $10^{-18}\ \mathrm m$. Jaka to względna zmiana długości (amplituda fali grawitacyjnej)? Porównaj z rozmiarem protonu.

<details>
<summary>Odpowiedź</summary>

$\Delta L/L \approx 2{,}5\cdot10^{-22}$. Proton ma ok. $10^{-15}\ \mathrm m$, więc zmiana jest tysiąc razy mniejsza od protonu.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 3 — §3.4 (interferencja w cienkich warstwach) i §3.5 (interferometr Michelsona).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §35.4–35.5; wyd. 1: t. 4, §36.7–36.8.
