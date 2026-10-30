# 05.05 — Układy o zmiennej masie — rakieta

> **Moduł:** [05 — Pęd, środek masy i zderzenia](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 9: [§9.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/9-7-naped-rakietowy) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §9.9 (s. 304)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§9.7, s. 219](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=231) — PDF z serwera AGH

← [Środek masy układu i bryły](04-srodek-masy.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Rakieta nie ma się od czego odepchnąć — w próżni napędza ją wyłącznie zasada zachowania pędu: wyrzucając gazy do tyłu, sama przyspiesza do przodu. Ponieważ jej masa maleje w trakcie lotu, wzór $F = ma$ nie wystarcza i trzeba wrócić do $F = dp/dt$. Wynik — wzór Ciołkowskiego — wyjaśnia, dlaczego rakiety są w 90% paliwem i dlaczego mają kilka stopni.

## Teoria w pigułce

**Model.** Rakieta o chwilowej masie $m$ porusza się z prędkością $v$. W czasie $dt$ wyrzuca masę gazów $\lvert dm\rvert$ z prędkością $u$ **względem rakiety** (do tyłu). Siły zewnętrzne na razie pomijamy (lot w próżni z dala od planet).

**Bilans pędu** w układzie inercjalnym, przed i po czasie $dt$:

$$mv = (m + dm)(v + dv) + (-dm)(v - u).$$

($dm < 0$, bo masa rakiety maleje; $-dm$ to masa wyrzuconych gazów.) Po wymnożeniu i pominięciu iloczynu $dm\,dv$:

$$m\,dv = -u\,dm.$$

**Siła ciągu.** Dzieląc przez $dt$: $m\dfrac{dv}{dt} = u\left\lvert\dfrac{dm}{dt}\right\rvert = F_{\text{ciągu}}$. Ciąg to iloczyn prędkości wypływu gazów i masowego natężenia przepływu.

**Wzór Ciołkowskiego.** Całkując od masy początkowej $m_0$ do końcowej $m_k$:

$$\Delta v = u\ln\frac{m_0}{m_k}.$$

Przyrost prędkości zależy tylko od prędkości wypływu i od **stosunku mas**, a nie od tego, jak szybko paliwo jest spalane. Logarytm rośnie bardzo wolno: żeby podwoić $\Delta v$, trzeba podnieść stosunek mas do kwadratu.

**Z grawitacją** (start pionowy, $g$ stałe): $v(t) = u\ln\dfrac{m_0}{m(t)} - gt$. Rakieta oderwie się od ziemi tylko wtedy, gdy ciąg przekracza ciężar: $u\lvert\dot{m}\rvert > m_0g$.

**Rakiety wielostopniowe.** Zrzucenie pustego zbiornika po wypaleniu stopnia sprawia, że kolejny stopień nie musi rozpędzać martwej masy — całkowite $\Delta v$ jest większe niż dla jednej rakiety o tej samej masie paliwa.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $F_{\text{ciągu}} = u\lvert dm/dt\rvert$ | siła ciągu | $u$ — prędkość gazów względem rakiety |
| $\Delta v = u\ln(m_0/m_k)$ | wzór Ciołkowskiego | brak sił zewnętrznych |
| $v(t) = u\ln\dfrac{m_0}{m(t)} - gt$ | start pionowy | $g$ stałe, bez oporu powietrza |
| $F = v\,dm/dt$ | siła potrzebna do ładowania masy na taśmę | masa dołączana z prędkością zerową |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Rakieta ma prędkość wypływu gazów $u = 3\ \mathrm{km/s}$, a stosunek masy początkowej do końcowej wynosi 10. Jaki przyrost prędkości uzyska w próżni? Ile wynosi ciąg, gdy spala 1000 kg paliwa na sekundę?

$\Delta v = 3000\ln10 \approx 6{,}9\ \mathrm{km/s}$ — mniej niż prędkość orbitalna (ok. 7,8 km/s). $F = 3000\cdot1000 = 3\ \mathrm{MN}$.

**Zadanie 2 — dlaczego stopnie.** Rakieta o masie 100 t zawiera 90 t paliwa i 10 t konstrukcji (bez ładunku). Porównaj $\Delta v$ rakiety jednostopniowej i dwustopniowej, w której każdy stopień ma 45 t paliwa i 5 t konstrukcji.

- Jeden stopień: $\Delta v = u\ln(100/10) \approx 2{,}30u$.
- Dwa stopnie: pierwszy spala 45 t ($100 \to 55$ t), zrzuca 5 t konstrukcji; drugi: $50 \to 5$ t.
  $\Delta v = u\left(\ln\dfrac{100}{55} + \ln\dfrac{50}{5}\right) \approx (0{,}60 + 2{,}30)u = 2{,}90u$.

Dla $u = 3\ \mathrm{km/s}$: 6,9 wobec 8,7 km/s — dopiero dwa stopnie pozwalają wejść na orbitę.

**Zadanie 3 — start z Ziemi.** Rakieta o masie 1000 kg (w tym 800 kg paliwa) spala 10 kg/s z prędkością wypływu 2000 m/s, startując pionowo. Jaką prędkość ma po wypaleniu paliwa (pomiń opór powietrza i zmianę $g$)?

Ciąg $20\ \mathrm{kN} > m_0g \approx 9{,}8\ \mathrm{kN}$ — rakieta wystartuje. Czas pracy silnika: 80 s.

$v = 2000\ln5 - 9{,}81\cdot80 \approx 3219 - 785 \approx 2430\ \mathrm{m/s}$.

Strata grawitacyjna $gt$ jest tym mniejsza, im krócej pracuje silnik — dlatego rakiety startują z dużym ciągiem.

## Typowe pułapki

- **Rakieta odpycha się od powietrza.** Nie — działa w próżni lepiej niż w atmosferze. Odpycha się od własnych gazów.
- **$F = ma$ z $m$ stałym.** Masa maleje; trzeba bilansować pęd.
- **Prędkość gazów względem ziemi.** We wzorze Ciołkowskiego $u$ to prędkość względem rakiety.
- **Szybsze spalanie daje większe $\Delta v$.** W próżni nie; przy starcie z Ziemi zmniejsza tylko straty grawitacyjne.

## Doświadczenie / symulacja

**Rakieta z balonu.** Przewlecz słomkę przez długą napiętą żyłkę, przyklej do niej nadmuchany balon i puść. Zmierz zasięg dla różnych objętości balonu. (Opór powietrza jest tu bardzo duży, ale zasada działania ta sama.)

**Rakieta wodna.** Butelka PET z wodą i sprężonym powietrzem to rakieta, w której „paliwem” jest woda wyrzucana do tyłu. Porównaj wysokość lotu dla różnych ilości wody — za mało i za dużo daje gorszy wynik.

**Python:** prędkość rakiety jedno- i dwustopniowej w funkcji czasu.

```python
import numpy as np
import matplotlib.pyplot as plt

u, rate = 3000.0, 1000.0                 # prędkość wypływu [m/s], spalanie [kg/s]

def burn(m0, fuel, v0=0.0, t0=0.0):
    t = np.linspace(0, fuel/rate, 200)
    m = m0 - rate*t
    return t0 + t, v0 + u*np.log(m0/m)

t1, v1 = burn(100e3, 90e3)
ta, va = burn(100e3, 45e3)
tb, vb = burn(50e3, 45e3, va[-1], ta[-1])      # po zrzuceniu 5 t konstrukcji
print(f"jednostopniowa: {v1[-1]/1000:.2f} km/s, dwustopniowa: {vb[-1]/1000:.2f} km/s")

plt.plot(t1, v1/1000, label="1 stopień")
plt.plot(np.r_[ta, tb], np.r_[va, vb]/1000, label="2 stopnie")
plt.xlabel("t [s]"); plt.ylabel("v [km/s]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Wyjaśnij, dlaczego rakieta może przyspieszać w próżni, gdzie nie ma się od czego odepchnąć.

<details>
<summary>Odpowiedź</summary>

Z zasady zachowania pędu: gazy wyrzucone do tyłu mają pęd skierowany do tyłu, więc rakieta zyskuje pęd do przodu. Siła działa między rakietą a gazami (III zasada).
</details>

2. Strażak trzyma wąż, z którego wypływa 10 kg wody na sekundę z prędkością 20 m/s. Jaką siłą musi trzymać wąż?

<details>
<summary>Odpowiedź</summary>

$F = \mu v = 200\ \mathrm{N}$ (siła odrzutu).
</details>

### B. Poziom akademicki

1. Jaki musi być stosunek mas rakiety jednostopniowej, żeby osiągnąć $\Delta v = 9{,}5\ \mathrm{km/s}$ (orbita z uwzględnieniem strat) przy prędkości wypływu 4,4 km/s (wodór i tlen)?

<details>
<summary>Odpowiedź</summary>

$m_0/m_k = e^{9{,}5/4{,}4} \approx 8{,}7$ — paliwo musi stanowić ok. 88% masy startowej.
</details>

2. Wyprowadź wzór Ciołkowskiego z $m\,dv = -u\,dm$.

<details>
<summary>Odpowiedź</summary>

$\displaystyle\int_{v_0}^{v}dv' = -u\int_{m_0}^{m}\frac{dm'}{m'} \Rightarrow v - v_0 = u\ln\frac{m_0}{m}$.
</details>

3. Piasek spada pionowo na poziomą taśmę transportera z szybkością $\mu = 20\ \mathrm{kg/s}$. Taśma porusza się ze stałą prędkością 2 m/s. Jaką siłą i z jaką mocą musi ją napędzać silnik? Porównaj moc z przyrostem energii kinetycznej piasku na sekundę.

<details>
<summary>Odpowiedź</summary>

$F = \mu v = 40\ \mathrm{N}$, $P = Fv = 80\ \mathrm{W}$. Energia kinetyczna rośnie o $\tfrac12\mu v^2 = 40\ \mathrm{W}$ — połowa mocy zamienia się w ciepło (tarcie przy rozpędzaniu piasku na taśmie).
</details>

4. Dla rakiety z zadania 3 w przykładzie oblicz wysokość w chwili wypalenia paliwa. (Wskazówka: $\int\ln\dfrac{m_0}{m_0 - \mu t}dt$ policz numerycznie albo przez podstawienie.)

<details>
<summary>Odpowiedź</summary>

$h = \displaystyle\int_0^{80}\left[2000\ln\frac{1000}{1000 - 10t} - 9{,}81t\right]dt \approx 64{,}2\ \mathrm{km}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 9 — §9.7: napęd rakietowy.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §9.9; wyd. 1: t. 1, §9.7.
