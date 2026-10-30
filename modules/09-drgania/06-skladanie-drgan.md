# 09.06 — Składanie drgań: dudnienia i krzywe Lissajous

> **Moduł:** [09 — Drgania](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 17: [§17.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/17-6-dudnienia) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/17-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §17.6 (s. 221)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§18.7, s. 171](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=187) — PDF z serwera AGH

← [Drgania wymuszone i rezonans](05-drgania-wymuszone-i-rezonans.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Gdy na ciało działa kilka drgań naraz, wypadkowy ruch bywa zaskakujący: dwa dźwięki o bliskich częstotliwościach dają rytmiczne „falowanie” głośności (dudnienia), a drgania prostopadłe rysują na oscyloskopie krzywe Lissajous. Składanie drgań to wstęp do interferencji fal (10.03, 18), analizy Fouriera i do pracy z oscyloskopem; dudnienia pozwalają stroić instrumenty na słuch.

## Teoria w pigułce

**Drgania w tym samym kierunku i o tej samej częstości.** Suma $x_1 = A_1\cos(\omega t + \varphi_1)$ i $x_2 = A_2\cos(\omega t + \varphi_2)$ to znowu drganie harmoniczne o tej samej częstości. Najłatwiej dodać je **wskazami** (fazorami) — wektorami o długościach $A_1$, $A_2$ obracającymi się z prędkością $\omega$:

$$A^2 = A_1^2 + A_2^2 + 2A_1A_2\cos(\varphi_2 - \varphi_1).$$

Zgodne fazy — amplitudy się dodają; przeciwne ($\Delta\varphi = \pi$) — odejmują (wygaszanie).

**Dudnienia** — drgania w tym samym kierunku o bliskich częstościach $\omega_1 \approx \omega_2$ i równych amplitudach:

$$x = A\cos\omega_1t + A\cos\omega_2t = 2A\cos\left(\frac{\omega_1 - \omega_2}{2}t\right)\cos\left(\frac{\omega_1 + \omega_2}{2}t\right).$$

Słyszymy ton o częstotliwości średniej, którego głośność narasta i opada z **częstotliwością dudnień**

$$f_{\text{d}} = \lvert f_1 - f_2\rvert.$$

(Obwiednia ma częstotliwość $\lvert f_1 - f_2\rvert/2$, ale głośność osiąga maksimum dwa razy w jej okresie.) Stroiciele zbliżają częstotliwości, aż dudnienia znikną.

**Drgania prostopadłe** $x = A\cos(\omega_xt)$, $y = B\cos(\omega_yt + \varphi)$ — punkt zakreśla **krzywą Lissajous**. Dla równych częstości: odcinek ($\varphi = 0$), elipsa, okrąg ($A = B$, $\varphi = 90^\circ$). Dla stosunku częstości $p : q$ (liczb całkowitych) krzywa jest zamknięta; stosunek odczytuje się z liczby styczności krzywej z bokami prostokąta.

**Analiza Fouriera** (zapowiedź): każde drganie okresowe da się przedstawić jako sumę drgań harmonicznych o częstotliwościach $f, 2f, 3f, \dots$ — stąd barwa dźwięku instrumentów (10.06).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $A = \sqrt{A_1^2 + A_2^2 + 2A_1A_2\cos\Delta\varphi}$ | amplituda sumy | ta sama częstość i kierunek |
| $\tan\varphi = \dfrac{A_1\sin\varphi_1 + A_2\sin\varphi_2}{A_1\cos\varphi_1 + A_2\cos\varphi_2}$ | faza sumy | j.w. |
| $f_{\text{d}} = \lvert f_1 - f_2\rvert$ | częstotliwość dudnień | $f_1 \approx f_2$ |
| $\cos a + \cos b = 2\cos\frac{a - b}{2}\cos\frac{a + b}{2}$ | tożsamość | — |
| $f_x : f_y = n_y : n_x$ | krzywe Lissajous | $n$ — liczba styczności z bokami prostokąta |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Złóż drgania $x_1 = 3\cos\omega t$ i $x_2 = 4\sin\omega t$ (cm).

$4\sin\omega t = 4\cos(\omega t - 90^\circ)$, więc różnica faz wynosi $90^\circ$: $A = \sqrt{9 + 16} = 5\ \mathrm{cm}$, $\tan\varphi = \dfrac{-4}{3} \Rightarrow \varphi \approx -53{,}1^\circ$. Wynik: $x = 5\cos(\omega t - 53{,}1^\circ)$.

**Zadanie 2.** Dwa kamertony mają częstotliwości 440 Hz i 444 Hz. Jaki ton słychać i ile dudnień na sekundę?

Ton o częstotliwości 442 Hz z dudnieniami 4 razy na sekundę.

## Typowe pułapki

- **Amplitudy się po prostu dodają.** Tylko przy zgodnych fazach; ogólnie — jak wektory.
- **Częstotliwość dudnień = połowa różnicy.** Słyszalna częstotliwość dudnień to pełna różnica $\lvert f_1 - f_2\rvert$.
- **Dudnienia przy dużej różnicy częstotliwości.** Gdy różnica przekracza kilkanaście Hz, ucho słyszy dwa osobne tony (lub szorstkość), a nie dudnienia.
- **$\sin$ i $\cos$ jako drgania „w tej samej fazie”.** Różnią się o $90^\circ$.

## Doświadczenie / symulacja

**Dudnienia w phyphox.** Uruchom na dwóch telefonach generator tonu (*Tone generator*) o częstotliwościach 440 i 443 Hz, a na trzecim (albo komputerze) — eksperyment *Audio Scope* / *Audio Spectrum*. Zobaczysz obwiednię i usłyszysz 3 dudnienia na sekundę. Zmierz częstotliwość dudnień z oscylogramu.

**Python:** dudnienia i krzywe Lissajous.

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 20000, endpoint=False)          # dokładnie 1 s → rozdzielczość widma 1 Hz
f1, f2 = 440, 444
x = np.cos(2*np.pi*f1*t) + np.cos(2*np.pi*f2*t)
env = 2*np.abs(np.cos(np.pi*(f2 - f1)*t))
spec = np.abs(np.fft.rfft(x)); freqs = np.fft.rfftfreq(t.size, t[1] - t[0])
print("częstotliwości w widmie:", freqs[spec > spec.max()/2])

fig, ax = plt.subplots(1, 2, figsize=(10, 3.5))
ax[0].plot(t, x, lw=0.4); ax[0].plot(t, env, "r"); ax[0].set_xlabel("t [s]"); ax[0].set_title("dudnienia 440 + 444 Hz")
tt = np.linspace(0, 2*np.pi, 1000)
for p, q, ph in [(1, 1, np.pi/4), (1, 2, 0), (3, 2, np.pi/2)]:
    ax[1].plot(np.cos(p*tt), np.cos(q*tt + ph), label=f"{p}:{q}")
ax[1].set_aspect("equal"); ax[1].legend(); ax[1].set_title("krzywe Lissajous")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Gitarzysta stroi strunę do kamertonu 440 Hz i słyszy 3 dudnienia na sekundę. Po lekkim napięciu struny dudnienia przyspieszają. Jaka była częstotliwość struny i co powinien zrobić?

<details>
<summary>Odpowiedź</summary>

443 Hz (napięcie podnosi częstotliwość i zwiększa różnicę); trzeba poluzować strunę.
</details>

2. Dwa drgania o tej samej częstotliwości i amplitudach 3 cm i 5 cm. Jaka może być najmniejsza i największa amplituda drgania wypadkowego?

<details>
<summary>Odpowiedź</summary>

2 cm (fazy przeciwne) i 8 cm (fazy zgodne).
</details>

### B. Poziom akademicki

1. Złóż drgania $x_1 = 2\cos(\omega t)$ i $x_2 = 2\cos(\omega t + 120^\circ)$. Dodaj trzecie $x_3 = 2\cos(\omega t + 240^\circ)$. Jaki jest wynik? Gdzie spotyka się taki układ?

<details>
<summary>Odpowiedź</summary>

$x_1 + x_2$: $A = 2$, faza $60^\circ$. Suma trzech: zero — tak działa sieć trójfazowa (suma prądów w zrównoważonym układzie wynosi zero).
</details>

2. Wyprowadź wzór na dudnienia z tożsamości na sumę cosinusów.

<details>
<summary>Odpowiedź</summary>

$\cos\omega_1t + \cos\omega_2t = 2\cos\dfrac{(\omega_1 - \omega_2)t}{2}\cos\dfrac{(\omega_1 + \omega_2)t}{2}$; obwiednia $\lvert\cos(\Delta\omega t/2)\rvert$ ma okres $2\pi/\Delta\omega$, czyli częstotliwość $\lvert f_1 - f_2\rvert$.
</details>

3. Krzywa Lissajous dotyka pionowych boków prostokąta 2 razy, a poziomych 3 razy. Częstotliwość drgań poziomych wynosi 300 Hz. Ile wynosi częstotliwość pionowych?

<details>
<summary>Odpowiedź</summary>

$f_x/f_y = n_y/n_x$, gdzie $n_y$ — styczności z bokiem poziomym, $n_x$ — z pionowym: $300/f_y = 3/2 \Rightarrow f_y = 200\ \mathrm{Hz}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1 — §17.6 (dudnienia) i §16.5 (superpozycja i interferencja).
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2, §17.6 — dudnienia.
