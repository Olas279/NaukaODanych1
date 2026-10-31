#nr studenta: 66193

import kagglehub
# 1. Załaduj bibliotekę pandas
import pandas as pd

import numpy as np

sciezka = kagglehub.dataset_download("uciml/iris")
print(sciezka) 

# 4. Wczytanie danych z CSV
df = pd.read_csv(f"{sciezka}/Iris.csv")
df.head()

# 2. Ramka danych ze słownika
dane_slownik = {
    "SepalLengthCm": [5.1, 4.9, 4.7],
    "SepalWidthCm": [3.5, 3.0, 3.2],
    "Species": ["Iris-setosa", "Iris-setosa", "Iris-setosa"],
}
df_slownik = pd.DataFrame(dane_slownik)
print(df_slownik)

# 3. Ramka danych z listy list
dane_listy = [
    [5.1, 3.5, "Iris-setosa"],
    [4.9, 3.0, "Iris-setosa"],
    [4.7, 3.2, "Iris-setosa"],
]
df_listy = pd.DataFrame(dane_listy, columns=["SepalLengthCm", "SepalWidthCm", "Species"])
print(df_listy)


# 4. Zamiana danych z CSV na XLSX oraz wczytanie danych do ramki
df.to_excel("Iris.xlsx", index=False)
df_xlsx = pd.read_excel("Iris.xlsx")
print(df_xlsx.head())

# 5. Transponowanie ramki
print(df.head().T)

# 6. Pierwsze 10 wierszy ramki
print(df.head(10))

# 7. Ostatnie 10 wierszy ramki
print(df.tail(10))

# 8. Informacje o ramce danych
df.info()

# 9. Ilość wierszy i kolumn w ramce
print(df.shape)
print("Wiersze:", df.shape[0])
print("Kolumny:", df.shape[1])

# 10. Statystyki kolumn liczbowych
kolumny_num = df.select_dtypes(include="number").drop(columns="Id")
print(kolumny_num.describe())

# 11. Statystyki kolumn kategoryzowanych
kolumny_kat = df.select_dtypes(include="object")
print(kolumny_kat.describe())

# 12. Usunięcie brakujących wartości z ramki danych
print("Braki przed usunięciem:\n", df.isnull().sum())
df = df.dropna()
print("Braki po usunięciu:\n", df.isnull().sum()) # dowód że ramka nie ma brakujących wartości
print("Rozmiar ramki:", df.shape)

# 13. Wybór wierszy i kolumn po nazwach oraz po indeksach, na różne sposoby
print(df["Species"]) # jedna kolumna 
print(df[["SepalLengthCm", "Species"]]) # kilka kolumn 
print(df.iloc[0:5, [1, 5]]) # wybrane kolumny po pozycjach
print(df.iloc[0:5, 1:4]) # zakres kolumn po pozycjach
print(df.loc[2:7]) # wiersze 2-7
print(df.loc[1:5, "SepalLengthCm"]) # wiersze 1-5, jedna kolumna

# 14. Wybierz wiersze pod warunkiem dotyczącym wartości jednej kolumny
dlugie_dzialki_kielicha = df[df["SepalLengthCm"] > 6.0]
print(dlugie_dzialki_kielicha)

# 15. Wybierz wiersze pod warunkiem spełnienia kilku warunków jednocześnie
wybrane = df[(df["SepalLengthCm"] > 5.5) & (df["PetalWidthCm"] < 1.5)]
print(wybrane)

# 16. Wybierz wiersze zawierające w kolumnie kategoryzowanej określone słowo
zawiera = df[df["Species"].str.contains("setosa")]
print(zawiera)

# 17. Wybierz wiersze niezawierające w kolumnie kategoryzowanej określonego słowa
nie_zawiera = df[~df["Species"].str.contains("setosa")]
print(nie_zawiera)

# 18. Utwórz nową kolumnę na podstawie istniejących
df["SepalArea"] = df["SepalLengthCm"] * df["SepalWidthCm"]
print(df.head())

# 19. Usuń kolumnę
df = df.drop(columns="SepalArea")
print(df.columns)

# 20. Zmień nazwę kolumny
df = df.rename(columns={"Species": "Gatunek"})
print(df.columns)
#df = df.rename(columns={"Gatunek": "Species"}) # kod zmieniający z powrotem nazwę kolumny

# 21. Zapisz ramkę danych jako plik CSV na dysku
df.to_csv("Iris_wynik.csv", index=False)
print("Zapisano plik Iris_wynik.csv")

# 22. Wyświetl średnią (oraz maksymalną i minimalną) wartość z wybranej kolumny
print("Średnia:", df["SepalLengthCm"].mean())
print("Maksimum:", df["SepalLengthCm"].max())
print("Minimum:", df["SepalLengthCm"].min())

# 23. Wyświetl liczbę wierszy
print("Liczba wierszy:", len(df)) # możliwe jest także wykorzystanie funkcji shape: df.shape[0]

# 24. Wyświetl wartości unikatowe w wybranej kolumnie
print(df["Gatunek"].unique())
print("Ile unikatowych:", df["Gatunek"].nunique())

# 25. Wyświetl liczbę rekordów odpowiadających poszczególnym wartościom
print(df["Gatunek"].value_counts())

# 26. Posortuj wiersze według wartości wybranej kolumny (rosnąco i malejąco)
print(df.sort_values("SepalLengthCm", ascending=True)) # rosnąco
print(df.sort_values("SepalLengthCm", ascending=False)) # malejąco

# 27. Wyświetl wiersze dla 10 największych i 10 najmniejszych wartości wybranej kolumny
print(df.nlargest(10, "SepalLengthCm"))
print(df.nsmallest(10, "SepalLengthCm"))

# 28. Wyświetl wiersze dla 10 największych wartości wybranej kolumny pod warunkiem określonych wartości innej kolumny
virginica = df[df["Gatunek"] == "Iris-virginica"] # wybrano gatunek iris- virginica
print(virginica.nlargest(10, "SepalLengthCm"))

# sztuczna kolumna kategoryzowana: płatek długi/krótki względem mediany
mediana = df["PetalLengthCm"].median()
df["RozmiarPlatka"] = np.where(df["PetalLengthCm"] > mediana, "dlugi", "krotki")

kolumny_liczbowe = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
# df = df.drop(columns="RozmiarPlatka") - kod usunięcia sztucznej kolumny

# 29. Pogrupuj wiersze według wartości kolumny kategoryzowanej i uśrednij wartości wszystkich kolumn w grupach (MultiIndex)
grupy = df.groupby(["Gatunek", "RozmiarPlatka"])[kolumny_liczbowe].mean()
print(grupy)
print(grupy.index) # wykorzystanie MultiIndex

# 30. Pogrupuj wiersze według kolumny kategoryzowanej i policz: średnią dla wybranych kolumn oraz liczbę wartości i medianę dla pozostałych
wynik30 = df.groupby("Gatunek").agg({
    "SepalLengthCm": ["mean"],
    "SepalWidthCm": ["mean"],
    "PetalLengthCm": ["count", "median"],
    "PetalWidthCm": ["count", "median"],
})
print(wynik30)

# 31. Wyświetl nazwy kolumn indeksu złożonego
print(grupy.index.names) # wyświetla kolumny ['Gatunek', 'RozmiarPlatka']

# 32. Posortuj po kolumnie indeksu złożonego
print(grupy.sort_index(level="RozmiarPlatka"))
print(grupy.sort_index(level="Gatunek", ascending=False))

# 33. Utwórz tabelę przestawną (pivot table) na podstawie ramki danych
pivot = df.pivot_table(
    values=["SepalLengthCm", "PetalLengthCm"],
    index="Gatunek",
    columns="RozmiarPlatka",
    aggfunc="mean",
)
print(pivot)

# 34. Wyświetl indeksy i kolumny tabeli przestawnej
print(pivot.index)
print(pivot.columns)

# 35. Utwórz indeks złożony tabeli przestawnej i wyświetl go.
pivot35 = df.pivot_table(
    values=["SepalLengthCm", "PetalLengthCm"],
    index=["Gatunek", "RozmiarPlatka"],
    aggfunc="mean",
)
print(pivot35)
print(pivot35.index)
print(pivot35.index.names)

# 36. Zaimportuj moduł pyplot z biblioteki matplotlib

# 37. Ustaw rysowanie wykresów bezpośrednio w zeszycie, a nie w osobnym oknie

# 38. Wyświetl wykres na podstawie tabeli przestawnej

# 39. Narysuj histogram na podstawie wartości wybranej kolumny

# 40. Przedstaw łączenie ramek danych metodami merge i concat

# 41. Dodaj nowe kolumny za pomocą operacji matematycznych

# 42. Dodaj nowe kolumny z użyciem funkcji lambda

# 43. Pokaż pracę z dużym plikiem przy użyciu argumentu chunksize

# 44. Średnia arytmetyczna. Policz średnią wybranej kolumny liczbowej (df["kol"].mean() lub np.mean). Zinterpretuj, jaki to typowy poziom wartości

# 45. Mediana. Policz medianę tej samej kolumny (df["kol"].median() lub np.median). Porównaj ze średnią i wyjaśnij różnicę w kontekście wartości odstających

# 46. Odchylenie standardowe. Policz odchylenie standardowe (df["kol"].std() lub np.std). Zinterpretuj jako miarę rozproszenia danych

# 47. Wariancja. Policz wariancję (df["kol"].var() lub np.var) i pokaż, że jest kwadratem odchylenia standardowego

# 48. Korelacja. Policz korelację Pearsona między dwiema kolumnami liczbowymi (df["a"].corr(df["b"]) lub np.corrcoef). Zinterpretuj znak i siłę zależności

# 49. Kowariancja. Policz kowariancję tych samych dwóch kolumn (df["a"].cov(df["b"]) lub np.cov). Wyjaśnij, czym różni się od korelacji

# 50. Zadanie podsumowujące