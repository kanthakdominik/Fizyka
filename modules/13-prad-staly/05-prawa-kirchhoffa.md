# 13.05 — Prawa Kirchhoffa i mierniki

> **Moduł:** [13 — Prąd stały](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 10: [§10.3–10.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/10-3-prawa-kirchhoffa) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §27.2–27.3 (s. 222)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §28.6–28.7, s. 164 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [SEM, opór wewnętrzny, łączenie oporników](04-sem-i-laczenie-opornikow.md) · [spis modułu](README.md) · [Obwody RC — ładowanie i rozładowanie](06-obwody-rc.md) →

## Po co to jest

Nie każdy obwód da się sprowadzić do połączeń szeregowych i równoległych. Gdy jest w nim kilka źródeł albo mostek, potrzebne są prawa Kirchhoffa. To dwie zasady zachowania: ładunku i energii. Z nich wynika układ równań liniowych, który rozwiązuje się ręcznie lub komputerowo. Tak samo działają programy symulujące obwody (SPICE). Mierniki elektryczne to w gruncie rzeczy oporniki w obwodzie i trzeba wiedzieć, jak je podłączać, żeby nie zafałszowały pomiaru.

## Teoria w pigułce

**I prawo Kirchhoffa (węzłów)** wynika z zasady zachowania ładunku. Suma prądów wpływających do węzła równa się sumie prądów wypływających:

$$\sum I_{\text{wpł}} = \sum I_{\text{wypł}}.$$

**II prawo Kirchhoffa (oczek)** wynika z zasady zachowania energii: potencjał jest jednoznaczną funkcją położenia (12.05). Suma zmian potencjału wzdłuż zamkniętego oczka wynosi zero:

$$\sum\varepsilon_i - \sum I_jR_j = 0.$$

**Przepis:**
1. Oznacz prądy w każdej gałęzi i wybierz ich zwroty dowolnie.
2. Zapisz prawo węzłów dla wszystkich węzłów oprócz jednego.
3. Zapisz prawo oczek dla niezależnych oczek. Przechodząc w wybranym kierunku obiegu:
   - opornik **zgodnie** z założonym prądem: $-IR$, przeciwnie: $+IR$;
   - źródło od $-$ do $+$: $+\varepsilon$, od $+$ do $-$: $-\varepsilon$.
4. Rozwiąż układ. Ujemny wynik oznacza, że prąd płynie przeciwnie do założonego. Wynik nadal jest poprawny.

**Mierniki:**
- **Amperomierz** włącza się **szeregowo**. Musi mieć bardzo mały opór, żeby nie zmieniać prądu. Galwanometr przerabia się na amperomierz, dołączając równolegle mały opornik (**bocznik**).
- **Woltomierz** włącza się **równolegle**. Musi mieć bardzo duży opór, żeby nie pobierać prądu. Galwanometr przerabia się na woltomierz, dołączając szeregowo duży opór (**posobnik**).
- Amperomierz podłączony równolegle do źródła to zwarcie, a często spalony bezpiecznik miernika.

**Mostek Wheatstone'a** to cztery oporniki w romb, z galwanometrem na przekątnej. Prąd przez galwanometr nie płynie, gdy $\dfrac{R_1}{R_2} = \dfrac{R_3}{R_4}$. Tak mierzy się nieznany opór z dużą dokładnością. Na mostkach działają też tensometry i wagi elektroniczne.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum I_{\text{wpł}} = \sum I_{\text{wypł}}$ | I prawo Kirchhoffa | każdy węzeł, stan ustalony |
| $\sum\varepsilon - \sum IR = 0$ | II prawo Kirchhoffa | każde oczko |
| $R_b = \dfrac{I_gR_g}{I - I_g}$ | bocznik amperomierza | zakres $I$, galwanometr $I_g$, $R_g$ |
| $R_s = U/I_g - R_g$ | posobnik woltomierza | zakres $U$ |
| $R_1/R_2 = R_3/R_4$ | równowaga mostka | brak prądu w przekątnej |

## Przykład rozwiązany

**Zadanie.** Dwa źródła i trzy oporniki są połączone między węzłami A i B w trzech gałęziach równoległych:
- gałąź 1: $\varepsilon_1 = 12\ \mathrm V$ i $R_1 = 2\ \Omega$;
- gałąź 2: $\varepsilon_2 = 6\ \mathrm V$ i $R_2 = 4\ \Omega$;
- gałąź 3: sam $R_3 = 6\ \Omega$.

Oba źródła mają biegun dodatni po stronie węzła A. Oblicz prądy.

Zakładamy prądy $I_1$, $I_2$ płynące przez źródła do węzła A i $I_3$ płynący z A przez $R_3$ do B.

- Węzeł A: $I_1 + I_2 = I_3$.
- Oczko 1–3: $12 - 2I_1 - 6I_3 = 0$.
- Oczko 2–3: $6 - 4I_2 - 6I_3 = 0$.

Rozwiązanie: $I_1 \approx 1{,}91\ \mathrm A$, $I_2 \approx -0{,}55\ \mathrm A$, $I_3 \approx 1{,}36\ \mathrm A$.

Ujemne $I_2$ oznacza, że przez źródło 6 V prąd płynie od plusa do minusa: silniejsze źródło je ładuje. Sprawdzenie: $U_{AB} = I_3R_3 \approx 8{,}18\ \mathrm V = 12 - 1{,}91\cdot2 = 6 + 0{,}55\cdot4$.

## Typowe pułapki

- **Zmiana założonych zwrotów w trakcie.** Raz założony zwrot prądu obowiązuje we wszystkich równaniach.
- **Znak przy źródle zależy od prądu.** Znak $\varepsilon$ zależy tylko od kierunku obiegu (od $-$ do $+$ to $+\varepsilon$), a znak $IR$ od zwrotu prądu względem obiegu.
- **Za dużo równań węzłów.** Dla $n$ węzłów niezależnych równań jest $n - 1$.
- **Amperomierz równolegle, woltomierz szeregowo.** Odwrotnie. Amperomierz równolegle do odbiornika zwiera go.
- **Ujemny wynik jest błędem.** Oznacza tylko przeciwny zwrot prądu.

## Doświadczenie / symulacja

**Sprawdzenie praw Kirchhoffa.** Zbuduj na płytce stykowej obwód z dwiema bateriami i trzema opornikami jak w przykładzie (np. 9 V i 4,5 V, oporniki 100–1000 Ω). Zmierz prądy i napięcia i sprawdź oba prawa. Porównaj z rozwiązaniem z Pythona.

**Mostek z potencjometrem.** Zbuduj mostek Wheatstone'a z potencjometrem jako dwoma ramionami i miernikiem w przekątnej. Znajdź równowagę i wyznacz nieznany opór.

**Symulacja PhET:** *Zestaw do budowy obwodów DC* — zbuduj obwód z dwoma źródłami i sprawdź prawa Kirchhoffa wirtualnymi miernikami.

**Python:** rozwiązanie układu równań Kirchhoffa macierzowo i mostek Wheatstone'a.

```python
import numpy as np

# przykład: niewiadome I1, I2, I3
A = np.array([[1, 1, -1],          # węzeł A
              [2, 0, 6],           # oczko 1–3: 2 I1 + 6 I3 = 12
              [0, 4, 6]])          # oczko 2–3: 4 I2 + 6 I3 = 6
b = np.array([0, 12, 6])
I1, I2, I3 = np.linalg.solve(A, b)
print(f"I1 = {I1:.3f} A, I2 = {I2:.3f} A, I3 = {I3:.3f} A, U_AB = {I3*6:.3f} V")

# mostek Wheatstone'a: potencjały węzłów (metoda węzłowa), źródło U między górą a dołem
def mostek(R1, R2, R3, R4, Rg, U=10.0):
    # węzły: a (między R1 i R2), b (między R3 i R4); góra = U, dół = 0
    G = np.array([[1/R1 + 1/R2 + 1/Rg, -1/Rg],
                  [-1/Rg, 1/R3 + 1/R4 + 1/Rg]])
    J = np.array([U/R1, U/R3])
    Va, Vb = np.linalg.solve(G, J)
    return (Va - Vb)/Rg
for R4 in (180, 200, 220):
    print(f"R4 = {R4} Ω: prąd galwanometru = {mostek(100, 100, 200, R4, 50)*1e3:+.3f} mA")
```

## Zadania

### A. Poziom maturalny

1. Do węzła wpływają prądy 3 A i 2 A, a wypływa prąd 4 A i nieznany prąd $I$. Oblicz $I$.

<details>
<summary>Odpowiedź</summary>

$I = 1\ \mathrm A$ (wypływający).
</details>

2. Galwanometr ma opór 50 Ω i pełne wychylenie przy 1 mA. Jak zrobić z niego amperomierz o zakresie 1 A i woltomierz o zakresie 10 V?

<details>
<summary>Odpowiedź</summary>

Bocznik równolegle: $R_b = \dfrac{0{,}001\cdot50}{0{,}999} \approx 0{,}050\ \Omega$. Posobnik szeregowo: $R_s = 10/0{,}001 - 50 = 9950\ \Omega$.
</details>

3. Mostek Wheatstone'a jest w równowadze przy $R_1 = 100\ \Omega$, $R_2 = 150\ \Omega$, $R_3 = 200\ \Omega$. Ile wynosi $R_4$?

<details>
<summary>Odpowiedź</summary>

$R_4 = R_2R_3/R_1 = 300\ \Omega$.
</details>

4. Woltomierz o oporze 10 kΩ mierzy napięcie na oporniku 10 kΩ w dzielniku z dwóch oporników 10 kΩ zasilanym 12 V. Co pokaże? Jaki wniosek dla pomiarów?

<details>
<summary>Odpowiedź</summary>

Równolegle z woltomierzem dolna część ma 5 kΩ, więc pokaże $12\cdot5/15 = 4\ \mathrm V$ zamiast 6 V. Opór woltomierza musi być dużo większy od oporów w obwodzie.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. W przykładzie zastąp $\varepsilon_2$ źródłem o nieznanej SEM. Przy jakiej wartości przez to źródło nie płynie prąd?

<details>
<summary>Odpowiedź</summary>

$I_2 = 0$: wtedy $I_1 = I_3 = 12/8 = 1{,}5\ \mathrm A$, a $\varepsilon_2 = U_{AB} = 6\cdot1{,}5 = 9\ \mathrm V$. Na tej zasadzie działa kompensacyjny pomiar SEM.
</details>

2. Pokaż, że II prawo Kirchhoffa wynika z $\oint\vec E\cdot d\vec l = 0$ dla pola elektrostatycznego. Kiedy przestaje obowiązywać?

<details>
<summary>Odpowiedź</summary>

Suma spadków napięć to całka z $\vec E$ po zamkniętej drodze, a dla pola zachowawczego wynosi zero. Przy zmiennym strumieniu magnetycznym pole elektryczne nie jest zachowawcze (indukcja, 15) i trzeba dopisać SEM indukcji.
</details>

3. Sześcian z 12 oporników po $R$. Oblicz opór między przeciwległymi wierzchołkami, korzystając z symetrii.

<details>
<summary>Odpowiedź</summary>

Z symetrii prąd $I$ dzieli się na 3, potem każda część na 2 (6 krawędzi po $I/6$), potem łączy w 3. Spadek: $\dfrac I3R + \dfrac I6R + \dfrac I3R = \dfrac56IR$, więc $R_{\text{ekw}} = \tfrac56R$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 10 — §10.3 (prawa Kirchhoffa) i §10.4 (mierniki elektryczne).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §27.2–27.3; wyd. 1: t. 3, §28.6–28.7.
- Symulacja PhET *Zestaw do budowy obwodów DC*.
