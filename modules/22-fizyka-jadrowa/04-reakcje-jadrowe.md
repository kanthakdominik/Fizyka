# 22.04 — Reakcje jądrowe i zasady zachowania

> **Moduł:** [22 — Fizyka jądrowa](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10: [§10.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-4-procesy-rozpadu) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-wstep)

← [Rozpady promieniotwórcze i prawo rozpadu](03-rozpady-promieniotworcze.md) · [spis modułu](README.md) · [Rozszczepienie jąder i reaktor](05-rozszczepienie.md) →

## Po co to jest

Reakcja jądrowa zmienia jeden pierwiastek w inny, o czym marzyli alchemicy. Rutherford dokonał tego pierwszy w 1919 r., zamieniając azot w tlen. Reakcje jądrowe wytwarzają izotopy medyczne w cyklotronach i reaktorach (fluor-18 do PET, technet-99m, kobalt-60), napędzają gwiazdy i elektrownie, wytwarzają tryt i pluton. Bilans energii reakcji, wartość $Q$, to podstawowe narzędzie, jak bilans cieplny w chemii.

## Teoria w pigułce

**Reakcja jądrowa:** $a + X \to Y + b$, zapisywana też $X(a, b)Y$. Przykład Rutherforda:

$$^{14}_7\mathrm N + {}^4_2\mathrm{He} \to {}^{17}_8\mathrm O + {}^1_1\mathrm H, \qquad {}^{14}\mathrm N(\alpha, p){}^{17}\mathrm O.$$

**Prawa zachowania:**
- ładunku (suma $Z$);
- liczby nukleonów (suma $A$);
- energii (z masami spoczynkowymi) i pędu;
- momentu pędu i innych liczb kwantowych.

**Energia reakcji (wartość Q):**

$$Q = (m_a + m_X - m_Y - m_b)c^2.$$

- $Q > 0$: reakcja **egzoenergetyczna**, wydziela energię (rozpad, rozszczepienie, synteza).
- $Q < 0$: reakcja **endoenergetyczna**, wymaga dostarczenia energii kinetycznej. Z zasady zachowania pędu **energia progowa** w układzie laboratoryjnym (tarcza nieruchoma) jest większa niż $\lvert Q\rvert$:

$$E_{\text{prog}} \approx \lvert Q\rvert\left(1 + \frac{m_a}{m_X}\right) \quad\text{(nierelatywistycznie)}.$$

Część energii pocisku musi pozostać jako energia ruchu środka masy.

**Neutrony jako pociski.** Neutron nie jest odpychany przez jądro, więc nawet bardzo powolny wnika do niego. Neutrony termiczne (0,025 eV) wywołują wychwyt, $(n, \gamma)$, i rozszczepienie. Tak wytwarza się kobalt-60 i pluton-239.

**Przekrój czynny** $\sigma$ (w barnach, $1\ \mathrm b = 10^{-28}\ \mathrm{m^2}$) to efektywna „tarcza”, jaką jądro przedstawia dla danej reakcji. Liczba reakcji na sekundę: $R = \sigma\Phi N$ ($\Phi$ — strumień cząstek na m² i s, $N$ — liczba jąder tarczy). Przekroje mogą być wielokrotnie większe od geometrycznego rozmiaru jądra (ksenon-135 dla neutronów termicznych: 2,6 mln b).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum Z$, $\sum A$ zachowane | bilans reakcji | — |
| $Q = (\sum m_{\text{przed}} - \sum m_{\text{po}})c^2$ | energia reakcji | masy atomowe, gdy liczba elektronów się zgadza |
| $E_{\text{prog}} \approx \lvert Q\rvert(1 + m_a/m_X)$ | energia progowa | $Q < 0$, tarcza w spoczynku |
| $R = \sigma\Phi N$ | tempo reakcji | cienka tarcza |
| $1\ \mathrm b = 10^{-28}\ \mathrm{m^2}$ | barn | — |

## Przykład rozwiązany

**Zadanie.** Oblicz $Q$ reakcji Rutherforda $^{14}\mathrm N(\alpha, p)^{17}\mathrm O$. Masy: ¹⁴N 14,003074 u, ⁴He 4,002603 u, ¹⁷O 16,999132 u, ¹H 1,007825 u. Jaka jest energia progowa?

$Q = (14{,}003074 + 4{,}002603 - 16{,}999132 - 1{,}007825)\cdot931{,}5 \approx -1{,}19\ \mathrm{MeV}$. Reakcja jest endoenergetyczna.

$E_{\text{prog}} \approx 1{,}19(1 + 4/14) \approx 1{,}53\ \mathrm{MeV}$. Cząstki alfa z naturalnych źródeł (5–8 MeV) mają dość energii, choć odpychanie kulombowskie sprawia, że reakcja zachodzi rzadko.

## Typowe pułapki

- **Masy się zachowują.** Zachowuje się liczba nukleonów. Masa spoczynkowa zmienia się o $Q/c^2$.
- **Endoenergetyczna reakcja zachodzi przy energii $\lvert Q\rvert$.** Potrzeba więcej, energii progowej, bo produkty muszą się poruszać.
- **Zapominanie o elektronach przy masach atomowych.** Przy reakcjach z udziałem elektronów lub pozytonów trzeba je bilansować osobno.
- **Przekrój czynny = pole przekroju jądra.** To miara prawdopodobieństwa, może być znacznie większa lub mniejsza.

## Doświadczenie / symulacja

**Bilans reakcji w Pythonie.** Policz $Q$ dla reakcji wytwarzania izotopów medycznych, np. $^{18}\mathrm O(p, n)^{18}\mathrm F$ (cyklotron do PET) i $^{59}\mathrm{Co}(n, \gamma)^{60}\mathrm{Co}$ (reaktor), korzystając z mas z tabel (np. NIST).

**Symulacja PhET:** *Rozszczepienie jądra* (*Nuclear Fission*) — neutrony uderzające w jądra.

**Python:** wartość Q, energia progowa i sprawdzenie zachowania ładunku i liczby nukleonów.

```python
uc2 = 931.494
masy = {"n": (0, 1, 1.008665), "p": (1, 1, 1.007825), "α": (2, 4, 4.002603), "d": (1, 2, 2.014102),
        "N14": (7, 14, 14.003074), "O17": (8, 17, 16.999132), "Li7": (3, 7, 7.016004),
        "Be7": (4, 7, 7.016929), "O18": (8, 18, 17.999160), "F18": (9, 18, 18.000938),
        "Co59": (27, 59, 58.933194), "Co60": (27, 60, 59.933817), "γ": (0, 0, 0.0)}

def reakcja(przed, po):
    Z = sum(masy[x][0] for x in przed), sum(masy[x][0] for x in po)
    A = sum(masy[x][1] for x in przed), sum(masy[x][1] for x in po)
    assert Z[0] == Z[1] and A[0] == A[1], "niezgodny bilans Z lub A"
    Q = (sum(masy[x][2] for x in przed) - sum(masy[x][2] for x in po))*uc2
    a, X = przed
    prog = -Q*(1 + masy[a][2]/masy[X][2]) if Q < 0 else 0
    print(f"{' + '.join(przed)} → {' + '.join(po)}: Q = {Q:+.3f} MeV" + (f", próg {prog:.2f} MeV" if prog else ""))

reakcja(["α", "N14"], ["O17", "p"])
reakcja(["p", "Li7"], ["α", "α"])
reakcja(["p", "O18"], ["F18", "n"])
reakcja(["n", "Co59"], ["Co60", "γ"])
```

## Zadania

### A. Poziom maturalny

1. Uzupełnij reakcje: $^9_4\mathrm{Be} + \alpha \to {}^{12}_6\mathrm C + ?$ (odkrycie neutronu, Chadwick) i $^{27}_{13}\mathrm{Al} + \alpha \to {}^{30}_{15}\mathrm P + ?$ (sztuczna promieniotwórczość, Joliot-Curie).

<details>
<summary>Odpowiedź</summary>

W obu przypadkach neutron $^1_0n$.
</details>

2. Reakcja $^7\mathrm{Li}(p, \alpha)\alpha$ była pierwszą reakcją wywołaną w akceleratorze (Cockcroft i Walton, 1932). Oblicz $Q$ (⁷Li 7,016004 u).

<details>
<summary>Odpowiedź</summary>

$Q = (1{,}007825 + 7{,}016004 - 2\cdot4{,}002603)\cdot931{,}5 \approx 17{,}3\ \mathrm{MeV}$.
</details>

3. Dlaczego neutrony łatwiej wywołują reakcje jądrowe niż protony?

<details>
<summary>Odpowiedź</summary>

Nie mają ładunku, więc nie są odpychane przez jądro i mogą do niego wniknąć nawet przy bardzo małej energii.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź energię progową $E_{\text{prog}} = \lvert Q\rvert(1 + m_a/m_X)$ z zasady zachowania pędu (nierelatywistycznie): na progu produkty poruszają się razem z prędkością środka masy.

<details>
<summary>Odpowiedź</summary>

Prędkość środka masy $V = m_av/(m_a + m_X)$. Energia „uwięziona” w ruchu środka masy: $\tfrac12(m_a + m_X)V^2 = E\dfrac{m_a}{m_a + m_X}$. Dostępne $E\dfrac{m_X}{m_a + m_X} = \lvert Q\rvert$, więc $E = \lvert Q\rvert\dfrac{m_a + m_X}{m_X}$.
</details>

2. Folia złota o grubości 1 μm ($5{,}9\cdot10^{28}$ atomów/m³) jest naświetlana strumieniem neutronów $10^{16}\ \mathrm{m^{-2}s^{-1}}$. Przekrój czynny na wychwyt wynosi 98,7 b. Ile jąder ¹⁹⁸Au powstaje na sekundę w 1 cm² folii?

<details>
<summary>Odpowiedź</summary>

$N = 5{,}9\cdot10^{28}\cdot10^{-6}\cdot10^{-4} = 5{,}9\cdot10^{18}$, $R = \sigma\Phi N = 98{,}7\cdot10^{-28}\cdot10^{16}\cdot5{,}9\cdot10^{18} \approx 5{,}8\cdot10^8\ \mathrm{s^{-1}}$.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 11.1 — równanie reakcji syntezy jądra Cn-277 ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2024, zad. 11.2 — równanie rozpadu β⁺ (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2024, zad. 11.3 — energia kinetyczna produktów rozpadu z mas (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2025, zad. 12.2 — stosunek energii kinetycznych jądra i cząstki α (zasada zachowania pędu) ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2026, zad. 11.1 — równanie rozpadu β⁻ neonu-23 (temat pomocniczy) ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10 — §10.4: przemiany jądrowe.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5, rozdz. 42–43 (reakcje omawiane przy rozpadach i energii jądrowej).
- Symulacja PhET *Rozszczepienie jądra*.
