# 21.04 — Zakaz Pauliego i układ okresowy

> **Moduł:** [21 — Fizyka atomowa](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 8: [§8.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/8-4-zakaz-pauliego-i-uklad-okresowy-pierwiastkow) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/8-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §40.4–40.5 (s. 101)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§41.7–41.9, s. 78](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=94) — PDF z serwera AGH

← [Orbitalny moment magnetyczny i spin elektronu](03-moment-magnetyczny-i-spin.md) · [spis modułu](README.md) · [Widma atomowe i promieniowanie rentgenowskie](05-widma-i-promieniowanie-x.md) →

## Po co to jest

Gdyby wszystkie elektrony mogły zająć najniższy stan, każdy atom byłby podobny do wodoru, a chemia by nie istniała. Zakaz Pauliego mówi, że dwa elektrony nie mogą mieć tych samych czterech liczb kwantowych. Wynika z niego budowa powłok elektronowych, a więc cały układ okresowy: dlaczego gazy szlachetne są obojętne, metale alkaliczne łatwo oddają elektron, a halogeny go przyjmują. Ta sama zasada odpowiada za sztywność materii, stabilność białych karłów i gwiazd neutronowych oraz za przewodnictwo metali (23.03).

## Teoria w pigułce

**Zakaz Pauliego (1925).** W atomie nie może być dwóch elektronów o tych samych liczbach kwantowych $(n, l, m_l, m_s)$. Ogólniej: dwa identyczne **fermiony** (cząstki o spinie połówkowym: elektrony, protony, neutrony) nie mogą zajmować tego samego stanu kwantowego. Bozony (fotony, hel-4) tego ograniczenia nie mają.

**Powłoki i podpowłoki.** Każdy orbital ($n$, $l$, $m_l$) mieści dwa elektrony o przeciwnych spinach.

| Element struktury | Liczba miejsc |
|---|---|
| podpowłoka $l$ (s, p, d, f) | $2(2l + 1)$: 2, 6, 10, 14 |
| powłoka $n$ (K, L, M, N…) | $2n^2$: 2, 8, 18, 32 |

**Kolejność zapełniania.** W atomach wieloelektronowych elektrony wewnętrzne ekranują ładunek jądra. Elektrony s wnikają głębiej niż p i d, więc mają niższą energię. Podpowłoki zapełniają się w kolejności rosnącego $n + l$, a przy równym $n + l$ według rosnącego $n$ (**reguła Madelunga**):

1s, 2s, 2p, 3s, 3p, **4s**, 3d, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p, …

Dlatego potas i wapń mają elektron 4s przed zapełnieniem 3d. Są wyjątki, np. Cr: [Ar] 3d⁵4s¹ i Cu: [Ar] 3d¹⁰4s¹ (półpełna i pełna podpowłoka d ma niższą energię).

**Reguła Hunda.** W podpowłoce elektrony najpierw zajmują osobne orbitale z równoległymi spinami. Dlatego tlen i żelazo mają niesparowane elektrony i są paramagnetyczne lub ferromagnetyczne (14.07).

**Układ okresowy.** Okres odpowiada kolejnej zapełnianej powłoce, a grupa liczbie elektronów walencyjnych.
- Gazy szlachetne mają zamknięte podpowłoki p (s² p⁶), dużą energię jonizacji i są chemicznie bierne.
- Metale alkaliczne mają jeden elektron s nad zamkniętą powłoką i łatwo go oddają (Na: 5,1 eV).
- Halogenom brakuje jednego elektronu do zamknięcia powłoki.
- Długości okresów (2, 8, 8, 18, 18, 32, 32) wynikają wprost z pojemności podpowłok.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| jeden elektron na stan $(n, l, m_l, m_s)$ | zakaz Pauliego | fermiony |
| $2(2l + 1)$ | pojemność podpowłoki | — |
| $2n^2$ | pojemność powłoki | — |
| zapełnianie według $n + l$, potem $n$ | reguła Madelunga | atomy w stanie podstawowym, z wyjątkami |

## Przykład rozwiązany

**Zadanie.** Zapisz konfiguracje elektronowe węgla (Z = 6), sodu (Z = 11), chloru (Z = 17) i żelaza (Z = 26). Ile niesparowanych elektronów ma węgiel i żelazo?

- C: 1s² 2s² 2p², 2 niesparowane elektrony p (reguła Hunda).
- Na: 1s² 2s² 2p⁶ 3s¹, czyli [Ne] 3s¹.
- Cl: [Ne] 3s² 3p⁵, brakuje jednego elektronu do zamknięcia.
- Fe: [Ar] 3d⁶ 4s². W 3d jest 5 orbitali na 6 elektronów, więc jeden orbital ma parę, a 4 elektrony są niesparowane. Stąd silny moment magnetyczny atomu żelaza.

## Typowe pułapki

- **Powłoka zapełnia się do końca przed następną.** 4s zapełnia się przed 3d, a 6s przed 4f i 5d.
- **Zakaz Pauliego dotyczy tylko atomów.** Dotyczy wszystkich identycznych fermionów (elektrony w metalu, neutrony w gwieździe neutronowej).
- **Dwa elektrony nie mogą być w tym samym orbitalu.** Mogą, jeśli mają przeciwne spiny.
- **Konfiguracja jonu żelaza Fe²⁺ to [Ar] 3d⁴ 4s².** Przy jonizacji metali przejściowych najpierw odchodzą elektrony 4s: Fe²⁺ to [Ar] 3d⁶.

## Doświadczenie / symulacja

**Energie jonizacji.** Pobierz pierwsze energie jonizacji pierwiastków (np. z bazy NIST) i narysuj je w funkcji $Z$. Ostre maksima przy gazach szlachetnych i minima przy metalach alkalicznych to bezpośredni ślad zamykania powłok.

**Symulacja PhET:** *Zbuduj atom* (*Build an Atom*) — protony, neutrony i elektrony na powłokach.

**Python:** konfiguracje elektronowe z reguły Madelunga i liczba niesparowanych elektronów z reguły Hunda.

```python
L = "spdf"
kolejnosc = sorted([(n, l) for n in range(1, 8) for l in range(0, min(n, 4))], key=lambda t: (t[0] + t[1], t[0]))

def konfiguracja(Z):
    wynik, zostalo = [], Z
    for n, l in kolejnosc:
        if zostalo == 0:
            break
        k = min(2*(2*l + 1), zostalo)
        wynik.append((n, l, k)); zostalo -= k
    return wynik

def niesparowane(n, l, k):
    orb = 2*l + 1
    return k if k <= orb else 2*orb - k

for Z, sym in [(6, "C"), (8, "O"), (11, "Na"), (17, "Cl"), (24, "Cr"), (26, "Fe"), (29, "Cu")]:
    konf = konfiguracja(Z)
    tekst = " ".join(f"{n}{L[l]}{k}" for n, l, k in konf)
    print(f"{sym:2s} (Z = {Z:2d}): {tekst}")
print("Uwaga: Cr i Cu w rzeczywistości mają 3d⁵4s¹ i 3d¹⁰4s¹ (wyjątki od reguły Madelunga).")
print("pojemności powłok 2n²:", [2*n**2 for n in range(1, 5)])
print("niesparowane w 3d⁶ (Fe):", niesparowane(3, 2, 6))
```

## Zadania

### A. Poziom maturalny

1. Ile elektronów mieści podpowłoka d? A cała powłoka M ($n = 3$)?

<details>
<summary>Odpowiedź</summary>

10 i 18.
</details>

2. Zapisz konfigurację elektronową potasu (Z = 19) i wyjaśnij, dlaczego jest metalem alkalicznym.

<details>
<summary>Odpowiedź</summary>

[Ar] 4s¹. Ma jeden słabo związany elektron nad zamkniętą konfiguracją argonu, który łatwo oddaje.
</details>

3. Dlaczego neon jest chemicznie obojętny, a fluor bardzo reaktywny?

<details>
<summary>Odpowiedź</summary>

Neon ma zamkniętą powłokę 2s² 2p⁶, której nie opłaca się ani zrywać, ani rozszerzać. Fluorowi brakuje jednego elektronu do takiej konfiguracji i silnie go przyciąga.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pokaż, że $\sum_{l=0}^{n-1}2(2l + 1) = 2n^2$.

<details>
<summary>Odpowiedź</summary>

$2\sum_{l=0}^{n-1}(2l + 1) = 2\left[2\cdot\dfrac{(n - 1)n}{2} + n\right] = 2n^2$.
</details>

2. Wyjaśnij, dlaczego długości okresów w układzie okresowym to 2, 8, 8, 18, 18, 32, 32, korzystając z reguły Madelunga.

<details>
<summary>Odpowiedź</summary>

Okres kończy się na zapełnieniu podpowłoki p. Okres 1: 1s (2). Okresy 2 i 3: ns np (8). Okresy 4 i 5: ns (n−1)d np (18). Okresy 6 i 7: ns (n−2)f (n−1)d np (32).
</details>

3. Gwiazda neutronowa ma masę 1,4 masy Słońca i promień 10 km. Oszacuj gęstość i porównaj z gęstością jądra atomowego (22.01). Co powstrzymuje ją przed dalszym zapadaniem?

<details>
<summary>Odpowiedź</summary>

$\rho = M/(\tfrac43\pi R^3) \approx 2{,}8\cdot10^{30}/4{,}2\cdot10^{12} \approx 7\cdot10^{17}\ \mathrm{kg/m^3}$, kilka razy więcej niż jądro ($2\cdot10^{17}$). Zapadaniu przeciwdziała ciśnienie zdegenerowanych neutronów (z zakazu Pauliego) i odpychanie jądrowe na małych odległościach.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 8 — §8.4: zakaz Pauliego i układ okresowy.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §40.4–40.5; wyd. 1: t. 5, §41.7–41.9.
- Symulacja PhET *Zbuduj atom*.
