# 08.04 — Lepkość i turbulencja

> **Moduł:** [08 — Mechanika płynów](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 14: [§14.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-7-lepkosc-i-turbulencje) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-wstep)

← [Równanie ciągłości i równanie Bernoulliego](03-rownanie-bernoulliego.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Prawdziwe płyny mają tarcie wewnętrzne — lepkość. To ona sprawia, że woda w rurze płynie najszybciej w środku, że do przepchnięcia cieczy przez długą rurę potrzebna jest różnica ciśnień, że miód spływa wolniej niż woda. Prawo Poiseuille'a tłumaczy, dlaczego niewielkie zwężenie tętnicy tak bardzo ogranicza przepływ krwi, a liczba Reynoldsa mówi, kiedy gładki przepływ zamienia się w turbulentny wir — od kranu po skrzydło samolotu.

## Teoria w pigułce

**Lepkość.** Warstwy płynu przesuwające się względem siebie działają na siebie siłą styczną (naprężeniem ścinającym) proporcjonalną do gradientu prędkości:

$$\tau = \eta\frac{dv}{dy}.$$

Współczynnik $\eta$ to **lepkość dynamiczna** ($\mathrm{Pa\cdot s}$): woda ok. $1{,}0\cdot10^{-3}$, krew ok. $3$–$4\cdot10^{-3}$, olej silnikowy ok. $0{,}1$–$0{,}3$, miód ok. $10$, powietrze $1{,}8\cdot10^{-5}$. Lepkość cieczy szybko maleje z temperaturą (stąd oleje zimowe), lepkość gazów — rośnie.

**Przepływ laminarny w rurze.** Płyn przy ściankach spoczywa (warunek przylegania), a prędkość rośnie ku osi rury, tworząc paraboliczny profil:

$$v(r) = \frac{\Delta p}{4\eta L}(R^2 - r^2).$$

**Prawo Poiseuille'a** — strumień objętości przez rurę o promieniu $R$ i długości $L$:

$$Q = \frac{\pi R^4\Delta p}{8\eta L}.$$

Zależność od **czwartej potęgi** promienia jest kluczowa: rura o połowę węższa przepuszcza 16 razy mniej. Analogia z prawem Ohma: $\Delta p = Q\cdot R_h$, opór hydrauliczny $R_h = 8\eta L/(\pi R^4)$.

**Liczba Reynoldsa** porównuje siły bezwładności z siłami lepkości:

$$\mathrm{Re} = \frac{\rho vd}{\eta},$$

gdzie $d$ — charakterystyczny rozmiar (np. średnica rury). Dla przepływu w rurze: $\mathrm{Re} \lesssim 2000$ — laminarny, $\mathrm{Re} \gtrsim 4000$ — **turbulentny** (chaotyczne wiry, znacznie większe straty energii). Liczba Reynoldsa decyduje też o tym, czy opór ciała jest liniowy (prawo Stokesa) czy kwadratowy (03.05).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\tau = \eta\,dv/dy$ | prawo lepkości Newtona | płyny newtonowskie (woda, olej, powietrze) |
| $v(r) = \dfrac{\Delta p}{4\eta L}(R^2 - r^2)$ | profil prędkości | przepływ laminarny w rurze |
| $Q = \dfrac{\pi R^4\Delta p}{8\eta L}$ | prawo Poiseuille'a | j.w. |
| $\bar{v} = Q/(\pi R^2) = v_{\max}/2$ | prędkość średnia | j.w. |
| $\mathrm{Re} = \rho vd/\eta$ | liczba Reynoldsa | $\mathrm{Re} < 2000$ — laminarny (rura) |
| $F = 6\pi\eta rv$ | prawo Stokesa | kula, $\mathrm{Re} \lesssim 1$ (03.05) |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1 — wyprowadzenie profilu i prawa Poiseuille'a.** Rozważ walec płynu o promieniu $r$ i długości $L$ wewnątrz rury. Różnica ciśnień pcha go siłą $\Delta p\cdot\pi r^2$, a lepkość na jego powierzchni bocznej hamuje siłą $\eta\left\lvert\dfrac{dv}{dr}\right\rvert2\pi rL$. W przepływie ustalonym siły się równoważą:

$$\Delta p\,\pi r^2 = -\eta\frac{dv}{dr}2\pi rL \Rightarrow \frac{dv}{dr} = -\frac{\Delta p}{2\eta L}r.$$

Całkując z warunkiem $v(R) = 0$: $v(r) = \dfrac{\Delta p}{4\eta L}(R^2 - r^2)$. Strumień objętości przez pierścienie o polu $2\pi r\,dr$:

$$Q = \int_0^Rv(r)\,2\pi r\,dr = \frac{\pi\Delta p}{2\eta L}\int_0^R(R^2r - r^3)\,dr = \frac{\pi R^4\Delta p}{8\eta L}.$$

**Zadanie 2 — rurka.** Woda ($\eta = 10^{-3}\ \mathrm{Pa\cdot s}$) płynie rurką o promieniu 1 mm i długości 1 m przy różnicy ciśnień 1000 Pa. Oblicz strumień, średnią prędkość i sprawdź, czy przepływ jest laminarny.

$Q = \dfrac{\pi(10^{-3})^4\cdot1000}{8\cdot10^{-3}\cdot1} \approx 3{,}9\cdot10^{-7}\ \mathrm{m^3/s} \approx 0{,}39\ \mathrm{mL/s}$; $\bar{v} = Q/(\pi R^2) \approx 0{,}125\ \mathrm{m/s}$; $\mathrm{Re} = \dfrac{1000\cdot0{,}125\cdot0{,}002}{10^{-3}} = 250$ — laminarny.

## Typowe pułapki

- **Strumień proporcjonalny do pola przekroju ($R^2$).** Przy stałej różnicy ciśnień — do $R^4$.
- **Poiseuille dla przepływu turbulentnego.** Wzór obowiązuje tylko dla przepływu laminarnego.
- **Średnica a promień w liczbie Reynoldsa.** Dla rur zwykle przyjmuje się średnicę; sprawdzaj konwencję.
- **Lepkość rośnie z temperaturą.** Dla cieczy maleje, dla gazów rośnie.
- **Bernoulli w długich, wąskich rurach.** Pomija spadek ciśnienia przez lepkość, który tam dominuje.

## Doświadczenie / symulacja

**Porównanie lepkości.** Zmierz czas wypływu tej samej objętości wody, oleju i (ogrzanego) miodu przez słomkę lub lejek. Porównaj z wartościami tablicowymi i sprawdź, jak czas wypływu oleju zmienia się z temperaturą (olej z lodówki i ciepły).

**Wiskozymetr Stokesa** — opadanie kulek w oleju lub miodzie, opisany w [03.05](../03-dynamika/05-opor-osrodka.md).

**Python:** profil prędkości i zależność strumienia od promienia — skutki zwężenia naczynia krwionośnego.

```python
import numpy as np
import matplotlib.pyplot as plt

eta, L, dp, R = 3.5e-3, 0.1, 500.0, 2e-3        # krew, odcinek 10 cm, Δp = 500 Pa, R = 2 mm
r = np.linspace(-R, R, 200)
v = dp/(4*eta*L)*(R**2 - r**2)
Q = np.pi*R**4*dp/(8*eta*L)
print(f"v_max = {v.max():.2f} m/s, Q = {Q*1e6:.2f} mL/s, Re ≈ {1060*Q/(np.pi*R**2)*2*R/eta:.0f}")
for f in (1.0, 0.9, 0.8, 0.5):
    print(f"promień {f:.0%}: przepływ {f**4:.0%} pierwotnego przy tej samej różnicy ciśnień")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].plot(v, r*1000); ax[0].set_xlabel("v [m/s]"); ax[0].set_ylabel("r [mm]"); ax[0].grid(True)
f = np.linspace(0.3, 1, 100)
ax[1].plot(f*100, f**4*100); ax[1].set_xlabel("promień [% pierwotnego]"); ax[1].set_ylabel("przepływ [%]"); ax[1].grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Dlaczego zimą olej w silniku samochodu stawia większy opór niż latem?

<details>
<summary>Odpowiedź</summary>

Lepkość cieczy rośnie wraz ze spadkiem temperatury.
</details>

2. Dlaczego dym z papierosa unosi się najpierw gładką smugą, a wyżej tworzy kłębiące się wiry?

<details>
<summary>Odpowiedź</summary>

Gorący dym przyspiesza, unosząc się; rośnie prędkość i szerokość smugi, a więc liczba Reynoldsa — przepływ przechodzi z laminarnego w turbulentny.
</details>

### B. Poziom akademicki

1. Oblicz liczbę Reynoldsa dla wody płynącej z prędkością 2 m/s w wężu ogrodowym o średnicy 1,6 cm. Jaki to przepływ?

<details>
<summary>Odpowiedź</summary>

$\mathrm{Re} = 1000\cdot2\cdot0{,}016/10^{-3} = 32\,000$ — turbulentny.
</details>

2. Tętnica zwęża się (np. przez blaszkę miażdżycową) tak, że jej promień maleje o 20%. Jak zmieni się przepływ krwi przy tej samej różnicy ciśnień? O ile musiałaby wzrosnąć różnica ciśnień, żeby zachować przepływ?

<details>
<summary>Odpowiedź</summary>

$0{,}8^4 \approx 0{,}41$ — przepływ spada do 41%; różnica ciśnień musiałaby wzrosnąć ok. 2,4 razy.
</details>

3. Pokaż, że średnia prędkość w przepływie Poiseuille'a jest połową prędkości maksymalnej.

<details>
<summary>Odpowiedź</summary>

$v_{\max} = \dfrac{\Delta pR^2}{4\eta L}$, $\bar{v} = \dfrac{Q}{\pi R^2} = \dfrac{\Delta pR^2}{8\eta L} = \dfrac{v_{\max}}{2}$.
</details>

4. Strzykawka ma tłok o średnicy 1 cm i igłę o długości 2 cm i średnicy wewnętrznej 0,4 mm. Jaką siłą trzeba naciskać tłok, żeby wstrzykiwać wodę z szybkością $0{,}5\ \mathrm{mL/s}$? (Pomiń opór w samej strzykawce.)

<details>
<summary>Odpowiedź</summary>

$\Delta p = \dfrac{8\eta LQ}{\pi R^4} = \dfrac{8\cdot10^{-3}\cdot0{,}02\cdot5\cdot10^{-7}}{\pi(2\cdot10^{-4})^4} \approx 1{,}6\cdot10^4\ \mathrm{Pa}$; $F = \Delta p\cdot\pi(0{,}005)^2 \approx 1{,}25\ \mathrm{N}$. ($\mathrm{Re} \approx 1600$ — jeszcze laminarny.)
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 14 — §14.7: lepkość i turbulencje, prawo Poiseuille'a, liczba Reynoldsa.
