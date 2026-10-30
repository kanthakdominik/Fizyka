# 14.03 — Efekt Halla, spektrometr masowy, cyklotron

> **Moduł:** [14 — Pole magnetyczne](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 11: [§11.6–11.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/11-6-efekt-halla) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/11-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §28.3 (s. 260), §28.5 (s. 269)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §29.3–29.4, s. 190, §29.6, s. 200 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Siła elektrodynamiczna i moment sił na ramkę z prądem](02-sila-elektrodynamiczna.md) · [spis modułu](README.md) · [Prawo Biota–Savarta](04-prawo-biota-savarta.md) →

## Po co to jest

Siła Lorentza ma trzy wielkie zastosowania pomiarowe i technologiczne.
- **Efekt Halla** pozwala zmierzyć pole magnetyczne. Hallotrony siedzą w kompasach telefonów, czujnikach ABS, klawiaturach i silnikach bezszczotkowych. Pokazuje też znak nośników prądu w materiale, co pozwoliło odkryć „dziury” w półprzewodnikach.
- **Spektrometr masowy** rozdziela jony według masy. Tak bada się izotopy, datuje próbki, wykrywa doping i analizuje białka.
- **Cyklotron** przyspiesza cząstki do energii dziesiątek MeV. Działa w szpitalach (protonoterapia, izotopy do PET) i laboratoriach, m.in. w krakowskim Centrum Cyklotronowym Bronowice.

## Teoria w pigułce

**Efekt Halla.** W płytce o grubości $t$ (w kierunku pola) płynie prąd $I$ prostopadły do pola $\vec B$. Siła Lorentza spycha nośniki na jeden bok płytki i powstaje poprzeczne pole elektryczne $E_H$. W stanie ustalonym równoważy ono siłę magnetyczną: $qE_H = qv_dB$. Z $I = nqv_dA$ (13.01) i szerokości płytki $w$ ($A = wt$):

$$U_H = E_Hw = \frac{IB}{nqt}.$$

- Znak napięcia Halla zależy od znaku nośników. W metalach to elektrony, w półprzewodnikach typu p dziury, czyli nośniki dodatnie (23).
- Napięcie jest odwrotnie proporcjonalne do $n$. W metalach ($n \sim 10^{29}\ \mathrm{m^{-3}}$) wynosi mikrowolty, w półprzewodnikach ($n \sim 10^{21}$–$10^{23}\ \mathrm{m^{-3}}$) miliwolty. Dlatego czujniki Halla robi się z półprzewodników.

**Spektrometr masowy (typu Bainbridge'a):**
1. Jony przechodzą przez selektor prędkości ($v = E/B_1$, 14.01).
2. Wpadają w pole $B_2$ i zataczają półokrąg o promieniu $r = mv/(qB_2)$.
3. Uderzają w detektor w odległości $2r$ od wlotu.

Stąd $m = qB_2r/v$, czyli położenie na detektorze mierzy masę. Wariant z przyspieszaniem napięciem $U$ zamiast selektora: $r = \dfrac1B\sqrt{\dfrac{2mU}{q}}$.

**Cyklotron.** Dwie metalowe „duanty” w kształcie litery D są w jednorodnym polu $B$, a między nimi przyłożone jest zmienne napięcie $U$. Cząstka zatacza półokręgi. Przy każdym przejściu szczeliny zyskuje energię $qU$. Okres obiegu nie zależy od prędkości (14.01), więc napięcie o stałej częstotliwości $f = \dfrac{qB}{2\pi m}$ jest zawsze w fazie. Największą energię wyznacza promień urządzenia $R$:

$$E_{k,\max} = \frac{q^2B^2R^2}{2m}.$$

Przy prędkościach relatywistycznych masa efektywna rośnie i częstotliwość trzeba zmieniać (synchrocyklotron, synchrotron, 19).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U_H = IB/(nqt)$ | napięcie Halla | jeden rodzaj nośników |
| $r = mv/(qB)$ | promień toru jonu | $\vec v \perp \vec B$ |
| $m = qBr/v$ | masa ze spektrometru | znane $v$ (selektor) |
| $f = qB/(2\pi m)$ | częstotliwość cyklotronu | $v \ll c$ |
| $E_{k,\max} = q^2B^2R^2/(2m)$ | energia końcowa | $v \ll c$ |

## Przykład rozwiązany

**Zadanie 1.** Przez pasek miedzi o grubości 0,1 mm płynie prąd 10 A w polu 1 T ($n = 8{,}5\cdot10^{28}\ \mathrm{m^{-3}}$). Oblicz napięcie Halla. Porównaj z czujnikiem półprzewodnikowym: $n = 10^{21}\ \mathrm{m^{-3}}$, grubość 0,5 mm, prąd 1 mA, pole 0,1 T.

Miedź: $U_H = \dfrac{10\cdot1}{8{,}5\cdot10^{28}\cdot1{,}6\cdot10^{-19}\cdot10^{-4}} \approx 7\ \mu\mathrm V$.

Półprzewodnik: $U_H = \dfrac{10^{-3}\cdot0{,}1}{10^{21}\cdot1{,}6\cdot10^{-19}\cdot5\cdot10^{-4}} \approx 1{,}2\ \mathrm{mV}$, prawie 200 razy więcej przy 10 000 razy mniejszym prądzie i 10 razy słabszym polu.

**Zadanie 2.** Jednokrotnie zjonizowane atomy węgla 12 i 14 przyspieszono napięciem 1000 V i wpuszczono w pole 0,1 T. Jak daleko od siebie uderzą w detektor?

$r = \dfrac1B\sqrt{\dfrac{2mU}{e}}$: dla ¹²C $r \approx 15{,}8\ \mathrm{cm}$, dla ¹⁴C $r \approx 17{,}0\ \mathrm{cm}$. Na detektorze odległość wynosi $2\Delta r \approx 2{,}5\ \mathrm{cm}$, łatwo rozróżnialne. Tak (w akceleratorowej spektrometrii mas) liczy się atomy ¹⁴C w datowaniu radiowęglowym.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Cyklotron ma pole 1,5 T i promień 0,5 m, a napięcie między duantami wynosi 50 kV. Oblicz częstotliwość, końcową energię protonów, liczbę obiegów i czas przyspieszania.

$f = \dfrac{eB}{2\pi m_p} \approx 22{,}9\ \mathrm{MHz}$.

$E_{\max} = \dfrac{(eBR)^2}{2m_p} \approx 4{,}3\cdot10^{-12}\ \mathrm J \approx 27\ \mathrm{MeV}$.

Na obieg proton zyskuje $2\cdot50\ \mathrm{keV}$, więc potrzeba ok. 270 obiegów, czyli ok. 12 μs.

Promień po $n$ obiegach: $E_n = 2neU$, $r_n = \dfrac{\sqrt{2m_pE_n}}{eB} \propto \sqrt n$. Kolejne okręgi są coraz gęściej upakowane. Prędkość końcowa to ok. 0,24c, więc poprawka relatywistyczna wynosi ok. 3% i w praktyce pole jest lekko kształtowane (cyklotron izochroniczny).

## Typowe pułapki

- **Napięcie Halla wzdłuż prądu.** Mierzy się je w poprzek przewodnika, prostopadle do prądu i do pola.
- **Większy prąd w miedzi daje duży sygnał Halla.** W metalach $n$ jest ogromne i sygnał jest znikomy. Liczy się małe $n$.
- **Częstotliwość cyklotronu rośnie z energią.** Dla prędkości nierelatywistycznych jest stała. To kluczowa idea cyklotronu.
- **Energia cyklotronu zależy od napięcia.** Energia końcowa zależy od $B$ i $R$. Napięcie zmienia tylko liczbę obiegów.
- **Spektrometr mierzy masę.** Mierzy stosunek $m/q$. Jony dwukrotnie zjonizowane wyglądają jak dwa razy lżejsze.

## Doświadczenie / symulacja

**Hallotron w telefonie.** Magnetometr w telefonie to zwykle czujnik Halla lub magnetorezystancyjny. W phyphox (*Magnetometer*) zbliżaj magnes i mierz pole w funkcji odległości. Dla magnesu sztabkowego daleko od niego pole maleje jak $1/r^3$ (dipol, 14.07). Sprawdź to na wykresie log–log.

**Czujnik Halla z Arduino.** Moduł z czujnikiem Halla (np. typu liniowego, kilka złotych) podłączony do wejścia analogowego daje napięcie proporcjonalne do pola. Skalibruj go magnetometrem telefonu i zmierz pole wewnątrz cewki (14.06).

**Python:** tory jonów w spektrometrze i cyklotron — symulacja przyspieszania.

```python
import numpy as np

e, mp, u = 1.602e-19, 1.673e-27, 1.6605e-27
B, U = 0.1, 1000.0
for A in (12, 13, 14):
    r = np.sqrt(2*A*u*U/e)/B
    print(f"C-{A}⁺: r = {r*100:.2f} cm, punkt uderzenia 2r = {2*r*100:.2f} cm")

B, R, Ud = 1.5, 0.5, 50e3                          # cyklotron
f = e*B/(2*np.pi*mp)
E, n = 0.0, 0
while np.sqrt(2*mp*(E + e*Ud))/(e*B) < R:         # kolejne przejścia przez szczelinę
    E += e*Ud; n += 1
print(f"f = {f/1e6:.1f} MHz, przejść szczeliny: {n}, obiegów: {n/2:.0f}, czas ≈ {n/2/f*1e6:.1f} µs")
print(f"energia końcowa ≈ {E/e/1e6:.1f} MeV (wzór: {(e*B*R)**2/(2*mp)/e/1e6:.1f} MeV), v/c = {np.sqrt(2*E/mp)/3e8:.2f}")
```

## Zadania

### A. Poziom maturalny

1. W spektrometrze jony o ładunku $+e$ i prędkości $10^5\ \mathrm{m/s}$ wpadają w pole 0,5 T. Oblicz odległość między śladami izotopów chloru ³⁵Cl i ³⁷Cl na detektorze.

<details>
<summary>Odpowiedź</summary>

$2r = 2mv/(eB)$: 14,5 cm i 15,3 cm, odległość ok. 8 mm.
</details>

2. Jak zmieni się napięcie Halla w czujniku, gdy dwukrotnie zwiększymy prąd, a pole zmniejszymy o połowę?

<details>
<summary>Odpowiedź</summary>

Nie zmieni się ($U_H \propto IB$).
</details>

3. Dlaczego częstotliwość napięcia w cyklotronie może być stała, choć cząstka przyspiesza?

<details>
<summary>Odpowiedź</summary>

Okres obiegu $2\pi m/(qB)$ nie zależy od prędkości. Szybsza cząstka zatacza większy okrąg w tym samym czasie.
</details>

### B. Poziom akademicki

1. Pasek półprzewodnika o grubości 1 mm przewodzi prąd 5 mA w polu 0,2 T. Napięcie Halla wynosi 6,25 mV. Oblicz koncentrację nośników.

<details>
<summary>Odpowiedź</summary>

$n = \dfrac{IB}{qtU_H} = \dfrac{0{,}005\cdot0{,}2}{1{,}6\cdot10^{-19}\cdot10^{-3}\cdot6{,}25\cdot10^{-3}} = 10^{21}\ \mathrm{m^{-3}}$.
</details>

2. Pokaż, że w cyklotronie promień rośnie jak pierwiastek z liczby obiegów i że odstęp między kolejnymi orbitami maleje jak $1/\sqrt n$.

<details>
<summary>Odpowiedź</summary>

$r_n = \dfrac{\sqrt{2m\cdot2nqU}}{qB} \propto \sqrt n$. $\Delta r \approx \dfrac{dr}{dn} \propto \dfrac{1}{2\sqrt n}$.
</details>

3. Ten sam cyklotron (1,5 T, 0,5 m) przyspiesza cząstki alfa ($m \approx 4u$, $q = 2e$). Jaka jest częstotliwość i energia końcowa?

<details>
<summary>Odpowiedź</summary>

$q/m$ jest dwa razy mniejsze, więc $f \approx 11{,}5\ \mathrm{MHz}$. $E = q^2B^2R^2/(2m)$: ładunek ×2, kwadrat ×4, masa ×4, więc energia taka sama, ok. 27 MeV.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 11 — §11.6 (efekt Halla) i §11.7 (zastosowania sił magnetycznych: spektrometr masowy, cyklotron).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §28.3, §28.5; wyd. 1: t. 3, §29.3–29.4, §29.6.
