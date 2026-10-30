# 13.02 — Opór, opór właściwy i prawo Ohma

> **Moduł:** [13 — Prąd stały](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 9: [§9.3–9.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/9-3-rezystywnosc-i-rezystancja) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §26.3–26.4 (s. 187)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §27.4–27.6, s. 135 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Natężenie i gęstość prądu, model przewodnictwa](01-prad-i-model-przewodnictwa.md) · [spis modułu](README.md) · [Praca i moc prądu](03-praca-i-moc-pradu.md) →

## Po co to jest

Opór decyduje o tym, jaki prąd popłynie przy danym napięciu. Od niego zależy grubość przewodów w instalacji domowej, spadek napięcia na przedłużaczu, bezpieczeństwo przy porażeniu i działanie grzałek, bezpieczników i czujników temperatury. Zależność oporu od temperatury wykorzystują termometry oporowe (Pt100) i termistory. Nadprzewodniki, które mają zerowy opór, umożliwiają budowę elektromagnesów w tomografach MRI i akceleratorach.

## Teoria w pigułce

**Opór elektryczny** przewodnika to stosunek napięcia do natężenia prądu:

$$R = \frac UI, \qquad 1\ \Omega = 1\ \mathrm{V/A}.$$

**Prawo Ohma:** dla wielu przewodników (metale w stałej temperaturze, oporniki) $R$ nie zależy od napięcia, więc $I \propto U$. Takie elementy nazywamy **omowymi**. Wykres $I(U)$ jest dla nich prostą.
- Dioda przewodzi tylko w jedną stronę i ma charakterystykę wykładniczą.
- Żarówka zwiększa opór w miarę nagrzewania.
- Takie elementy nie spełniają prawa Ohma, choć $R = U/I$ można dla nich policzyć w każdym punkcie.

**Opór właściwy.** Opór jednorodnego przewodnika o długości $L$ i przekroju $A$:

$$R = \rho\frac LA.$$

| Materiał | $\rho$ w 20°C [Ω·m] | $\alpha$ [1/K] |
|---|---|---|
| srebro | $1{,}59\cdot10^{-8}$ | $3{,}8\cdot10^{-3}$ |
| miedź | $1{,}68\cdot10^{-8}$ | $3{,}9\cdot10^{-3}$ |
| aluminium | $2{,}65\cdot10^{-8}$ | $3{,}9\cdot10^{-3}$ |
| wolfram | $5{,}6\cdot10^{-8}$ | $4{,}5\cdot10^{-3}$ |
| nichrom | $1{,}1\cdot10^{-6}$ | $0{,}4\cdot10^{-3}$ |
| krzem (czysty) | ok. $10^{3}$ | ujemny |
| szkło | $10^{10}$–$10^{14}$ | — |

Zakres oporu właściwego materiałów to ponad 20 rzędów wielkości, więcej niż dla prawie każdej innej wielkości fizycznej.

**Zależność od temperatury.** W metalach opór rośnie z temperaturą, bo drgania sieci silniej rozpraszają elektrony:

$$\rho(T) \approx \rho_0[1 + \alpha(T - T_0)].$$

W półprzewodnikach opór maleje z temperaturą, bo przybywa nośników. Na tym działają termistory NTC. W niektórych materiałach poniżej temperatury krytycznej opór spada dokładnie do zera (**nadprzewodnictwo**).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $R = U/I$ | definicja oporu | — |
| $I = U/R$, $R$ = const | prawo Ohma | elementy omowe, stała temperatura |
| $R = \rho L/A$ | opór przewodnika | jednorodny, stały przekrój |
| $\rho = \rho_0[1 + \alpha\Delta T]$ | zależność od temperatury | metale, umiarkowane $\Delta T$ |
| $R = \int\rho\,dl/A(l)$ | przekrój zmienny | prąd wzdłuż osi |

## Przykład rozwiązany

**Zadanie 1.** Oblicz opór miedzianego przewodu o długości 100 m i przekroju 1,5 mm².

$R = 1{,}68\cdot10^{-8}\cdot100/1{,}5\cdot10^{-6} \approx 1{,}12\ \Omega$.

**Zadanie 2.** Żarówka tradycyjna 60 W / 230 V ma włókno wolframowe nagrzane do ok. 2500°C. Oblicz opór gorącego włókna, opór w 20°C i prąd w chwili włączenia.

Na gorąco: $R = U^2/P \approx 880\ \Omega$ (13.03), prąd ok. 0,26 A.

Na zimno: $R_0 = \dfrac{880}{1 + 4{,}5\cdot10^{-3}\cdot2480} \approx 73\ \Omega$. To tylko szacunek, bo dla wolframu zależność nie jest liniowa w tak szerokim zakresie.

Prąd w chwili włączenia wynosi ok. 3 A, ponad 10 razy więcej niż w pracy. Dlatego żarówki najczęściej przepalały się przy włączaniu.

## Typowe pułapki

- **Opór zależy od napięcia.** Dla elementów omowych nie zależy. $R = U/I$ to definicja, a prawo Ohma mówi, że ten stosunek jest stały.
- **Grubszy przewód ma większy opór.** Ma mniejszy, bo $R \propto 1/A$. Średnica dwa razy większa oznacza opór cztery razy mniejszy.
- **mm² w obliczeniach.** $1\ \mathrm{mm^2} = 10^{-6}\ \mathrm{m^2}$.
- **Przedłużacz o długości 10 m.** Prąd płynie tam i z powrotem, więc długość przewodu to 20 m.
- **Opór właściwy a opór.** $\rho$ to cecha materiału, $R$ cecha konkretnego przedmiotu.

## Doświadczenie / symulacja

**Charakterystyki $I(U)$.** Zasilacz regulowany (lub baterie 1,5–9 V), miernik i trzy elementy: opornik, żarówka (latarkowa) i dioda LED z opornikiem. Zmierz $I(U)$ i narysuj trzy wykresy. Tylko dla opornika wyjdzie prosta.

**Opór a temperatura.** Zmierz miernikiem opór cewki z miedzianego drutu (np. ze starego transformatora) w temperaturze pokojowej, a potem w wodzie z lodem i w gorącej wodzie. Wyznacz $\alpha$ miedzi.

**Symulacje PhET:** *Prawo Ohma* (*Ohm's Law*) i *Opór przewodu* (*Resistance in a Wire*) — [phet.colorado.edu/pl](https://phet.colorado.edu/pl/).

**Python:** opór przewodów i charakterystyki elementów nieomowych.

```python
import numpy as np
import matplotlib.pyplot as plt

rho = {"miedź": 1.68e-8, "aluminium": 2.65e-8, "nichrom": 1.1e-6}
for mat, r in rho.items():
    print(f"{mat:10s}: 100 m, 1,5 mm² → R = {r*100/1.5e-6:8.2f} Ω")

U = np.linspace(-1, 3, 400)
R = 100.0
I_rez = U/R
I_diody = 1e-12*(np.exp(np.clip(U, None, 0.8)/0.05) - 1)              # dioda (model Shockleya)
U_z = np.linspace(0, 3, 200)
R_z = 5*(1 + 4.5e-3*600*(U_z/3)**1.6)                                  # włókno grzeje się z napięciem
plt.plot(U, I_rez*1e3, label="opornik 100 Ω")
plt.plot(U, np.clip(I_diody*1e3, None, 40), label="dioda")
plt.plot(U_z, U_z/R_z*1e3, label="żarówka (model)")
plt.xlabel("U [V]"); plt.ylabel("I [mA]"); plt.grid(True); plt.legend(); plt.show()
print(f"żarówka 60 W / 230 V: R_gorące = {230**2/60:.0f} Ω, R_zimne ≈ {230**2/60/(1 + 4.5e-3*2480):.0f} Ω")
```

## Zadania

### A. Poziom maturalny

1. Przez opornik przy napięciu 12 V płynie prąd 0,4 A. Jaki prąd popłynie przy 9 V?

<details>
<summary>Odpowiedź</summary>

$R = 30\ \Omega$, $I = 0{,}3\ \mathrm A$.
</details>

2. Drut przeciągnięto tak, że jego długość wzrosła dwukrotnie przy tej samej objętości. Jak zmienił się opór?

<details>
<summary>Odpowiedź</summary>

Długość ×2, przekrój ×½, więc opór ×4.
</details>

3. Przedłużacz o długości 10 m ma przewody miedziane o przekroju 1 mm². Jaki jest spadek napięcia i moc tracona przy prądzie 10 A?

<details>
<summary>Odpowiedź</summary>

Przewód tam i z powrotem: $R = \rho\cdot20/10^{-6} \approx 0{,}34\ \Omega$, spadek 3,4 V, strata ok. 34 W.
</details>

4. Czujnik Pt100 ma opór 100 Ω w 0°C i $\alpha = 3{,}85\cdot10^{-3}\ \mathrm{K^{-1}}$. Jaki opór ma w 100°C? Jaką temperaturę wskazuje opór 110 Ω?

<details>
<summary>Odpowiedź</summary>

138,5 Ω; ok. 26°C.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Przewodnik ma kształt ściętego stożka o długości $L$ i promieniach podstaw $a$ i $b$. Pokaż, że $R = \dfrac{\rho L}{\pi ab}$.

<details>
<summary>Odpowiedź</summary>

$r(x) = a + (b - a)x/L$, $R = \displaystyle\int_0^L\frac{\rho\,dx}{\pi r^2} = \frac{\rho L}{\pi(b - a)}\left[\frac1a - \frac1b\right] = \frac{\rho L}{\pi ab}$.
</details>

2. Prąd płynie radialnie między wewnętrzną a zewnętrzną okładziną walca (promienie $a$ i $b$, długość $L$) wypełnionego materiałem o oporze $\rho$. Oblicz opór. Gdzie to się stosuje?

<details>
<summary>Odpowiedź</summary>

$R = \displaystyle\int_a^b\frac{\rho\,dr}{2\pi rL} = \frac{\rho}{2\pi L}\ln\frac ba$. Tak liczy się upływność izolacji kabla koncentrycznego i opór uziemień.
</details>

3. Ile razy lżejszy jest przewód aluminiowy od miedzianego o tym samym oporze i długości ($\rho_{\text{Al}} = 2{,}65\cdot10^{-8}$, $d_{\text{Al}} = 2700\ \mathrm{kg/m^3}$; $\rho_{\text{Cu}} = 1{,}68\cdot10^{-8}$, $d_{\text{Cu}} = 8960\ \mathrm{kg/m^3}$)? Dlaczego linie wysokiego napięcia są aluminiowe?

<details>
<summary>Odpowiedź</summary>

Przy tym samym $R$ przekrój Al musi być 1,58 razy większy, a masa wynosi $\dfrac{2{,}65\cdot2700}{1{,}68\cdot8960} \approx 0{,}48$ masy miedzi. Linie są lżejsze i tańsze, a słupy mogą stać rzadziej.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 9 — §9.3 (opór i opór właściwy) i §9.4 (prawo Ohma).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §26.3–26.4; wyd. 1: t. 3, §27.4–27.6.
- Symulacje PhET *Prawo Ohma* i *Opór przewodu*.
