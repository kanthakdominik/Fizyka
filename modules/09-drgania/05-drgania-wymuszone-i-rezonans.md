# 09.05 — Drgania wymuszone i rezonans

> **Moduł:** [09 — Drgania](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15: [§15.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-6-drgania-wymuszone) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §15.6 (s. 140)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§16.9, s. 112](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=128) — PDF z serwera AGH

← [Drgania tłumione](04-drgania-tlumione.md) · [spis modułu](README.md) · [Składanie drgań: dudnienia i krzywe Lissajous](06-skladanie-drgan.md) →

## Po co to jest

Gdy drgający układ jest okresowo popychany, może zgromadzić ogromną energię — jeśli popychamy go w rytmie jego własnych drgań. To **rezonans**: rozbija kieliszek dźwiękiem, sprawia, że pralka podskakuje przy pewnych obrotach, a most chwieje się pod maszerującymi żołnierzami. Rezonans jest też narzędziem: dostraja się do niego radio (15.05), działa na nim mikrofalówka, instrumenty muzyczne i rezonans magnetyczny w medycynie.

## Teoria w pigułce

**Model.** Oscylator tłumiony z siłą wymuszającą $F_0\cos\omega t$:

$$\ddot x + 2\beta\dot x + \omega_0^2x = \frac{F_0}{m}\cos\omega t.$$

Po zaniknięciu stanu przejściowego (drgań własnych) układ drga z częstością **siły wymuszającej** $\omega$, a nie własną:

$$x(t) = A(\omega)\cos(\omega t - \delta), \qquad A(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + (2\beta\omega)^2}}.$$

**Krzywa rezonansowa.**
- Dla $\omega \ll \omega_0$: $A \approx F_0/k$ — ciało podąża za siłą (jak przy statycznym rozciąganiu).
- Dla $\omega \approx \omega_0$: amplituda jest największa, $A_{\max} \approx \dfrac{F_0}{2m\beta\omega_0} = Q\dfrac{F_0}{k}$ — **$Q$ razy większa** niż statyczna.
- Dla $\omega \gg \omega_0$: $A \approx F_0/(m\omega^2) \to 0$ — układ „nie nadąża”.

Im mniejsze tłumienie, tym wyższy i węższy szczyt; szerokość rezonansu (w połowie mocy) $\Delta\omega \approx 2\beta = \omega_0/Q$.

**Faza.** Przesunięcie $\delta$ rośnie od 0 (poniżej rezonansu, ruch zgodny z siłą) przez $90^\circ$ (w rezonansie) do $180^\circ$ (powyżej). W rezonansie siła jest zgodna w fazie z **prędkością**, więc stale wykonuje dodatnią pracę — dlatego amplituda rośnie, aż straty zrównoważą dostarczaną moc.

**Przykłady.** Huśtawka popychana w rytmie jej drgań; śpiewak rozbijający kieliszek; drgania pralki przy obrotach równych częstości własnej; dostrajanie odbiornika radiowego. (Katastrofa mostu Tacoma Narrows w 1940 r. jest często podawana jako przykład rezonansu, ale jej mechanizm był bardziej złożony — flatter aerodynamiczny, czyli samowzbudne drgania.)

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $A(\omega) = \dfrac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\beta^2\omega^2}}$ | amplituda drgań wymuszonych | stan ustalony |
| $\tan\delta = \dfrac{2\beta\omega}{\omega_0^2 - \omega^2}$ | przesunięcie fazy | j.w. |
| $\omega_{\text{rez}} = \sqrt{\omega_0^2 - 2\beta^2}$ | częstość największej amplitudy | $\beta < \omega_0/\sqrt2$ |
| $A_{\max} \approx QF_0/k$ | amplituda w rezonansie | $Q \gg 1$ |
| $\Delta\omega \approx 2\beta = \omega_0/Q$ | szerokość rezonansu | j.w. |

## Przykład rozwiązany

**Zadanie (poziom maturalny).** Dlaczego żołnierze przechodząc przez most, mają zmylić krok?

Marsz w równym rytmie to okresowa siła o częstotliwości ok. 2 Hz. Jeśli częstotliwość drgań własnych mostu jest podobna, drgania rosną z każdym krokiem (rezonans). Bez wspólnego rytmu siły od poszczególnych osób mają przypadkowe fazy i się nie sumują.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Oscylator z 09.04 ($m = 0{,}5\ \mathrm{kg}$, $k = 200\ \mathrm{N/m}$, $\beta = 0{,}5\ \mathrm{s^{-1}}$) jest wymuszany siłą o amplitudzie $F_0 = 1\ \mathrm{N}$. Oblicz amplitudę drgań w rezonansie i dla $\omega = 0{,}9\omega_0$.

- Statycznie: $F_0/k = 5\ \mathrm{mm}$.
- W rezonansie: $A = \dfrac{F_0}{2m\beta\omega_0} = \dfrac{1}{2\cdot0{,}5\cdot0{,}5\cdot20} = 0{,}1\ \mathrm{m}$ — 20 razy więcej ($Q = 20$).
- Dla $\omega = 18\ \mathrm{rad/s}$: $A = \dfrac{2}{\sqrt{(400 - 324)^2 + 18^2}} \approx 2{,}6\ \mathrm{cm}$ — odstrojenie o 10% zmniejsza amplitudę prawie 4 razy.

**Metoda zespolona.** Szukamy rozwiązania $x = \operatorname{Re}(\tilde Ae^{i\omega t})$. Wstawiając $\tilde Ae^{i\omega t}$ do równania z prawą stroną $(F_0/m)e^{i\omega t}$:

$$(-\omega^2 + 2i\beta\omega + \omega_0^2)\tilde A = \frac{F_0}{m} \Rightarrow \tilde A = \frac{F_0/m}{\omega_0^2 - \omega^2 + 2i\beta\omega}.$$

Moduł $\tilde A$ to amplituda, argument (z minusem) — przesunięcie fazy. Ta sama metoda w obwodach prądu przemiennego to rachunek impedancji (15.06).

## Typowe pułapki

- **Układ drga z częstością własną.** W stanie ustalonym — z częstością siły wymuszającej.
- **W rezonansie amplituda nieskończona.** Tylko bez tłumienia; tłumienie ją ogranicza.
- **Rezonans dokładnie w $\omega_0$.** Szczyt amplitudy przesuwa się nieco w dół ($\sqrt{\omega_0^2 - 2\beta^2}$); szczyt mocy — dokładnie w $\omega_0$.
- **Tacoma Narrows = rezonans z wiatrem.** To uproszczenie; wiatr nie był okresowy.

## Doświadczenie / symulacja

**Rezonans gumki.** Zawieś ciężarek (np. klucze) na gumce i poruszaj ręką w górę i w dół z różną częstotliwością. Znajdź częstotliwość, przy której drgania są największe, i porównaj z okresem swobodnych drgań. Zwróć uwagę na fazę: poniżej rezonansu ciężarek porusza się razem z ręką, powyżej — przeciwnie.

**Symulacja PhET:** *Rezonans* (*Resonance*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** krzywe rezonansowe dla różnych tłumień i porównanie z symulacją (amplituda stanu ustalonego).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

m, k, F0 = 0.5, 200.0, 1.0
w0 = np.sqrt(k/m)
w = np.linspace(0.5, 40, 800)
for beta in (0.5, 2.0, 5.0):
    A = F0/m/np.sqrt((w0**2 - w**2)**2 + (2*beta*w)**2)
    plt.plot(w/w0, A*100, label=f"β = {beta} 1/s, Q = {w0/(2*beta):.0f}")

beta, wd = 0.5, 0.9*w0                        # sprawdzenie symulacją
sol = solve_ivp(lambda t, s: [s[1], F0/m*np.cos(wd*t) - 2*beta*s[1] - w0**2*s[0]], (0, 40), [0, 0], max_step=0.005)
A_sim = np.max(abs(sol.y[0][sol.t > 30]))
A_th = F0/m/np.sqrt((w0**2 - wd**2)**2 + (2*beta*wd)**2)
print(f"ω = 0,9ω0: amplituda z symulacji {A_sim*100:.2f} cm, ze wzoru {A_th*100:.2f} cm")
plt.xlabel("ω / ω0"); plt.ylabel("A [cm]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Huśtawka ma okres drgań 3 s. Jak często należy ją popychać, żeby rozhuśtać ją najmocniej?

<details>
<summary>Odpowiedź</summary>

Co 3 s (lub co 6 s, 9 s… — w każdym przypadku w zgodnej fazie), w chwili gdy huśtawka zaczyna się oddalać.
</details>

2. Pralka mocno drga tylko przy pewnej prędkości wirowania, a przy większej znowu pracuje spokojnie. Wyjaśnij.

<details>
<summary>Odpowiedź</summary>

Niewyważony bęben działa siłą okresową; przy częstotliwości równej częstotliwości drgań własnych obudowy na sprężynach występuje rezonans. Powyżej rezonansu amplituda maleje.
</details>

3. Śpiewak rozbija kieliszek. Jaki warunek musi spełniać dźwięk?

<details>
<summary>Odpowiedź</summary>

Częstotliwość równa częstotliwości drgań własnych kieliszka i dostatecznie duże natężenie; kieliszek musi mieć dużą dobroć (cienkie szkło dobrej jakości).
</details>

### B. Poziom akademicki

1. Wyprowadź amplitudę drgań wymuszonych metodą zespoloną.

<details>
<summary>Odpowiedź</summary>

$\lvert\tilde A\rvert = \dfrac{F_0/m}{\lvert\omega_0^2 - \omega^2 + 2i\beta\omega\rvert} = \dfrac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\beta^2\omega^2}}$.
</details>

2. Znajdź częstość, przy której amplituda jest największa, różniczkując mianownik.

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{d\omega}[(\omega_0^2 - \omega^2)^2 + 4\beta^2\omega^2] = -4\omega(\omega_0^2 - \omega^2) + 8\beta^2\omega = 0 \Rightarrow \omega^2 = \omega_0^2 - 2\beta^2$.
</details>

3. Pokaż, że średnia moc dostarczana przez siłę wymuszającą wynosi $\bar P = m\beta\omega^2A^2$ i jest największa dokładnie dla $\omega = \omega_0$.

<details>
<summary>Odpowiedź</summary>

Moc średnia = moc tracona na tłumienie: $b\overline{\dot x^2} = 2m\beta\cdot\tfrac12\omega^2A^2$. Wstawiając $A$: $\bar P = \dfrac{F_0^2}{m}\cdot\dfrac{\beta\omega^2}{(\omega_0^2 - \omega^2)^2 + 4\beta^2\omega^2}$; po podzieleniu licznika i mianownika przez $\omega^2$ mianownik $(\omega_0^2/\omega - \omega)^2 + 4\beta^2$ jest najmniejszy dla $\omega = \omega_0$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15 — §15.6: drgania wymuszone i rezonans.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §15.6; wyd. 1: t. 2, §16.9.
- Symulacja PhET *Rezonans*.
