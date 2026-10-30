# 24.03 — Akceleratory i detektory cząstek

> **Moduł:** [24 — Cząstki elementarne i kosmologia](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 11: [§11.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/11-4-akceleratory-i-detektory-czastek) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/11-wstep)

← [Kwarki i Model Standardowy](02-kwarki-i-model-standardowy.md) · [spis modułu](README.md) · [Prawo Hubble'a, Wielki Wybuch i ewolucja Wszechświata](04-wielki-wybuch.md) →

## Po co to jest

Żeby zbadać strukturę mniejszą niż proton, potrzeba fal o długości poniżej $10^{-15}$ m, czyli cząstek o energiach rzędu GeV (20.04). Żeby wytworzyć ciężkie cząstki (W, Z, Higgs, kwark t), potrzeba energii zderzenia rzędu setek GeV ($E = mc^2$). Akceleratory to największe maszyny zbudowane przez ludzi, a detektory to wielopiętrowe „aparaty fotograficzne” robiące 40 milionów zdjęć na sekundę. Ta sama fizyka (siła Lorentza, dynamika relatywistyczna, oddziaływanie promieniowania z materią) działa w akceleratorach medycznych do radioterapii, w tomografii PET i w źródłach synchrotronowych, takich jak SOLARIS w Krakowie.

## Teoria w pigułce

**Akceleratory liniowe.** Cząstki przelatują przez kolejne wnęki rezonansowe, w których pole elektryczne fali o częstotliwości radiowej przyspiesza je we właściwej fazie. Przykłady: akceleratory medyczne (elektrony kilka–20 MeV), SLAC (3 km, 50 GeV).

**Cyklotron** (14.03). Pole magnetyczne zakrzywia tor, a napięcie zmienne między duantami przyspiesza cząstkę dwa razy na obieg. Częstotliwość obiegu $f = qB/(2\pi m)$ nie zależy od prędkości, dopóki cząstka nie jest relatywistyczna. Cyklotrony produkują izotopy medyczne (np. ¹⁸F do PET) i służą do protonoterapii (Centrum Cyklotronowe Bronowice w Krakowie).

**Synchrotron.** Przy energiach relatywistycznych masa efektywna rośnie, więc pole magnetyczne zwiększa się razem z energią, a cząstki krążą po stałym okręgu. Promień toru:

$$R = \frac{p}{qB}, \qquad p\,[\mathrm{GeV}/c] \approx 0{,}3\,B\,[\mathrm T]\,R\,[\mathrm m].$$

**LHC** (CERN): obwód 26,7 km, protony do 7 TeV, nadprzewodzące dipole 8,3 T (23.06). Protony mają $\gamma \approx 7500$ i są wolniejsze od światła o ok. 3 m/s.

**Promieniowanie synchrotronowe.** Cząstka na zakrzywionym torze promieniuje (16.05). Strata energii na obieg rośnie jak $\gamma^4/R$, więc dla elektronów ($m$ 1836 razy mniejsza) jest $1836^4 \approx 10^{13}$ razy większa niż dla protonów o tej samej energii. Dlatego zderzacze elektronów buduje się jako liniowe albo bardzo duże. Promieniowanie synchrotronowe jest też pożytecznym, bardzo jasnym źródłem promieniowania X i UV do badań materiałów i białek.

**Zderzacz czy tarcza?** Przy wiązce na nieruchomej tarczy większość energii idzie na ruch środka masy (24.01). Energia dostępna do tworzenia cząstek:
- tarcza: $\sqrt s \approx \sqrt{2mc^2E}$ (rośnie jak pierwiastek z $E$);
- dwie przeciwbieżne wiązki: $\sqrt s = 2E$.

Wiązka 7 TeV na tarczę daje tylko ok. 115 GeV, a zderzenie dwóch wiązek po 7 TeV daje 14 TeV.

**Detektory** wykorzystują jonizację i wzbudzenia wywołane przez cząstki naładowane:
- **dawniej**: emulsje fotograficzne, komory mgłowe (Wilsona) i pęcherzykowe — ślady widoczne bezpośrednio;
- **detektory śladowe** (krzemowe paski i piksele, komory gazowe) w polu magnetycznym: z krzywizny toru wyznacza się pęd i znak ładunku;
- **kalorymetry** pochłaniają cząstkę i mierzą jej całkowitą energię: elektromagnetyczne (elektrony, fotony) i hadronowe;
- **komory mionowe** na zewnątrz — miony przechodzą przez wszystko inne;
- **detektory Czerenkowa**: cząstka szybsza od światła w ośrodku ($v > c/n$) emituje stożek światła pod kątem $\cos\theta = 1/(n\beta)$ (Super-Kamiokande, wykrywanie neutrin);
- neutrina rejestruje się tylko pośrednio: po brakującym pędzie poprzecznym albo w ogromnych detektorach (50 000 t wody).

Wielki detektor (ATLAS, CMS) to warstwy wszystkich tych elementów ułożone jak cebula wokół punktu zderzenia.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $f = qB/(2\pi m)$, $K_{\max} = \dfrac{(qBR)^2}{2m}$ | cyklotron | $v \ll c$ |
| $p = qBR$; $p\,[\mathrm{GeV}/c] \approx 0{,}3BR$ | promień toru | dowolne $v$ (pęd relatywistyczny) |
| $\sqrt s = \sqrt{2mc^2E + 2(mc^2)^2}$ | energia w układzie środka masy | wiązka na tarczę (te same cząstki) |
| $\sqrt s = 2E$ | — | zderzacz symetryczny |
| $\Delta E_{\text{obieg}} \propto \gamma^4/R$; dla $e$: $88{,}5\ \mathrm{keV}\cdot E^4[\mathrm{GeV}]/R[\mathrm m]$ | strata na promieniowanie | synchrotron |
| $\cos\theta = 1/(n\beta)$, próg $\beta > 1/n$ | promieniowanie Czerenkowa | ośrodek o współczynniku $n$ |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Protony w LHC mają energię 7 TeV, a dipole wytwarzają 8,33 T. Oblicz promień zakrzywienia toru, czynnik Lorentza i różnicę prędkości protonów i światła.

$R = \dfrac{p}{eB} = \dfrac{7\cdot10^{12}\ \mathrm{eV}/c}{c\cdot8{,}33\ \mathrm T} \approx 2{,}8\ \mathrm{km}$ (dipole zajmują ok. dwie trzecie obwodu 26,7 km).

$\gamma = E/(m_pc^2) \approx 7460$. Z $\beta = \sqrt{1 - 1/\gamma^2} \approx 1 - \dfrac{1}{2\gamma^2}$: $c - v \approx \dfrac{c}{2\gamma^2} \approx 2{,}7\ \mathrm{m/s}$.

**Zadanie 2.** Elektrony w LEP (CERN, 1989–2000) miały 104,5 GeV, a promień zakrzywienia 3096 m. Ile energii traciły na obieg? Ile traciłby proton o tej samej energii?

$\Delta E = 88{,}5\ \mathrm{keV}\cdot104{,}5^4/3096 \approx 3{,}4\ \mathrm{GeV}$ na obieg — ponad 3% energii! Proton: mniej o $(m_p/m_e)^4 \approx 10^{13}$, czyli ok. 0,3 meV. Dlatego LHC (w tym samym tunelu) przyspiesza protony.

**Zadanie 3.** Wyprowadź energię dostępną przy zderzeniu z tarczą. Niezmiennik $s = (E_1 + E_2)^2 - (p_1c + p_2c)^2$ dla wiązki ($E$, $p$) i tarczy w spoczynku ($mc^2$, 0):

$$s = (E + mc^2)^2 - (pc)^2 = E^2 - (pc)^2 + 2Emc^2 + (mc^2)^2 = 2(mc^2)^2 + 2Emc^2.$$

Dla $E = 7\ \mathrm{TeV}$: $\sqrt s \approx 115\ \mathrm{GeV}$. Żeby na tarczy uzyskać 13,6 TeV (LHC, Run 3), wiązka musiałaby mieć ok. $10^{17}$ eV — energię spotykaną tylko w najbardziej energetycznym promieniowaniu kosmicznym.

## Typowe pułapki

- **Cyklotron przyspiesza do dowolnej energii.** Przy prędkościach relatywistycznych częstotliwość obiegu maleje i cząstka wypada z fazy. Potrzebny jest synchrocyklotron albo synchrotron.
- **Cząstki w LHC przyspiesza pole magnetyczne.** Pole magnetyczne tylko zakrzywia tor (siła prostopadła do prędkości nie wykonuje pracy). Przyspieszają wnęki z polem elektrycznym.
- **Promieniowanie Czerenkowa oznacza, że cząstka przekracza prędkość światła.** Przekracza prędkość światła w ośrodku ($c/n$), a nie $c$.
- **Detektor „widzi” cząstki.** Rejestruje sygnały elektryczne z jonizacji i błysków. Cząstki identyfikuje się, łącząc pomiary z wielu warstw.

## Doświadczenie / symulacja

**Komora mgłowa** (24.01) z magnesem neodymowym pod spodem: ślady lekkich elektronów zakrzywiają się wyraźnie, a ślady cząstek α prawie wcale.

**Detektor w smartfonie.** Aplikacje typu CREDO (projekt IFJ PAN) wykrywają cząstki promieniowania kosmicznego jako jasne punkty na zasłoniętej matrycy aparatu. Matryca CMOS to w istocie krzemowy detektor pikselowy (23.05).

**Python:** od krzywizny toru do pędu (dopasowanie okręgu do punktów z detektora z szumem), straty synchrotronowe i energia w układzie środka masy.

```python
import numpy as np

c, e, me, mp = 2.99792458e8, 1.602176634e-19, 0.000510999, 0.938272   # masy w GeV/c²
E, B = 7000.0, 8.33
print(f"LHC: R = {E*1e9/(c*B):.0f} m, γ = {E/mp:.0f}, c − v = {c/(2*(E/mp)**2):.2f} m/s")
print(f"LEP: strata na obieg {88.46e-6*104.5**4/3096:.2f} GeV; proton 7 TeV w LHC: {88.46*7000**4/2804*(me/mp)**4:.1f} keV")
for Ew in (7000, 1e5, 1e8):
    print(f"wiązka {Ew:.3g} GeV na tarczę: √s = {np.sqrt(2*mp*Ew + 2*mp**2):.0f} GeV; zderzacz {Ew:.3g} + {Ew:.3g} GeV: √s = {2*Ew:.3g} GeV")

# ślad cząstki w polu 2 T: punkty pomiarowe z 10 warstw krzemowych, rozdzielczość 20 μm
rng = np.random.default_rng(1)
Bp, p_true = 2.0, 1.5                                  # T, GeV/c
R_true = p_true/(0.3*Bp)
r_warstwy = np.linspace(0.05, 1.0, 10)                 # odległości warstw od osi [m]
phi = np.arcsin(r_warstwy/(2*R_true))                   # okrąg przechodzący przez (0, 0)
x = r_warstwy*np.cos(phi) + rng.normal(0, 20e-6, 10)
y = r_warstwy*np.sin(phi) + rng.normal(0, 20e-6, 10)
A = np.column_stack([x, y, np.ones_like(x)])            # dopasowanie okręgu x² + y² + Dx + Ey + F = 0
D, Ee, Fc = np.linalg.lstsq(A, -(x**2 + y**2), rcond=None)[0]
R_fit = np.sqrt(D**2/4 + Ee**2/4 - Fc)
print(f"promień toru: prawdziwy {R_true:.3f} m, dopasowany {R_fit:.3f} m → p = {0.3*Bp*R_fit:.3f} GeV/c")
n = 1.33
g = 1/np.sqrt(1 - 1/n**2)
print(f"próg Czerenkowa w wodzie: elektron K > {(g - 1)*me*1e3:.3f} MeV, mion K > {(g - 1)*0.10566*1e3:.1f} MeV, kąt maks. {np.degrees(np.arccos(1/n)):.1f}°")
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Cyklotron ma pole 1,5 T i promień 0,5 m. Oblicz częstotliwość obiegu protonu i jego maksymalną energię kinetyczną.

<details>
<summary>Odpowiedź</summary>

$f = \dfrac{eB}{2\pi m_p} \approx 22{,}9\ \mathrm{MHz}$. $K = \dfrac{(eBR)^2}{2m_p} \approx 27\ \mathrm{MeV}$ (jeszcze nierelatywistycznie: $K/m_pc^2 \approx 3\%$).
</details>

2. Dlaczego detektor cząstek umieszcza się w silnym polu magnetycznym?

<details>
<summary>Odpowiedź</summary>

Z kierunku zakrzywienia toru wynika znak ładunku, a z promienia krzywizny pęd cząstki: $p = qBR$.
</details>

### B. Poziom akademicki

1. Ślad w polu 4 T ma promień krzywizny 1 m. Jaki jest pęd cząstki? Jaka jest strzałka łuku $s = L^2/(8R)$ na odcinku $L = 1\ \mathrm m$ dla $R = 10\ \mathrm m$ i co z tego wynika dla pomiaru bardzo dużych pędów?

<details>
<summary>Odpowiedź</summary>

$p \approx 0{,}3\cdot4\cdot1 = 1{,}2\ \mathrm{GeV}/c$. Strzałka 12,5 mm; dla $R$ 100 razy większego (pęd 100 razy większy) tylko 0,125 mm. Ślady wysokoenergetycznych cząstek są prawie proste, więc względna niepewność pędu rośnie proporcjonalnie do $p$. Potrzebne są silne pola, długie ślady i precyzja rzędu mikrometrów.
</details>

2. Oblicz progową energię kinetyczną dla promieniowania Czerenkowa elektronu i mionu w wodzie ($n = 1{,}33$).

<details>
<summary>Odpowiedź</summary>

$\beta > 1/n \Rightarrow \gamma > 1/\sqrt{1 - 1/n^2} \approx 1{,}52$. Elektron: $K > 0{,}52\cdot0{,}511 \approx 0{,}26\ \mathrm{MeV}$. Mion: $K > 0{,}52\cdot105{,}7 \approx 55\ \mathrm{MeV}$. Kąt stożka dla $\beta \to 1$: $\arccos(1/1{,}33) \approx 41°$.
</details>

3. Wiązka LHC zawiera ok. 2800 paczek po $1{,}15\cdot10^{11}$ protonów o energii 6,8 TeV. Oblicz energię wiązki i porównaj z energią kinetyczną pociągu (400 t, 150 km/h).

<details>
<summary>Odpowiedź</summary>

$E \approx 2800\cdot1{,}15\cdot10^{11}\cdot6{,}8\cdot10^{12}\cdot1{,}6\cdot10^{-19}\ \mathrm J \approx 350\ \mathrm{MJ}$. Pociąg: $\tfrac12\cdot4\cdot10^5\cdot41{,}7^2 \approx 350\ \mathrm{MJ}$ — tyle samo. Dlatego wiązkę wyprowadza się do specjalnego bloku pochłaniającego (*beam dump*).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 11 — §11.4: akceleratory i detektory cząstek.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3, §28.5 (cyklotron i synchrotron) — fizyka akceleratorów kołowych (moduł 14.03).
- CERN, *LHC: the guide* — liczby i budowa LHC (materiał dodatkowy, po angielsku).
