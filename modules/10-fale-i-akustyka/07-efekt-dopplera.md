# 10.07 — Efekt Dopplera i fala uderzeniowa

> **Moduł:** [10 — Fale mechaniczne i akustyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 17: [§17.7–17.8](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/17-7-efekt-dopplera) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/17-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §17.7–17.8 (s. 223)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§18.8–18.9, s. 173](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=189) — PDF z serwera AGH

← [Struny i piszczałki: mody własne, dudnienia](06-struny-rury-dudnienia.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Syrena karetki brzmi wyżej, gdy pojazd się zbliża, i niżej, gdy się oddala. To efekt Dopplera, czyli zmiana odbieranej częstotliwości przy ruchu źródła lub obserwatora. Wykorzystują go radary drogowe, ultrasonografia dopplerowska (pomiar przepływu krwi), radary meteorologiczne i astronomia (prędkości gwiazd, odkrywanie planet pozasłonecznych, ucieczka galaktyk — 19, 24). Gdy źródło jest szybsze od fali, powstaje fala uderzeniowa, którą słychać jako huk samolotu ponaddźwiękowego.

## Teoria w pigułce

**Mechanizm.** Fale dźwiękowe biegną względem powietrza z prędkością $v$.
- **Źródło** poruszające się w stronę obserwatora wysyła kolejne grzbiety z coraz bliższych miejsc. Grzbiety są ściśnięte, długość fali przed źródłem maleje do $\lambda' = (v - v_s)/f$ i odbierana częstotliwość rośnie.
- **Obserwator** poruszający się w stronę źródła napotyka grzbiety częściej, z prędkością względną $v + v_o$, choć długość fali się nie zmienia.

**Wzór ogólny** (ruch wzdłuż prostej łączącej źródło i obserwatora, prędkości względem powietrza):

$$f' = f\,\frac{v \pm v_o}{v \mp v_s}.$$

**Znaki** dobiera się według zasady „zbliżanie podwyższa”:
- w liczniku $+v_o$, gdy obserwator zbliża się do źródła;
- w mianowniku $-v_s$, gdy źródło zbliża się do obserwatora;
- przy oddalaniu znaki są przeciwne.

Ruch źródła i ruch obserwatora z tą samą prędkością dają nieco inne wyniki, bo dla dźwięku liczy się ruch względem ośrodka.

**Odbicie od ruchomej przeszkody** (radar, USG, nietoperz) to podwójny efekt. Przeszkoda najpierw odbiera falę jako obserwator, a potem wysyła ją jako źródło. Dla fal elektromagnetycznych i małych prędkości:

$$\Delta f \approx 2\frac{u}{c}f.$$

**Fala uderzeniowa.** Gdy $v_s > v$, czoła fal kulistych mają obwiednię w postaci **stożka Macha** o kącie połówkowym

$$\sin\theta = \frac{v}{v_s} = \frac{1}{\mathrm{Ma}},$$

gdzie $\mathrm{Ma} = v_s/v$ to liczba Macha. Wzdłuż stożka skupia się energia i słychać grom dźwiękowy. Odpowiedniki to fala dziobowa łodzi i promieniowanie Czerenkowa w reaktorach.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $f' = f\dfrac{v \pm v_o}{v \mp v_s}$ | efekt Dopplera dla dźwięku | ruch wzdłuż prostej; $v_s < v$; górne znaki — zbliżanie |
| $\lambda' = (v \mp v_s)/f$ | długość fali przed / za źródłem | — |
| $\Delta f \approx 2uf/c$ | radar, odbicie od ruchomego obiektu | $u \ll c$ |
| $\sin\theta = v/v_s$ | kąt stożka Macha | $v_s > v$ |

## Przykład rozwiązany

**Zadanie 1.** Karetka z syreną o częstotliwości 700 Hz jedzie z prędkością 25 m/s (90 km/h). Jaką częstotliwość słyszy stojący pieszy, gdy karetka się zbliża, a jaką, gdy się oddala?

Zbliżanie: $f' = 700\cdot\dfrac{343}{343 - 25} \approx 755\ \mathrm{Hz}$. Oddalanie: $f' = 700\cdot\dfrac{343}{343 + 25} \approx 652\ \mathrm{Hz}$. Ton spada o ok. 100 Hz, czyli ponad półtora tonu.

**Zadanie 2.** Rowerzysta jedzie z prędkością 20 m/s w stronę nieruchomego głośnika, który gra 500 Hz. Co słyszy?

$f' = 500\cdot\dfrac{343 + 20}{343} \approx 529\ \mathrm{Hz}$.

**Zadanie 3.** Radar drogowy pracuje na częstotliwości 24 GHz. Jaką różnicę częstotliwości zmierzy dla samochodu jadącego z prędkością 30 m/s (108 km/h)?

$\Delta f = 2\cdot30\cdot24\cdot10^9/(3\cdot10^8) = 4800\ \mathrm{Hz}$. Zmierzenie tak małej zmiany przy 24 GHz umożliwia mieszanie sygnału wysłanego z odbitym, które daje dudnienia o częstotliwości $\Delta f$.

**Zadanie 4.** Samolot leci z prędkością Ma = 2. Jaki jest kąt stożka Macha?

$\sin\theta = 1/2$, więc $\theta = 30^\circ$.

## Typowe pułapki

- **Zamiana znaków.** Sprawdzaj wynik zdrowym rozsądkiem: przy zbliżaniu częstotliwość ma wzrosnąć.
- **Efekt zależy od odległości.** Zależy od prędkości. Stała prędkość daje stałą (choć inną) częstotliwość. Słyszymy jej skok w chwili mijania, a nie stopniowy wzrost przy zbliżaniu.
- **Ruch prostopadły.** Liczy się składowa prędkości wzdłuż linii źródło–obserwator. Przy mijaniu w pewnej odległości ton zmienia się płynnie.
- **Wiatr.** Wiatr przesuwa ośrodek; wszystkie prędkości trzeba liczyć względem powietrza.
- **Grom dźwiękowy tylko w chwili przekraczania bariery.** Stożek ciągnie się za samolotem przez cały czas lotu ponaddźwiękowego, a każdy obserwator słyszy huk w chwili, gdy stożek go mija.

## Doświadczenie / symulacja

**Doppler w phyphox.** Eksperyment *Doppler effect*: jeden telefon gra stały ton (np. 5 kHz), a drugi go rejestruje. Biegnij z grającym telefonem w stronę odbiornika lub kręć nim na sznurku. Z przesunięcia częstotliwości wyznacz prędkość i porównaj z prędkością zmierzoną inaczej (np. akcelerometrem lub stoperem).

**Nagranie przejeżdżającego samochodu.** Nagraj telefonem przejazd auta z trąbiącym klaksonem lub karetki. W spektrogramie (phyphox *Audio Spectrum* albo Audacity) odczytaj częstotliwości przed i po minięciu i oblicz prędkość pojazdu.

**Python:** odbierana częstotliwość dla źródła mijającego obserwatora w odległości $d$.

```python
import numpy as np
import matplotlib.pyplot as plt

v, f0, vs, d = 343.0, 700.0, 25.0, 10.0
t_emit = np.linspace(-6, 6, 2000)                # chwile wysłania
xs = vs*t_emit                                   # źródło jedzie po osi x, obserwator w (0, d)
r = np.hypot(xs, d)
v_rad = vs*xs/r                                  # prędkość oddalania wzdłuż promienia
f_obs = f0*v/(v + v_rad)
t_arr = t_emit + r/v                             # chwila odbioru
print(f"skrajne częstotliwości: {f_obs.max():.0f} Hz i {f_obs.min():.0f} Hz")
vs_back = v*(f_obs.max() - f_obs.min())/(f_obs.max() + f_obs.min())
print(f"prędkość odtworzona z dwóch częstotliwości: {vs_back:.1f} m/s")
plt.plot(t_arr, f_obs); plt.axhline(f0, ls="--", color="gray")
plt.xlabel("czas odbioru [s]"); plt.ylabel("f [Hz]"); plt.title("karetka mijająca pieszego (d = 10 m)"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Pociąg jedzie z prędkością 30 m/s i trąbi z częstotliwością 500 Hz. Jaką częstotliwość słyszy człowiek na peronie przed i za pociągiem?

<details>
<summary>Odpowiedź</summary>

Przed pociągiem ok. 548 Hz, za nim ok. 460 Hz.
</details>

2. Przy mijaniu karetki ton syreny spada z 755 Hz do 652 Hz. Oblicz prędkość karetki.

<details>
<summary>Odpowiedź</summary>

$\dfrac{f_1}{f_2} = \dfrac{v + v_s}{v - v_s}$, więc $v_s = v\dfrac{f_1 - f_2}{f_1 + f_2} \approx 25\ \mathrm{m/s}$.
</details>

3. Samochód jedzie z prędkością 20 m/s w stronę ściany i trąbi z częstotliwością 1000 Hz. Jaką częstotliwość echa słyszy kierowca?

<details>
<summary>Odpowiedź</summary>

Ściana odbiera $1000\cdot\dfrac{343}{323}$, a kierowca jako ruchomy obserwator słyszy echo $1000\cdot\dfrac{343 + 20}{343 - 20} \approx 1124\ \mathrm{Hz}$.
</details>

4. Dlaczego przy przelocie samolotu ponaddźwiękowego słychać huk dopiero po tym, jak samolot przeleciał nad głową?

<details>
<summary>Odpowiedź</summary>

Stożek Macha ciągnie się za samolotem. Dociera do obserwatora dopiero wtedy, gdy samolot jest już za nim.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź wzór na częstotliwość odbieraną od źródła zbliżającego się z prędkością $v_s$. Rozważ odległość między dwoma kolejnymi grzbietami wysłanymi w odstępie $T$.

<details>
<summary>Odpowiedź</summary>

W czasie $T$ pierwszy grzbiet przebywa $vT$, a źródło $v_sT$. Odległość grzbietów to $\lambda' = (v - v_s)T$, więc $f' = v/\lambda' = f\,v/(v - v_s)$.
</details>

2. Samolot leci z prędkością Ma = 2 na wysokości 8 km. Ile sekund po przelocie nad głową obserwator usłyszy grom dźwiękowy?

<details>
<summary>Odpowiedź</summary>

$\theta = 30^\circ$. Stożek dociera do obserwatora, gdy samolot jest w odległości poziomej $h/\tan\theta \approx 13{,}9\ \mathrm{km}$, czyli po $13{,}9\ \mathrm{km}/686\ \mathrm{m/s} \approx 20\ \mathrm{s}$.
</details>

3. Aparat USG wysyła 5 MHz, a krew płynie z prędkością 0,5 m/s wzdłuż wiązki ($v = 1540\ \mathrm{m/s}$ w tkankach). Jakie jest przesunięcie częstotliwości? Dlaczego aparat może je odtworzyć jako dźwięk?

<details>
<summary>Odpowiedź</summary>

$\Delta f \approx 2uf/v \approx 3{,}2\ \mathrm{kHz}$. Leży w zakresie słyszalnym, więc różnicę częstotliwości można wprost puścić na głośnik i usłyszeć „szum przepływu”.
</details>

4. Pokaż, że dla $v_s, v_o \ll v$ efekt zależy w pierwszym przybliżeniu tylko od prędkości względnej: $f' \approx f(1 + u/v)$, gdzie $u$ to prędkość zbliżania.

<details>
<summary>Odpowiedź</summary>

$\dfrac{v + v_o}{v - v_s} = \left(1 + \dfrac{v_o}{v}\right)\left(1 - \dfrac{v_s}{v}\right)^{-1} \approx 1 + \dfrac{v_o + v_s}{v}$, a $u = v_o + v_s$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 17 — §17.7 (efekt Dopplera) i §17.8 (fale uderzeniowe).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §17.7–17.8; wyd. 1: t. 2, §18.8–18.9.
