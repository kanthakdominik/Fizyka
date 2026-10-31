# 06.04 — Toczenie bez poślizgu

> **Moduł:** [06 — Bryła sztywna, statyka i sprężystość](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 11: [§11.1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/11-1-toczenie-sie-cial) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/11-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §11.1–11.3 (s. 375)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§12.1–12.4, s. 297](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=309) — PDF z serwera AGH

← [Moment siły i dynamika ruchu obrotowego](03-moment-sily.md) · [spis modułu](README.md) · [Moment pędu i zasada jego zachowania](05-moment-pedu.md) →

## Po co to jest

Koła, kulki łożysk, piłki, walce — toczenie łączy ruch postępowy z obrotowym. Ten temat odpowiada na zaskakujące pytanie: dlaczego pełna kula stacza się z równi szybciej niż obręcz o tej samej masie i promieniu? Odpowiedź (część energii idzie w obrót) wraca w łożyskach, kołach zamachowych, a nawet przy wyznaczaniu $g$ za pomocą kulki na równi, gdzie łatwo popełnić błąd 40%.

## Teoria w pigułce

**Toczenie bez poślizgu.** Punkt styku z podłożem chwilowo spoczywa. Stąd **warunek toczenia**:

$$v_{\mathrm{SM}} = \omega R, \qquad a_{\mathrm{SM}} = \varepsilon R.$$

Punkt na szczycie koła ma prędkość $2v_{\mathrm{SM}}$, punkt styku — zero. Ruch można opisać jako złożenie postępowego ruchu środka i obrotu wokół środka albo jako czysty obrót wokół punktu styku.

**Energia kinetyczna toczenia:**

$$E_k = \tfrac12Mv^2 + \tfrac12I_{\mathrm{SM}}\omega^2 = \tfrac12Mv^2\left(1 + \frac{I_{\mathrm{SM}}}{MR^2}\right).$$

Współczynnik $\beta = I_{\mathrm{SM}}/(MR^2)$ mówi, jaka część energii jest „uwięziona” w obrocie: kula $\tfrac25$, walec $\tfrac12$, obręcz $1$.

**Staczanie z równi o kącie $\alpha$.** Z zasady zachowania energii (tarcie statyczne nie wykonuje pracy, bo punkt styku się nie przesuwa):

$$v = \sqrt{\frac{2gh}{1 + \beta}}, \qquad a = \frac{g\sin\alpha}{1 + \beta}.$$

Wynik nie zależy od masy ani promienia — tylko od kształtu (rozkładu masy). Kolejność na mecie: kula ($a = \tfrac57g\sin\alpha$), walec ($\tfrac23$), obręcz ($\tfrac12$); ciało ślizgające się bez tarcia wygrywa ze wszystkimi ($a = g\sin\alpha$).

**Rola tarcia.** Tarcie statyczne jest potrzebne, żeby ciało się toczyło, a nie ślizgało — to ono daje moment siły rozkręcający bryłę. Jeśli współczynnik tarcia jest za mały, bryła toczy się z poślizgiem.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $v_{\mathrm{SM}} = \omega R$ | warunek toczenia | brak poślizgu |
| $E_k = \tfrac12Mv^2(1 + \beta)$ | energia toczenia | $\beta = I_{\mathrm{SM}}/(MR^2)$ |
| $a = g\sin\alpha/(1 + \beta)$ | przyspieszenie na równi | toczenie bez poślizgu |
| $T = \dfrac{\beta}{1 + \beta}Mg\sin\alpha$ | potrzebne tarcie statyczne | j.w. |
| $\mu_s \ge \dfrac{\beta}{1 + \beta}\tan\alpha$ | warunek toczenia bez poślizgu | j.w. |

## Przykład rozwiązany

**Zadanie.** Kula, walec i obręcz staczają się bez poślizgu z wysokości 1 m. Oblicz prędkość każdego z ciał na dole.

$v = \sqrt{2gh/(1 + \beta)}$:
- kula ($\beta = 0{,}4$): $v = \sqrt{19{,}62/1{,}4} \approx 3{,}74\ \mathrm{m/s}$,
- walec ($\beta = 0{,}5$): $v \approx 3{,}62\ \mathrm{m/s}$,
- obręcz ($\beta = 1$): $v = \sqrt{gh} \approx 3{,}13\ \mathrm{m/s}$.

Dla porównania: klocek bez tarcia — $4{,}43\ \mathrm{m/s}$. Obręcz połowę energii „trzyma” w obrocie.

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie z momentów sił.** Dla walca na równi: wzdłuż równi $Mg\sin\alpha - T = Ma$; względem środka masy $TR = I\varepsilon = \tfrac12MR^2\cdot a/R$. Stąd $T = \tfrac12Ma$ i

$$a = \frac{g\sin\alpha}{1 + 1/2} = \frac23g\sin\alpha, \qquad T = \frac13Mg\sin\alpha.$$

Szybciej: momenty względem punktu styku (chwilowa oś obrotu, $I_P = I + MR^2$). Jedyną siłą z momentem jest składowa ciężaru: $Mg\sin\alpha\cdot R = \tfrac32MR^2\varepsilon$.

**Kula do kręgli puszczona ślizgiem.** Kula rzucona z prędkością $v_0$ bez obrotu najpierw się ślizga; tarcie kinetyczne hamuje ją i jednocześnie rozkręca. Toczenie zaczyna się, gdy $v = \omega R$. Z równań $\dot{v} = -\mu g$, $\dot{\omega} = \dfrac{\mu MgR}{\tfrac25MR^2}$ wynika, że w tej chwili $v = \tfrac57v_0$ — niezależnie od $\mu$.

## Typowe pułapki

- **$v = \sqrt{2gh}$ dla toczącego się ciała.** Pomija energię obrotu.
- **Tarcie toczenia wykonuje pracę.** Przy toczeniu bez poślizgu tarcie statyczne nie wykonuje pracy — energia mechaniczna jest zachowana.
- **Wynik zależy od masy lub promienia.** Zależy tylko od $\beta$, czyli od kształtu.
- **Wszystkie punkty koła mają prędkość $v$.** Górny punkt ma $2v$, punkt styku — zero.

## Doświadczenie / symulacja

**Wyścig na równi.** Ustaw deskę pod niewielkim kątem i puszczaj parami: pełną puszkę, pustą rurę, piłkę tenisową, kulkę szklaną. Zmierz czasy (np. telefonem w zwolnionym tempie albo *Acoustic Stopwatch*) i porównaj stosunki przyspieszeń z $1/(1 + \beta)$.

**$g$ z kulki na równi.** Wyznacz $g$ z czasu staczania kulki stalowej po rynience. Porównaj wynik obliczony ze wzorem dla klocka ($a = g\sin\alpha$) i dla kuli ($a = \tfrac57g\sin\alpha$) — który jest bliżej 9,81 m/s²?

**Python:** symulacja kuli puszczonej ślizgiem — przejście od poślizgu do toczenia.

```python
import numpy as np
import matplotlib.pyplot as plt

g, mu, R, v0 = 9.81, 0.2, 0.11, 8.0          # kula do kręgli
dt = 1e-4
t, v, w = [0.0], [v0], [0.0]
while v[-1] - w[-1]*R > 1e-6:                 # poślizg trwa, dopóki v > ωR
    v.append(v[-1] - mu*g*dt)
    w.append(w[-1] + mu*g/(0.4*R)*dt)          # ε = μMgR / (2/5 MR²)
    t.append(t[-1] + dt)
print(f"toczenie od t = {t[-1]:.3f} s, v = {v[-1]:.3f} m/s (5/7·v0 = {5/7*v0:.3f})")
plt.plot(t, v, label="v środka"); plt.plot(t, np.array(w)*R, label="ωR")
plt.xlabel("t [s]"); plt.ylabel("[m/s]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Koło samochodu o promieniu 0,3 m toczy się bez poślizgu, samochód jedzie 72 km/h. Oblicz prędkość kątową koła oraz prędkość najwyższego i najniższego punktu opony względem drogi.

<details>
<summary>Odpowiedź</summary>

$\omega \approx 66{,}7\ \mathrm{rad/s}$; górny punkt $40\ \mathrm{m/s}$, dolny $0$.
</details>

2. Jaka część energii kinetycznej toczącej się pełnej kuli przypada na ruch obrotowy?

<details>
<summary>Odpowiedź</summary>

$\dfrac{\beta}{1 + \beta} = \dfrac{0{,}4}{1{,}4} = \dfrac27 \approx 29\%$.
</details>

3. Walec stacza się bez poślizgu z równi o kącie $30^\circ$ i długości 2 m. Oblicz przyspieszenie i prędkość na dole.

<details>
<summary>Odpowiedź</summary>

$a = \tfrac23g\sin30^\circ \approx 3{,}27\ \mathrm{m/s^2}$; $v = \sqrt{2\cdot3{,}27\cdot2} \approx 3{,}62\ \mathrm{m/s}$.
</details>

4. Puszka z zupą (prawie pełny walec) i pusta puszka (prawie obręcz) o tych samych wymiarach staczają się z równi. Która będzie pierwsza? Czy zależy to od masy puszek?

<details>
<summary>Odpowiedź</summary>

Pełna (mniejsze $\beta$). Nie zależy od masy ani promienia, tylko od rozkładu masy.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Jo-jo to walec o promieniu $R$ i masie $M$ z nicią nawiniętą na oś o promieniu $r = R/3$. Oblicz przyspieszenie opadania.

<details>
<summary>Odpowiedź</summary>

$a = \dfrac{g}{1 + I/(Mr^2)} = \dfrac{g}{1 + \tfrac12\cdot9} = \dfrac{g}{5{,}5} \approx 1{,}78\ \mathrm{m/s^2}$.
</details>

2. Jaki najmniejszy współczynnik tarcia statycznego pozwala pełnej kuli staczać się bez poślizgu z równi o kącie $45^\circ$?

<details>
<summary>Odpowiedź</summary>

$\mu_s \ge \tfrac27\tan45^\circ \approx 0{,}29$.
</details>

3. Pokaż, że kula do kręgli rzucona ślizgiem z prędkością $v_0$ zaczyna toczyć się z prędkością $\tfrac57v_0$. Ile energii traci na tarcie?

<details>
<summary>Odpowiedź</summary>

Moment pędu względem punktu na podłodze jest zachowany (tarcie przechodzi przez ten punkt): $MRv_0 = MRv + \tfrac25MR^2\cdot\tfrac vR \Rightarrow v = \tfrac57v_0$. Energia końcowa $\tfrac12Mv^2\cdot\tfrac75 = \tfrac57\cdot\tfrac12Mv_0^2$ — traci $\tfrac27$ energii.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 3.1 — toczenie bez poślizgu — energia ruchu postępowego i obrotowego ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2024, zad. 2.1 — stosunek energii kinetycznej ruchu postępowego do całkowitej toczącego się walca ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2024, zad. 2.2 — przyspieszenie środka masy toczącego się walca ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2025, zad. 2.1 — walce: momenty bezwładności, energie i prędkości (temat pomocniczy) ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2025, zad. 2.2 — przyspieszenie walca toczącego się po równi ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 11 — §11.1: toczenie się ciał, z przykładami staczania z równi.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §11.1–11.3; wyd. 1: t. 1, §12.1–12.4 (w tym jo-jo).
