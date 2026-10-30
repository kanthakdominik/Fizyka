# 18.07 — Dyfrakcja promieni X i prawo Bragga

> **Moduł:** [18 — Optyka falowa](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 4: [§4.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/4-6-dyfrakcja-rentgenowska) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/4-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §36.7 (s. 170)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§37.9, s. 134](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=149) — PDF z serwera AGH

← [Polaryzacja światła: prawo Malusa i kąt Brewstera](06-polaryzacja.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Promieniowanie rentgenowskie ma długość fali porównywalną z odległościami między atomami w krysztale, więc kryształ działa dla niego jak trójwymiarowa siatka dyfrakcyjna. Z obrazów dyfrakcyjnych odczytuje się położenia atomów. W ten sposób poznano budowę soli, metali, minerałów, leków i białek, a zdjęcie 51 Rosalind Franklin pomogło odkryć podwójną helisę DNA. Dyfraktometry rentgenowskie to standardowe wyposażenie laboratoriów materiałowych i farmaceutycznych.

## Teoria w pigułce

**Promieniowanie rentgenowskie** ma długość fali ok. 0,01–10 nm (16.04). W lampie rentgenowskiej elektrony uderzające w anodę z miedzi dają charakterystyczną linię Cu Kα o $\lambda = 0{,}154\ \mathrm{nm}$ (21).

**Warunek Bragga.** Atomy w krysztale leżą w równoległych płaszczyznach odległych o $d$. Promieniowanie odbite od kolejnych płaszczyzn wzmacnia się, gdy różnica dróg $2d\sin\theta$ jest wielokrotnością długości fali:

$$2d\sin\theta = m\lambda, \qquad m = 1, 2, \dots$$

Kąt $\theta$ mierzy się tu **od płaszczyzny** kryształu (kąt poślizgu), a nie od normalnej. Promień odbity jest odchylony od padającego o $2\theta$.

**Zastosowania:**
- przy znanej $\lambda$ mierzy się odległości $d$ i strukturę kryształu (krystalografia);
- przy znanym $d$ mierzy się długość fali (spektroskopia rentgenowska);
- metoda proszkowa (Debye'a–Scherrera): przypadkowo ułożone kryształki dają pierścienie dla wszystkich rodzin płaszczyzn, co pozwala identyfikować substancje.

Ten sam warunek obowiązuje dla elektronów i neutronów o odpowiedniej długości fali de Broglie'a (20.04). Doświadczenie Davissona–Germera (1927) potwierdziło w ten sposób falową naturę elektronów.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $2d\sin\theta = m\lambda$ | warunek Bragga | $\theta$ od płaszczyzny kryształu |
| kąt odchylenia $2\theta$ | geometria pomiaru | — |
| $\lambda \le 2d$ | warunek istnienia odbić | $m = 1$, $\sin\theta \le 1$ |

## Przykład rozwiązany

**Zadanie.** Promieniowanie Cu Kα (0,154 nm) pada na kryształ soli kuchennej ($d = 0{,}282\ \mathrm{nm}$). Pod jakimi kątami obserwuje się odbicia Bragga?

$m = 1$: $\sin\theta = 0{,}154/0{,}564 \approx 0{,}273 \Rightarrow \theta \approx 15{,}8^\circ$.

$m = 2$: $\sin\theta \approx 0{,}546 \Rightarrow \theta \approx 33{,}1^\circ$.

$m = 3$: $\sin\theta \approx 0{,}82 \Rightarrow \theta \approx 55^\circ$.

$m = 4$: $\sin\theta > 1$, odbicie nie istnieje.

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie.** Promień odbity od drugiej płaszczyzny przebywa dodatkową drogę: w dół $d\sin\theta$ i w górę $d\sin\theta$, razem $2d\sin\theta$. Wzmocnienie wymaga, by była to wielokrotność $\lambda$.

**Czułość pomiaru.** Różniczkując warunek Bragga przy stałym $\lambda$: $2\,\Delta d\sin\theta + 2d\cos\theta\,\Delta\theta = 0$, więc

$$\frac{\Delta d}{d} = -\cot\theta\,\Delta\theta.$$

Dla dużych kątów (blisko $90^\circ$) $\cot\theta$ jest mały, więc ten sam błąd kąta daje mniejszy błąd $d$. Dlatego do dokładnych pomiarów stałych sieci używa się odbić pod dużymi kątami. Przy $\theta = 60^\circ$ i dokładności kąta $0{,}01^\circ$: $\Delta d/d \approx 0{,}58\cdot1{,}75\cdot10^{-4} \approx 10^{-4}$.

## Typowe pułapki

- **$\theta$ od normalnej.** W warunku Bragga $\theta$ mierzy się od płaszczyzny kryształu. Kąt odchylenia wiązki to $2\theta$.
- **Światło widzialne też da obraz Bragga na krysztale.** $\lambda$ światła (500 nm) jest tysiące razy większa od $d$ i warunek $\lambda \le 2d$ nie jest spełniony.
- **Jedna płaszczyzna daje odbicie.** Wzmocnienie powstaje z interferencji odbić od wielu płaszczyzn. W krysztale jest wiele rodzin płaszczyzn o różnych $d$.

## Doświadczenie / symulacja

**Model z mikrofalami.** W pracowni z nadajnikiem mikrofal (ok. 3 cm) zamiast promieni rentgenowskich można użyć sześcianu z kulek metalowych rozmieszczonych co kilka centymetrów jako „kryształu” i zmierzyć kąty Bragga.

**Dyfrakcja na siatce jako analog.** Spójrz przez gęstą tkaninę (np. parasol, firanka) na odległą latarnię. Widać dwuwymiarowy wzór plamek. To dyfrakcja na siatce dwuwymiarowej, a kryształ to jej trójwymiarowy odpowiednik.

**Python:** kąty Bragga dla kilku kryształów i lampy miedzianej.

```python
import numpy as np

lam = 0.154                                    # nm, Cu Kα
krysztaly = {"NaCl (200)": 0.282, "Si (111)": 0.3135, "Al (111)": 0.2338, "grafit (002)": 0.335}
for nazwa, d in krysztaly.items():
    katy = [np.degrees(np.arcsin(m*lam/(2*d))) for m in range(1, 6) if m*lam/(2*d) <= 1]
    print(f"{nazwa:13s} d = {d:.4f} nm: θ = " + ", ".join(f"{k:.1f}°" for k in katy))
th = np.radians(60); dth = np.radians(0.01)
print(f"czułość: Δd/d = {dth/np.tan(th):.1e} przy θ = 60° i Δθ = 0,01°")
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Odbicie pierwszego rzędu od kryształu o $d = 0{,}3\ \mathrm{nm}$ obserwuje się pod kątem $15^\circ$. Jaka jest długość fali?

<details>
<summary>Odpowiedź</summary>

$\lambda = 2d\sin\theta \approx 0{,}155\ \mathrm{nm}$.
</details>

2. Dlaczego do badania kryształów nie używa się światła widzialnego?

<details>
<summary>Odpowiedź</summary>

Długość fali światła (setki nm) jest dużo większa od odległości między atomami (ok. 0,1–0,5 nm). Warunek Bragga nie może być spełniony.
</details>

### B. Poziom akademicki

1. Elektrony przyspieszone napięciem 54 V odbijają się od kryształu niklu (doświadczenie Davissona–Germera). Oblicz ich długość fali de Broglie'a (20.04) i porównaj z odległością między płaszczyznami (0,091 nm). Pod jakim kątem Bragga wystąpi pierwsze odbicie?

<details>
<summary>Odpowiedź</summary>

$\lambda = h/\sqrt{2meU} \approx 0{,}167\ \mathrm{nm}$. $\sin\theta = 0{,}167/(2\cdot0{,}091) \approx 0{,}92 \Rightarrow \theta \approx 66^\circ$ (kąt poślizgu). Davisson i Germer zmierzyli maksimum przy kącie $50^\circ$ między wiązką padającą a rozproszoną, czyli $180^\circ - 2\theta \approx 50^\circ$ dla $\theta \approx 65^\circ$.
</details>

2. W metodzie proszkowej na kliszy walcowej o promieniu 5 cm wokół próbki pierścień pierwszego rzędu dla Al (111) ($d = 0{,}234\ \mathrm{nm}$, Cu Kα) leży pod jakim kątem odchylenia? W jakiej odległości od miejsca wejścia wiązki (wzdłuż kliszy)?

<details>
<summary>Odpowiedź</summary>

$\theta = \arcsin(0{,}154/0{,}468) \approx 19{,}2^\circ$, odchylenie $2\theta \approx 38{,}4^\circ$. Na kliszy po stronie wyjścia wiązki łuk $R\cdot2\theta \approx 3{,}4\ \mathrm{cm}$ od miejsca, gdzie wiązka przechodzi bez odchylenia.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 4 — §4.6: dyfrakcja promieniowania rentgenowskiego.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §36.7; wyd. 1: t. 4, §37.9.
