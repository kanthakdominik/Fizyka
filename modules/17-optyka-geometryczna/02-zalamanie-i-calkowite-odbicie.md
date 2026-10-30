# 17.02 — Załamanie światła i całkowite wewnętrzne odbicie

> **Moduł:** [17 — Optyka geometryczna](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1: [§1.3–1.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-3-zalamanie) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §33.5–33.6 (s. 23)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§34.7–34.8, s. 21](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=36) — PDF z serwera AGH

← [Rozchodzenie się światła i prawo odbicia](01-rozchodzenie-i-odbicie.md) · [spis modułu](README.md) · [Rozszczepienie światła i pryzmat](03-dyspersja.md) →

## Po co to jest

Łyżeczka w szklance „łamie się”, basen wydaje się płytszy, niż jest, a diament błyszczy jak żaden inny kamień. Wszystko to robi załamanie światła. Całkowite wewnętrzne odbicie prowadzi światło w światłowodach, którymi płynie prawie cały internet, a także w endoskopach medycznych. Bez prawa Snelliusa nie ma soczewek (17.05), okularów ani aparatów.

## Teoria w pigułce

**Współczynnik załamania** ośrodka to stosunek prędkości światła w próżni do prędkości w ośrodku:

$$n = \frac cv \ge 1.$$

Przykładowe wartości (dla światła żółtego):

| Ośrodek | $n$ |
|---|---|
| powietrze | 1,0003 |
| woda | 1,33 |
| szkło | 1,5–1,9 |
| diament | 2,42 |

**Prawo załamania (Snelliusa):**

$$n_1\sin\theta_1 = n_2\sin\theta_2.$$

Wynika z zasady Huygensa (10.04) lub z zasady Fermata (najkrótszy czas). Przy przejściu do ośrodka gęstszego optycznie ($n_2 > n_1$) promień załamuje się **do normalnej**. Częstotliwość się nie zmienia, a długość fali maleje: $\lambda_n = \lambda/n$.

**Całkowite wewnętrzne odbicie.** Przy przejściu z ośrodka gęstszego do rzadszego ($n_1 > n_2$) kąt załamania jest większy od kąta padania. Od **kąta granicznego**

$$\sin\theta_{\text{gr}} = \frac{n_2}{n_1}$$

światło w ogóle nie wychodzi i całe się odbija. Dla szkła w powietrzu $\theta_{\text{gr}} \approx 42^\circ$, a dla diamentu tylko $24{,}4^\circ$, więc światło odbija się w nim wielokrotnie i wychodzi głównie przez górne ścianki szlifu.

**Światłowód.** Rdzeń o większym $n_1$ otacza płaszcz o mniejszym $n_2$. Promienie padające na granicę pod kątem większym od granicznego biegną zygzakiem, nie tracąc energii przez ścianki. Do światłowodu trafiają tylko promienie w stożku określonym przez **aperturę numeryczną** $\mathrm{NA} = \sqrt{n_1^2 - n_2^2}$.

**Głębokość pozorna.** Patrząc pionowo w dół na przedmiot pod wodą, widzimy go na głębokości $h' \approx h/n$. Basen o głębokości 2 m wydaje się mieć 1,5 m.

**Miraż.** Nad rozgrzanym asfaltem powietrze ma mniejszy współczynnik załamania niż wyżej. Promienie od nieba zakrzywiają się ku górze i widzimy „kałużę”, czyli odbicie nieba (10.04, zadanie B3, analogiczny efekt dla dźwięku).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $n = c/v$, $\ \lambda_n = \lambda/n$ | współczynnik załamania | — |
| $n_1\sin\theta_1 = n_2\sin\theta_2$ | prawo Snelliusa | — |
| $\sin\theta_{\text{gr}} = n_2/n_1$ | kąt graniczny | $n_1 > n_2$ |
| $h' \approx h/n$ | głębokość pozorna | patrzenie prawie pionowe |
| $\mathrm{NA} = \sin\theta_{\max} = \sqrt{n_1^2 - n_2^2}$ | apertura numeryczna światłowodu | wejście z powietrza |

## Przykład rozwiązany

**Zadanie 1.** Promień pada z powietrza na wodę pod kątem $45^\circ$. Oblicz kąt załamania i kąt graniczny dla granicy woda–powietrze.

$\sin\theta_2 = \sin45^\circ/1{,}33 \approx 0{,}53 \Rightarrow \theta_2 \approx 32^\circ$. $\theta_{\text{gr}} = \arcsin(1/1{,}33) \approx 48{,}8^\circ$.

Nurek patrzący w górę widzi całe niebo w stożku o kącie połówkowym $48{,}8^\circ$ (okno Snella), a poza nim lustrzane odbicie dna.

**Zadanie 2.** Światłowód ma rdzeń o $n_1 = 1{,}48$ i płaszcz o $n_2 = 1{,}46$. Oblicz kąt graniczny na granicy rdzeń–płaszcz i największy kąt, pod jakim może wejść światło z powietrza.

$\theta_{\text{gr}} = \arcsin(1{,}46/1{,}48) \approx 80{,}6^\circ$. $\mathrm{NA} = \sqrt{1{,}48^2 - 1{,}46^2} \approx 0{,}24$, więc kąt wejścia do ok. $14^\circ$.

## Typowe pułapki

- **Całkowite odbicie przy przejściu do ośrodka gęstszego.** Zachodzi tylko przy przejściu z gęstszego do rzadszego.
- **Przy załamaniu zmienia się częstotliwość (kolor).** Zmienia się długość fali, a częstotliwość i kolor nie.
- **Kąty od powierzchni.** We wzorze Snelliusa kąty są mierzone od normalnej.
- **Głębokość pozorna dla dowolnego kąta.** Wzór $h/n$ działa tylko przy patrzeniu prawie pionowym. Pod ukosem basen wydaje się jeszcze płytszy.
- **Gęstość optyczna = gęstość masy.** Nie zawsze: olej jest lżejszy od wody, ale ma większe $n$.

## Doświadczenie / symulacja

**Prawo Snelliusa z laserem i akwarium.** Wskaźnik laserowy skieruj ukośnie na powierzchnię wody w przezroczystym pojemniku z odrobiną mleka (rozpraszanie uwidacznia wiązkę). Zmierz kąty padania i załamania kątomierzem i wyznacz $n$ wody z wykresu $\sin\theta_1$ od $\sin\theta_2$. Skieruj wiązkę od dołu, przez ściankę, i znajdź kąt graniczny.

**Światłowód z wody.** Strumień wody wypływający z otworu w butelce, oświetlony laserem od tyłu przez wodę, prowadzi światło po łuku (fontanna świetlna Colladona).

**Symulacja PhET:** *Załamanie światła* (*Bending Light*) — zmieniaj ośrodki i kąty, obserwuj całkowite wewnętrzne odbicie.

**Python:** kąt załamania i współczynniki odbicia w funkcji kąta (wzory Fresnela dla światła niespolaryzowanego).

```python
import numpy as np
import matplotlib.pyplot as plt

def fresnel(n1, n2, th1):
    s = n1/n2*np.sin(th1)
    th2 = np.arcsin(np.clip(s, -1, 1))
    rs = ((n1*np.cos(th1) - n2*np.cos(th2))/(n1*np.cos(th1) + n2*np.cos(th2)))**2
    rp = ((n1*np.cos(th2) - n2*np.cos(th1))/(n1*np.cos(th2) + n2*np.cos(th1)))**2
    R = np.where(s >= 1, 1.0, (rs + rp)/2)          # całkowite wewnętrzne odbicie
    return np.degrees(th2), R

th = np.radians(np.linspace(0, 89.9, 500))
for n1, n2, lab in [(1.0, 1.33, "powietrze → woda"), (1.33, 1.0, "woda → powietrze")]:
    _, R = fresnel(n1, n2, th)
    plt.plot(np.degrees(th), R, label=lab)
t2, R0 = fresnel(1.0, 1.33, np.radians(45))
print(f"45° powietrze → woda: θ2 = {float(t2):.1f}°, odbija się {float(R0)*100:.1f} %")
print(f"kąt graniczny woda: {np.degrees(np.arcsin(1/1.33)):.1f}°, diament: {np.degrees(np.arcsin(1/2.42)):.1f}°")
plt.xlabel("kąt padania [°]"); plt.ylabel("współczynnik odbicia"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Światło biegnie w szkle o $n = 1{,}5$. Jaka jest jego prędkość i długość fali, jeśli w próżni ma 600 nm?

<details>
<summary>Odpowiedź</summary>

$v = 2\cdot10^8\ \mathrm{m/s}$, $\lambda = 400\ \mathrm{nm}$ (kolor się nie zmienia).
</details>

2. Oblicz kąt graniczny dla szkła ($n = 1{,}5$) i diamentu ($n = 2{,}42$) w powietrzu.

<details>
<summary>Odpowiedź</summary>

$41{,}8^\circ$ i $24{,}4^\circ$.
</details>

3. Moneta leży na dnie basenu o głębokości 2 m. Na jakiej głębokości widzimy ją, patrząc pionowo w dół?

<details>
<summary>Odpowiedź</summary>

Ok. 1,5 m.
</details>

4. Promień przechodzi przez płytkę szklaną o równoległych ściankach. Pokaż, że wychodzi równolegle do kierunku wejścia.

<details>
<summary>Odpowiedź</summary>

Na pierwszej ściance $\sin\theta_1 = n\sin\theta_2$, na drugiej $n\sin\theta_2 = \sin\theta_3$, więc $\theta_3 = \theta_1$. Promień jest tylko przesunięty równolegle.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Oblicz przesunięcie promienia przechodzącego przez płytkę szklaną ($n = 1{,}5$) o grubości 1 cm pod kątem $45^\circ$.

<details>
<summary>Odpowiedź</summary>

$\theta_2 = \arcsin(0{,}707/1{,}5) \approx 28{,}1^\circ$, $s = t\dfrac{\sin(\theta_1 - \theta_2)}{\cos\theta_2} \approx 3{,}3\ \mathrm{mm}$.
</details>

2. Wyprowadź wzór na głębokość pozorną $h' = h\dfrac{\tan\theta_2}{\tan\theta_1}$ i pokaż, że dla małych kątów daje $h/n$.

<details>
<summary>Odpowiedź</summary>

Promień z przedmiotu wychodzi w odległości poziomej $h\tan\theta_2$ (pod wodą) i przedłużony pod kątem $\theta_1$ w powietrzu przecina pion na głębokości $h\tan\theta_2/\tan\theta_1$. Dla małych kątów $\tan \approx \sin$, a $\sin\theta_2/\sin\theta_1 = 1/n$.
</details>

3. Współczynnik załamania powietrza zmienia się z wysokością. Promień biegnący prawie poziomo zakrzywia się wtedy z promieniem krzywizny $R = n/\lvert dn/dz\rvert$. Nad asfaltem $dn/dz \approx 10^{-5}\ \mathrm{m^{-1}}$. Oszacuj $R$ i odległość, z jakiej widać miraż przy oczach na wysokości 1,6 m.

<details>
<summary>Odpowiedź</summary>

$R \approx 10^5\ \mathrm m = 100\ \mathrm{km}$. Strzałka łuku $h = d^2/(2R)$, więc $d = \sqrt{2Rh} \approx \sqrt{2\cdot10^5\cdot1{,}6} \approx 570\ \mathrm m$. Miraż widać kilkaset metrów przed sobą.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1 — §1.3 (załamanie światła) i §1.4 (całkowite wewnętrzne odbicie).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §33.5–33.6; wyd. 1: t. 4, §34.7–34.8.
- Symulacja PhET *Załamanie światła*.
