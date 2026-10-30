# 01.03 — Niepewności pomiarowe: typ A, typ B, niepewność złożona

> **Moduł:** [01 — Pomiar, jednostki i niepewności](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 1: [§1.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-6-cyfry-znaczace) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-wstep)

← [Analiza wymiarowa i szacowanie rzędu wielkości](02-analiza-wymiarowa-i-szacowanie.md) · [spis modułu](README.md) · [Wykresy, linearyzacja i dopasowanie prostej](04-wykresy-i-dopasowanie.md) →

## Po co to jest

Żaden pomiar nie jest dokładny. Wynik bez niepewności nie pozwala odpowiedzieć na najprostsze pytanie: czy zmierzone $g = 9{,}85\ \mathrm{m/s^2}$ zgadza się z wartością $9{,}81\ \mathrm{m/s^2}$, czy nie? Szacowanie niepewności jest wymagane na maturze rozszerzonej (zadania doświadczalne), na każdej pracowni fizycznej na studiach i w każdym pomiarze inżynierskim.

## Teoria w pigułce

**Błąd a niepewność.** Błąd to różnica między wynikiem a (nieznaną) wartością prawdziwą. Niepewność to liczba, która mówi, **jak bardzo nie jesteśmy pewni** wyniku — szerokość przedziału, w którym wartość prawdziwa leży z dużym prawdopodobieństwem. Wynik zapisujemy jako

$$x = \bar{x} \pm u(x)\ \ [\text{jednostka}], \qquad \text{np. } T = (2{,}002 \pm 0{,}009)\ \mathrm{s}.$$

**Rodzaje błędów.**
- **Przypadkowe** — za każdym razem inne (czas reakcji przy stoperze, drgania ręki). Widać je w rozrzucie wyników; maleją przy uśrednianiu.
- **Systematyczne** — za każdym razem takie same (źle wyzerowana waga, linijka przyłożona od złego miejsca). Uśrednianie ich nie usuwa — trzeba je znaleźć i poprawić.
- **Grube** (pomyłki) — źle zapisana liczba, pomiar „nie z tej serii”. Takie wyniki odrzucamy, uzasadniając dlaczego.

**Niepewność typu A — z serii pomiarów.** Dla $n$ wyników $x_1, \dots, x_n$:

$$\bar{x} = \frac1n\sum x_i, \qquad s = \sqrt{\frac{\sum(x_i - \bar{x})^2}{n - 1}}, \qquad u_A(\bar{x}) = \frac{s}{\sqrt{n}}.$$

$s$ opisuje rozrzut pojedynczych wyników, $u_A$ — niepewność **średniej**. Średnia z wielu pomiarów jest pewniejsza niż pojedynczy pomiar, ale tylko jak $1/\sqrt{n}$: żeby zmniejszyć niepewność dwa razy, trzeba cztery razy więcej pomiarów.

**Niepewność typu B — z innych informacji**, zwykle z dokładności przyrządu. Jeśli wiemy tylko, że wynik leży w przedziale $\pm\Delta$ (działka elementarna, klasa przyrządu, dokładność z instrukcji miernika), przyjmujemy rozkład równomierny i

$$u_B = \frac{\Delta}{\sqrt3}.$$

Na maturze zwykle wystarcza prostsze oszacowanie: niepewność równa działce elementarnej przyrządu albo oszacowana z rozrzutu wyników — treść zadania mówi, jak ją przyjąć.

**Niepewność wielkości obliczanej (złożona).** Jeśli $y = f(x_1, x_2, \dots)$, a niepewności $x_i$ są niezależne:

$$u(y) = \sqrt{\left(\frac{\partial f}{\partial x_1}u(x_1)\right)^2 + \left(\frac{\partial f}{\partial x_2}u(x_2)\right)^2 + \dots}$$

Dla iloczynów i ilorazów potęg, $y = C\,x_1^{a}x_2^{b}$, wygodniej liczyć **niepewności względne**:

$$\frac{u(y)}{y} = \sqrt{\left(a\frac{u(x_1)}{x_1}\right)^2 + \left(b\frac{u(x_2)}{x_2}\right)^2}.$$

Prostsza i ostrożniejsza wersja (szacowanie „najmniej korzystnego przypadku”) dodaje te składniki zamiast sumować w kwadratach — daje niepewność większą, ale łatwiejszą do policzenia na kartce.

**Zaokrąglanie.** Niepewność podajemy z jedną albo dwiema cyframi znaczącymi, a wynik zaokrąglamy do tego samego miejsca dziesiętnego: $9{,}8499 \pm 0{,}0869 \to (9{,}85 \pm 0{,}09)\ \mathrm{m/s^2}$.

**Zgodność wyników.** Wynik uznajemy za zgodny z wartością odniesienia, jeśli różnica nie przekracza **niepewności rozszerzonej** $U = 2u$ (przedział obejmuje wtedy ok. 95% prawdopodobieństwa).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $u_A = s/\sqrt{n}$ | niepewność średniej z $n$ pomiarów | wyniki niezależne, rozrzut przypadkowy; $n \gtrsim 5$ |
| $u_B = \Delta/\sqrt3$ | niepewność z dokładności przyrządu | znamy tylko granice $\pm\Delta$ |
| $u = \sqrt{u_A^2 + u_B^2}$ | łączenie obu typów | źródła niezależne |
| $u(x \pm y) = \sqrt{u_x^2 + u_y^2}$ | suma i różnica — niepewności **bezwzględne** | $x, y$ niezależne |
| $\dfrac{u(xy)}{xy} = \sqrt{\left(\tfrac{u_x}{x}\right)^2 + \left(\tfrac{u_y}{y}\right)^2}$ | iloczyn i iloraz — niepewności **względne** | to samo dla $x/y$ |
| $\dfrac{u(x^n)}{x^n} = \lvert n\rvert\dfrac{u_x}{x}$ | potęga | wykładnik mnoży niepewność względną |
| $\lvert x - x_{\text{ref}}\rvert \le 2u$ | wynik zgodny z odniesieniem | poziom ufności ok. 95% |

## Przykład rozwiązany

**Zadanie.** Wahadło o długości $l = (1{,}000 \pm 0{,}002)\ \mathrm{m}$. Pięć razy zmierzono stoperem czas 10 okresów: $20{,}1$; $19{,}8$; $20{,}3$; $20{,}0$; $19{,}9\ \mathrm{s}$. Wyznacz $g$ z niepewnością i sprawdź zgodność z $9{,}81\ \mathrm{m/s^2}$.

**Czas 10 okresów.** Średnia $\bar{t} = 20{,}02\ \mathrm{s}$, odchylenie standardowe $s = 0{,}19\ \mathrm{s}$, niepewność średniej $u_A = 0{,}19/\sqrt5 = 0{,}086\ \mathrm{s}$. Rozdzielczość stopera (0,01 s) jest pomijalna wobec rozrzutu, który obejmuje czas reakcji.

**Okres.** $T = \bar{t}/10 = 2{,}002\ \mathrm{s}$, $u(T) = 0{,}0086\ \mathrm{s}$ — mierząc 10 okresów naraz, dzielimy niepewność przez 10.

**Przyspieszenie.** $g = \dfrac{4\pi^2l}{T^2} = 9{,}850\ \mathrm{m/s^2}$.

**Niepewność względna** ($g \propto l^1T^{-2}$):

$$\frac{u(g)}{g} = \sqrt{\left(\frac{0{,}002}{1{,}000}\right)^2 + \left(2\cdot\frac{0{,}0086}{2{,}002}\right)^2} = \sqrt{0{,}002^2 + 0{,}0086^2} \approx 0{,}0088.$$

$u(g) = 0{,}0088\cdot9{,}85 \approx 0{,}09\ \mathrm{m/s^2}$. **Wynik:** $g = (9{,}85 \pm 0{,}09)\ \mathrm{m/s^2}$.

**Zgodność.** $\lvert9{,}85 - 9{,}81\rvert = 0{,}04 < 2\cdot0{,}09$ — wynik zgodny z wartością tablicową. Dominuje niepewność czasu (składnik 0,0086 wobec 0,002) — żeby poprawić wynik, trzeba lepiej mierzyć czas (np. więcej okresów albo czujnik), a nie długość.

### Wersja z rachunkiem różniczkowym i całkowym

Wzór na niepewność złożoną wynika z rozwinięcia $f$ w szereg Taylora do pierwszego rzędu: mała zmiana $\delta x_i$ zmienia wynik o $\delta y \approx \sum_i\dfrac{\partial f}{\partial x_i}\delta x_i$. Dla niezależnych przypadkowych $\delta x_i$ wariancje się dodają, stąd suma kwadratów.

**Zadanie.** Zasięg rzutu poziomego z wysokości $h$ z prędkością $v$: $z = v\sqrt{2h/g}$. Zmierzono $h = (1{,}20 \pm 0{,}01)\ \mathrm{m}$, $z = (1{,}50 \pm 0{,}02)\ \mathrm{m}$. Wyznacz $v = z\sqrt{g/(2h)}$ z niepewnością ($g$ traktujemy jako dokładne).

$v = 1{,}50\sqrt{9{,}81/2{,}40} \approx 3{,}03\ \mathrm{m/s}$. Pochodne cząstkowe: $\dfrac{\partial v}{\partial z} = \dfrac{v}{z}$, $\dfrac{\partial v}{\partial h} = -\dfrac{v}{2h}$, więc

$$\frac{u(v)}{v} = \sqrt{\left(\frac{0{,}02}{1{,}50}\right)^2 + \left(\frac12\cdot\frac{0{,}01}{1{,}20}\right)^2} \approx 0{,}014, \qquad v = (3{,}03 \pm 0{,}04)\ \mathrm{m/s}.$$

## Typowe pułapki

- **Za dużo cyfr.** „$g = 9{,}849894\ \mathrm{m/s^2}$” przy niepewności 0,09 udaje dokładność, której nie ma.
- **Odchylenie standardowe zamiast niepewności średniej.** $s$ to rozrzut pojedynczego pomiaru; niepewność średniej to $s/\sqrt{n}$.
- **Odejmowanie bliskich liczb.** Różnica $10{,}0 \pm 0{,}3$ i $9{,}0 \pm 0{,}4$ to $1{,}0 \pm 0{,}5$ — niepewność względna skacze z kilku do 50%. Projektuj pomiary tak, żeby tego unikać.
- **Uśrednianie błędu systematycznego.** Sto pomiarów źle wyzerowaną wagą daje bardzo pewny, ale zły wynik.
- **Niepewność względna w sumie.** Dla sumy i różnicy dodaje się niepewności bezwzględne, nie względne.
- **Brak jednostki przy niepewności.** Piszemy $(9{,}85 \pm 0{,}09)\ \mathrm{m/s^2}$ — nawias obejmuje obie liczby.

## Doświadczenie / symulacja

**Czas reakcji.** Zmierz stoperem w telefonie dziesięć razy czas spadku piłki z wysokości ok. 1 m (start w chwili puszczenia, stop przy uderzeniu). Oblicz średnią, $s$ i $u_A$. Porównaj z czasem $\sqrt{2h/g}$ i z pomiarem eksperymentem *Acoustic Stopwatch* w phyphox (start i stop na dźwięk). Która metoda ma mniejszy rozrzut i dlaczego?

**Python:** obliczenia z przykładu oraz sprawdzenie wzoru na niepewność złożoną metodą Monte Carlo — losujemy wiele możliwych wartości $l$ i $T$ zgodnie z ich niepewnościami i patrzymy na rozrzut $g$.

```python
import numpy as np

t10 = np.array([20.1, 19.8, 20.3, 20.0, 19.9])     # czas 10 okresów [s]
n = t10.size
s = t10.std(ddof=1)                                 # ddof=1 → dzielenie przez n−1
uA = s / np.sqrt(n)
T, uT = t10.mean() / 10, uA / 10
l, ul = 1.000, 0.002

g = 4 * np.pi**2 * l / T**2
ug = g * np.sqrt((ul / l)**2 + (2 * uT / T)**2)
print(f"T = {T:.4f} ± {uT:.4f} s,  g = {g:.3f} ± {ug:.3f} m/s²")

# Monte Carlo: rozrzut g przy losowych l i T
rng = np.random.default_rng(0)
l_mc = rng.normal(l, ul, 200_000)
T_mc = rng.normal(T, uT, 200_000)
g_mc = 4 * np.pi**2 * l_mc / T_mc**2
print(f"Monte Carlo: g = {g_mc.mean():.3f} ± {g_mc.std():.3f} m/s²")
print("zgodny z 9,81?", abs(g - 9.81) <= 2 * ug)
```

## Zadania

### A. Poziom maturalny

1. Długość zmierzono linijką z działką 1 mm i odczytano $23{,}4\ \mathrm{cm}$. Zapisz wynik z niepewnością równą działce elementarnej w milimetrach i podaj niepewność względną.

<details>
<summary>Odpowiedź</summary>

$(234 \pm 1)\ \mathrm{mm}$; $1/234 \approx 0{,}4\%$.
</details>

2. Pięć pomiarów czasu: $2{,}31$; $2{,}35$; $2{,}29$; $2{,}33$; $2{,}32\ \mathrm{s}$. Oblicz średnią, odchylenie standardowe i niepewność średniej.

<details>
<summary>Odpowiedź</summary>

$\bar{t} = 2{,}32\ \mathrm{s}$, $s \approx 0{,}022\ \mathrm{s}$, $u_A = 0{,}010\ \mathrm{s}$; $t = (2{,}32 \pm 0{,}01)\ \mathrm{s}$.
</details>

3. Boki prostokąta: $(20{,}0 \pm 0{,}1)\ \mathrm{cm}$ i $(10{,}0 \pm 0{,}1)\ \mathrm{cm}$. Oblicz pole z niepewnością, dodając niepewności względne (najmniej korzystny przypadek).

<details>
<summary>Odpowiedź</summary>

$0{,}5\% + 1\% = 1{,}5\%$; $P = (200 \pm 3)\ \mathrm{cm^2}$. (Sumując w kwadratach: $\pm2\ \mathrm{cm^2}$.)
</details>

4. Uczeń wyznaczył $g = (9{,}6 \pm 0{,}1)\ \mathrm{m/s^2}$. Czy wynik jest zgodny z wartością $9{,}81\ \mathrm{m/s^2}$? Co może być przyczyną?

<details>
<summary>Odpowiedź</summary>

Nie: $0{,}21 > 2\cdot0{,}1$. Prawdopodobny błąd systematyczny, np. długość wahadła zmierzona do punktu zawieszenia ciężarka zamiast do jego środka albo zbyt duża amplituda.
</details>

5. Dlaczego mierzy się czas 10 okresów, a nie jednego?

<details>
<summary>Odpowiedź</summary>

Niepewność ręcznego pomiaru czasu (czas reakcji, ok. 0,1–0,2 s) jest podobna dla jednego i dla 10 okresów, a po podzieleniu przez 10 niepewność okresu maleje dziesięciokrotnie.
</details>

### B. Poziom akademicki

1. Średnica kulki: $d = (2{,}00 \pm 0{,}02)\ \mathrm{cm}$. Oblicz objętość $V = \pi d^3/6$ z niepewnością.

<details>
<summary>Odpowiedź</summary>

Niepewność względna $3\cdot1\% = 3\%$; $V = (4{,}19 \pm 0{,}13)\ \mathrm{cm^3}$.
</details>

2. Multimetr wskazuje $12{,}47\ \mathrm{V}$; dokładność z instrukcji: $\pm(0{,}5\%\ \text{wskazania} + 2\ \text{cyfry})$, gdzie cyfra to 0,01 V. Oblicz niepewność typu B.

<details>
<summary>Odpowiedź</summary>

$\Delta = 0{,}062 + 0{,}02 \approx 0{,}082\ \mathrm{V}$, $u_B = \Delta/\sqrt3 \approx 0{,}05\ \mathrm{V}$.
</details>

3. Odchylenie standardowe pojedynczego pomiaru czasu wynosi $0{,}1\ \mathrm{s}$. Ile pomiarów trzeba wykonać, żeby niepewność średniej była mniejsza niż $0{,}02\ \mathrm{s}$?

<details>
<summary>Odpowiedź</summary>

$0{,}1/\sqrt{n} < 0{,}02 \Rightarrow n > 25$, czyli co najmniej 26.
</details>

4. Masa $m = (0{,}500 \pm 0{,}005)\ \mathrm{kg}$, prędkość $v = (4{,}0 \pm 0{,}1)\ \mathrm{m/s}$. Oblicz energię kinetyczną z niepewnością złożoną.

<details>
<summary>Odpowiedź</summary>

$E = 4{,}0\ \mathrm{J}$; $\dfrac{u(E)}{E} = \sqrt{1\%^2 + (2\cdot2{,}5\%)^2} \approx 5{,}1\%$; $E = (4{,}0 \pm 0{,}2)\ \mathrm{J}$.
</details>

5. Wyprowadź wzór na niepewność $y = \ln x$ i oblicz ją dla $x = (50 \pm 2)$.

<details>
<summary>Odpowiedź</summary>

$u(y) = \left\lvert\dfrac{dy}{dx}\right\rvert u(x) = \dfrac{u(x)}{x}$ — niepewność logarytmu to niepewność względna argumentu. $y = 3{,}91 \pm 0{,}04$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 1 — §1.6: cyfry znaczące, dokładność i precyzja pomiaru.
- CKE, [Informator o egzaminie maturalnym z fizyki](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Informatory/2024/Informator_EM2024_fizyka.pdf) — zadania doświadczalne z szacowaniem niepewności na poziomie maturalnym.
- [JCGM 100:2008 — Guide to the Expression of Uncertainty in Measurement (GUM)](https://www.bipm.org/en/doi/10.59161/jcgm100-2008e) _(po angielsku)_ — międzynarodowy standard, z którego pochodzą pojęcia niepewności typu A i B.
