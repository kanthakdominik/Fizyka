# 19.05 — Pęd i energia relatywistyczna, E = mc²

> **Moduł:** [19 — Szczególna teoria względności](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 5: [§5.8–5.9](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/5-8-ped-relatywistyczny) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/5-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §37.6 (s. 215)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§38.11–38.12, s. 171](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=186) — PDF z serwera AGH

← [Relatywistyczny efekt Dopplera](04-relatywistyczny-doppler.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

$E = mc^2$ to najsłynniejszy wzór fizyki. Mówi, że masa jest formą energii. Wyjaśnia, skąd Słońce bierze energię, jak działają elektrownie jądrowe (22) i dlaczego w akceleratorach z energii zderzeń powstają nowe cząstki. Relatywistyczne wzory na pęd i energię są potrzebne wszędzie, gdzie cząstki poruszają się z prędkościami bliskimi światła: w lampach rentgenowskich, mikroskopach elektronowych, akceleratorach medycznych i w promieniowaniu kosmicznym.

## Teoria w pigułce

**Pęd relatywistyczny.** Żeby zasada zachowania pędu obowiązywała we wszystkich układach inercjalnych, pęd musi mieć postać

$$\vec p = \gamma m\vec v.$$

$m$ to masa (spoczynkowa), taka sama we wszystkich układach. Przy $v \to c$ pęd rośnie nieograniczenie, więc żadna skończona siła nie rozpędzi ciała do prędkości światła.

**Energia całkowita i spoczynkowa:**

$$E = \gamma mc^2, \qquad E_0 = mc^2, \qquad E_k = E - mc^2 = (\gamma - 1)mc^2.$$

Dla $v \ll c$: $(\gamma - 1)mc^2 \approx \tfrac12mv^2$, czyli wzór klasyczny.

**Związek energii z pędem:**

$$E^2 = (pc)^2 + (mc^2)^2.$$

Dla cząstek bezmasowych (foton): $E = pc$, a prędkość zawsze wynosi $c$. Dla cząstek ultrarelatywistycznych ($E \gg mc^2$) też $E \approx pc$.

**Jednostki w fizyce cząstek:** energia w eV (12.05), pęd w eV/$c$, masa w eV/$c^2$. Elektron ma $m_ec^2 = 0{,}511\ \mathrm{MeV}$, proton $938{,}3\ \mathrm{MeV}$.

**Równoważność masy i energii.** Masa układu związanego jest mniejsza od sumy mas składników o energię wiązania podzieloną przez $c^2$: $\Delta m = E_{\text{wiązania}}/c^2$ (**defekt masy**). W reakcjach chemicznych to ułamki miliardowe masy, niemierzalne. W reakcjach jądrowych to ułamki procenta (22). Słońce traci w ten sposób ok. 4 mln ton masy na sekundę.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec p = \gamma m\vec v$ | pęd relatywistyczny | — |
| $E = \gamma mc^2$, $E_0 = mc^2$ | energia całkowita i spoczynkowa | — |
| $E_k = (\gamma - 1)mc^2$ | energia kinetyczna | — |
| $E^2 = (pc)^2 + (mc^2)^2$ | związek energii z pędem | — |
| $E = pc$ | cząstka bezmasowa | foton |
| $v/c = pc/E$ | prędkość z energii i pędu | — |

## Przykład rozwiązany

**Zadanie 1.** Elektron ma energię kinetyczną 1 MeV. Oblicz $\gamma$, prędkość i pęd. Porównaj z wynikiem klasycznym.

$\gamma = 1 + E_k/(m_ec^2) = 1 + 1/0{,}511 \approx 2{,}96$. $v = c\sqrt{1 - 1/\gamma^2} \approx 0{,}94c$.

$pc = \sqrt{E^2 - (mc^2)^2} = \sqrt{1{,}511^2 - 0{,}511^2} \approx 1{,}42\ \mathrm{MeV}$, czyli $p \approx 1{,}42\ \mathrm{MeV}/c$.

Klasycznie: $v = \sqrt{2E_k/m} = c\sqrt{2/0{,}511} \approx 1{,}98c$. To jest niemożliwe, więc wzór klasyczny zawodzi całkowicie.

**Zadanie 2.** Protony w LHC mają energię 6,8 TeV. Oblicz $\gamma$ i o ile ich prędkość jest mniejsza od prędkości światła.

$\gamma = E/(mc^2) = 6800/0{,}938 \approx 7250$. $1 - v/c \approx \dfrac{1}{2\gamma^2} \approx 9{,}5\cdot10^{-9}$. Protony są wolniejsze od światła o ok. 3 m/s.

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie energii kinetycznej.** Praca siły przy rozpędzaniu ze spoczynku:

$$E_k = \int F\,dx = \int\frac{dp}{dt}v\,dt = \int v\,dp.$$

Przez części: $E_k = pv - \displaystyle\int_0^vp\,dv' = \gamma mv^2 - \int_0^v\frac{mv'}{\sqrt{1 - v'^2/c^2}}dv' = \gamma mv^2 + mc^2\left(\sqrt{1 - v^2/c^2} - 1\right).$

Po uproszczeniu: $E_k = \gamma mc^2 - mc^2$. Rozwinięcie dla małych $v$: $\gamma \approx 1 + \tfrac12\beta^2 + \tfrac38\beta^4$, więc $E_k \approx \tfrac12mv^2 + \tfrac38mv^4/c^2$.

## Typowe pułapki

- **Masa rośnie z prędkością.** We współczesnym ujęciu masa jest stała, a rośnie energia i pęd ($\gamma m$ to dawna „masa relatywistyczna”, pojęcie mylące).
- **$E_k = \tfrac12mv^2$ przy dużych prędkościach.** Daje bezsensowne wyniki ($v > c$). Trzeba używać $(\gamma - 1)mc^2$.
- **$E = mc^2$ dla ciała w ruchu.** $mc^2$ to energia spoczynkowa. Całkowita to $\gamma mc^2$.
- **Foton ma masę $E/c^2$.** Foton ma masę zero. Ma energię i pęd $E/c$.
- **Defekt masy tylko w reakcjach jądrowych.** Dotyczy każdego układu związanego, ale w chemii jest niemierzalnie mały.

## Doświadczenie / symulacja

**Masa i energia w liczbach.** Policz w Pythonie (kod niżej), ile masy traci Słońce na sekundę, ile energii daje 1 g materii i jaki jest defekt masy cząsteczki wodoru. Porównaj rzędy wielkości reakcji chemicznych i jądrowych.

**Python:** prędkość w funkcji energii kinetycznej (relatywistycznie i klasycznie) i przykłady $E = mc^2$.

```python
import numpy as np
import matplotlib.pyplot as plt

c = 2.998e8
me, mp = 0.511, 938.272                              # MeV
Ek = np.logspace(-3, 2, 300)                         # MeV
for m, nazwa in [(me, "elektron"), (mp, "proton")]:
    g = 1 + Ek/m
    plt.semilogx(Ek, np.sqrt(1 - 1/g**2), label=f"{nazwa} (SR)")
    plt.semilogx(Ek, np.minimum(np.sqrt(2*Ek/m), 2), "--", label=f"{nazwa} (klasycznie)")
g = 1 + 1/me
print(f"elektron 1 MeV: γ = {g:.2f}, v = {np.sqrt(1 - 1/g**2):.3f}c, pc = {np.sqrt((1 + me)**2 - me**2):.2f} MeV")
gL = 6800e3/mp
print(f"LHC 6,8 TeV: γ = {gL:.0f}, c − v ≈ {c/(2*gL**2):.1f} m/s")
print(f"Słońce traci {3.83e26/c**2:.2e} kg/s; 1 g ↔ {1e-3*c**2:.2e} J ≈ {1e-3*c**2/4.184e12:.1f} kt TNT")
print(f"H2: energia wiązania 4,5 eV to {4.5/(2*938.8e6):.1e} masy cząsteczki")
plt.xlabel("E_k [MeV]"); plt.ylabel("v / c"); plt.ylim(0, 1.5); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Ile energii odpowiada masie 1 g? Ile to kiloton trotylu (1 kt = $4{,}18\cdot10^{12}$ J)?

<details>
<summary>Odpowiedź</summary>

$E = mc^2 \approx 9\cdot10^{13}\ \mathrm J \approx 21{,}5\ \mathrm{kt}$.
</details>

2. Słońce emituje moc $3{,}83\cdot10^{26}\ \mathrm W$. Ile masy traci na sekundę?

<details>
<summary>Odpowiedź</summary>

$\Delta m = P/c^2 \approx 4{,}3\cdot10^9\ \mathrm{kg/s}$, ok. 4 mln ton na sekundę.
</details>

3. Przy jakiej prędkości energia kinetyczna ciała równa się jego energii spoczynkowej?

<details>
<summary>Odpowiedź</summary>

$\gamma = 2 \Rightarrow v = c\sqrt3/2 \approx 0{,}87c$.
</details>

4. Ile energii (w MeV) trzeba, żeby rozpędzić elektron do $0{,}99c$?

<details>
<summary>Odpowiedź</summary>

$\gamma \approx 7{,}09$, $E_k = (\gamma - 1)\cdot0{,}511 \approx 3{,}1\ \mathrm{MeV}$.
</details>

### B. Poziom akademicki

1. Pokaż, że $E^2 - (pc)^2 = (mc^2)^2$, wstawiając $E = \gamma mc^2$ i $p = \gamma mv$.

<details>
<summary>Odpowiedź</summary>

$\gamma^2m^2c^4 - \gamma^2m^2v^2c^2 = \gamma^2m^2c^4(1 - v^2/c^2) = m^2c^4$.
</details>

2. Pion ($m_\pi c^2 = 139{,}6\ \mathrm{MeV}$) w spoczynku rozpada się na mion ($105{,}7\ \mathrm{MeV}$) i neutrino (masa pomijalna). Oblicz energię kinetyczną mionu.

<details>
<summary>Odpowiedź</summary>

Pędy równe i przeciwne: $E_\nu = pc$, $E_\mu = \sqrt{(pc)^2 + m_\mu^2c^4}$, $E_\mu + E_\nu = m_\pi c^2$. Stąd $E_\mu = \dfrac{m_\pi^2 + m_\mu^2}{2m_\pi}c^2 \approx 109{,}8\ \mathrm{MeV}$, czyli $E_k \approx 4{,}1\ \mathrm{MeV}$.
</details>

3. Dwa protony zderzają się czołowo, każdy z energią całkowitą $E$. Jaka energia jest dostępna na wytworzenie nowych cząstek? Porównaj z protonem o energii $E'$ uderzającym w nieruchomy proton (tarcza stała). Jaka musi być $E'$, żeby dostępna energia była taka sama dla $E = 6{,}8\ \mathrm{TeV}$?

<details>
<summary>Odpowiedź</summary>

W wiązkach przeciwbieżnych cała energia $2E$ jest dostępna (pęd całkowity zero). Dla tarczy stałej energia dostępna to $\sqrt{2E'mc^2 + 2(mc^2)^2} \approx \sqrt{2E'mc^2}$. Równość z $2E$ wymaga $E' = 2E^2/(mc^2) \approx 10^{8}\ \mathrm{GeV}$, czyli $10^{17}$ eV. Dlatego buduje się zderzacze.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 10.1 — wykres energii całkowitej elektronu w funkcji prędkości ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2023, zad. 10.2 — v/c elektronu o energii kinetycznej równej 2 energiom spoczynkowym ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2023, zad. 10.3 — napięcie przyspieszające elektron ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2024, zad. 10.1 — stosunek energii całkowitej do spoczynkowej rozpędzonego elektronu ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2024, zad. 10.2 — napięcie przyspieszające elektron (relatywistycznie) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2025, zad. 10 — energia całkowita, masa i energia spoczynkowa ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2026, zad. 10 — v/c cząstki β⁻ o energii kinetycznej 1,311 MeV ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 5 — §5.8 (pęd relatywistyczny) i §5.9 (energia relatywistyczna).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §37.6; wyd. 1: t. 4, §38.11–38.12.
