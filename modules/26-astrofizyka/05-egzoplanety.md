# 26.05 — Egzoplanety: metody wykrywania i warunki do życia

> **Moduł:** [26 — Astrofizyka](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Czarne dziury i fale grawitacyjne](04-czarne-dziury.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Do 1992 r. nie znaliśmy żadnej planety poza Układem Słonecznym. Dziś znamy ich ponad 6000, a szacuje się, że w Drodze Mlecznej jest więcej planet niż gwiazd. Pierwsze egzoplanety odkrył polski astronom Aleksander Wolszczan (wokół pulsara PSR B1257+12, 1992), a warszawski projekt OGLE jest jednym z pionierów wykrywania planet przez mikrosoczewkowanie grawitacyjne. Egzoplanety odkrywa się prawie wyłącznie pośrednio — przez efekt Dopplera (10.07), zaćmienia, prawa Keplera (07.04) i środek masy (05.04). To świetne pole do zastosowania fizyki z matury: z kilku liczb da się wyznaczyć masę, promień, gęstość i temperaturę planety, której nikt nie widział.

## Teoria w pigułce

**Metoda prędkości radialnych (dopplerowska).** Gwiazda i planeta krążą wokół wspólnego środka masy. Gwiazda zatacza mały okrąg z prędkością $v_*$, więc jej linie widmowe przesuwają się okresowo o $\Delta\lambda/\lambda = v_r/c$. Z zasady zachowania pędu (środek masy w spoczynku) $M_*v_* = m_pv_p$. Amplituda prędkości gwiazdy:

$$K = \left(\frac{2\pi G}{P}\right)^{1/3}\frac{m_p\sin i}{M_*^{2/3}} \quad (m_p \ll M_*,\ \text{orbita kołowa}).$$

Jowisz porusza Słońce z prędkością 12,5 m/s, Ziemia — tylko 9 cm/s. Najlepsze spektrografy mierzą ok. 0,3–1 m/s, czyli względne przesunięcie linii $\sim10^{-9}$. Metoda daje $m_p\sin i$ ($i$ — nachylenie orbity, zwykle nieznane), więc tylko dolne oszacowanie masy. Tak odkryto pierwszą planetę wokół gwiazdy podobnej do Słońca: 51 Pegasi b (Mayor i Queloz, 1995, Nagroda Nobla 2019) — „gorący Jowisz” obiegający gwiazdę w 4,2 dnia.

**Metoda tranzytów.** Gdy planeta przechodzi przed tarczą gwiazdy, strumień spada o ułamek równy stosunkowi pól tarcz:

$$\frac{\Delta F}{F} = \left(\frac{R_p}{R_*}\right)^2.$$

Jowisz przed Słońcem: 1%; Ziemia: 0,008% (84 ppm). Tranzyt widać tylko wtedy, gdy orbita jest prawie „z boku”. Prawdopodobieństwo to ok. $R_*/a$ — dla Ziemi 0,5%. Dlatego satelity (Kepler, TESS) obserwują setki tysięcy gwiazd naraz. Ok. 3/4 znanych egzoplanet odkryto tą metodą. Tranzyt i prędkości radialne razem dają masę i promień, czyli **gęstość**: można odróżnić planetę skalistą od gazowej.

**Inne metody:**
- **mikrosoczewkowanie grawitacyjne** — gwiazda z planetą przechodzi przed odległą gwiazdą i wzmacnia jej światło jak soczewka (26.04); planeta daje krótki dodatkowy pik. Czuła na planety daleko od gwiazdy i nawet swobodne planety bez gwiazdy (OGLE);
- **chronometraż pulsarów** — planeta zaburza bardzo regularne impulsy (odkrycie Wolszczana);
- **bezpośrednie obrazowanie** — wymaga zasłonięcia blasku gwiazdy (koronograf); działa dla młodych, gorących planet daleko od gwiazdy;
- **astrometria** — chwianie się pozycji gwiazdy na niebie (satelita Gaia).

**Temperatura i ekosfera.** Planeta w odległości $a$ od gwiazdy pochłania moc $(1 - A)\dfrac{L}{4\pi a^2}\pi R_p^2$ ($A$ — albedo, ułamek odbitego światła) i wypromieniowuje $4\pi R_p^2\sigma T^4$. Stąd **temperatura równowagowa**

$$T_{\text{rów}} = T_*\sqrt{\frac{R_*}{2a}}(1 - A)^{1/4}.$$

Dla Ziemi ($A = 0{,}3$) to 255 K. Rzeczywista średnia temperatura (288 K) jest wyższa dzięki efektowi cieplarnianemu. **Ekosfera** (strefa zamieszkiwalna) to zakres odległości, w którym na powierzchni planety skalistej może istnieć woda w stanie ciekłym. Przy czerwonych karłach leży blisko gwiazdy, więc tam łatwiej wykryć małe planety: Proxima b (najbliższa egzoplaneta, 4,2 roku świetlnego) i siedem planet wielkości Ziemi wokół TRAPPIST-1.

**Atmosfery.** W czasie tranzytu światło gwiazdy przechodzi przez atmosferę planety. Porównując głębokość tranzytu w różnych długościach fal, Teleskop Jamesa Webba wykrywa w atmosferach egzoplanet wodę, CO₂ i metan (spektroskopia, 21.05).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $M_*v_* = m_pv_p$, $M_*a_* = m_pa_p$ | ruch wokół środka masy | układ izolowany |
| $K = \left(\dfrac{2\pi G}{P}\right)^{1/3}\dfrac{m_p\sin i}{M_*^{2/3}}$ | amplituda prędkości radialnej | orbita kołowa, $m_p \ll M_*$ |
| $\Delta\lambda/\lambda = v_r/c$ | przesunięcie dopplerowskie | $v \ll c$ |
| $\Delta F/F = (R_p/R_*)^2$ | głębokość tranzytu | planeta całkowicie na tle tarczy |
| $p_{\text{tr}} \approx R_*/a$ | prawdopodobieństwo tranzytu | losowa orientacja orbity |
| $T^2 = \dfrac{4\pi^2a^3}{G(M_* + m_p)}$ | III prawo Keplera | — |
| $T_{\text{rów}} = T_*\sqrt{R_*/(2a)}(1 - A)^{1/4}$ | temperatura równowagowa | szybki obrót lub atmosfera wyrównująca temperaturę |

## Przykład rozwiązany

**Zadanie 1.** Jak bardzo Jowisz porusza Słońcem? Oblicz promień orbity Słońca wokół środka masy układu i prędkość Słońca ($m_J = 1{,}9\cdot10^{27}\ \mathrm{kg}$, $a = 5{,}2\ \mathrm{AU}$, $P = 11{,}86$ roku).

$a_\odot = a\,m_J/M_\odot \approx 5{,}2\cdot9{,}5\cdot10^{-4}\ \mathrm{AU} \approx 0{,}005\ \mathrm{AU} = 7{,}4\cdot10^5\ \mathrm{km}$ — tuż ponad promieniem Słońca. $v_\odot = 2\pi a_\odot/P \approx 12{,}5\ \mathrm{m/s}$.

**Zadanie 2.** Tranzyt planety wokół gwiazdy podobnej do Słońca ma głębokość 1,0%, a okres 3,5 dnia. Oblicz promień planety i jej odległość od gwiazdy.

$R_p = R_*\sqrt{0{,}01} = 0{,}1R_\odot \approx 70\,000\ \mathrm{km}$ — rozmiar Jowisza. Z III prawa Keplera: $a = \left(\dfrac{GM_\odot P^2}{4\pi^2}\right)^{1/3} \approx 0{,}045\ \mathrm{AU}$ — „gorący Jowisz”, ponad 8 razy bliżej niż Merkury.

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie amplitudy $K$.** Planeta i gwiazda krążą z tą samą prędkością kątową $\omega = 2\pi/P$ wokół środka masy, w odległościach $a_p$ i $a_*$, gdzie $M_*a_* = m_pa_p$ i $a_* + a_p = a$. Prędkość gwiazdy $v_* = \omega a_* = \omega a\dfrac{m_p}{M_* + m_p}$. Z III prawa Keplera $a = \left(\dfrac{G(M_* + m_p)}{\omega^2}\right)^{1/3}$, więc

$$v_* = \frac{(G\omega)^{1/3}m_p}{(M_* + m_p)^{2/3}} \approx \left(\frac{2\pi G}{P}\right)^{1/3}\frac{m_p}{M_*^{2/3}}.$$

Obserwujemy tylko składową wzdłuż linii widzenia: $v_r(t) = K\sin(\omega t)$ z $K = v_*\sin i$.

**Czas trwania tranzytu** (orbita kołowa, przejście przez środek tarczy): planeta pokonuje cięciwę $2R_*$ z prędkością $2\pi a/P$, więc $t_{\text{tr}} \approx \dfrac{P}{\pi}\dfrac{R_*}{a}$. Dla Ziemi: ok. 13 godzin raz w roku.

## Typowe pułapki

- **Gwiazda stoi, a planeta krąży.** Obie krążą wokół środka masy. Bez tego ruchu gwiazdy metoda dopplerowska byłaby niemożliwa.
- **Metoda dopplerowska daje masę planety.** Daje $m\sin i$, czyli dolne oszacowanie. Pełną masę daje dopiero połączenie z tranzytem (wtedy $i \approx 90°$).
- **Brak tranzytu oznacza brak planety.** Większość orbit jest nachylona tak, że tranzytu nie widać.
- **Ekosfera oznacza życie.** Oznacza tylko, że na powierzchni mogłaby istnieć ciekła woda — o ile planeta ma odpowiednią atmosferę. Wenus leży na skraju ekosfery Słońca, a ma powierzchnię o temperaturze 460°C.

## Doświadczenie / symulacja

**Tranzyt w domu.** Postaw lampkę (gwiazda), a przed nią przesuwaj na nitce kulki różnej wielkości (planety). Mierz natężenie światła luksomierzem w phyphox (*Natężenie światła*). Sprawdź, że spadek jest proporcjonalny do pola przekroju kulki.

**Obserwacja prawdziwego tranzytu.** Almanach *Urania* zawiera tabele tranzytów egzoplanet widocznych z Polski ze spadkiem jasności powyżej 0,01 mag. Taki tranzyt można zarejestrować teleskopem o średnicy 20 cm z aparatem cyfrowym ([opis po polsku](https://www.urania.edu.pl/pliki/almanach/2024/Bloki/Egzoplanety_opis.pdf)).

**Python:** krzywa prędkości radialnej i krzywa jasności z szumem, dopasowanie amplitudy $K$ i głębokości tranzytu, wyznaczenie masy, promienia i gęstości planety.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

G, Msun, Rsun, MJ, RJ, dzien = 6.674e-11, 1.989e30, 6.957e8, 1.898e27, 6.9911e7, 86400
P, mp_true, Rp_true = 3.5*dzien, 0.7*MJ, 1.2*RJ             # gorący Jowisz wokół gwiazdy podobnej do Słońca
a = (G*Msun*P**2/(4*np.pi**2))**(1/3)
K_true = (2*np.pi*G/P)**(1/3)*mp_true/Msun**(2/3)
rng = np.random.default_rng(5)

t_rv = np.sort(rng.uniform(0, 20*dzien, 40))
rv = K_true*np.sin(2*np.pi*t_rv/P) + rng.normal(0, 5, t_rv.size)       # szum spektrografu 5 m/s
(K, faza), cov = curve_fit(lambda t, K, f: K*np.sin(2*np.pi*t/P + f), t_rv, rv, p0=[50, 0], sigma=np.full(t_rv.size, 5.0), absolute_sigma=True)
mp = K*Msun**(2/3)/(2*np.pi*G/P)**(1/3)
print(f"K = {abs(K):.1f} ± {np.sqrt(cov[0, 0]):.1f} m/s → m_p = {abs(mp)/MJ:.2f} M_J (prawdziwa {mp_true/MJ:.2f})")

t = np.linspace(-0.2*dzien, 0.2*dzien, 600)                   # wokół środka tranzytu
x = 2*np.pi*a*t/P                                           # położenie planety na tle tarczy
depth_true = (Rp_true/Rsun)**2
F = 1 - depth_true*(np.abs(x) < Rsun) + rng.normal(0, 1e-3, t.size)
depth = 1 - F[np.abs(x) < 0.8*Rsun].mean()
Rp = Rsun*np.sqrt(depth)
rho = abs(mp)/(4/3*np.pi*Rp**3)
print(f"głębokość {depth*100:.2f}% → R_p = {Rp/RJ:.2f} R_J, gęstość {rho:.0f} kg/m³ (Jowisz 1330, Ziemia 5510)")
print(f"a = {a/1.496e11:.3f} AU, czas tranzytu ≈ {P/np.pi*Rsun/a/3600:.1f} h, prawdopodobieństwo tranzytu ≈ {Rsun/a:.0%}")
for nazwa, P_, m_, M_ in [("Jowisz–Słońce", 11.86*365.25, MJ, Msun), ("Ziemia–Słońce", 365.25, 5.972e24, Msun),
                          ("51 Peg b", 4.23, 0.47*MJ, 1.11*Msun), ("Proxima b", 11.19, 1.07*5.972e24, 0.122*Msun)]:
    print(f"{nazwa:14s}: K = {(2*np.pi*G/(P_*dzien))**(1/3)*m_/M_**(2/3):7.2f} m/s")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.errorbar(t_rv/dzien % 3.5, rv, yerr=5, fmt="o"); ax1.set_xlabel("faza [dni]"); ax1.set_ylabel("v_r [m/s]")
ax2.plot(t/3600, F, ".", ms=2); ax2.set_xlabel("t [h]"); ax2.set_ylabel("strumień (wzgl.)")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Linia widmowa 656,280 nm w widmie gwiazdy zmienia się okresowo między 656,2799 a 656,2801 nm. Oblicz amplitudę prędkości radialnej gwiazdy.

<details>
<summary>Odpowiedź</summary>

$\Delta\lambda = 0{,}0001\ \mathrm{nm}$, $v = c\Delta\lambda/\lambda = 3\cdot10^8\cdot10^{-4}/656{,}28 \approx 46\ \mathrm{m/s}$.
</details>

2. Planeta wielkości Ziemi przechodzi przed czerwonym karłem o promieniu $0{,}12R_\odot$. Ile wynosi spadek jasności? Porównaj z tranzytem Ziemi przed Słońcem.

<details>
<summary>Odpowiedź</summary>

$(R_Z/0{,}12R_\odot)^2 \approx 0{,}6\%$ — 70 razy więcej niż przed Słońcem (0,008%). Dlatego planety skaliste łatwiej wykryć wokół małych gwiazd (np. TRAPPIST-1).
</details>

3. Planeta obiega gwiazdę o masie Słońca w ciągu 4 dni. Oblicz promień orbity.

<details>
<summary>Odpowiedź</summary>

$a = (GM_\odot P^2/4\pi^2)^{1/3} \approx 7{,}4\cdot10^9\ \mathrm m \approx 0{,}05\ \mathrm{AU}$.
</details>

### B. Poziom akademicki

1. Oblicz temperaturę równowagową Ziemi bez atmosfery dla albedo 0,3 i 0. Wyjaśnij różnicę względem średniej temperatury 288 K.

<details>
<summary>Odpowiedź</summary>

$T = 5772\sqrt{R_\odot/(2\cdot1\ \mathrm{AU})}(1 - A)^{1/4}$: dla $A = 0{,}3$ — 255 K, dla $A = 0$ — 278 K. Różnicę 33 K względem 288 K daje efekt cieplarniany atmosfery (CO₂, para wodna).
</details>

2. Wyprowadź wzór na temperaturę równowagową z bilansu mocy pochłanianej i wypromieniowywanej.

<details>
<summary>Odpowiedź</summary>

Pochłaniana: $(1 - A)\dfrac{4\pi R_*^2\sigma T_*^4}{4\pi a^2}\pi R_p^2$. Wypromieniowywana: $4\pi R_p^2\sigma T^4$. Po przyrównaniu $T^4 = (1 - A)T_*^4\dfrac{R_*^2}{4a^2}$, czyli $T = T_*\sqrt{R_*/(2a)}(1 - A)^{1/4}$.
</details>

3. Oblicz amplitudę $K$, jaką Proxima b ($m\sin i = 1{,}07M_Z$, $P = 11{,}19$ dnia) wywołuje u swojej gwiazdy ($0{,}122M_\odot$). Dlaczego ta planeta była możliwa do wykrycia, a analog Ziemi wokół Słońca jest poza zasięgiem obecnych spektrografów?

<details>
<summary>Odpowiedź</summary>

$K \approx 1{,}2\ \mathrm{m/s}$ — 14 razy więcej niż Ziemia wokół Słońca (0,09 m/s). Mała masa gwiazdy i krótki okres zwiększają $K$ ($K \propto P^{-1/3}M_*^{-2/3}$).
</details>

4. Uruchom kod i zmień szum spektrografu na 20 m/s. Jak zmienia się niepewność masy planety? Ile pomiarów trzeba, żeby wrócić do poprzedniej niepewności?

<details>
<summary>Odpowiedź</summary>

Niepewność $K$ (i masy) rośnie 4 razy, bo jest proporcjonalna do szumu. Maleje jak $1/\sqrt N$, więc potrzeba 16 razy więcej pomiarów (640 zamiast 40).
</details>

## Źródła

- Moduły 05.04 (środek masy), 07.04 (prawa Keplera), 10.07 i 19.04 (efekt Dopplera), 26.01 (moc promieniowania gwiazd).
- *Urania — Almanach astronomiczny*, „Tranzyty egzoplanet” — [tabele tranzytów widocznych z Polski](https://www.urania.edu.pl/pliki/almanach/2024/Bloki/Egzoplanety_opis.pdf) (po polsku).
- [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) — katalog znanych egzoplanet (materiał dodatkowy, po angielsku).
- OpenStax, *Astronomy 2e*, rozdz. 21.4 (planety poza Układem Słonecznym) — [openstax.org/details/books/astronomy-2e](https://openstax.org/details/books/astronomy-2e), materiał dodatkowy, po angielsku.
