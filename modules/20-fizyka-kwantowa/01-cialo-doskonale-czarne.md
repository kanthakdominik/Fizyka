# 20.01 — Promieniowanie ciała doskonale czarnego

> **Moduł:** [20 — Podstawy fizyki kwantowej](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6: [§6.1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-1-promieniowanie-ciala-doskonale-czarnego) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §38.4 (s. 16)

← (początek modułu) · [spis modułu](README.md) · [Efekt fotoelektryczny](02-efekt-fotoelektryczny.md) →

## Po co to jest

Rozgrzany metal świeci najpierw na czerwono, potem na żółto, w końcu na biało. Fizyka klasyczna nie potrafiła wyjaśnić widma takiego świecenia: przewidywała nieskończoną energię w ultrafiolecie. W 1900 r. Planck rozwiązał ten problem, zakładając, że energia jest wymieniana porcjami $hf$. Tak narodziła się fizyka kwantowa. Prawo Plancka opisuje świecenie gwiazd, żarówek, ludzkiego ciała (termowizja) i promieniowanie reliktowe Wszechświata (24).

## Teoria w pigułce

**Ciało doskonale czarne** pochłania całe padające promieniowanie. W równowadze termicznej emituje widmo zależne **tylko od temperatury**. Dobrym modelem jest mały otwór w zamkniętej wnęce o stałej temperaturze. Gwiazdy, a nawet węgiel w ognisku, są niezłymi przybliżeniami.

**Prawa doświadczalne** (11.03):
- **Stefan–Boltzmann:** moc z jednostki powierzchni $\sigma T^4$, $\sigma = 5{,}67\cdot10^{-8}\ \mathrm{W/(m^2K^4)}$.
- **Wien:** $\lambda_{\max}T = b \approx 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$. Gorętsze ciała świecą krócej falowo.

**Katastrofa w nadfiolecie.** Klasyczna fizyka (ekwipartycja energii, 11.04) przypisuje każdemu modowi fali stojącej we wnęce średnią energię $kT$. Modów o krótkich falach jest nieskończenie wiele, więc wzór Rayleigha–Jeansa

$$B_\lambda \approx \frac{2ckT}{\lambda^4}$$

daje nieskończoną moc w nadfiolecie. Zgadza się z doświadczeniem tylko dla długich fal.

**Hipoteza Plancka.** Oscylatory w ściankach wnęki mogą mieć tylko energie będące wielokrotnością $hf$:

$$E_n = nhf, \qquad h = 6{,}626\cdot10^{-34}\ \mathrm{J\cdot s}.$$

Mody o $hf \gg kT$ są prawie niewzbudzone, bo pierwsza porcja energii jest dla nich za duża. Średnia energia modu wynosi $\dfrac{hf}{e^{hf/kT} - 1}$ zamiast $kT$. Prowadzi to do **prawa Plancka**:

$$B_\lambda(T) = \frac{2hc^2}{\lambda^5}\cdot\frac{1}{e^{hc/(\lambda kT)} - 1}.$$

Z niego wynikają prawo Wiena i prawo Stefana–Boltzmanna, z $\sigma$ wyrażonym przez $h$, $c$, $k$. Einstein (1905) poszedł dalej: samo światło składa się z porcji energii $hf$, czyli **fotonów** (20.02).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E = hf = hc/\lambda$ | kwant energii (foton) | — |
| $B_\lambda = \dfrac{2hc^2}{\lambda^5}\dfrac{1}{e^{hc/\lambda kT} - 1}$ | prawo Plancka | ciało doskonale czarne |
| $\lambda_{\max}T = 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$ | prawo Wiena | j.w. |
| $P/A = \sigma T^4$ | prawo Stefana–Boltzmanna | j.w. |
| $B_\lambda \approx 2ckT/\lambda^4$ | Rayleigh–Jeans | $hc/\lambda \ll kT$ |

## Przykład rozwiązany

**Zadanie.** Oblicz długość fali maksimum emisji dla Słońca (5772 K), włókna żarówki (2800 K) i ciała człowieka (310 K). Dlaczego tradycyjna żarówka jest tak mało wydajnym źródłem światła?

Słońce: $\lambda_{\max} \approx 502\ \mathrm{nm}$ (zielononiebieski, w środku zakresu widzialnego).

Żarówka: $\approx 1{,}04\ \mu\mathrm m$, w podczerwieni. Większość mocy idzie w ciepło, a w zakres widzialny trafia kilka procent.

Człowiek: $\approx 9{,}3\ \mu\mathrm m$, daleka podczerwień. Na tym zakresie działają kamery termowizyjne.

## Typowe pułapki

- **Ciało czarne jest czarne.** Gorące ciało czarne świeci jasno (Słońce). „Czarne” oznacza, że pochłania całe padające promieniowanie.
- **Maksimum widma Słońca ma kolor zielony, więc Słońce jest zielone.** Oko widzi sumę wszystkich długości fal, czyli światło białe.
- **Kwantyzacja dotyczy tylko światła.** Planck skwantował energię oscylatorów w ściankach. Einstein rozciągnął to na samo światło.
- **Temperatura w °C w prawie Wiena.** Trzeba używać kelwinów.

## Doświadczenie / symulacja

**Barwa żarówki a napięcie.** Tradycyjną żarówkę (lub halogen) zasilaj przez regulator (ściemniacz albo zasilacz) i obserwuj przez siatkę dyfrakcyjną (CD, 18.03), jak widmo przesuwa się w stronę niebieskiego przy wyższym napięciu. Opór włókna (13.02) pozwala oszacować temperaturę.

**Symulacja PhET:** *Widmo ciała doskonale czarnego* (*Blackbody Spectrum*) — zmieniaj temperaturę i porównuj z gwiazdami, żarówką, Ziemią ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** prawo Plancka a Rayleigh–Jeans i sprawdzenie praw Wiena i Stefana–Boltzmanna.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

h, c, k = 6.62607015e-34, 2.99792458e8, 1.380649e-23
planck = lambda lam, T: 2*h*c**2/lam**5/np.expm1(h*c/(lam*k*T))
rj = lambda lam, T: 2*c*k*T/lam**4

lam = np.linspace(100e-9, 3000e-9, 1000)
for T in (3000, 4500, 5772):
    B = planck(lam, T)
    plt.plot(lam*1e9, B/1e12, label=f"{T} K")
    print(f"T = {T} K: λ_max = {lam[np.argmax(B)]*1e9:.0f} nm (Wien: {2.898e-3/T*1e9:.0f} nm)")
plt.plot(lam*1e9, rj(lam, 5772)/1e12, "k--", label="Rayleigh–Jeans 5772 K")

T = 5772
M = np.pi*quad(lambda l: planck(l, T), 50e-9, 1e-3, limit=200)[0]    # moc z m² (całka po półsferze daje π); poniżej 50 nm wkład znikomy
print(f"σT⁴ = {5.670374e-8*T**4:.3e} W/m², całka z Plancka = {M:.3e} W/m²")
plt.ylim(0, 40); plt.xlabel("λ [nm]"); plt.ylabel("B_λ [TW/(m²·sr·m)]"); plt.legend(); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Gwiazda Betelgeza ma temperaturę ok. 3500 K, a Rigel ok. 12 000 K. Oblicz $\lambda_{\max}$ dla obu. Jakie mają barwy?

<details>
<summary>Odpowiedź</summary>

Betelgeza ok. 830 nm, czerwonawa. Rigel ok. 240 nm, niebieskobiała.
</details>

2. Ile razy wzrośnie moc promieniowania ciała, gdy jego temperatura bezwzględna wzrośnie o 10%?

<details>
<summary>Odpowiedź</summary>

$1{,}1^4 \approx 1{,}46$ razy.
</details>

3. Oblicz energię fotonu światła zielonego (550 nm) w dżulach i elektronowoltach.

<details>
<summary>Odpowiedź</summary>

$E = hc/\lambda \approx 3{,}6\cdot10^{-19}\ \mathrm J \approx 2{,}25\ \mathrm{eV}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pokaż, że dla długich fal ($hc/\lambda \ll kT$) prawo Plancka przechodzi w prawo Rayleigha–Jeansa.

<details>
<summary>Odpowiedź</summary>

$e^x - 1 \approx x$ dla małych $x = hc/(\lambda kT)$, więc $B \approx \dfrac{2hc^2}{\lambda^5}\cdot\dfrac{\lambda kT}{hc} = \dfrac{2ckT}{\lambda^4}$.
</details>

2. Wyprowadź prawo Wiena, szukając maksimum $B_\lambda$. Wskazówka: z podstawieniem $x = hc/(\lambda kT)$ warunek ma postać $x = 5(1 - e^{-x})$, a jego rozwiązanie to $x \approx 4{,}965$.

<details>
<summary>Odpowiedź</summary>

$B \propto x^5/(e^x - 1)$ jako funkcja $x$ (przy stałym $T$, a $\lambda \propto 1/x$). Pochodna po $\lambda$ daje $5(e^x - 1) = xe^x$. Stąd $\lambda_{\max}T = hc/(4{,}965k) \approx 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$.
</details>

3. Oblicz średnią energię modu o częstotliwości $f$ w temperaturze $T$ jako średnią z rozkładu Boltzmanna po energiach $nhf$. Pokaż, że daje to $\dfrac{hf}{e^{hf/kT} - 1}$.

<details>
<summary>Odpowiedź</summary>

$\bar E = \dfrac{\sum nhf\,e^{-nx}}{\sum e^{-nx}}$, $x = hf/kT$. $\sum e^{-nx} = \dfrac{1}{1 - e^{-x}}$, a licznik to $-hf\dfrac{d}{dx}$ tej sumy. Wychodzi $\bar E = \dfrac{hfe^{-x}}{1 - e^{-x}} = \dfrac{hf}{e^x - 1}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6 — §6.1: promieniowanie ciała doskonale czarnego.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5, §38.4. (W wyd. 1 promieniowanie cieplne omawiane jest przy prawie Stefana–Boltzmanna w t. 2, rozdz. 19.)
- Symulacja PhET *Widmo ciała doskonale czarnego*.
