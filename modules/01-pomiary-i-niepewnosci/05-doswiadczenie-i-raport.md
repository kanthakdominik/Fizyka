# 01.05 — Planowanie doświadczenia i raport z pomiarów

> **Moduł:** [01 — Pomiar, jednostki i niepewności](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 1: [§1.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-7-rozwiazywanie-zadan-z-zakresu-fizyki) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-wstep)

← [Wykresy, linearyzacja i dopasowanie prostej](04-wykresy-i-dopasowanie.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Matura rozszerzona z fizyki zawiera zadania, w których trzeba **zaplanować** doświadczenie: wybrać wielkości do zmierzenia, przyrządy, sposób opracowania wyników i ocenić, co psuje dokładność. Na studiach każda pracownia kończy się sprawozdaniem. Ten temat zbiera moduł 01 w jedną procedurę, której będziesz używać w sekcjach „Doświadczenie” w całym repozytorium.

## Teoria w pigułce

**Etapy doświadczenia.**

1. **Cel i model.** Co chcemy wyznaczyć albo sprawdzić i jakie prawo (wzór) to opisuje. Przykład: wyznaczyć $g$ ze swobodnego spadku, model $h = \tfrac12gt^2$.
2. **Zmienne.**
   - *niezależna* — ustawiamy ją (wysokość $h$),
   - *zależna* — mierzymy jej odpowiedź (czas spadku $t$),
   - *kontrolowane* — trzymamy stałe (to samo ciało, bez rozpędu na starcie).
3. **Plan pomiarów.** Zakres zmiennej niezależnej (jak najszerszy), liczba punktów (zwykle 5–10), powtórzenia każdego punktu (3–5), przyrządy i ich niepewności.
4. **Linearyzacja.** Wybór osi tak, żeby model dał prostą: $h$ od $t^2$, nachylenie $g/2$.
5. **Pomiary** zapisywane od razu w tabeli, z jednostkami; surowe dane się zachowuje, także „dziwne”.
6. **Opracowanie.** Średnie i niepewności, wykres z niepewnościami, dopasowanie prostej, wynik z niepewnością.
7. **Wnioski.** Czy wynik zgadza się z wartością odniesienia lub z modelem? Co dominuje w niepewności? Jakie są możliwe błędy systematyczne i jak je zmniejszyć?

**Budżet niepewności.** Przed pomiarem warto policzyć, który składnik da największy wkład do niepewności wyniku — tam opłaca się poprawić pomiar. Jeśli $y \propto x_1^ax_2^b$, wkłady to $\lvert a\rvert\,u(x_1)/x_1$ i $\lvert b\rvert\,u(x_2)/x_2$.

**Sprawozdanie (raport)** ma stały układ:

```markdown
# Tytuł doświadczenia

## Cel
## Model i wzory
## Układ pomiarowy i przyrządy (z niepewnościami)
## Przebieg pomiarów
## Wyniki (tabela z jednostkami)
## Opracowanie (wykres, dopasowanie, obliczenie wyniku i niepewności)
## Wnioski (zgodność, dominujące źródło niepewności, błędy systematyczne, propozycje ulepszeń)
```

## Wzory i założenia

| Zasada | Uzasadnienie |
|---|---|
| szeroki zakres zmiennej niezależnej | nachylenie prostej jest wtedy wyznaczone pewniej |
| pomiar wielu okresów / wielu kartek / wielu obrotów naraz | niepewność odczytu dzieli się przez ich liczbę |
| powtórzenia pomiaru | pozwalają oszacować niepewność typu A i wykryć pomyłki |
| zmiana tylko jednej zmiennej naraz | inaczej nie wiadomo, co spowodowało efekt |
| wynik jako $(x \pm u)$ jednostka, niepewność 1–2 cyfry znaczące | standard zapisu |
| zgodność: $\lvert x - x_{\text{ref}}\rvert \le 2u$ | poziom ufności ok. 95% |

## Przykład rozwiązany

**Zadanie (planowanie, poziom maturalny).** Zaplanuj wyznaczenie przyspieszenia ziemskiego ze swobodnego spadku stalowej kulki, mając do dyspozycji telefon z aplikacją phyphox i taśmę mierniczą.

**Model.** Kulka puszczona bez prędkości początkowej: $h = \tfrac12gt^2$, więc wykres $h(t^2)$ to prosta o nachyleniu $g/2$.

**Pomiar czasu.** Eksperyment *Acoustic Stopwatch* w phyphox startuje na pierwszy głośny dźwięk i zatrzymuje się na drugi. Start: kulka uderza w krawędź stołu albo puszczamy ją z klaśnięciem przy uchwycie; stop: uderzenie o podłogę. Telefon kładziemy w połowie drogi między źródłami dźwięku, żeby opóźnienia dojścia dźwięku (ok. 3 ms na metr) się znosiły.

**Plan.** Wysokości $h$ od 0,5 m do 2,0 m co 0,25 m (7 punktów), dla każdej 5 powtórzeń. Niepewność wysokości: ok. 0,5 cm (taśma, położenie środka kulki).

**Opracowanie.** Dla każdej wysokości średni czas i $u_A$; tabela $h$, $t^2$; wykres $h(t^2)$; prosta najmniejszych kwadratów; $g = 2a$, $u(g) = 2u(a)$.

**Budżet niepewności dla jednego punktu** ($h = 1{,}000\ \mathrm{m}$, $t = 0{,}452\ \mathrm{s}$, $u(h) = 0{,}005\ \mathrm{m}$, $u(t) = 0{,}005\ \mathrm{s}$): $g = 2h/t^2 = 9{,}79\ \mathrm{m/s^2}$, wkład wysokości $0{,}5\%$, wkład czasu $2\cdot1{,}1\% = 2{,}2\%$. Łącznie ok. $2{,}3\%$, czyli $u(g) \approx 0{,}22\ \mathrm{m/s^2}$ — dominuje czas. Wniosek: opłaca się poprawić pomiar czasu (więcej powtórzeń, większe wysokości), a nie dokładniej mierzyć wysokość.

**Możliwe błędy systematyczne.** Opór powietrza (dla stalowej kulki mały), opóźnienie startu przy ręcznym puszczaniu, czas dojścia dźwięku, wysokość mierzona od złego punktu kulki. Ostatni błąd przesuwa wykres — dlatego dopasowujemy prostą z wyrazem wolnym, a $g$ bierzemy z nachylenia.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Okres wahadła mierzymy stoperem, czas reakcji wprowadza niepewność $u_r = 0{,}1\ \mathrm{s}$ na każdy pomiar czasu niezależnie od jego długości. Okres wynosi ok. 2 s. Ile okresów $N$ trzeba mierzyć naraz, żeby niepewność względna okresu była poniżej 0,1%?

$u(T) = u_r/N$, więc $\dfrac{u(T)}{T} = \dfrac{u_r}{NT} < 0{,}001 \Rightarrow N > \dfrac{0{,}1}{0{,}001\cdot2} = 50$.

Przy 50 okresach (ok. 100 s) zaczyna jednak działać tłumienie: amplituda maleje, a dla dużych amplitud okres zależy od amplitudy (temat 00.06). Plan doświadczenia to zawsze kompromis między składnikami niepewności.

## Typowe pułapki

- **Zmienianie kilku rzeczy naraz.** Inna kulka i inna wysokość w jednym pomiarze — nie da się rozdzielić efektów.
- **Za wąski zakres.** Pięć wysokości między 1,00 a 1,10 m daje bardzo niepewne nachylenie.
- **Wynik bez niepewności i bez porównania.** Sam „$g = 9{,}7$” nic nie mówi o jakości pomiaru.
- **Wnioski ogólnikowe.** „Błędy wynikały z niedokładności przyrządów” — to nie jest wniosek. Wskaż, który składnik dominuje i jak go zmniejszyć.
- **Poprawianie danych.** Wynik odrzucamy tylko z konkretnym powodem (np. zauważony błąd startu), nie dlatego, że „nie pasuje”.

## Doświadczenie / symulacja

**Wykonaj doświadczenie z przykładu** i napisz pełne sprawozdanie według szablonu z teorii. To jest też projekt modułowy (patrz [README modułu](README.md)).

**Python:** symulacja doświadczenia **przed** pomiarem. Losujemy wyniki z zakładanymi niepewnościami i sprawdzamy, jakiej niepewności $g$ możemy się spodziewać przy danym planie — i jak zmieni się, gdy zmienimy zakres wysokości.

```python
import numpy as np

rng = np.random.default_rng(3)
g_true = 9.81

def simulate(heights, n_rep=5, u_h=0.005, u_t=0.005, n_exp=2000):
    """Zwraca rozrzut wyznaczonego g przy danym planie pomiarów."""
    results = []
    for _ in range(n_exp):
        h_meas = heights + rng.normal(0, u_h, heights.size)
        t_true = np.sqrt(2 * heights / g_true)
        t_mean = (t_true[:, None] + rng.normal(0, u_t, (heights.size, n_rep))).mean(axis=1)
        a, b = np.polyfit(t_mean**2, h_meas, 1)
        results.append(2 * a)
    results = np.array(results)
    return results.mean(), results.std()

for label, h in [("0,5–2,0 m, 7 punktów", np.linspace(0.5, 2.0, 7)),
                 ("1,0–1,2 m, 7 punktów", np.linspace(1.0, 1.2, 7))]:
    m, s = simulate(h)
    print(f"{label}: oczekiwane g = {m:.3f} ± {s:.3f} m/s²")
```

## Zadania

### A. Poziom maturalny

1. Zaplanuj doświadczenie sprawdzające, jak okres drgań ciężarka na sprężynie zależy od jego masy. Podaj zmienną niezależną, zależną i kontrolowane, potrzebne przyrządy oraz wykres, który narysujesz.

<details>
<summary>Odpowiedź</summary>

Niezależna: masa $m$; zależna: okres $T$ (mierzony jako czas np. 10 drgań); kontrolowane: ta sama sprężyna, mała amplituda. Przyrządy: waga, stoper (lub phyphox). Wykres $T^2(m)$ — prosta o nachyleniu $4\pi^2/k$.
</details>

2. Uczeń wyznaczał $g$, mierząc czas spadku kartki papieru z wysokości 2 m, i otrzymał $3{,}5\ \mathrm{m/s^2}$. Wskaż przyczynę i zaproponuj poprawkę.

<details>
<summary>Odpowiedź</summary>

Opór powietrza — model swobodnego spadku nie obowiązuje. Użyć ciała o dużej gęstości i małym przekroju (stalowa kulka) albo zgniecionej w kulkę kartki dla porównania.
</details>

3. Dlaczego przy wyznaczaniu oporu opornika lepiej narysować wykres $U(I)$ dla kilku napięć i dopasować prostą, niż obliczyć średnią z ilorazów $U/I$?

<details>
<summary>Odpowiedź</summary>

Dopasowanie pokazuje, czy zależność jest rzeczywiście liniowa, a wyraz wolny ujawnia błąd systematyczny (np. przesunięte zero miernika), który w średniej ilorazów byłby niewidoczny.
</details>

4. Jakie elementy powinny się znaleźć we wnioskach ze sprawozdania?

<details>
<summary>Odpowiedź</summary>

Wynik z niepewnością; porównanie z wartością odniesienia (zgodny/niezgodny i dlaczego); który składnik dominuje w niepewności; możliwe błędy systematyczne; konkretne propozycje ulepszenia pomiaru.
</details>

### B. Poziom akademicki

1. W swobodnym spadku z $h = (1{,}000 \pm 0{,}005)\ \mathrm{m}$ zmierzono $t = (0{,}452 \pm 0{,}005)\ \mathrm{s}$. Oblicz $g$ z niepewnością i wskaż dominujący składnik.

<details>
<summary>Odpowiedź</summary>

$g = 9{,}79\ \mathrm{m/s^2}$; wkłady $0{,}5\%$ (wysokość) i $2{,}2\%$ (czas); $g = (9{,}8 \pm 0{,}2)\ \mathrm{m/s^2}$, dominuje czas.
</details>

2. W doświadczeniu z poprzedniego zadania czas mierzy się dźwiękiem, a telefon leży przy miejscu upadku, 1 m od miejsca startu. O ile i w którą stronę zmienia to zmierzony czas i wynik $g$? (Prędkość dźwięku 343 m/s.)

<details>
<summary>Odpowiedź</summary>

Sygnał startu dociera z opóźnieniem ok. 2,9 ms, a stopu — praktycznie od razu, więc zmierzony czas jest krótszy o ok. 2,9 ms. Dla $t = 0{,}452\ \mathrm{s}$ to $0{,}65\%$, a $g \propto t^{-2}$ rośnie o ok. 1,3% (ok. $0{,}13\ \mathrm{m/s^2}$) — błąd systematyczny porównywalny z niepewnością.
</details>

3. Masz do wyboru: zmierzyć czas spadku z jednej wysokości 50 razy albo z 10 wysokości po 5 razy. Która strategia jest lepsza i dlaczego?

<details>
<summary>Odpowiedź</summary>

Z 10 wysokości: przy podobnej liczbie pomiarów pozwala sprawdzić model (liniowość $h(t^2)$) i oddzielić błędy systematyczne stałe (wyraz wolny prostej) od nachylenia. Jedna wysokość daje mniejszą niepewność przypadkową, ale nie ujawnia błędu systematycznego.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 1 — §1.7: rozwiązywanie zadań i sprawdzanie sensowności wyników.
- CKE, [Informator o egzaminie maturalnym z fizyki](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Informatory/2024/Informator_EM2024_fizyka.pdf) — przykładowe zadania z planowania doświadczeń i opracowania wyników.
- [phyphox](https://phyphox.org/) — opisy eksperymentów i eksport danych z telefonu.
