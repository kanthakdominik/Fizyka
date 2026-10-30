# 22.07 — Oddziaływanie promieniowania z materią, dawki i ochrona

> **Moduł:** [22 — Fizyka jądrowa](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10: [§10.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-7-skutki-biologiczne-i-zastosowania-medyczne-promieniowania-jadrowego) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §42.7 (s. 187)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§43.7, s. 154](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=170) — PDF z serwera AGH

← [Synteza termojądrowa i energia gwiazd](06-synteza.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Promieniowanie jonizujące otacza nas zawsze: z kosmosu, ze skał, z radonu w piwnicach, z potasu we własnym ciele, a do tego z badań medycznych. Żeby rozsądnie ocenić ryzyko (zdjęcie RTG, tomografia, lot samolotem, mieszkanie w domu z granitu, elektrownia jądrowa), trzeba znać jednostki dawek, ich typowe wartości i sposoby ochrony. Ta wiedza jest też podstawą radioterapii i ochrony radiologicznej w szpitalach i przemyśle.

## Teoria w pigułce

**Promieniowanie jonizujące** ma energię wystarczającą do wybicia elektronów z atomów (od ok. 10 eV). Rodzaje i przenikliwość:
- **α** (jądra helu): silnie jonizuje, zasięg kilka cm w powietrzu. Zatrzymuje je kartka papieru lub naskórek. Niebezpieczne po wchłonięciu (radon, polon).
- **β** (elektrony, pozytony): zasięg do kilku metrów w powietrzu i kilku milimetrów w tkance. Zatrzymuje je kilka mm aluminium lub pleksi.
- **γ i promieniowanie rentgenowskie**: bardzo przenikliwe. Natężenie maleje wykładniczo, $I = I_0e^{-\mu x}$, a osłabia je ołów lub beton. **Warstwa połówkowa** to grubość zmniejszająca natężenie o połowę, np. ok. 1,2 cm ołowiu dla γ z kobaltu-60.
- **neutrony**: przenikliwe, spowalnia się je materiałami z wodorem (woda, polietylen) i pochłania borem.

**Wielkości dozymetryczne:**

| Wielkość | Definicja | Jednostka |
|---|---|---|
| aktywność | rozpady na sekundę (22.03) | Bq |
| dawka pochłonięta $D$ | energia pochłonięta na kg | grej, $1\ \mathrm{Gy} = 1\ \mathrm{J/kg}$ |
| dawka równoważna $H$ | $H = w_RD$, $w_R$ — czynnik wagowy promieniowania: 1 (γ, β), 20 (α), 2,5–20 (neutrony) | siwert (Sv) |
| dawka skuteczna $E$ | suma po narządach z czynnikami wagowymi tkanek | Sv |

**Typowe dawki (orientacyjne):**
- zjedzenie banana (potas-40): ok. 0,1 μSv;
- zdjęcie RTG klatki piersiowej: ok. 0,02–0,1 mSv;
- lot transatlantycki: ok. 0,05 mSv;
- średnia roczna dawka w Polsce: ok. 3 mSv, w większości ze źródeł naturalnych (radon, promieniowanie kosmiczne, ziemia, potas w ciele) i z diagnostyki medycznej;
- tomografia komputerowa brzucha: ok. 5–10 mSv;
- dopuszczalna dawka dla pracowników narażonych zawodowo: 20 mSv rocznie;
- jednorazowa dawka powodująca chorobę popromienną: od ok. 1 Sv; ok. 4–5 Sv jest śmiertelne dla połowy osób bez leczenia.

**Skutki biologiczne:**
- **deterministyczne** pojawiają się powyżej progu (rzędu 0,5–1 Sv) i są tym cięższe, im większa dawka: oparzenia, choroba popromienna;
- **stochastyczne** (nowotwory, skutki genetyczne): prawdopodobieństwo rośnie z dawką. Do celów ochrony przyjmuje się ok. 5% wzrostu ryzyka nowotworu śmiertelnego na siwert (model liniowy bezprogowy, ostrożne założenie dla małych dawek).

**Zasady ochrony:** czas (krócej), odległość (natężenie od źródła punktowego maleje jak $1/r^2$), osłona (warstwy połówkowe).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $D = E_{\text{poch}}/m$ [Gy] | dawka pochłonięta | — |
| $H = w_RD$ [Sv] | dawka równoważna | $w_R$: γ, β = 1; α = 20 |
| $I = I_0e^{-\mu x} = I_0(1/2)^{x/x_{1/2}}$ | osłabienie promieniowania γ | wiązka wąska |
| $\dot D \propto 1/r^2$ | odległość od źródła punktowego | brak osłon |
| $N_{\text{rozp}} = A_0\tau = A_0T_{1/2}/\ln2$ | wszystkie rozpady źródła | całkowity rozpad |

## Przykład rozwiązany

**Zadanie 1.** Człowiek o masie 70 kg pochłonął 0,07 J energii promieniowania γ. Oblicz dawkę pochłoniętą i równoważną. Ile wynosiłaby dawka równoważna, gdyby była to ta sama energia od cząstek α (np. z radonu w płucach)?

$D = 0{,}07/70 = 1\ \mathrm{mGy}$, $H = 1\ \mathrm{mSv}$ dla γ. Dla α: $H = 20\ \mathrm{mSv}$. Ta sama energia jest dla α wielokrotnie groźniejsza, bo jonizacja jest skupiona na krótkim odcinku i silniej uszkadza DNA.

Dawka 0,07 J podniosłaby temperaturę ciała o zaledwie $3\cdot10^{-7}$ K. Szkodliwość promieniowania nie wynika z energii, tylko z rozrywania pojedynczych cząsteczek.

**Zadanie 2.** Ile ołowiu osłabi promieniowanie γ kobaltu-60 100 razy? Ile razy osłabi je odsunięcie się od źródła z 1 m na 10 m?

$(1/2)^{x/1{,}2} = 0{,}01 \Rightarrow x = 1{,}2\cdot\log_2100 \approx 8\ \mathrm{cm}$ ołowiu. Odsunięcie: $(10/1)^2 = 100$ razy, tyle samo.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Pacjent dostaje do badania PET 300 MBq fluoru-18 ($T_{1/2} = 110\ \mathrm{min}$). Ile rozpadów zajdzie w jego ciele, jeśli pominiemy wydalanie? Ile energii unoszą fotony anihilacyjne?

$$N = \int_0^\infty A_0e^{-\lambda t}dt = \frac{A_0}{\lambda} = A_0\frac{T_{1/2}}{\ln2} = 3\cdot10^8\cdot\frac{6600}{0{,}693} \approx 2{,}9\cdot10^{12}.$$

Każdy rozpad daje dwa fotony 511 keV, czyli razem ok. 0,47 J. Tylko część energii zostaje pochłonięta w ciele (reszta wylatuje i jest rejestrowana przez detektory PET). Typowa dawka skuteczna z takiego badania to kilka mSv.

## Typowe pułapki

- **Bekerele = siwerty.** Bq mierzy aktywność źródła, a Sv skutek biologiczny w organizmie. Przeliczenie zależy od rodzaju promieniowania, energii, odległości i czasu.
- **Każda dawka jest niebezpieczna w równym stopniu.** Ryzyko rośnie z dawką. Naturalne tło (ok. 3 mSv rocznie) to punkt odniesienia.
- **Cząstki α są niegroźne, bo zatrzymuje je kartka.** Na zewnątrz ciała tak. Wewnątrz (radon, polon) są najbardziej szkodliwe.
- **Napromieniowany przedmiot staje się promieniotwórczy.** Promieniowanie γ i X nie powoduje promieniotwórczości. Neutrony mogą ją wywołać (aktywacja).
- **Ołów zatrzymuje wszystko.** Na neutrony lepsza jest woda lub polietylen.

## Doświadczenie / symulacja

**Licznik Geigera i odległość.** Ze szkolnym źródłem (lub z płytkami ceramicznymi z uranowym szkliwem, siatką do lamp gazowych z torem, nawozem potasowym) zmierz liczbę zliczeń w funkcji odległości i grubości osłon (papier, aluminium, ołów). Sprawdź prawo odwrotnych kwadratów i wyznacz warstwę połówkową. Odejmij tło.

**Radon w domu.** Detektory radonu (pasywne, na kilka miesięcy) pokazują stężenie w piwnicy i na parterze. Wyniki zależą od podłoża i wentylacji. Mapa radonowa Polski jest dostępna w Państwowej Agencji Atomistyki.

**Python:** osłabienie promieniowania w osłonach i dawka od źródła w czasie.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 15, 300)                           # cm
for nazwa, x12 in [("ołów", 1.2), ("stal", 2.1), ("beton", 6.2)]:
    plt.semilogy(x, 0.5**(x/x12), label=f"{nazwa} (warstwa połówkowa {x12} cm)")
    print(f"{nazwa}: osłabienie 100× wymaga {x12*np.log2(100):.1f} cm")
D, m = 0.07, 70.0
print(f"dawka {D/m*1e3:.1f} mGy; γ: {D/m*1e3:.1f} mSv, α: {20*D/m*1e3:.0f} mSv; ogrzanie ciała {D/(m*3500):.1e} K")
A0, T = 300e6, 110*60
print(f"F-18: rozpadów {A0*T/np.log(2):.2e}, energia fotonów {A0*T/np.log(2)*2*511e3*1.602e-19:.2f} J")
plt.xlabel("grubość [cm]"); plt.ylabel("I / I0 (Co-60)"); plt.legend(); plt.grid(True, which="both"); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Uszereguj promieniowanie α, β i γ według przenikliwości. Czym najlepiej osłonić każde z nich?

<details>
<summary>Odpowiedź</summary>

α < β < γ. α: kartka papieru. β: kilka mm aluminium lub pleksi. γ: ołów lub gruby beton.
</details>

2. Dawka pochłonięta od cząstek α wynosi 0,5 mGy. Ile wynosi dawka równoważna?

<details>
<summary>Odpowiedź</summary>

10 mSv.
</details>

3. Przy źródle w odległości 2 m moc dawki wynosi 40 μSv/h. Jak daleko trzeba odejść, żeby spadła do 1 μSv/h?

<details>
<summary>Odpowiedź</summary>

Natężenie maleje jak $1/r^2$: $r = 2\sqrt{40} \approx 12{,}6\ \mathrm m$.
</details>

4. Ile tomografii komputerowych (po ok. 8 mSv) odpowiada rocznemu limitowi dla pracowników (20 mSv)? A ile lat naturalnego tła (3 mSv)?

<details>
<summary>Odpowiedź</summary>

2,5 badania; ok. 2,7 roku tła na jedną tomografię.
</details>

### B. Poziom akademicki

1. Współczynnik osłabienia $\mu$ wiąże się z warstwą połówkową wzorem $x_{1/2} = \ln2/\mu$. Wyprowadź go z $I = I_0e^{-\mu x}$ i oblicz $\mu$ dla ołowiu i Co-60.

<details>
<summary>Odpowiedź</summary>

$e^{-\mu x_{1/2}} = \tfrac12 \Rightarrow x_{1/2} = \ln2/\mu$. Dla 1,2 cm: $\mu \approx 0{,}58\ \mathrm{cm^{-1}}$.
</details>

2. Źródło γ ma aktywność $A$ i emituje fotony o energii $E$ izotropowo. Pokaż, że strumień energii w odległości $r$ wynosi $\dfrac{AE}{4\pi r^2}$. Oblicz go dla 1 MBq Co-60 (dwa fotony: 1,17 i 1,33 MeV) w odległości 1 m.

<details>
<summary>Odpowiedź</summary>

Wszystkie fotony przechodzą przez sferę $4\pi r^2$. Strumień: $10^6\cdot2{,}5\cdot1{,}6\cdot10^{-13}/(4\pi) \approx 3{,}2\cdot10^{-8}\ \mathrm{W/m^2}$. Tylko niewielka część tej energii zostaje pochłonięta w ciele, co daje moc dawki rzędu 0,3 μSv/h.
</details>

3. Zgodnie z modelem liniowym bezprogowym ryzyko nowotworu śmiertelnego rośnie o ok. 5% na Sv. Oszacuj dodatkowe ryzyko dla jednej tomografii (8 mSv) i porównaj z ryzykiem bazowym ok. 25%.

<details>
<summary>Odpowiedź</summary>

$0{,}008\cdot0{,}05 = 4\cdot10^{-4}$, czyli 0,04 punktu procentowego. To bardzo mało wobec ryzyka bazowego i zwykle dużo mniej niż korzyść z trafnej diagnozy. Model liniowy dla tak małych dawek jest założeniem ostrożnościowym, a nie zmierzoną zależnością.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10 — §10.7: biologiczne skutki promieniowania jądrowego.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §42.7; wyd. 1: t. 5, §43.7.
- Państwowa Agencja Atomistyki — raporty roczne o dawkach promieniowania w Polsce (paa.gov.pl).
