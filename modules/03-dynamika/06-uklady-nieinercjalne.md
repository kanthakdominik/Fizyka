# 03.06 — Układy nieinercjalne i siły bezwładności

> **Moduł:** [03 — Dynamika punktu materialnego](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 6: [§6.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/6-3-sila-dosrodkowa) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/6-wstep)

← [Opór ośrodka i prędkość graniczna — równanie ruchu](05-opor-osrodka.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

W hamującym autobusie coś „pcha” nas do przodu, na karuzeli coś „wyrzuca” nas na zewnątrz. W układzie inercjalnym tych sił nie ma — to bezwładność. Ale opisywanie ruchu z punktu widzenia przyspieszającego pojazdu albo obracającej się Ziemi bywa znacznie prostsze, jeśli dopiszemy **siły bezwładności**. Ten temat jest w podstawie programowej matury rozszerzonej, a na studiach prowadzi do siły Coriolisa, która kształtuje wiatry i prądy oceaniczne.

## Teoria w pigułce

**Układ inercjalny** to taki, w którym obowiązuje I zasada dynamiki. Każdy układ poruszający się względem inercjalnego ze stałą prędkością też jest inercjalny (02.07). Układ, który przyspiesza lub się obraca, jest **nieinercjalny**.

**Siła bezwładności w układzie poruszającym się z przyspieszeniem $\vec{A}$.** Żeby w takim układzie móc pisać II zasadę dynamiki, dodajemy do sił rzeczywistych siłę

$$\vec{F}_b = -m\vec{A}.$$

Nie ma ona źródła (żadne ciało jej nie wywiera) i nie ma do niej siły reakcji — to skutek wyboru układu odniesienia.

**Przykłady.**
- **Hamujący autobus** ($\vec{A}$ do tyłu): siła bezwładności do przodu, pasażer „leci” do przodu.
- **Winda przyspieszająca w górę:** siła bezwładności w dół, „efektywne $g$” rośnie do $g + A$ (03.01).
- **Wahadło w przyspieszającym samochodzie** odchyla się do tyłu o kąt $\tan\theta = A/g$ — prosty przyspieszeniomierz.

**Układ obracający się z prędkością kątową $\omega$.** Pojawiają się dwie siły bezwładności:
- **odśrodkowa** $F = m\omega^2r$, skierowana od osi obrotu — działa na każde ciało, także spoczywające w tym układzie;
- **Coriolisa** $\vec{F}_C = -2m\vec{\omega}\times\vec{v}\,'$ — działa tylko na ciała poruszające się względem obracającego się układu, prostopadle do ich prędkości. Na półkuli północnej odchyla ruch w prawo.

**Ziemia** jest układem obracającym się, ale powoli: siła odśrodkowa zmniejsza $g$ na równiku o ok. 0,3%, a siła Coriolisa jest zauważalna dopiero na dużych skalach (cyklony, prądy morskie, wahadło Foucaulta, pociski artyleryjskie).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec{F}_b = -m\vec{A}$ | siła bezwładności | układ poruszający się postępowo z przyspieszeniem $\vec{A}$ |
| $\vec{g}_{\text{ef}} = \vec{g} - \vec{A}$ | efektywne przyspieszenie „grawitacyjne” | j.w. |
| $\tan\theta = A/g$ | odchylenie wahadła | przyspieszenie poziome |
| $F_{\text{odśr}} = m\omega^2r$ | siła odśrodkowa | układ obracający się, $r$ — odległość od osi |
| $\vec{F}_C = -2m\vec{\omega}\times\vec{v}\,'$ | siła Coriolisa | $\vec{v}\,'$ — prędkość względem układu obracającego się |
| $T_F = \dfrac{T_{\text{doby gw}}}{\sin\varphi}$ | okres obrotu płaszczyzny wahadła Foucaulta | szerokość geograficzna $\varphi$ |

## Przykład rozwiązany

**Zadanie (poziom maturalny).** W samochodzie ruszającym z przyspieszeniem $3\ \mathrm{m/s^2}$ wisi na nitce zawieszka. O jaki kąt odchyli się od pionu i w którą stronę? Rozwiąż w układzie samochodu i w układzie drogi.

**Układ samochodu (nieinercjalny).** Zawieszka spoczywa. Działają: ciężar $mg$ (w dół), naciąg $T$ (wzdłuż nitki), siła bezwładności $mA$ (do tyłu). Równowaga: $T\sin\theta = mA$, $T\cos\theta = mg$, więc $\tan\theta = A/g$, $\theta \approx 17^\circ$ do tyłu.

**Układ drogi (inercjalny).** Zawieszka przyspiesza razem z samochodem. Składowa pozioma naciągu nadaje jej przyspieszenie: $T\sin\theta = mA$; pionowo $T\cos\theta = mg$. Wynik ten sam.

Oba opisy są równoważne; siła bezwładności to po prostu przeniesienie wyrazu $m\vec{A}$ na drugą stronę równania.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Kamień spada swobodnie z wieży o wysokości 100 m na równiku. O ile odchyli się od pionu na skutek siły Coriolisa i w którą stronę?

Na równiku $\vec{\omega}$ jest poziome (na północ), prędkość spadania pionowa (w dół), więc $-2\vec{\omega}\times\vec{v}$ jest skierowane na **wschód** i ma wartość $2\omega v = 2\omega gt$. Przyspieszenie na wschód $a_E = 2\omega gt$, stąd

$$v_E = \omega gt^2, \qquad x_E = \frac{\omega gt^3}{3}.$$

Czas spadku $t = \sqrt{2h/g} \approx 4{,}52\ \mathrm{s}$, $\omega = 7{,}29\cdot10^{-5}\ \mathrm{rad/s}$:

$$x_E \approx \frac{7{,}29\cdot10^{-5}\cdot9{,}81\cdot92{,}0}{3} \approx 2{,}2\ \mathrm{cm}.$$

Efekt jest mały, ale mierzalny — zmierzył go już w XIX wieku F. Reich w kopalni we Freibergu.

**Wyjaśnienie bez siły Coriolisa.** Szczyt wieży jest dalej od osi Ziemi niż jej podstawa, więc porusza się na wschód nieco szybciej. Kamień zachowuje tę nadwyżkę prędkości i „wyprzedza” podstawę wieży.

## Typowe pułapki

- **Siły bezwładności w układzie inercjalnym.** Rozwiązując zadanie z punktu widzenia ziemi, nie dodajemy siły odśrodkowej ani siły $-m\vec{A}$.
- **Mieszanie układów.** Wybierz jeden układ i trzymaj się go w całym zadaniu.
- **Szukanie reakcji na siłę bezwładności.** Nie istnieje — siła bezwładności nie pochodzi od żadnego ciała.
- **Siła odśrodkowa zamiast dośrodkowej.** W układzie inercjalnym ciało na karuzeli potrzebuje siły dośrodkowej; „wyrzucanie na zewnątrz” to brak tej siły (ciało chce poruszać się po prostej).
- **Woda w wannie skręca przez siłę Coriolisa.** W skali wanny efekt jest znikomy wobec przypadkowych ruchów wody.

## Doświadczenie / symulacja

**Przyspieszeniomierz z nitki.** Zawieś w samochodzie lub tramwaju lekki przedmiot na nitce i zrób zdjęcie przy ruszaniu na tle kratki. Zmierz kąt odchylenia i oblicz przyspieszenie. Porównaj z odczytem phyphox (*Acceleration (without g)*) z telefonu położonego płasko.

**Obracająca się woda.** Zakręć wodą w szklance (albo postaw szklankę na obrotowej podstawce) — powierzchnia przyjmuje kształt paraboloidy. W układzie obracającym się wyjaśnia to siła odśrodkowa: powierzchnia jest prostopadła do $\vec{g}_{\text{ef}}$.

**Python:** odchylenie pocisku przez siłę Coriolisa — ruch ciała w obracającym się układzie (zadanie z wieży, numerycznie).

```python
import numpy as np
from scipy.integrate import solve_ivp

omega = 7.292e-5                     # prędkość kątowa Ziemi [rad/s]
g, h = 9.81, 100.0
W = np.array([0.0, omega, 0.0])      # na równiku: osie x — wschód, y — północ, z — w górę

def rhs(t, s):
    r, v = s[:3], s[3:]
    a = np.array([0, 0, -g]) - 2*np.cross(W, v)   # siła odśrodkowa wliczona w g
    return np.concatenate([v, a])

def ground(t, s): return s[2]
ground.terminal = True

sol = solve_ivp(rhs, (0, 10), [0, 0, h, 0, 0, 0], events=ground, rtol=1e-10, atol=1e-12)
t_end = sol.t[-1]
print(f"czas spadku {t_end:.3f} s, odchylenie na wschód {sol.y[0, -1]*100:.2f} cm")
print(f"wzór ωgt³/3 = {omega*g*t_end**3/3*100:.2f} cm")
```

## Zadania

### A. Poziom maturalny

1. Zawieszka w samochodzie odchyliła się o $10^\circ$ od pionu do tyłu. Z jakim przyspieszeniem jedzie samochód?

<details>
<summary>Odpowiedź</summary>

$A = g\tan10^\circ \approx 1{,}73\ \mathrm{m/s^2}$ (do przodu).
</details>

2. Osoba o masie 70 kg stoi na wadze w windzie przyspieszającej w dół z przyspieszeniem $2\ \mathrm{m/s^2}$. Co pokazuje waga? Rozwiąż w układzie windy.

<details>
<summary>Odpowiedź</summary>

Siła bezwładności w górę $mA$: $N = m(g - A) \approx 547\ \mathrm{N}$, waga pokaże ok. 56 kg.
</details>

3. Stacja kosmiczna w kształcie koła o promieniu 100 m obraca się, wytwarzając „sztuczną grawitację” równą $g$ na obwodzie. Oblicz prędkość kątową i okres obrotu.

<details>
<summary>Odpowiedź</summary>

$\omega = \sqrt{g/R} \approx 0{,}31\ \mathrm{rad/s}$, $T \approx 20\ \mathrm{s}$ (3 obroty na minutę).
</details>

4. Wiadro z wodą stoi na wózku, który przyspiesza poziomo z przyspieszeniem $A$. Jak ustawi się powierzchnia wody?

<details>
<summary>Odpowiedź</summary>

Prostopadle do $\vec{g}_{\text{ef}} = \vec{g} - \vec{A}$: nachylona pod kątem $\tan\theta = A/g$, wyżej z tyłu wózka.
</details>

5. Dlaczego na równiku waga pokazuje nieco mniej niż na biegunie? Oszacuj różnicę dla osoby o masie 70 kg (uwzględnij tylko obrót Ziemi).

<details>
<summary>Odpowiedź</summary>

Na równiku działa siła odśrodkowa $m\omega^2R \approx 70\cdot0{,}034 \approx 2{,}4\ \mathrm{N}$, czyli ok. 0,24 kg mniej. (Spłaszczenie Ziemi daje dodatkowy, podobny efekt.)
</details>

### B. Poziom akademicki

1. Pokaż, że powierzchnia wody w naczyniu obracającym się z prędkością kątową $\omega$ ma kształt $z(r) = \dfrac{\omega^2r^2}{2g} + z_0$. O ile poziom przy ściance jest wyżej niż na osi, gdy $\omega = 10\ \mathrm{rad/s}$, $r = 10\ \mathrm{cm}$?

<details>
<summary>Odpowiedź</summary>

Powierzchnia prostopadła do $\vec{g}_{\text{ef}}$: $\dfrac{dz}{dr} = \dfrac{\omega^2r}{g}$, po scałkowaniu paraboloida. $\Delta z = 100\cdot0{,}01/19{,}62 \approx 5{,}1\ \mathrm{cm}$.
</details>

2. Oblicz okres obrotu płaszczyzny drgań wahadła Foucaulta w Krakowie ($\varphi \approx 50^\circ$). Doba gwiazdowa trwa 23,93 h.

<details>
<summary>Odpowiedź</summary>

$T = 23{,}93/\sin50^\circ \approx 31{,}2\ \mathrm{h}$.
</details>

3. Pociąg o masie 500 t jedzie na północ z prędkością 30 m/s na szerokości $50^\circ$ N. Oblicz siłę Coriolisa i wskaż, na którą szynę naciska mocniej.

<details>
<summary>Odpowiedź</summary>

Pozioma składowa: $F = 2m\omega v\sin\varphi \approx 2\cdot5\cdot10^5\cdot7{,}29\cdot10^{-5}\cdot30\cdot0{,}766 \approx 1{,}7\ \mathrm{kN}$, w prawo (na wschód) — mocniej naciska na prawą szynę.
</details>

4. Wyprowadź z $\vec{a} = \vec{a}\,' + \vec{A}$ (02.07), że w układzie poruszającym się z przyspieszeniem $\vec{A}$ obowiązuje $m\vec{a}\,' = \sum\vec{F} - m\vec{A}$.

<details>
<summary>Odpowiedź</summary>

W układzie inercjalnym $m\vec{a} = \sum\vec{F}$; wstawiając $\vec{a} = \vec{a}\,' + \vec{A}$ i przenosząc $m\vec{A}$ na prawą stronę.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1 — §6.3 (fragment o układach nieinercjalnych i sile Coriolisa) oraz §4.5 (ruch względny).
- Wahadło Foucaulta można zobaczyć m.in. w kościele św. Piotra i Pawła w Krakowie.
