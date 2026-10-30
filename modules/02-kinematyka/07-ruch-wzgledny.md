# 02.07 — Ruch względny i transformacja Galileusza

> **Moduł:** [02 — Kinematyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 4: [§4.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/4-5-ruch-wzgledny-w-jednym-i-dwoch-wymiarach) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/4-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §4.6–4.7 (s. 98)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§4.8–4.9, s. 74](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=86) — PDF z serwera AGH

← [Ruch po okręgu: jednostajny i niejednostajny](06-ruch-po-okregu.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Ruch zawsze opisujemy względem czegoś: pasażer w pociągu siedzi, a dla obserwatora na peronie pędzi z prędkością pociągu. Składanie prędkości względnych jest potrzebne w zadaniach o łodziach na rzece i samolotach w wietrze, a idea, że prawa fizyki są takie same w układach poruszających się jednostajnie, prowadzi prosto do szczególnej teorii względności (moduł 19).

## Teoria w pigułce

**Układy odniesienia.** Mamy układ $S$ (np. brzeg) i układ $S'$ (np. woda), który porusza się względem $S$ ze stałą prędkością $\vec{V}$. Położenia tego samego ciała w obu układach wiąże **transformacja Galileusza**:

$$\vec{r} = \vec{r}\,' + \vec{V}t, \qquad t = t'.$$

**Składanie prędkości.** Różniczkując po czasie:

$$\vec{v} = \vec{v}\,' + \vec{V},$$

czyli prędkość względem brzegu = prędkość względem wody + prędkość wody względem brzegu. Użyteczny zapis z indeksami: $\vec{v}_{A/C} = \vec{v}_{A/B} + \vec{v}_{B/C}$ — indeksy „skracają się” w środku.

**Prędkość względna** dwóch ciał: $\vec{v}_{A/B} = \vec{v}_A - \vec{v}_B$. Pociągi jadące naprzeciw siebie z prędkościami 72 i 54 km/h zbliżają się z prędkością 126 km/h.

**Przyspieszenie jest takie samo** w obu układach, bo $\vec{V}$ jest stałe: $\vec{a} = \vec{a}\,'$. Dlatego zasady dynamiki Newtona obowiązują w każdym układzie poruszającym się ze stałą prędkością względem układu inercjalnego (zasada względności Galileusza). W układach przyspieszających tak nie jest — temat 03.06.

**Granica stosowalności.** Transformacja Galileusza zakłada, że czas płynie tak samo w obu układach. Przy prędkościach porównywalnych z prędkością światła trzeba ją zastąpić transformacją Lorentza (19.03).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec{r} = \vec{r}\,' + \vec{V}t$, $\ t = t'$ | transformacja Galileusza | $\vec{V} = \text{const}$, $V \ll c$ |
| $\vec{v} = \vec{v}\,' + \vec{V}$ | składanie prędkości | j.w. |
| $\vec{v}_{A/B} = \vec{v}_A - \vec{v}_B$ | prędkość względna | — |
| $\vec{a} = \vec{a}\,'$ | przyspieszenie niezmiennicze | układy inercjalne |

## Przykład rozwiązany

**Zadanie.** Rzeka ma szerokość 100 m, prąd płynie z prędkością 1,5 m/s. Łódź płynie względem wody z prędkością 2,5 m/s.

a) Sternik kieruje łódź prostopadle do brzegu. Ile trwa przeprawa i o ile łódź zniesie w dół rzeki?

Prędkość względem brzegu: $(1{,}5;\ 2{,}5)\ \mathrm{m/s}$. Czas zależy tylko od składowej prostopadłej: $t = 100/2{,}5 = 40\ \mathrm{s}$. Zniesienie: $1{,}5\cdot40 = 60\ \mathrm{m}$.

b) Pod jakim kątem trzeba sterować, żeby przepłynąć dokładnie na drugą stronę? Ile wtedy trwa przeprawa?

Składowa łodzi wzdłuż rzeki musi zniwelować prąd: $2{,}5\sin\theta = 1{,}5$, $\theta \approx 36{,}9^\circ$ w górę rzeki. Prędkość w poprzek: $2{,}5\cos\theta = 2{,}0\ \mathrm{m/s}$, czas $50\ \mathrm{s}$ — dłużej niż w a).

**Sprawdzenie.** Gdyby prąd był szybszy niż łódź ($1{,}5 > 2{,}5$ nie zachodzi), przepłynięcie prosto byłoby niemożliwe — $\sin\theta > 1$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Statek A znajduje się w punkcie $(0,\ 0)$ i płynie na północ z prędkością 10 km/h. Statek B jest 20 km na wschód od A i płynie na zachód z prędkością 15 km/h. Jak blisko siebie się znajdą?

Położenie B względem A: $\vec{r}_{B/A}(t) = (20 - 15t,\ -10t)$ km. Kwadrat odległości:

$$d^2(t) = (20 - 15t)^2 + 100t^2, \qquad \frac{d(d^2)}{dt} = -30(20 - 15t) + 200t = 0 \Rightarrow t = \frac{600}{650} \approx 0{,}92\ \mathrm{h}.$$

$d_{\min} = \sqrt{(20 - 13{,}85)^2 + 9{,}23^2} \approx 11{,}1\ \mathrm{km}$.

W układzie A statek B porusza się po prostej ze stałą prędkością $(-15,\ -10)$ km/h — zadanie sprowadza się do odległości punktu od prostej.

## Typowe pułapki

- **Dodawanie wartości zamiast wektorów.** Prędkości składamy wektorowo; wartość wypadkowej zależy od kąta między nimi.
- **Mylenie „wiatr z zachodu” i „wiatr na zachód”.** Wiatr zachodni wieje *z* zachodu, czyli na wschód.
- **Kierunek sterowania a kierunek ruchu.** Łódź ustawiona prostopadle do brzegu nie płynie prostopadle do brzegu.
- **Średnia prędkość w obie strony.** Pływak w górę i w dół rzeki traci więcej czasu pod prąd niż zyskuje z prądem — średnia nie wynosi prędkości w wodzie stojącej.

## Doświadczenie / symulacja

**Doświadczenie myślowe z pociągu.** W jadącym równomiernie pociągu upuść klucze: spadają pionowo pod rękę. Dla obserwatora na peronie spadają po paraboli (rzut poziomy z prędkością pociągu). Oba opisy są poprawne — to ten sam ruch w dwóch układach.

**Python:** tor kulki upuszczonej w jadącym pociągu, w obu układach odniesienia.

```python
import numpy as np
import matplotlib.pyplot as plt

g, V, h = 9.81, 20.0, 1.5            # prędkość pociągu [m/s], wysokość upuszczenia [m]
t = np.linspace(0, np.sqrt(2*h/g), 50)
x_pociag, y = np.zeros_like(t), h - 0.5*g*t**2
x_peron = x_pociag + V*t              # transformacja Galileusza

print(f"czas spadku {t[-1]:.3f} s; w tym czasie pociąg przejechał {V*t[-1]:.2f} m")
fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].plot(x_pociag, y, "o-"); ax[0].set_title("w pociągu"); ax[0].set_xlim(-1, 1)
ax[1].plot(x_peron, y, "o-"); ax[1].set_title("z peronu")
for a in ax: a.set_xlabel("x [m]"); a.set_ylabel("y [m]"); a.grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Dwa pociągi jadą naprzeciw siebie z prędkościami 72 km/h i 54 km/h. Pasażer pierwszego pociągu widzi, że drugi pociąg przejeżdża obok jego okna w ciągu 4 s. Jaka jest długość drugiego pociągu?

<details>
<summary>Odpowiedź</summary>

Prędkość względna $126\ \mathrm{km/h} = 35\ \mathrm{m/s}$; długość $140\ \mathrm{m}$.
</details>

2. Idąc po nieruchomych schodach ruchomych, wchodzisz na górę w 90 s; stojąc na ruchomych — w 60 s. Ile czasu zajmie wejście, gdy idziesz po ruchomych schodach?

<details>
<summary>Odpowiedź</summary>

Prędkości się dodają: $t = \dfrac{1}{1/90 + 1/60} = 36\ \mathrm{s}$.
</details>

3. Samolot leci z prędkością 200 km/h względem powietrza i ma dotrzeć na północ. Wieje wiatr zachodni (na wschód) z prędkością 50 km/h. Jaki kurs musi obrać pilot i jaka będzie jego prędkość względem ziemi?

<details>
<summary>Odpowiedź</summary>

$\sin\theta = 50/200$, $\theta \approx 14{,}5^\circ$ na zachód od północy; $v = \sqrt{200^2 - 50^2} \approx 194\ \mathrm{km/h}$.
</details>

4. Pływak płynie z prędkością 1 m/s względem wody. Przepływa 100 m pod prąd rzeki płynącej z prędkością 0,5 m/s i wraca. Ile trwa cała droga? Porównaj z wodą stojącą.

<details>
<summary>Odpowiedź</summary>

$100/0{,}5 + 100/1{,}5 \approx 267\ \mathrm{s}$ wobec $200\ \mathrm{s}$.
</details>

5. Deszcz pada pionowo z prędkością 8 m/s. Pod jakim kątem do pionu widzi krople pasażer samochodu jadącego 15 m/s?

<details>
<summary>Odpowiedź</summary>

$\tan\alpha = 15/8$, $\alpha \approx 62^\circ$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pokaż, że jeśli układ $S'$ porusza się względem $S$ ze stałą prędkością, to przyspieszenie ciała jest w obu układach takie samo. Co się zmienia, gdy $S'$ przyspiesza z przyspieszeniem $\vec{A}$?

<details>
<summary>Odpowiedź</summary>

$\vec{v} = \vec{v}\,' + \vec{V} \Rightarrow \vec{a} = \vec{a}\,' + d\vec{V}/dt$. Dla $\vec{V} = \text{const}$: $\vec{a} = \vec{a}\,'$; dla przyspieszającego układu $\vec{a}\,' = \vec{a} - \vec{A}$ — pojawia się „siła bezwładności” $-m\vec{A}$ (temat 03.06).
</details>

2. Rozwiąż zadanie o statkach z przykładu, gdy B płynie na południowy zachód z prędkością 15 km/h. Czy statki się zderzą?

<details>
<summary>Odpowiedź</summary>

$\vec{v}_{B/A} = (-10{,}6;\ -20{,}6)\ \mathrm{km/h}$; $d^2 = (20 - 10{,}6t)^2 + (20{,}6t)^2$, minimum dla $t \approx 0{,}39\ \mathrm{h}$, $d_{\min} \approx 17{,}8\ \mathrm{km}$ — nie zderzą się.
</details>

3. Łódź płynie z prędkością $u$ względem wody na rzece o szerokości $L$, w której prędkość prądu zmienia się od zera przy brzegach do $v_m$ na środku: $v(y) = 4v_m\dfrac{y}{L}\left(1 - \dfrac{y}{L}\right)$. Sternik kieruje łódź prostopadle do brzegu. O ile zniesie ją prąd?

<details>
<summary>Odpowiedź</summary>

$dx = v(y)\,dt = v(y)\dfrac{dy}{u}$; $x = \dfrac{4v_m}{u}\displaystyle\int_0^L\frac{y}{L}\left(1 - \frac{y}{L}\right)dy = \dfrac{2v_mL}{3u}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 4 — §4.5: ruch względny w jednym i dwóch wymiarach.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §4.6–4.7; wyd. 1: t. 1, §4.8–4.9.
