# Fungování programu
V této části popíši procházení dat programem a popíši jejich úpravu. Hlavním souborem je soubor s názvem du4.py. V ostatních souborech jsou definovány třídy týkajících se jednotlivých objektů vstupních dat ve formátu GEOJSON, resp. JSON.

## du4.py
Jedná se o hlavní soubor, ve kterém jsou definovány vstupní povinné parametry pomocí knihovny 'argparse'. Povinným parametrem je název vstupního souboru, jméno výstupního souboru a maximální délka jednoho segmentu lomenné čáry. Program se sputí na základě následujícího příkazu:
`py du4.py -f dataExample.json -o vystup.json -l 30`

Do popisovaného souboru vstupují metody třídy sloužící pro čtení vstupního souboru a pro zápis do výstupního souboru. Metoda s názvem `process` provádí úpravu dat před samotným zápisem do nového souboru. Přepírá metodu `divide_long_segment` třídy `Polyline`, která zapíše nové segmenty do seznamu dvojic hodnot na základě uživatelem určené maximální délky. Tato metoda je později volána pro vstupní soubor.

## GeoJSON
Jedná se o třídu, pomocí metod `read` zpřístupní data programu z vstupního souboru. Metoda `write` je vytvořena pro zápis do nového souboru, ale také využívá metodu pro vytvoření nového atributu třídy `Polyline`. Tento nový atribut je následně zapsán do nového souboru. Volání metody je opět prováděno v souboru `du4.py`.

## Point
Jedná se o základní třídu, která inicializuje základní objekt formálu Linestring, kterým je Bod. Bod Určuje segment a vzdálenost mezi nimi jeho délku. Bod je určen parametry `x` a `y`.

## Segment
Třída segment určuje objekt, který je úsečkou mezi dvěma body. Tato třída obsahuje metody, které slouží pro určení vzdálenosti mezi 2 body. Vzdálenost je určena Pythagorovou větou. Dále je na základě výpočtu úhlopříčky čtyřúhelníku vypočten bod, dělící segment v jeho středu. Pro tento účel bylo vyhotoveno několik metod, které jsou použity v případě, že maximální délka segmentu je větší než uživatelem zadaná mezní hodnota. Tato čáse je definováno v metodě `divide`. V případě splnění této podmínky jsou zavolány metody třídy `Polyline`, která bude popsána později. Zjednodušeně se vytvoří vždy dva nové segmenty mezi jedním počátečním bodem a středním bodem. V případě že je segment stále delší než zadaná hodnota, znovu se segment rozdělí. Pomocí metody `segmentAdd` třídy definující lomenou linii se zapíše mezi ostatní segmenty. Metoda divide je dále volána ve třídě polyline na každý segment jednotlivých lomených linií.

## Polyline
Jedná se o třídu, která je použita ve spustitelném souboru `du4.py`. Jak již bylo řečeno, obsahuje metodu pro vytvoření nového atributu sloužící pro následný zápis do nového souboru. Stejně jako v případě třídy `Segment` je definována metoda pro vytvoření nové lomenné čáry na základě segmentů. Jedná se o metodu `divide_long_segments`, která využívá metodu divide pro rozdělení segmentu. V této části je volána metoda třídy `Polyline` s názvem `polylineAdd` v cyklu vrací jednotlivé vzniklé segmenty pomocí funkce `segmentAdd`.