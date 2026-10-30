# 05.02 — Zasada zachowania pędu

> **Moduł:** [05 — Pęd, środek masy i zderzenia](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 9: [§9.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/9-3-zasada-zachowania-pedu) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §9.5 (s. 290)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§9.5–9.6, s. 214](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=226) — PDF z serwera AGH

← [Pęd i popęd siły](01-ped-i-poped.md) · [spis modułu](README.md) · [Zderzenia sprężyste i niesprężyste w 1D i 2D](03-zderzenia.md) →

## Po co to jest

Zasada zachowania pędu pozwala przewidzieć wynik zderzenia, wybuchu albo odrzutu bez wiedzy o siłach działających w jego trakcie — a te siły są zwykle ogromne, krótkotrwałe i nieznane. Wynika wprost z III zasady dynamiki, a w fizyce współczesnej okazuje się jednym z najbardziej podstawowych praw przyrody (związanym z jednorodnością przestrzeni). Tak działa odrzut broni, napęd rakiety, a w fizyce cząstek — odkrycie neutrina.

## Teoria w pigułce

**Układ ciał** dzielimy na siły **wewnętrzne** (między ciałami układu) i **zewnętrzne** (od ciał spoza układu). Pęd układu to suma pędów: $\vec{P} = \sum m_i\vec{v}_i$.

**Zasada zachowania pędu.** Jeśli wypadkowa sił zewnętrznych jest zerowa, całkowity pęd układu jest stały:

$$\sum\vec{F}_{\text{zewn}} = 0 \ \Rightarrow\ \vec{P} = \text{const}.$$

**Skąd to wynika.** Siły wewnętrzne występują parami (III zasada): siła A na B i B na A są przeciwne, więc ich wpływ na sumę pędów się znosi: $\dfrac{d\vec{P}}{dt} = \sum\vec{F}_{\text{zewn}}$.

**Kiedy można stosować.**
- Gdy siły zewnętrzne są zerowe albo się równoważą (ruch po poziomym stole bez tarcia: ciężar i nacisk).
- W krótkich zderzeniach i wybuchach, gdy siły wewnętrzne są o wiele większe niż zewnętrzne (ciężar, tarcie) — pęd jest zachowany w przybliżeniu tuż przed i tuż po zdarzeniu.
- Dla każdej składowej osobno: jeśli siły zewnętrzne nie mają składowej poziomej, zachowana jest pozioma składowa pędu, nawet gdy pionowa się zmienia.

**Odrzut.** Układ początkowo w spoczynku ma pęd zero; po wystrzale lub odepchnięciu części poruszają się w przeciwne strony tak, że $m_1\vec{v}_1 + m_2\vec{v}_2 = 0$. Lżejsza część odlatuje szybciej.

**Pęd a energia.** Pęd jest zachowany w każdym zderzeniu i wybuchu, ale energia kinetyczna — nie: w wybuchu rośnie (kosztem energii chemicznej), w zderzeniu niesprężystym maleje (05.03).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum m_i\vec{v}_i = \sum m_i\vec{v}_i\,'$ | zachowanie pędu | brak (lub pomijalne) siły zewnętrzne |
| $m_1v_1 = m_2v_2$ | odrzut z układu w spoczynku | wartości prędkości, zwroty przeciwne |
| $d\vec{P}/dt = \sum\vec{F}_{\text{zewn}}$ | II zasada dla układu | zawsze |
| $P_x = \text{const}$ | zachowanie składowej | $\sum F_{\text{zewn},x} = 0$ |

## Przykład rozwiązany

**Zadanie 1 — odrzut.** Karabin o masie 4 kg wystrzeliwuje pocisk o masie 10 g z prędkością 400 m/s. Z jaką prędkością odrzuca karabin?

Przed strzałem pęd jest zerowy. Po strzale: $0{,}01\cdot400 + 4\cdot v_k = 0 \Rightarrow v_k = -1\ \mathrm{m/s}$.

Energia kinetyczna pocisku to 800 J, karabinu — tylko 2 J: przy równych pędach energia trafia głównie do lżejszego ciała.

**Zadanie 2 — łyżwiarze.** Łyżwiarze o masach 60 kg i 40 kg stoją na lodzie i odpychają się. Cięższy odjeżdża z prędkością 2 m/s. Z jaką prędkością odjeżdża lżejszy?

$60\cdot2 = 40v \Rightarrow v = 3\ \mathrm{m/s}$ w przeciwną stronę.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Pocisk wystrzelony ukośnie rozpada się w najwyższym punkcie toru na dwie równe części. Jedna z nich spada pionowo w dół (ma po wybuchu prędkość zero). Gdzie upadnie druga, jeśli bez wybuchu pocisk upadłby w odległości $Z$ od działa?

W najwyższym punkcie pocisk ma tylko prędkość poziomą $v$ i znajduje się w odległości $Z/2$. Zachowanie poziomej składowej pędu: $2m\cdot v = m\cdot0 + m\cdot v_2 \Rightarrow v_2 = 2v$. Obie części spadają z tej samej wysokości w tym samym czasie, w którym pocisk przebyłby drugą połowę zasięgu z prędkością $v$. Druga część przebędzie więc $2\cdot Z/2 = Z$ i upadnie w odległości $\tfrac32Z$.

Środek masy obu części upada tam, gdzie upadłby cały pocisk (05.04): $\tfrac12\left(\tfrac12Z + \tfrac32Z\right) = Z$.

## Typowe pułapki

- **Zachowanie pędu przy działaniu siły zewnętrznej.** Wózek hamowany tarciem traci pęd; w zderzeniu trwającym milisekundy to tarcie jest jednak pomijalne.
- **Brak znaków.** Prędkości w przeciwnych kierunkach mają przeciwne znaki — wybierz zwrot osi.
- **Zachowanie energii kinetycznej w wybuchu.** Pęd tak, energia kinetyczna nie.
- **Dodawanie wartości pędów w 2D.** Pęd sumujemy wektorowo — składowa po składowej.

## Doświadczenie / symulacja

**Symulacja PhET:** *Laboratorium zderzeń* (*Collision Lab*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)) — ustaw dwie kule i włącz wektory pędu. Sprawdź, że suma pędów przed i po zderzeniu jest taka sama dla dowolnej sprężystości.

**Odrzut na deskorolce.** Stań na deskorolce (lub krześle biurowym na kółkach) i rzuć piłkę lekarską do przodu. Oszacuj prędkość odrzutu z drogi i czasu, porównaj z $m_pv_p/M$.

**Python:** rozpad pocisku w locie — tory obu części i ich środka masy.

```python
import numpy as np
import matplotlib.pyplot as plt

g, v0, alpha = 9.81, 30.0, np.radians(50)
vx, vy = v0*np.cos(alpha), v0*np.sin(alpha)
t_top = vy/g; x_top = vx*t_top; h_top = vy**2/(2*g)
Z = 2*x_top

t = np.linspace(0, t_top, 100)
plt.plot(vx*t, vy*t - g*t**2/2, "k", label="przed wybuchem")
tf = np.linspace(0, t_top, 100)
y = h_top - g*tf**2/2
plt.plot(np.full_like(tf, x_top), y, label="część 1 (v = 0)")
plt.plot(x_top + 2*vx*tf, y, label="część 2 (2v)")
plt.plot(x_top + vx*tf, y, "--", label="środek masy")
print(f"zasięg bez wybuchu Z = {Z:.1f} m; część 2 upada w {x_top + 2*vx*t_top:.1f} m = 1,5 Z")
plt.xlabel("x [m]"); plt.ylabel("y [m]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Człowiek o masie 50 kg wyskakuje z łodzi o masie 100 kg na brzeg z prędkością 3 m/s. Z jaką prędkością odpłynie łódź?

<details>
<summary>Odpowiedź</summary>

$1{,}5\ \mathrm{m/s}$ w przeciwną stronę.
</details>

2. Spoczywający pocisk o masie 2 kg rozpada się na dwie części. Część o masie 1,2 kg porusza się z prędkością 10 m/s. Z jaką prędkością porusza się druga część?

<details>
<summary>Odpowiedź</summary>

$1{,}2\cdot10 = 0{,}8v \Rightarrow v = 15\ \mathrm{m/s}$ w przeciwną stronę.
</details>

3. Astronauta o masie 80 kg wisi nieruchomo obok stacji kosmicznej i rzuca klucz o masie 2 kg z prędkością 5 m/s. Jak szybko odpłynie w przeciwną stronę?

<details>
<summary>Odpowiedź</summary>

$0{,}125\ \mathrm{m/s}$.
</details>

4. Działo o masie 1000 kg na kołach wystrzeliwuje poziomo kulę o masie 10 kg z prędkością 300 m/s. Oblicz prędkość odrzutu i porównaj energie kinetyczne kuli i działa.

<details>
<summary>Odpowiedź</summary>

$v = 3\ \mathrm{m/s}$; $E_{\text{kuli}} = 450\ \mathrm{kJ}$, $E_{\text{działa}} = 4{,}5\ \mathrm{kJ}$.
</details>

5. Wagon o masie 20 t jedzie z prędkością 2 m/s i zderza się z nieruchomym wagonem o masie 30 t, sczepiając się z nim. Z jaką prędkością jadą razem?

<details>
<summary>Odpowiedź</summary>

$v = 20\cdot2/50 = 0{,}8\ \mathrm{m/s}$.
</details>

### B. Poziom akademicki

1. Człowiek o masie 60 kg przechodzi z rufy na dziób łodzi o masie 120 kg i długości 4 m. Łódź jest początkowo nieruchoma, opór wody pomijamy. O ile przesunie się łódź względem brzegu?

<details>
<summary>Odpowiedź</summary>

Środek masy układu się nie przesuwa: $60(4 - d) = 120d \Rightarrow d = 4\cdot60/180 \approx 1{,}33\ \mathrm{m}$.
</details>

2. Nieruchomy pocisk rozpada się na trzy równe części. Dwie z nich odlatują z prędkościami 10 m/s: jedna na wschód, druga na północ. Jak porusza się trzecia?

<details>
<summary>Odpowiedź</summary>

$\vec{v}_3 = -(10,\ 10)\ \mathrm{m/s}$: wartość $14{,}1\ \mathrm{m/s}$ na południowy zachód.
</details>

3. Jądro o masie $M$ w spoczynku emituje cząstkę alfa o masie $m$ i energii kinetycznej $E_\alpha$. Wyznacz energię kinetyczną odrzutu jądra-produktu (masa $M - m$).

<details>
<summary>Odpowiedź</summary>

Pędy równe: $E_{\text{odrz}} = \dfrac{p^2}{2(M - m)} = E_\alpha\dfrac{m}{M - m}$. Dla rozpadu uranu-238 to ok. 1,7% energii cząstki alfa.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 9 — §9.3: zasada zachowania pędu.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §9.5; wyd. 1: t. 1, §9.5–9.6.
- Symulacja PhET *Laboratorium zderzeń*.
