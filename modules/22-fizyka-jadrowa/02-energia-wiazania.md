# 22.02 — Energia wiązania i deficyt masy

> **Moduł:** [22 — Fizyka jądrowa](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10: [§10.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-2-energia-wiazania-jadra) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §42.2 (s. 167)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§43.2, s. 137](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=153) — PDF z serwera AGH

← [Budowa jądra atomowego i izotopy](01-budowa-jadra.md) · [spis modułu](README.md) · [Rozpady promieniotwórcze i prawo rozpadu](03-rozpady-promieniotworcze.md) →

## Po co to jest

Jądro waży mniej niż osobno wzięte protony i neutrony, z których się składa. Brakująca masa to energia wiązania podzielona przez $c^2$ (19.05). Wykres energii wiązania na nukleon w funkcji liczby masowej to najważniejszy wykres fizyki jądrowej: z niego wynika, dlaczego energię daje zarówno rozszczepienie ciężkich jąder (elektrownie jądrowe), jak i synteza lekkich (Słońce, bomba wodorowa, ITER) i dlaczego żelazo jest „popiołem” gwiazd.

## Teoria w pigułce

**Defekt masy.** Masa jądra jest mniejsza od sumy mas nukleonów:

$$\Delta m = Zm_p + Nm_n - m_{\text{jądra}}.$$

**Energia wiązania** to energia potrzebna do rozbicia jądra na swobodne nukleony:

$$E_w = \Delta m\,c^2.$$

W praktyce używa się mas **atomów** (tak są podawane w tablicach), a zamiast masy protonu masy atomu wodoru ¹H. Masy elektronów się wtedy znoszą:

$$E_w = [Zm(^1\mathrm H) + Nm_n - m(^A\mathrm X)]\cdot931{,}5\ \mathrm{MeV/u}.$$

**Energia wiązania na nukleon** $E_w/A$:
- rośnie szybko dla lekkich jąder (deuter 1,1 MeV, ⁴He 7,1 MeV, ze szczególnie silnie związanym ⁴He);
- osiąga maksimum ok. 8,8 MeV przy żelazie i niklu ($A \approx 56$–62);
- powoli maleje dla ciężkich (uran ok. 7,6 MeV).

**Wnioski z wykresu:**
- **rozszczepienie** ciężkiego jądra na dwa średnie podnosi energię wiązania na nukleon o ok. 0,9 MeV, co daje ok. 200 MeV na rozszczepienie (22.05);
- **synteza** lekkich jąder w cięższe daje jeszcze więcej na nukleon (22.06);
- jądra w pobliżu żelaza nie dają energii ani przy rozszczepieniu, ani przy syntezie. Gwiazdy kończą wytwarzanie energii na żelazie, a cięższe pierwiastki powstają w wybuchach supernowych i zderzeniach gwiazd neutronowych.

**Model kroplowy.** Przebieg krzywej dobrze opisuje model jądra jako kropli cieczy (wzór Weizsäckera): energia objętościowa $\propto A$, poprawka powierzchniowa $\propto A^{2/3}$, odpychanie kulombowskie $\propto Z^2/A^{1/3}$, człon asymetrii $\propto (N - Z)^2/A$ i człon parowania. Do tego dochodzą efekty powłokowe: jądra z „magiczną” liczbą protonów lub neutronów (2, 8, 20, 28, 50, 82, 126) są szczególnie trwałe.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Delta m = Zm_p + Nm_n - m_j$ | defekt masy | — |
| $E_w = \Delta mc^2$ | energia wiązania | — |
| $E_w = [Zm(^1\mathrm H) + Nm_n - m_{\text{atom}}]\cdot931{,}5\ \mathrm{MeV/u}$ | z mas atomowych | elektrony się znoszą |
| $m(^1\mathrm H) = 1{,}007825\ \mathrm u$, $m_n = 1{,}008665\ \mathrm u$ | masy | — |

## Przykład rozwiązany

**Zadanie.** Oblicz energię wiązania i energię wiązania na nukleon dla ⁴He (4,002603 u), ⁵⁶Fe (55,934936 u) i ²³⁸U (238,050788 u).

⁴He: $\Delta m = 2\cdot1{,}007825 + 2\cdot1{,}008665 - 4{,}002603 = 0{,}030377\ \mathrm u$, $E_w \approx 28{,}3\ \mathrm{MeV}$, czyli $7{,}07\ \mathrm{MeV}$ na nukleon.

⁵⁶Fe: $\Delta m \approx 0{,}5285\ \mathrm u$, $E_w \approx 492\ \mathrm{MeV}$, $8{,}79\ \mathrm{MeV}$ na nukleon.

²³⁸U: $\Delta m \approx 1{,}934\ \mathrm u$, $E_w \approx 1802\ \mathrm{MeV}$, $7{,}57\ \mathrm{MeV}$ na nukleon.

Defekt masy helu to 0,76% masy, a w reakcjach chemicznych to rzędu $10^{-9}$ masy.

## Typowe pułapki

- **Energia wiązania jest zawarta w jądrze.** To energia, którą trzeba **dostarczyć**, żeby jądro rozbić. Przy powstawaniu jądra została ona wydzielona.
- **Mieszanie mas jąder i atomów.** Licząc z mas atomowych, użyj masy atomu wodoru zamiast protonu.
- **Większa energia wiązania = większa energia jądra.** Jądro silniej związane ma **niższą** energię (mniejszą masę).
- **Uran ma najwięcej energii wiązania, więc jest najtrwalszy.** Liczy się energia na nukleon. Ta jest największa przy żelazie.

## Doświadczenie / symulacja

**Krzywa energii wiązania z danych.** Pobierz masy atomowe izotopów (np. z tabeli AME, Atomic Mass Evaluation) i narysuj $E_w/A$ od $A$ dla wszystkich stabilnych jąder. Zaznacz ⁴He, ⁵⁶Fe, ²³⁵U i porównaj z modelem kroplowym (kod niżej).

**Python:** energia wiązania z mas atomowych i krzywa modelu kroplowego (wzór Weizsäckera).

```python
import numpy as np
import matplotlib.pyplot as plt

mH, mn, uc2 = 1.007825, 1.008665, 931.494
masy = {"²H": (1, 2, 2.014102), "⁴He": (2, 4, 4.002603), "⁷Li": (3, 7, 7.016004), "¹²C": (6, 12, 12.0),
        "¹⁶O": (8, 16, 15.994915), "⁵⁶Fe": (26, 56, 55.934936), "²³⁵U": (92, 235, 235.043930), "²³⁸U": (92, 238, 238.050788)}
for nazwa, (Z, A, m) in masy.items():
    Ew = (Z*mH + (A - Z)*mn - m)*uc2
    print(f"{nazwa:5s}: E_w = {Ew:8.2f} MeV, E_w/A = {Ew/A:.3f} MeV")

def weizsacker(Z, A):                               # współczynniki w MeV
    aV, aS, aC, aA, aP = 15.75, 17.8, 0.711, 23.7, 11.18
    d = 0 if A % 2 else (aP/np.sqrt(A) if Z % 2 == 0 else -aP/np.sqrt(A))
    return aV*A - aS*A**(2/3) - aC*Z*(Z - 1)/A**(1/3) - aA*(A - 2*Z)**2/A + d

A = np.arange(10, 250)
Zs = np.round(A/(1.98 + 0.0155*A**(2/3)))           # przybliżona ścieżka stabilności
plt.plot(A, [weizsacker(z, a)/a for z, a in zip(Zs, A)], label="model kroplowy")
for nazwa, (Z, Am, m) in masy.items():
    plt.plot(Am, (Z*mH + (Am - Z)*mn - m)*uc2/Am, "o")
    plt.annotate(nazwa, (Am, (Z*mH + (Am - Z)*mn - m)*uc2/Am))
plt.xlabel("A"); plt.ylabel("E_w / A [MeV]"); plt.ylim(0, 9.5); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Oblicz energię wiązania deuteru (²H, 2,014102 u). Jakiej energii fotonu potrzeba, żeby rozbić deuter na proton i neutron?

<details>
<summary>Odpowiedź</summary>

$\Delta m = 1{,}007825 + 1{,}008665 - 2{,}014102 = 0{,}002388\ \mathrm u$, $E_w \approx 2{,}22\ \mathrm{MeV}$. Foton musi mieć co najmniej 2,22 MeV.
</details>

2. Które jądro jest silniej związane (na nukleon): ¹²C czy ¹⁶O?

<details>
<summary>Odpowiedź</summary>

¹⁶O: 7,98 MeV wobec 7,68 MeV dla ¹²C.
</details>

3. Dlaczego energię można uzyskać zarówno z rozszczepienia uranu, jak i z syntezy wodoru?

<details>
<summary>Odpowiedź</summary>

W obu procesach powstają jądra silniej związane (o większej $E_w/A$), bliższe maksimum krzywej przy żelazie. Różnica energii wiązania się wydziela.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Oszacuj z krzywej energii wiązania energię wydzieloną przy rozszczepieniu ²³⁵U na dwa jądra o $A \approx 117$ (ok. 8,5 MeV na nukleon).

<details>
<summary>Odpowiedź</summary>

$235\cdot(8{,}5 - 7{,}6) \approx 210\ \mathrm{MeV}$.
</details>

2. W modelu kroplowym znajdź, przy jakim $Z$ (dla danego $A$) energia wiązania jest największa (pomijając człon parowania). Sprawdź dla $A = 56$ i $A = 238$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{\partial E_w}{\partial Z} = 0$ z członami kulombowskim i asymetrii: $Z = \dfrac{A/2}{1 + a_CA^{2/3}/(4a_A)}$. Dla $A = 56$: $Z \approx 25$ (żelazo ma 26). Dla $A = 238$: $Z \approx 92$ (uran).
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 11.3 — energia potrzebna do rozbicia jądra na nukleony (energia wiązania) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2024, zad. 11.3 — energia kinetyczna produktów rozpadu z mas ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2026, zad. 11.2 — masa jądra a suma mas produktów rozpadu ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10 — §10.2: energia wiązania jądra.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §42.2; wyd. 1: t. 5, §43.2.
