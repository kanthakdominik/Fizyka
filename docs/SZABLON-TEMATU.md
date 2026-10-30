# Szablon tematu

Każdy plik tematu w `modules/NN-nazwa/` ma ten sam układ. Ten dokument opisuje, co powinno się znaleźć w każdej sekcji, żeby moduły były spójne niezależnie od tego, kiedy i przez kogo zostały napisane.

## Nagłówek

```markdown
# 02.05 — Rzut poziomy i ukośny

> **Moduł:** [02 — Kinematyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 4: [§4.3](link do paragrafu) · [wstęp do rozdziału](link)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, t. 1: §4.4 (s. 87)

← [poprzedni temat](...) · [spis modułu](README.md) · [następny temat](...) →
```

## Sekcje

| Sekcja | Zawartość | Wskazówki |
|---|---|---|
| **Po co to jest** | 2–4 zdania: gdzie temat wraca dalej (w fizyce i technice) | Konkretnie: „bez tego nie policzysz X w module Y” |
| **Teoria w pigułce** | Pojęcia i prawa, intuicja, rysunek (Mermaid lub opis) | Bez wyprowadzeń krok po kroku — te idą do przykładów |
| **Wzory i założenia** | Tabela: wzór, znaczenie symboli, jednostki, **kiedy obowiązuje** | Każdy wzór z warunkiem stosowalności |
| **Przykład rozwiązany** | 1–2 zadania rozwiązane w całości: dane, rysunek, model, rachunek, sprawdzenie jednostek i przypadków granicznych | Dla 🟢🔵 i 🔵 dodatkowo podsekcja **Wersja z rachunkiem różniczkowym i całkowym** |
| **Typowe pułapki** | 3–6 punktów | Najczęstsze błędy z matury i kolokwiów |
| **Doświadczenie / symulacja** | Jedno z trzech: pomiar phyphox, symulacja PhET z pytaniami, krótki program w Pythonie | Zawsze z opracowaniem: co mierzymy, jaki model, jak liczymy niepewność |
| **Zadania** | **A. Poziom maturalny** (3–6 zadań), **B. Poziom akademicki** (3–6 zadań z pochodną, całką lub równaniem różniczkowym) | Odpowiedzi pod `<details>`; zadania własne, nie kopiowane z arkuszy i podręczników |
| **Źródła** | Konkretne paragrafy i strony, symulacje, zadania maturalne CKE | Źródła polskie; anglojęzyczne tylko jako uzupełnienie, z oznaczeniem |

Dla tematów 🟢 część B jest opcjonalna, dla tematów 🔵 — część A.

## Format odpowiedzi do zadań

```markdown
1. Treść zadania…

<details>
<summary>Odpowiedź</summary>

$v = 12\text{,}5\ \mathrm{m/s}$ — krótkie uzasadnienie lub kluczowy krok.
</details>
```

## Konwencje zapisu

- Przecinek dziesiętny: `12\text{,}5`. Jednostki pismem prostym: `\mathrm{m/s}`, odstęp `\ ` między liczbą a jednostką.
- Wektory: `\vec{v}` lub `\mathbf{F}`; pochodna po czasie: `\dot{x}`, `\ddot{x}` albo `\frac{dx}{dt}`.
- W tabelach Markdown zamiast `|` w module liczby pisz `\lvert x \rvert`.
- Kod w Pythonie w blokach ` ```python ` — musi się uruchamiać samodzielnie (sprawdza go CI). Wykresy kończ `plt.show()`.
- Bloki wymagające SymPy lub plików z danymi są pomijane przez CI — oznacz to w komentarzu na początku bloku.

## Status tematu i modułu

- 🔲 szkielet — tylko nagłówki i mapowanie źródeł.
- 🟡 w trakcie — część sekcji wypełniona.
- ✅ pełny — wszystkie sekcje, zadania z odpowiedziami, działający kod.

Po wypełnieniu tematu zmień status w nagłówku pliku, w tabeli tematów w `README.md` modułu oraz — gdy cały moduł jest gotowy — w mapie modułów w głównym `README.md`.
