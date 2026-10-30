# 01.02 — Analiza wymiarowa i szacowanie rzędu wielkości

> **Moduł:** [01 — Pomiar, jednostki i niepewności](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 1: [§1.4–1.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-4-analiza-wymiarowa) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §1.1 (s. 1)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003): [t. 1, rozdz. 1](https://home.agh.edu.pl/~czapli/Resnick_1.pdf) — PDF z serwera AGH

← [Układ SI i stałe definicyjne](01-uklad-si.md) · [spis modułu](README.md) · [Niepewności pomiarowe: typ A, typ B, niepewność złożona](03-niepewnosci-pomiarowe.md) →

## Po co to jest

Dwie umiejętności, które pozwalają sprawdzić wynik bez rozwiązywania zadania drugi raz. **Analiza wymiarowa** wyłapuje błędne wzory (jeśli jednostki się nie zgadzają, wzór jest zły na pewno) i pozwala zgadnąć postać zależności, zanim się ją wyprowadzi. **Szacowanie rzędu wielkości** mówi, czy wynik ma sens: jeśli z obliczeń wychodzi, że samochód hamuje na drodze 3 km, trzeba szukać błędu.

## Teoria w pigułce

**Wymiar** wielkości to jej zapis przez wielkości podstawowe: długość $\mathsf{L}$, masę $\mathsf{M}$, czas $\mathsf{T}$ (oraz prąd, temperaturę itd.). Wymiar zapisujemy w nawiasach kwadratowych: $[v] = \mathsf{L\,T^{-1}}$, $[F] = \mathsf{M\,L\,T^{-2}}$, $[E] = \mathsf{M\,L^2\,T^{-2}}$.

**Zasada jednorodności wymiarowej.** Obie strony równania i każdy składnik sumy muszą mieć ten sam wymiar. Argumenty funkcji $\sin$, $\cos$, $\exp$, $\ln$ muszą być bezwymiarowe.

**Wyprowadzanie zależności.** Jeśli wiemy, od jakich wielkości zależy wynik, możemy zgadnąć wzór z dokładnością do stałej bezwymiarowej. Przykład: okres wahadła może zależeć od długości $l$, masy $m$ i przyspieszenia $g$. Zakładamy $T = C\,l^a m^b g^c$ i porównujemy wykładniki:

$$\mathsf{T}^1 = \mathsf{L}^a\,\mathsf{M}^b\,(\mathsf{L\,T^{-2}})^c \ \Rightarrow\ \mathsf{M}: b = 0;\ \ \mathsf{T}: -2c = 1;\ \ \mathsf{L}: a + c = 0.$$

Stąd $c = -\tfrac12$, $a = \tfrac12$, $b = 0$: $T = C\sqrt{l/g}$. Analiza wymiarowa sama pokazała, że okres **nie zależy od masy**. Stałej $C = 2\pi$ nie wyznaczy — do tego potrzebna jest fizyka albo pomiar.

**Ograniczenia.** Analiza wymiarowa nie widzi stałych bezwymiarowych ($2\pi$, $\tfrac12$), nie odróżnia $\theta$ od $\sin\theta$ i zawodzi, gdy pominiemy jakąś istotną wielkość albo gdy z danych da się zbudować więcej niż jedną kombinację bezwymiarową.

**Szacowanie (metoda Fermiego).** Trudne pytanie rozkładamy na czynniki, które umiemy oszacować z dokładnością do rzędu wielkości, i mnożymy. Błędy pojedynczych czynników częściowo się znoszą, więc wynik jest zaskakująco dobry. Wynik podajemy jako potęgę dziesięciu albo z jedną cyfrą znaczącą.

## Wzory i założenia

| Wielkość | Wymiar | Wielkość | Wymiar |
|---|---|---|---|
| prędkość | $\mathsf{L\,T^{-1}}$ | energia, praca | $\mathsf{M\,L^2\,T^{-2}}$ |
| przyspieszenie | $\mathsf{L\,T^{-2}}$ | moc | $\mathsf{M\,L^2\,T^{-3}}$ |
| siła | $\mathsf{M\,L\,T^{-2}}$ | ciśnienie | $\mathsf{M\,L^{-1}\,T^{-2}}$ |
| pęd | $\mathsf{M\,L\,T^{-1}}$ | gęstość | $\mathsf{M\,L^{-3}}$ |
| częstotliwość, $\omega$ | $\mathsf{T^{-1}}$ | kąt, liczba | bezwymiarowe |

| Wartość do szacunków | Rząd wielkości |
|---|---|
| rok | $3\cdot10^7\ \mathrm{s}$ |
| promień Ziemi | $6\cdot10^6\ \mathrm{m}$ |
| masa człowieka | $70\ \mathrm{kg} \sim 10^2\ \mathrm{kg}$ |
| liczba Polaków | $4\cdot10^7$ |
| gęstość wody, skał | $10^3$, $3\cdot10^3\ \mathrm{kg/m^3}$ |

## Przykład rozwiązany

**Zadanie (szacowanie).** Ile razy uderza serce człowieka w ciągu życia?

**Rozkład na czynniki.** Tętno ok. $70$ na minutę, czyli ok. $10^5$ na dobę ($70\cdot60\cdot24 \approx 1{,}0\cdot10^5$). Rok to ok. $365$ dób, życie ok. $80$ lat.

**Wynik.** $10^5\cdot365\cdot80 \approx 3\cdot10^9$ — około trzech miliardów uderzeń.

**Sprawdzenie.** Rząd wielkości zgadza się z wartościami podawanymi w fizjologii ($2$–$3\cdot10^9$). Nawet gdyby tętno było 60 albo 90, wynik zmieniłby się mniej niż o połowę — rząd wielkości zostaje.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Siła oporu powietrza działająca na kulę zależy od gęstości powietrza $\rho$, prędkości $v$ i promienia $r$. Znajdź postać zależności i wyprowadź z niej, jak prędkość graniczna spadającej kropli zależy od jej promienia.

$F = C\rho^av^br^c$: $\ \mathsf{M\,L\,T^{-2}} = \mathsf{M}^a\mathsf{L}^{-3a}\,\mathsf{L}^b\mathsf{T}^{-b}\,\mathsf{L}^c$, stąd $a = 1$, $b = 2$, $c = 2$:

$$F = C\rho v^2r^2.$$

Kropla wody o gęstości $\rho_w$ osiąga prędkość graniczną, gdy opór równoważy ciężar: $C\rho v_g^2r^2 = \tfrac43\pi r^3\rho_wg$, więc $v_g \propto \sqrt{r}$. Kropla cztery razy większa spada dwa razy szybciej. (W ruchu bardzo wolnym, np. mgły, ważna staje się lepkość i wynik jest inny — analiza wymiarowa zależy od tego, jakie wielkości uznamy za istotne.)

## Typowe pułapki

- **Dodawanie wielkości o różnych wymiarach.** Wyrażenie $v + at^2$ jest błędne niezależnie od liczb.
- **„Wymiarowo poprawny” nie znaczy „poprawny”.** $T = \pi\sqrt{l/g}$ ma dobry wymiar, ale złą stałą.
- **Wymiar a jednostka.** Wymiar to $\mathsf{L}$, jednostka to metr, centymetr albo cal. Analiza wymiarowa sprawdza wymiar; przeliczanie jednostek to osobny krok.
- **Fałszywa precyzja w szacunkach.** Wynik „3 128 450 000 uderzeń” sugeruje dokładność, której nie ma. Podawaj jedną, najwyżej dwie cyfry znaczące.
- **Szacowanie bez sprawdzenia skrajności.** Zapytaj, czy wynik nie jest absurdalnie duży albo mały w porównaniu z czymś znanym.

## Doświadczenie / symulacja

**Czy okres wahadła zależy od masy?** Analiza wymiarowa twierdzi, że nie. Sprawdź: zawieś telefon na sznurku i zmierz okres w phyphox (eksperyment *Pendulum*), potem przyklej do telefonu ciężki przedmiot (np. baterię albo słoik z monetami), zachowując tę samą długość do środka masy, i zmierz ponownie.

**Python:** wykładniki z analizy wymiarowej to układ równań liniowych — rozwiązujemy go macierzowo.

```python
import numpy as np

# Wymiary w bazie (M, L, T)
dim = {
    "l": [0, 1, 0],     # długość
    "m": [1, 0, 0],     # masa
    "g": [0, 1, -2],    # przyspieszenie
}
target = [0, 0, 1]      # szukamy okresu: wymiar T

A = np.array([dim["l"], dim["m"], dim["g"]]).T     # kolumny = zmienne
a, b, c = np.linalg.solve(A, target)
print(f"T ∝ l^{a:.2f} · m^{b:.2f} · g^{c:.2f}")

# Opór: F(ρ, v, r), wymiar F = M L T^-2
B = np.array([[1, -3, 0], [0, 1, -1], [0, 1, 0]]).T  # ρ, v, r
print("F ∝ ρ^{:.0f} v^{:.0f} r^{:.0f}".format(*np.linalg.solve(B, [1, 1, -2])))
```

## Zadania

### A. Poziom maturalny

1. Które wzory są niepoprawne wymiarowo? a) $s = vt + at^2$, b) $v = at^2$, c) $E = mgh + \tfrac12mv$, d) $p = \rho gh$.

<details>
<summary>Odpowiedź</summary>

Niepoprawne: b) ($\mathsf{L\,T^{-1}} \neq \mathsf{L}$) i c) ($\tfrac12mv$ ma wymiar pędu). Wzór a) jest poprawny wymiarowo, choć ma złą stałą przy $at^2$.
</details>

2. Okres drgań ciężarka na sprężynie zależy od masy $m$ i współczynnika sprężystości $k$ (jednostka N/m). Wyznacz postać zależności.

<details>
<summary>Odpowiedź</summary>

$T = C\sqrt{m/k}$ (w rzeczywistości $C = 2\pi$).
</details>

3. Oszacuj, ile litrów wody wypija człowiek w ciągu życia.

<details>
<summary>Odpowiedź</summary>

ok. $2\ \mathrm{L/dobę}\cdot365\cdot80 \approx 6\cdot10^4\ \mathrm{L}$ — rząd $10^4$–$10^5$ L.
</details>

4. Oszacuj liczbę ziarenek piasku w 1 kg piasku (ziarno o średnicy ok. 0,5 mm, gęstość kwarcu ok. $2600\ \mathrm{kg/m^3}$).

<details>
<summary>Odpowiedź</summary>

Objętość ziarna $\approx \tfrac{\pi}{6}d^3 \approx 6{,}5\cdot10^{-11}\ \mathrm{m^3}$, masa $\approx 1{,}7\cdot10^{-7}\ \mathrm{kg}$; ok. $6\cdot10^{6}$ ziaren (rząd $10^6$–$10^7$).
</details>

### B. Poziom akademicki

1. Prędkość fali na napiętej strunie zależy od siły naciągu $F$ i gęstości liniowej $\mu$ (kg/m). Znajdź postać zależności.

<details>
<summary>Odpowiedź</summary>

$v = C\sqrt{F/\mu}$ (dokładnie $C = 1$).
</details>

2. Prędkość fal na głębokiej wodzie zależy od długości fali $\lambda$ i przyspieszenia $g$ (gęstość wody wypada z rachunku). Wyznacz zależność. Ile razy szybciej biegnie fala czterokrotnie dłuższa?

<details>
<summary>Odpowiedź</summary>

$v = C\sqrt{g\lambda}$ (dokładnie $C = 1/\sqrt{2\pi}$); dwa razy szybciej.
</details>

3. Promień kuli ognistej wybuchu jądrowego $R$ zależy od energii $E$, czasu $t$ i gęstości powietrza $\rho$. Pokaż, że $R = C\left(\dfrac{Et^2}{\rho}\right)^{1/5}$. (Tak G. I. Taylor oszacował w 1950 roku tajną moc pierwszej bomby atomowej ze zdjęć w prasie.)

<details>
<summary>Odpowiedź</summary>

$R = CE^at^b\rho^c$: $\mathsf{M}: a + c = 0$; $\mathsf{L}: 2a - 3c = 1$; $\mathsf{T}: -2a + b = 0$. Stąd $a = \tfrac15$, $c = -\tfrac15$, $b = \tfrac25$.
</details>

4. Oszacuj całkowitą moc promieniowania Słońca docierającą do Ziemi. Natężenie na orbicie Ziemi wynosi ok. $1360\ \mathrm{W/m^2}$.

<details>
<summary>Odpowiedź</summary>

$P = S\cdot\pi R_Z^2 \approx 1360\cdot\pi\cdot(6{,}37\cdot10^6)^2 \approx 1{,}7\cdot10^{17}\ \mathrm{W}$ (liczy się przekrój, nie powierzchnia kuli).
</details>

5. Energia wiązania ciała przez jego własną grawitację zależy od $G$, masy $M$ i promienia $R$. Znajdź postać zależności i oszacuj jej rząd dla Ziemi ($M = 6\cdot10^{24}\ \mathrm{kg}$, $R = 6{,}4\cdot10^6\ \mathrm{m}$, $G = 6{,}7\cdot10^{-11}$ SI).

<details>
<summary>Odpowiedź</summary>

$E = C\dfrac{GM^2}{R}$ (dla kuli jednorodnej $C = 3/5$); $GM^2/R \approx 4\cdot10^{32}\ \mathrm{J}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 1 — §1.4 (analiza wymiarowa) i §1.5 (szacowanie i pytania Fermiego), z przykładami i zadaniami.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1, rozdz. 1 — §1.1: wielkości fizyczne, jednostki i rzędy wielkości.
