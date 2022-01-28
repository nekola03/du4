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
Třída segment určuje objekt, který je úsečkou mezi dvěma body.

## Polyline
Třída, která


