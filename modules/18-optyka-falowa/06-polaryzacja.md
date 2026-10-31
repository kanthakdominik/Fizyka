# 18.06 — Polaryzacja światła: prawo Malusa i kąt Brewstera

> **Moduł:** [18 — Optyka falowa](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1: [§1.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-7-polaryzacja) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §33.4 (s. 17), §33.7 (s. 32)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§34.6, s. 16](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=31), [§34.9, s. 29](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=44) — PDF z serwera AGH

← [Dyfrakcja na szczelinie i zdolność rozdzielcza](05-dyfrakcja-i-rozdzielczosc.md) · [spis modułu](README.md) · [Dyfrakcja promieni X i prawo Bragga](07-dyfrakcja-rentgenowska.md) →

## Po co to jest

Światło jest falą poprzeczną (16.02), więc ma kierunek drgań: polaryzację. Oko jej nie widzi, ale wykorzystują ją okulary przeciwsłoneczne polaryzacyjne (gaszą odblaski od wody i szosy), ekrany LCD w telefonach i monitorach, kino 3D, fotografia (filtr polaryzacyjny), badanie naprężeń w plastikach i szkle (elastooptyka) oraz pszczoły nawigujące według polaryzacji nieba.

## Teoria w pigułce

**Polaryzacja liniowa**: wektor $\vec E$ drga w jednej płaszczyźnie. Światło słoneczne i z żarówki jest **niespolaryzowane**, czyli składa się z fal o chaotycznie zmieniających się kierunkach drgań.

**Polaryzator** (np. folia polaroidowa z równoległymi łańcuchami polimerów) przepuszcza składową $\vec E$ wzdłuż swojej osi i pochłania prostopadłą.
- Światło niespolaryzowane po przejściu przez polaryzator ma natężenie $I_0/2$ i jest spolaryzowane liniowo.
- **Prawo Malusa.** Światło spolaryzowane pada na polaryzator (analizator), którego oś tworzy kąt $\theta$ z kierunkiem polaryzacji. Przechodzi składowa $E_0\cos\theta$, więc

$$I = I_0\cos^2\theta.$$

Skrzyżowane polaryzatory ($90^\circ$) nie przepuszczają nic. Trzeci polaryzator wstawiony między nie pod kątem $45^\circ$ przywraca część światła: $I_0/8$ dla światła niespolaryzowanego na wejściu.

**Polaryzacja przez odbicie.** Światło odbite od szkła, wody czy asfaltu jest częściowo spolaryzowane poziomo. Przy kącie **Brewstera**, gdy promień odbity i załamany są prostopadłe, odbite jest spolaryzowane całkowicie:

$$\tan\theta_B = \frac{n_2}{n_1}.$$

Dla wody $\theta_B \approx 53^\circ$, dla szkła ok. $56^\circ$. Okulary polaryzacyjne mają oś pionową, więc gaszą poziomo spolaryzowane odblaski.

**Polaryzacja przez rozpraszanie.** Światło nieba rozproszone pod kątem $90^\circ$ od kierunku do Słońca jest silnie spolaryzowane (rozpraszanie Rayleigha, 17.03).

**Dwójłomność.** W niektórych kryształach (kalcyt) i naprężonych plastikach współczynnik załamania zależy od kierunku polaryzacji. Daje to podwójny obraz w kalcycie, a między skrzyżowanymi polaryzatorami barwne prążki ujawniające naprężenia (elastooptyka). Płytki falowe zamieniają polaryzację liniową na kołową. Na tym działa kino 3D z okularami polaryzacyjnymi.

**Ekran LCD.** Ciekły kryształ między skrzyżowanymi polaryzatorami obraca płaszczyznę polaryzacji o $90^\circ$ i piksel świeci. Napięcie prostuje cząsteczki, obrót znika i piksel gaśnie.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $I = I_0/2$ | światło niespolaryzowane przez polaryzator | polaryzator idealny |
| $I = I_0\cos^2\theta$ | prawo Malusa | światło spolaryzowane liniowo |
| $\tan\theta_B = n_2/n_1$ | kąt Brewstera | odbicie od dielektryka |
| $\theta_B + \theta_2 = 90^\circ$ | odbity ⊥ załamany | przy kącie Brewstera |

## Przykład rozwiązany

**Zadanie 1.** Światło niespolaryzowane o natężeniu $I_0$ przechodzi przez trzy polaryzatory o osiach pod kątami $0^\circ$, $45^\circ$ i $90^\circ$. Jakie natężenie wychodzi? A gdy usunąć środkowy?

$I = \dfrac{I_0}{2}\cos^245^\circ\cos^245^\circ = \dfrac{I_0}{8}$. Bez środkowego: $\dfrac{I_0}2\cos^290^\circ = 0$. Dodatkowy polaryzator zwiększa natężenie, bo „obraca” polaryzację po drodze.

**Zadanie 2.** Pod jakim kątem nad poziomem Słońce musi oświetlać jezioro, żeby odbicie było całkowicie spolaryzowane?

$\theta_B = \arctan1{,}33 \approx 53^\circ$ od normalnej, czyli Słońce ok. $37^\circ$ nad horyzontem.

### Wersja z rachunkiem różniczkowym i całkowym

**Natężenie światła niespolaryzowanego po polaryzatorze.** Kąt $\theta$ między kierunkiem drgań a osią polaryzatora jest losowy i rozłożony równomiernie, więc

$$I = I_0\frac{1}{2\pi}\int_0^{2\pi}\cos^2\theta\,d\theta = \frac{I_0}{2}.$$

**Wiele polaryzatorów.** $N$ polaryzatorów obróconych kolejno o $90^\circ/N$ przepuszcza spolaryzowane światło z natężeniem $I = I_0\cos^{2N}\left(\dfrac{\pi}{2N}\right)$. Dla $N \to \infty$: $\ln I/I_0 \approx -N\dfrac{\pi^2}{4N^2} \to 0$. Nieskończenie wiele polaryzatorów obraca polaryzację o $90^\circ$ bez strat. Tak działa ciekły kryształ w ekranie LCD, który stopniowo skręca polaryzację.

## Typowe pułapki

- **Polaryzator przepuszcza połowę światła spolaryzowanego.** Połowę przepuszcza tylko dla światła **niespolaryzowanego**. Dla spolaryzowanego obowiązuje $\cos^2\theta$.
- **Malus z $\cos\theta$.** Amplituda zmienia się jak $\cos\theta$, natężenie jak $\cos^2\theta$.
- **Kąt Brewstera od powierzchni.** Mierzy się go od normalnej.
- **Dźwięk można spolaryzować.** W powietrzu dźwięk jest falą podłużną i nie ma polaryzacji.

## Doświadczenie / symulacja

**Ekran telefonu i okulary polaryzacyjne.** Patrz na ekran LCD przez okulary polaryzacyjne i obracaj głowę lub telefon. Ekran ciemnieje przy $90^\circ$. (Ekrany OLED też mają polaryzator, a niektóre nowe nie.) Sprawdź prawo Malusa: zmierz natężenie luksomierzem drugiego telefonu dla kilku kątów i porównaj z $\cos^2\theta$.

**Naprężenia w plastiku.** Przezroczysty plastikowy kątomierz lub widelec między ekranem LCD a okularami polaryzacyjnymi pokazuje kolorowe prążki naprężeń. Zegnij go i obserwuj zmiany.

**Kąt Brewstera.** Patrz przez okulary polaryzacyjne na odbicie lampy od blatu lub szyby i zmieniaj kąt patrzenia. Przy kącie Brewstera odbicie znika.

**Python:** prawo Malusa i natężenie po $N$ polaryzatorach.

```python
import numpy as np
import matplotlib.pyplot as plt

th = np.linspace(0, np.pi, 200)
plt.plot(np.degrees(th), np.cos(th)**2)
print(f"trzy polaryzatory 0°/45°/90°: I/I0 = {0.5*np.cos(np.pi/4)**4:.3f}")
for N in (1, 2, 5, 10, 100):
    print(f"N = {N:3d} polaryzatorów co {90/N:.1f}°: I/I0_spolar = {np.cos(np.pi/(2*N))**(2*N):.3f}")
print(f"kąt Brewstera: woda {np.degrees(np.arctan(1.33)):.1f}°, szkło {np.degrees(np.arctan(1.5)):.1f}°")
plt.xlabel("kąt [°]"); plt.ylabel("I / I0"); plt.title("prawo Malusa"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Światło spolaryzowane pada na polaryzator, którego oś tworzy z kierunkiem polaryzacji kąt $30^\circ$. Jaka część natężenia przechodzi?

<details>
<summary>Odpowiedź</summary>

$\cos^230^\circ = 0{,}75$, czyli 75%.
</details>

2. Dlaczego okulary polaryzacyjne mają oś przepuszczania pionową?

<details>
<summary>Odpowiedź</summary>

Odblaski od poziomych powierzchni (woda, szosa, maska samochodu) są spolaryzowane poziomo i są wtedy wygaszane.
</details>

3. Oblicz kąt Brewstera dla szkła o $n = 1{,}5$ i sprawdź, że promień odbity i załamany są prostopadłe.

<details>
<summary>Odpowiedź</summary>

$\theta_B \approx 56{,}3^\circ$. Kąt załamania: $\sin\theta_2 = \sin56{,}3^\circ/1{,}5 \Rightarrow \theta_2 \approx 33{,}7^\circ$, a $56{,}3^\circ + 33{,}7^\circ = 90^\circ$.
</details>

### B. Poziom akademicki

1. Wyprowadź warunek Brewstera z prawa Snelliusa i warunku $\theta_B + \theta_2 = 90^\circ$.

<details>
<summary>Odpowiedź</summary>

$n_1\sin\theta_B = n_2\sin(90^\circ - \theta_B) = n_2\cos\theta_B \Rightarrow \tan\theta_B = n_2/n_1$.
</details>

2. Wiązka jest mieszaniną światła niespolaryzowanego o natężeniu $I_n$ i spolaryzowanego $I_p$. Po obrocie polaryzatora natężenie zmienia się od $I_{\min}$ do $I_{\max} = 3I_{\min}$. Oblicz stopień polaryzacji $I_p/(I_p + I_n)$.

<details>
<summary>Odpowiedź</summary>

$I_{\max} = I_n/2 + I_p$, $I_{\min} = I_n/2$. $3I_n/2 = I_n/2 + I_p \Rightarrow I_p = I_n$, stopień polaryzacji 50%.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2025, zad. 9.1 — fala elektromagnetyczna i polaryzacja (temat pomocniczy) ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2025, zad. 9.2 — natężenie światła po dwóch polaryzatorach ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1 — §1.7: polaryzacja.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §33.4, §33.7; wyd. 1: t. 4, §34.6, §34.9.
