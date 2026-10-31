# 05.03 — Zderzenia sprężyste i niesprężyste w 1D i 2D

> **Moduł:** [05 — Pęd, środek masy i zderzenia](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 9: [§9.4–9.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/9-4-rodzaje-zderzen) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §9.6–9.8 (s. 294)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§10.3–10.6, s. 239](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=251) — PDF z serwera AGH

← [Zasada zachowania pędu](02-zasada-zachowania-pedu.md) · [spis modułu](README.md) · [Środek masy układu i bryły](04-srodek-masy.md) →

## Po co to jest

Zderzenia są wszędzie: samochody na skrzyżowaniu, kule bilardowe, cząsteczki gazu (11), neutrony w reaktorze (22), cząstki w akceleratorze (24). Zasada zachowania pędu obowiązuje w każdym zderzeniu, a energia kinetyczna — tylko w sprężystym. Łącząc te dwa prawa, możemy przewidzieć prędkości po zderzeniu, nie wiedząc nic o siłach działających w jego trakcie.

## Teoria w pigułce

**Rodzaje zderzeń.**

| Rodzaj | Pęd | Energia kinetyczna | Przykład |
|---|---|---|---|
| sprężyste | zachowany | zachowana | kule bilardowe, cząsteczki gazu |
| niesprężyste | zachowany | maleje | większość zderzeń makroskopowych |
| doskonale niesprężyste | zachowany | maleje najbardziej | ciała sklejają się (wahadło balistyczne, sczepienie wagonów) |

**Doskonale niesprężyste w 1D.** Ciała poruszają się po zderzeniu razem:

$$m_1v_1 + m_2v_2 = (m_1 + m_2)V.$$

**Sprężyste w 1D** (czołowe). Z zachowania pędu i energii:

$$v_1' = \frac{m_1 - m_2}{m_1 + m_2}v_1 + \frac{2m_2}{m_1 + m_2}v_2, \qquad v_2' = \frac{2m_1}{m_1 + m_2}v_1 + \frac{m_2 - m_1}{m_1 + m_2}v_2.$$

Przypadki szczególne (ciało 2 w spoczynku):
- równe masy — ciała **wymieniają się prędkościami** (wahadło Newtona, bilard);
- $m_1 \ll m_2$ — lekkie ciało odbija się z tą samą szybkością (piłka od ściany);
- $m_1 \gg m_2$ — ciężkie jedzie dalej prawie bez zmian, lekkie odlatuje z prędkością $2v_1$.

**Współczynnik restytucji** mierzy sprężystość: $e = \dfrac{\lvert v_2' - v_1'\rvert}{\lvert v_1 - v_2\rvert}$ (stosunek prędkości oddalania i zbliżania). $e = 1$ — sprężyste, $e = 0$ — doskonale niesprężyste. Dla piłki odbijającej się od podłogi $e = \sqrt{h_2/h_1}$.

**Zderzenia w 2D.** Zachowanie pędu zapisujemy osobno dla składowych $x$ i $y$. Przy sprężystym zderzeniu równych mas, gdy jedna spoczywała, kule rozbiegają się pod kątem prostym.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum m\vec{v} = \sum m\vec{v}\,'$ | zachowanie pędu | każde zderzenie (krótkie, siły wewnętrzne dominują) |
| $\sum\tfrac12mv^2 = \sum\tfrac12mv'^2$ | zachowanie energii kinetycznej | tylko zderzenie sprężyste |
| $V = \dfrac{m_1v_1 + m_2v_2}{m_1 + m_2}$ | doskonale niesprężyste | ciała po zderzeniu razem |
| $v_1' = \dfrac{m_1 - m_2}{m_1 + m_2}v_1$, $\ v_2' = \dfrac{2m_1}{m_1 + m_2}v_1$ | sprężyste, ciało 2 spoczywa | czołowe (1D) |
| $v_1 - v_2 = -(v_1' - v_2')$ | sprężyste: prędkość względna zmienia znak | 1D |
| $v = \dfrac{m + M}{m}\sqrt{2gh}$ | wahadło balistyczne | pocisk $m$ grzęźnie w klocku $M$ |

## Przykład rozwiązany

**Zadanie 1 — stłuczka.** Samochód o masie 1000 kg jadący z prędkością 20 m/s uderza w tył stojącego samochodu o masie 1500 kg i oba sczepiają się. Oblicz wspólną prędkość i energię zamienioną na odkształcenia i ciepło.

$V = \dfrac{1000\cdot20}{2500} = 8\ \mathrm{m/s}$. Energia przed: 200 kJ, po: $\tfrac12\cdot2500\cdot64 = 80\ \mathrm{kJ}$. Strata: **120 kJ** (60%).

**Zadanie 2 — wahadło balistyczne.** Pocisk o masie 10 g wbija się w drewniany klocek o masie 2 kg zawieszony na linkach. Klocek z pociskiem wznosi się na wysokość 5 cm. Oblicz prędkość pocisku.

Dwa etapy, dwa różne prawa:
1. **Zderzenie** (doskonale niesprężyste, krótkie) — zachowanie pędu: $mv = (m + M)V$.
2. **Wznoszenie** — zachowanie energii: $\tfrac12(m + M)V^2 = (m + M)gh \Rightarrow V = \sqrt{2gh} \approx 0{,}99\ \mathrm{m/s}$.

$v = \dfrac{2{,}01}{0{,}01}\cdot0{,}99 \approx 199\ \mathrm{m/s}$.

Energii nie można użyć w etapie 1 — ponad 99% energii pocisku zamienia się w ciepło.

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie wzorów dla zderzenia sprężystego.** Z zachowania pędu i energii (ciało 2 spoczywa):

$$m_1(v_1 - v_1') = m_2v_2', \qquad m_1(v_1^2 - v_1'^2) = m_2v_2'^2.$$

Dzieląc drugie przez pierwsze ($v_1 \ne v_1'$): $v_1 + v_1' = v_2'$. Wstawiając do pierwszego, dostajemy wzory z tabeli.

**Zadanie 2D.** Krążek hokejowy o masie 0,2 kg i prędkości 5 m/s uderza sprężyście w identyczny spoczywający krążek i odbija się pod kątem $30^\circ$ do pierwotnego kierunku. Oblicz prędkości po zderzeniu.

Dla równych mas i zderzenia sprężystego kąt między prędkościami po zderzeniu wynosi $90^\circ$ (z $\vec{v}_1 = \vec{v}_1' + \vec{v}_2'$ i $v_1^2 = v_1'^2 + v_2'^2$ — twierdzenie Pitagorasa). Drugi krążek odlatuje pod kątem $60^\circ$ po drugiej stronie, a prędkości to rzuty: $v_1' = 5\cos30^\circ \approx 4{,}33\ \mathrm{m/s}$, $v_2' = 5\cos60^\circ = 2{,}5\ \mathrm{m/s}$.

## Typowe pułapki

- **Zachowanie energii w zderzeniu niesprężystym.** Energia kinetyczna nie jest zachowana; pęd — tak.
- **Wahadło balistyczne „jednym prawem”.** Zderzenie: pęd; wznoszenie: energia. Pomylenie kolejności daje wynik zły o czynnik rzędu $\sqrt{M/m}$.
- **Znaki prędkości.** Ciało odbijające się ma prędkość ujemną (przy osi skierowanej do przodu).
- **„Zderzenie sprężyste = ciała odbijają się”.** Ciała mogą się odbić także w zderzeniu niesprężystym; o sprężystości decyduje bilans energii.

## Doświadczenie / symulacja

**Współczynnik restytucji piłek.** Eksperyment *(In)elastic collision* w phyphox mierzy czasy między odbiciami piłki od podłogi i oblicza współczynnik restytucji i wysokości. Porównaj piłkę tenisową, pingpongową, kauczukową i plastelinową kulkę.

**Symulacja PhET:** *Laboratorium zderzeń* — zmieniaj sprężystość od 0 do 100% i obserwuj energię kinetyczną przed i po.

**Python:** prędkości po czołowym zderzeniu sprężystym w funkcji stosunku mas.

```python
import numpy as np
import matplotlib.pyplot as plt

r = np.logspace(-2, 2, 400)              # m1/m2
v1 = 1.0
v1p = (r - 1)/(r + 1)*v1
v2p = 2*r/(r + 1)*v1
frac = 1 - v1p**2                        # część energii przekazana ciału 2
for ratio in (1/12, 1, 12):
    print(f"m1/m2 = {ratio:6.3f}: v1' = {(ratio-1)/(ratio+1):+.3f}, v2' = {2*ratio/(ratio+1):.3f}, przekazana energia {1-((ratio-1)/(ratio+1))**2:.3f}")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].semilogx(r, v1p, label="v1'"); ax[0].semilogx(r, v2p, label="v2'")
ax[0].set_xlabel("m1/m2"); ax[0].set_ylabel("v'/v1"); ax[0].grid(True, which="both"); ax[0].legend()
ax[1].semilogx(r, frac); ax[1].set_xlabel("m1/m2"); ax[1].set_ylabel("przekazana część energii")
ax[1].grid(True, which="both")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Kulka plasteliny o masie 2 kg (to duża kulka!) lecąca z prędkością 3 m/s przykleja się do spoczywającego wózka o masie 1 kg. Oblicz prędkość po zderzeniu i utraconą energię.

<details>
<summary>Odpowiedź</summary>

$V = 2\ \mathrm{m/s}$; energia z 9 J spada do 6 J — strata 3 J.
</details>

2. Kula o masie 1 kg i prędkości 4 m/s uderza czołowo i sprężyście w spoczywającą kulę o masie 3 kg. Oblicz prędkości po zderzeniu.

<details>
<summary>Odpowiedź</summary>

$v_1' = \tfrac{1-3}{4}\cdot4 = -2\ \mathrm{m/s}$ (odbija się), $v_2' = \tfrac{2}{4}\cdot4 = 2\ \mathrm{m/s}$.
</details>

3. Piłkę upuszczono z wysokości 1 m; odbiła się na 64 cm. Ile wynosi współczynnik restytucji i jaka część energii została utracona?

<details>
<summary>Odpowiedź</summary>

$e = \sqrt{0{,}64} = 0{,}8$; utracono 36% energii.
</details>

4. Pocisk o masie 5 g wbija się w klocek o masie 1 kg wiszący na linkach, który wznosi się na wysokość 8 cm. Oblicz prędkość pocisku.

<details>
<summary>Odpowiedź</summary>

$V = \sqrt{2g\cdot0{,}08} \approx 1{,}25\ \mathrm{m/s}$; $v = \tfrac{1{,}005}{0{,}005}\cdot1{,}25 \approx 252\ \mathrm{m/s}$.
</details>

5. W wahadle Newtona puszczamy jedną kulkę — odskakuje jedna kulka z drugiej strony. Dlaczego nie dwie kulki z połową prędkości?

<details>
<summary>Odpowiedź</summary>

Dwie kulki z połową prędkości miałyby ten sam pęd, ale tylko połowę energii kinetycznej. Zderzenia są prawie sprężyste, więc muszą być zachowane jednocześnie pęd i energia — spełnia to tylko jedna kulka z pełną prędkością.
</details>

### B. Poziom akademicki

1. Pokaż, że w doskonale niesprężystym zderzeniu ciała $m_1$ z ciałem spoczywającym $m_2$ traci się ułamek energii równy $\dfrac{m_2}{m_1 + m_2}$.

<details>
<summary>Odpowiedź</summary>

$E' = \dfrac{(m_1v)^2}{2(m_1 + m_2)}$, $\dfrac{E'}{E} = \dfrac{m_1}{m_1 + m_2}$, strata $= 1 - \dfrac{m_1}{m_1 + m_2}$.
</details>

2. Neutron zderza się czołowo i sprężyście ze spoczywającym jądrem węgla (masa 12 razy większa). Jaką część energii zachowuje? Ile takich zderzeń jest potrzebnych, żeby spowolnić go od 2 MeV do 0,025 eV? (W rzeczywistości zderzenia nie są czołowe i potrzeba ich ok. 110.)

<details>
<summary>Odpowiedź</summary>

Zachowuje $\left(\tfrac{11}{13}\right)^2 \approx 0{,}716$; $n = \dfrac{\ln(0{,}025/2\cdot10^6)}{\ln0{,}716} \approx 55$.
</details>

3. Pokaż, że w zderzeniu sprężystym równych mas, gdy jedna spoczywała, prędkości po zderzeniu są prostopadłe.

<details>
<summary>Odpowiedź</summary>

$\vec{v} = \vec{v}_1' + \vec{v}_2'$, podnosząc do kwadratu: $v^2 = v_1'^2 + v_2'^2 + 2\vec{v}_1'\cdot\vec{v}_2'$. Z zachowania energii $v^2 = v_1'^2 + v_2'^2$, więc $\vec{v}_1'\cdot\vec{v}_2' = 0$.
</details>

4. Piłka o współczynniku restytucji $e$ spada z wysokości $h$. Oblicz całkowitą drogę i całkowity czas odbijania się do zatrzymania.

<details>
<summary>Odpowiedź</summary>

Wysokości $h, e^2h, e^4h, \dots$: droga $s = h\dfrac{1 + e^2}{1 - e^2}$; czas $t = \sqrt{\dfrac{2h}{g}}\cdot\dfrac{1 + e}{1 - e}$ (szeregi geometryczne — czas jest skończony).
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 2.2 — prędkości krążków po zderzeniu doskonale sprężystym ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 9 — §9.4 (rodzaje zderzeń) i §9.5 (zderzenia w wielu wymiarach).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §9.6–9.8; wyd. 1: t. 1, §10.3–10.6.
- Symulacja PhET *Laboratorium zderzeń*.
