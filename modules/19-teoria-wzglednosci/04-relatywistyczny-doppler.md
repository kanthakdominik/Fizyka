# 19.04 — Relatywistyczny efekt Dopplera

> **Moduł:** [19 — Szczególna teoria względności](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 5: [§5.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/5-7-relatywistyczny-efekt-dopplera) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/5-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §37.5 (s. 211)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§38.10, s. 166](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=181) — PDF z serwera AGH

← [Transformacja Lorentza i składanie prędkości](03-transformacja-lorentza.md) · [spis modułu](README.md) · [Pęd i energia relatywistyczna, E = mc²](05-ped-i-energia-relatywistyczna.md) →

## Po co to jest

Z przesunięcia linii widmowych odczytuje się prędkość gwiazd i galaktyk, odkrywa planety pozasłoneczne i mierzy rozszerzanie Wszechświata (24). Dla dużych prędkości wzór Dopplera dla dźwięku (10.07) trzeba zastąpić relatywistycznym, bo światło nie ma ośrodka i liczy się tylko prędkość względna, a do tego dochodzi dylatacja czasu źródła. Ten sam efekt uwzględnia się w GPS, w radarach laserowych i w badaniach szybkich wiązek jonów.

## Teoria w pigułce

**Wzór relatywistyczny.** Źródło i odbiornik oddalają się z prędkością względną $v$ wzdłuż łączącej je prostej. Odbierana częstotliwość:

$$f = f_0\sqrt{\frac{1 - \beta}{1 + \beta}}, \qquad \beta = \frac vc.$$

Dla zbliżania zmienia się znak $\beta$. Wzór zależy tylko od prędkości względnej. Nie ma różnicy, czy porusza się źródło, czy odbiornik, bo nie ma ośrodka.

**Skąd się bierze.** Jeśli źródło się oddala, kolejne grzbiety są wysyłane z coraz dalszych miejsc, jak przy dźwięku. Dodatkowo okres zegara źródła jest wydłużony o czynnik $\gamma$ (dylatacja czasu). Iloczyn obu efektów daje pierwiastek.

**Poprzeczny efekt Dopplera.** Gdy źródło porusza się prostopadle do linii widzenia, klasyczny efekt znika, ale relatywistyczny pozostaje: $f = f_0/\gamma$. To bezpośredni pomiar dylatacji czasu (Ives–Stilwell, 1938).

**Przesunięcie ku czerwieni** $z = \dfrac{\lambda - \lambda_0}{\lambda_0}$:

$$1 + z = \sqrt{\frac{1 + \beta}{1 - \beta}}.$$

Dla małych prędkości $z \approx \beta$.
- Galaktyki oddalają się zgodnie z prawem Hubble'a $v = H_0d$, a ich widma są przesunięte ku czerwieni.
- Przy dużych odległościach przesunięcie jest skutkiem rozszerzania przestrzeni i interpretuje się je kosmologicznie (24), a nie jako prosty efekt Dopplera.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $f = f_0\sqrt{(1 - \beta)/(1 + \beta)}$ | oddalanie | ruch wzdłuż linii widzenia |
| $f = f_0\sqrt{(1 + \beta)/(1 - \beta)}$ | zbliżanie | j.w. |
| $1 + z = \sqrt{(1 + \beta)/(1 - \beta)}$, $z \approx \beta$ | przesunięcie ku czerwieni | $z \approx \beta$ dla $\beta \ll 1$ |
| $f = f_0/\gamma$ | poprzeczny efekt Dopplera | ruch prostopadły |
| $\Delta f \approx 2vf/c$ | radar | $v \ll c$, odbicie |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Linia wodoru $\mathrm H\alpha$ (656,3 nm) w widmie galaktyki ma długość 721,9 nm. Oblicz $z$ i prędkość oddalania z wzoru relatywistycznego i nierelatywistycznego.

$z = 65{,}6/656{,}3 \approx 0{,}100$. Nierelatywistycznie $v \approx 0{,}100c$. Relatywistycznie $(1 + z)^2 = \dfrac{1 + \beta}{1 - \beta} \Rightarrow \beta = \dfrac{(1 + z)^2 - 1}{(1 + z)^2 + 1} \approx 0{,}095$. Różnica 5%.

**Zadanie 2.** Wyprowadź wzór relatywistyczny. Źródło oddala się z prędkością $v$ i wysyła grzbiety co $T_0$ (czas własny).

W układzie odbiornika okres źródła wynosi $\gamma T_0$. W tym czasie źródło oddala się o $v\gamma T_0$, więc kolejny grzbiet ma dłuższą drogę. Odstęp czasu między grzbietami docierającymi do odbiornika:

$$T = \gamma T_0\left(1 + \frac vc\right) = T_0\frac{1 + \beta}{\sqrt{1 - \beta^2}} = T_0\sqrt{\frac{1 + \beta}{1 - \beta}}.$$

Stąd $f = 1/T = f_0\sqrt{(1 - \beta)/(1 + \beta)}$.

**Zadanie 3.** Rozwiń wzór dla małych $\beta$ do drugiego rzędu i porównaj z wzorem klasycznym dla poruszającego się źródła $f_0/(1 + \beta)$.

$\sqrt{\dfrac{1 - \beta}{1 + \beta}} \approx 1 - \beta + \dfrac{\beta^2}{2}$, a $\dfrac{1}{1 + \beta} \approx 1 - \beta + \beta^2$. Różnią się w drugim rzędzie o $-\beta^2/2$, czyli dokładnie o czynnik $1/\gamma$ (poprzeczny efekt Dopplera).

## Typowe pułapki

- **Wzór dla dźwięku dla światła.** Dla światła nie ma ośrodka. Liczy się tylko prędkość względna, w relatywistycznym wzorze.
- **Brak efektu przy ruchu poprzecznym.** Relatywistycznie występuje: $f = f_0/\gamma$.
- **Prędkość galaktyki $v = zc$ dla dużych $z$.** Dla $z > 1$ dałoby to $v > c$. Wzór relatywistyczny daje $v < c$, a dla galaktyk bardzo odległych trzeba modelu kosmologicznego.
- **Zbliżanie = przesunięcie ku czerwieni.** Zbliżanie daje przesunięcie ku fioletowi (np. galaktyka Andromedy).

## Doświadczenie / symulacja

**Prędkość gwiazdy z widma.** Pobierz widmo gwiazdy z publicznej bazy (np. SDSS lub ELODIE) i znajdź przesunięcie linii wodoru względem wartości laboratoryjnych. Oblicz prędkość radialną. Dla gwiazd w Galaktyce wychodzą dziesiątki km/s.

**Python:** porównanie wzoru klasycznego i relatywistycznego oraz prędkość z przesunięcia ku czerwieni.

```python
import numpy as np
import matplotlib.pyplot as plt

b = np.linspace(-0.9, 0.9, 400)
rel = np.sqrt((1 - b)/(1 + b))
klas_zrodlo = 1/(1 + b)
klas_odb = 1 - b
plt.plot(b, rel, label="relatywistyczny"); plt.plot(b, klas_zrodlo, "--", label="klasyczny, ruchome źródło")
plt.plot(b, klas_odb, ":", label="klasyczny, ruchomy odbiornik")
for z in (0.01, 0.1, 1.0, 3.0):
    beta = ((1 + z)**2 - 1)/((1 + z)**2 + 1)
    print(f"z = {z:5.2f}: β relatywistycznie = {beta:.4f}, β ≈ z = {z:.2f}")
print(f"Hα 656,3 nm przy z = 0,1: λ = {656.3*1.1:.1f} nm")
plt.xlabel("β (dodatnie: oddalanie)"); plt.ylabel("f / f0"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Galaktyka zbliża się do nas. Czy jej linie widmowe są przesunięte ku czerwieni, czy ku fioletowi?

<details>
<summary>Odpowiedź</summary>

Ku fioletowi (krótsze fale).
</details>

2. Linia o długości 500 nm w widmie gwiazdy ma 500,05 nm. Z jaką prędkością gwiazda się oddala?

<details>
<summary>Odpowiedź</summary>

$z = 10^{-4}$, $v \approx zc = 30\ \mathrm{km/s}$.
</details>

### B. Poziom akademicki

1. Statek kosmiczny zbliża się do Ziemi z prędkością $0{,}5c$ i nadaje na częstotliwości 1 GHz. Jaką częstotliwość odbiera stacja? A gdy się oddala?

<details>
<summary>Odpowiedź</summary>

Zbliżanie: $\sqrt{3} \approx 1{,}73\ \mathrm{GHz}$. Oddalanie: $1/\sqrt3 \approx 0{,}58\ \mathrm{GHz}$.
</details>

2. Kwazar ma $z = 2$. Oblicz $\beta$ ze wzoru Dopplera. Dlaczego ten wynik jest tylko orientacyjny?

<details>
<summary>Odpowiedź</summary>

$(1 + z)^2 = 9 \Rightarrow \beta = 8/10 = 0{,}8$. Przy tak dużych odległościach przesunięcie wynika głównie z rozszerzania Wszechświata, a „prędkość” zależy od przyjętego modelu kosmologicznego (24).
</details>

3. Pokaż, że dla radaru (odbicie od obiektu oddalającego się z prędkością $v$) odbierana częstotliwość wynosi $f_0\dfrac{1 - \beta}{1 + \beta}$, a dla małych $\beta$ przesunięcie to $2vf_0/c$.

<details>
<summary>Odpowiedź</summary>

Obiekt odbiera $f_0\sqrt{(1 - \beta)/(1 + \beta)}$ i jako źródło wysyła ją z powrotem, więc czynnik działa dwa razy. Dla małych $\beta$: $\dfrac{1 - \beta}{1 + \beta} \approx 1 - 2\beta$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 5 — §5.7: relatywistyczny efekt Dopplera.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §37.5; wyd. 1: t. 4, §38.10.
