# 10.06 — Struny i piszczałki: mody własne, dudnienia

> **Moduł:** [10 — Fale mechaniczne i akustyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 17: [§17.4–17.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/17-4-tryby-drgan-fali-stojacej) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/17-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §17.5–17.6 (s. 216)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§18.6–18.7, s. 168](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=184) — PDF z serwera AGH

← [Dźwięk: prędkość, natężenie, poziom w decybelach](05-dzwiek-i-natezenie.md) · [spis modułu](README.md) · [Efekt Dopplera i fala uderzeniowa](07-efekt-dopplera.md) →

## Po co to jest

Każdy instrument muzyczny to rezonator, w którym powstają fale stojące: struna w gitarze i fortepianie, słup powietrza we flecie, organach i butelce, w którą dmuchamy. Wysokość dźwięku zależy od długości rezonatora i prędkości fali. Barwa zależy od tego, które harmoniczne są obecne. Ta sama fizyka wyjaśnia, dlaczego głos po wdechu helu brzmi jak u kreskówki, dlaczego ucho jest najczulsze na częstotliwości ok. 3 kHz i jak stroi się instrumenty na słuch, za pomocą dudnień.

## Teoria w pigułce

**Struna** zamocowana na obu końcach ma węzły na końcach (10.03):

$$f_n = n\frac{v}{2L} = \frac{n}{2L}\sqrt{\frac F\mu}, \qquad n = 1, 2, 3, \dots$$

Wyżej brzmi struna krótsza (przyciśnięta palcem), mocniej napięta lub lżejsza (cieńsza).

**Słup powietrza w rurze.** W fali stojącej dźwięku na końcu zamkniętym jest węzeł wychylenia (powietrze nie może się ruszać) i strzałka ciśnienia. Na końcu otwartym jest strzałka wychylenia i węzeł ciśnienia, bo ciśnienie jest tam równe atmosferycznemu.

- **Rura otwarta z obu stron** (flet, piszczałka otwarta): strzałki na obu końcach, więc mieści się całkowita liczba połówek fali.
  $$f_n = n\frac{v}{2L}, \qquad n = 1, 2, 3, \dots$$
- **Rura zamknięta z jednej strony** (butelka, piszczałka kryta, przewód słuchowy): węzeł na jednym końcu i strzałka na drugim, więc mieści się nieparzysta liczba ćwiartek fali.
  $$f_n = n\frac{v}{4L}, \qquad n = 1, 3, 5, \dots$$

  Ton podstawowy brzmi oktawę niżej niż w rurze otwartej o tej samej długości. Brakuje parzystych harmonicznych, co nadaje charakterystyczną „pustą” barwę (klarnet).

W praktyce strzałka na końcu otwartym wystaje nieco poza rurę. Uwzględnia to **poprawka wylotowa** $\Delta L \approx 0{,}6r$ dla rury o promieniu $r$.

**Barwa dźwięku.** Instrument wydaje jednocześnie ton podstawowy i harmoniczne o różnych amplitudach. Ten sam dźwięk A (440 Hz) na flecie i skrzypcach ma inne widmo harmonicznych. To jest analiza Fouriera z 09.06 w praktyce.

**Dudnienia.** Dwa tony o bliskich częstotliwościach dają okresowe zmiany głośności z częstotliwością $f_{\text{d}} = \lvert f_1 - f_2\rvert$ (wyprowadzenie w 09.06). Stroiciel zmienia naciąg struny, aż dudnienia z wzorcem znikną.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $f_n = nv/(2L)$, $n = 1, 2, 3, \dots$ | struna; rura otwarta z obu stron | — |
| $f_n = nv/(4L)$, $n = 1, 3, 5, \dots$ | rura zamknięta z jednej strony | — |
| $v = \sqrt{F/\mu}$ / $v \approx 343\ \mathrm{m/s}$ | prędkość fali na strunie / w powietrzu | powietrze w 20°C |
| $\Delta L \approx 0{,}6r$ | poprawka wylotowa | rura o promieniu $r$, koniec otwarty |
| $f_{\text{d}} = \lvert f_1 - f_2\rvert$ | dudnienia | $f_1 \approx f_2$ |

## Przykład rozwiązany

**Zadanie 1.** Oblicz trzy najniższe częstotliwości rezonansowe rury o długości 0,5 m: (a) otwartej z obu stron, (b) zamkniętej z jednej strony.

(a) $f_1 = 343/(2\cdot0{,}5) = 343\ \mathrm{Hz}$; dalej 686 i 1029 Hz.

(b) $f_1 = 343/(4\cdot0{,}5) \approx 172\ \mathrm{Hz}$; dalej $3f_1 \approx 515$ i $5f_1 \approx 858\ \mathrm{Hz}$.

**Zadanie 2.** Przewód słuchowy ma ok. 2,5 cm długości i jest zamknięty błoną bębenkową. Przy jakiej częstotliwości rezonuje?

$f_1 = 343/(4\cdot0{,}025) \approx 3{,}4\ \mathrm{kHz}$. Właśnie w tym zakresie ucho jest najczulsze.

**Zadanie 3.** Flet i klarnet mają podobną długość, ok. 0,6 m. Klarnet zachowuje się jak rura zamknięta z jednej strony (ustnik ze stroikiem), flet jak otwarta. Porównaj ich najniższe dźwięki.

Flet: $343/1{,}2 \approx 290\ \mathrm{Hz}$. Klarnet: $343/2{,}4 \approx 140\ \mathrm{Hz}$, czyli oktawę niżej. Rzeczywiste najniższe dźwięki to ok. 262 Hz i ok. 147 Hz, bo efektywna długość i poprawki są inne niż w prostym modelu.

## Typowe pułapki

- **Rura zamknięta ma wszystkie harmoniczne.** Ma tylko nieparzyste: $f_1, 3f_1, 5f_1, \dots$
- **Węzeł ciśnienia = węzeł wychylenia.** Jest odwrotnie: na końcu zamkniętym jest węzeł wychylenia i strzałka ciśnienia.
- **Gorętsze powietrze obniża dźwięk piszczałki.** W cieplejszym powietrzu $v$ rośnie, więc dźwięk piszczałki **rośnie**. Struny natomiast się rozszerzają i luzują, więc ich dźwięk spada.
- **Hel zmienia wysokość głosu.** Struny głosowe drgają tak samo. Hel przesuwa rezonanse (formanty) jamy ustnej i gardła, więc zmienia się barwa.

## Doświadczenie / symulacja

**Butelka jako piszczałka.** Dmuchaj nad szyjką butelki i zmierz częstotliwość w phyphox (*Audio Spectrum* lub *Audio Autocorrelation*). Dolewaj wody, by skracać słup powietrza, i narysuj $f$ od $1/L$. Prosta wyjdzie tylko w przybliżeniu, bo butelka z wąską szyjką to bardziej rezonator Helmholtza niż rura.

**Rezonans słupa powietrza.** Rura (np. od odkurzacza lub karton po folii aluminiowej) i generator tonu w telefonie: zmieniaj częstotliwość i szukaj najgłośniejszych rezonansów. Porównaj z $nv/(2L)$ i wyznacz prędkość dźwięku. Zakryj jeden koniec dłonią i sprawdź, że znikają parzyste harmoniczne.

**Dudnienia.** Graj na dwóch telefonach tony 440 i 442 Hz i porównaj liczbę dudnień na sekundę z przewidywaniem.

**Python:** widmo harmonicznych rury otwartej i zamkniętej oraz rozkład ciśnienia w modach.

```python
import numpy as np
import matplotlib.pyplot as plt

v, L = 343.0, 0.5
open_f = [n*v/(2*L) for n in range(1, 6)]
closed_f = [n*v/(4*L) for n in (1, 3, 5, 7, 9)]
print("rura otwarta  [Hz]:", [round(f) for f in open_f])
print("rura zamknięta [Hz]:", [round(f) for f in closed_f])

x = np.linspace(0, L, 300)
fig, ax = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)
for n in (1, 2, 3):                     # ciśnienie: węzły na obu otwartych końcach
    ax[0].plot(x*100, np.sin(n*np.pi*x/L), label=f"n = {n}, {n*v/(2*L):.0f} Hz")
for n in (1, 3, 5):                     # x = 0 zamknięty (strzałka ciśnienia), x = L otwarty
    ax[1].plot(x*100, np.cos(n*np.pi*x/(2*L)), label=f"n = {n}, {n*v/(4*L):.0f} Hz")
ax[0].set_title("rura otwarta — amplituda ciśnienia"); ax[1].set_title("rura zamknięta z lewej")
for a in ax:
    a.set_xlabel("x [cm]"); a.grid(True); a.legend(fontsize=8)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Piszczałka organowa zamknięta z jednej strony ma długość 20 cm. Oblicz częstotliwość jej tonu podstawowego i następnej harmonicznej.

<details>
<summary>Odpowiedź</summary>

$f_1 = 343/0{,}8 \approx 429\ \mathrm{Hz}$, następna $3f_1 \approx 1290\ \mathrm{Hz}$.
</details>

2. Rura otwarta z obu stron ma kolejne częstotliwości rezonansowe 400 Hz i 500 Hz. Oblicz częstotliwość podstawową i długość rury.

<details>
<summary>Odpowiedź</summary>

Kolejne harmoniczne rury otwartej różnią się o $f_1$, więc $f_1 = 100\ \mathrm{Hz}$ i $L = v/(2f_1) \approx 1{,}7\ \mathrm{m}$.
</details>

3. Rura ma kolejne rezonanse 300 Hz i 500 Hz. Czy jest otwarta, czy zamknięta z jednej strony? Jaka jest częstotliwość podstawowa?

<details>
<summary>Odpowiedź</summary>

Różnica wynosi $200\ \mathrm{Hz} = 2f_1$, czyli $f_1 = 100\ \mathrm{Hz}$. Wtedy 300 i 500 Hz to $3f_1$ i $5f_1$, więc rura jest zamknięta z jednej strony.
</details>

4. Gitarzysta słyszy 3 dudnienia na sekundę między struną a kamertonem 440 Hz. Gdy lekko poluzuje strunę, dudnienia zwalniają. Jaka była częstotliwość struny?

<details>
<summary>Odpowiedź</summary>

443 Hz. Poluzowanie obniża częstotliwość i zbliża ją do 440 Hz.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. O ile procent trzeba zmienić naciąg struny, żeby jej częstotliwość wzrosła z 440 Hz do 443 Hz? Porównaj z przybliżeniem różniczkowym $\dfrac{dF}{F} = 2\dfrac{df}{f}$.

<details>
<summary>Odpowiedź</summary>

$F \propto f^2$, więc $(443/440)^2 - 1 \approx 1{,}37\%$. Przybliżenie daje $2\cdot3/440 \approx 1{,}36\%$.
</details>

2. Piszczałkę otwartą dostrojono do 440 Hz w temperaturze 20°C. Jaką częstotliwość wyda w zimnym kościele w 5°C? O ile to zmienia strój (ile dudnień z kamertonem 440 Hz)?

<details>
<summary>Odpowiedź</summary>

$f \propto v \propto \sqrt T$: $440\sqrt{278/293} \approx 428{,}6\ \mathrm{Hz}$, czyli ok. 11 dudnień na sekundę. To prawie ćwierć tonu niżej.
</details>

3. Uzasadnij, dlaczego w rurze zamkniętej z jednej strony mogą istnieć tylko nieparzyste harmoniczne. Zapisz rozkład wychylenia $s(x)$ spełniający warunki $s(0) = 0$ i $\dfrac{ds}{dx}(L) = 0$ (strzałka wychylenia na końcu otwartym).

<details>
<summary>Odpowiedź</summary>

$s = s_m\sin kx$ spełnia $s(0) = 0$. Warunek $\cos kL = 0$ daje $kL = (2m + 1)\pi/2$, czyli $L = (2m + 1)\lambda/4$ i $f = (2m + 1)v/(4L)$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 17 — §17.4 (tryby drgań fali stojącej), §17.5 (źródła dźwięków muzycznych), §17.6 (dudnienia).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §17.5–17.6; wyd. 1: t. 2, §18.6–18.7.
