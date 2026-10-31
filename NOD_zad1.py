#nr studenta: 66193

import kagglehub
# 1. Załaduj bibliotekę pandas
import pandas as pd

sciezka = kagglehub.dataset_download("uciml/iris")
print(sciezka) 

# 4. Wczytanie danych z CSV
df = pd.read_csv(f"{sciezka}/Iris.csv")
df.head()

# 4. Zamiana danych z CSV na XLSX oraz wczytanie danych do ramki
df.to_excel("Iris.xlsx", index=False)
df_xlsx = pd.read_excel("Iris.xlsx")
print(df_xlsx.head())

# 5. Transponowanie ramki

# 6. Pierwsze 10 wierszy ramki

# 7. Ostatnie 10 wierszy ramki

# 8. Informacje o ramce danych

# 9. Ilość wierszy i kolumn w ramce

# 10. Statystyki kolumn liczbowych

# 11. Statystyki kolumn kategoryzowanych

# 12. Usunięcie brakujących wartości z ramki danych

# 13. Wybór wierszy i kolumn po nazwach oraz po indeksach, na różne sposoby

# 14. Wybierz wiersze pod warunkiem dotyczącym wartości jednej kolumny

# 15. Wybierz wiersze pod warunkiem spełnienia kilku warunków jednocześnie

# 16. Wybierz wiersze zawierające w kolumnie kategoryzowanej określone słowo

# 17. Wybierz wiersze niezawierające w kolumnie kategoryzowanej określonego słowa

# 18. Utwórz nową kolumnę na podstawie istniejących

# 19. Usuń kolumnę

# 20. Zmień nazwę kolumny

# 21. Zapisz ramkę danych jako plik CSV na dysku

# 22. Wyświetl średnią (oraz maksymalną i minimalną) wartość z wybranej kolumny

# 23. Wyświetl liczbę wierszy

# 24. Wyświetl wartości unikatowe w wybranej kolumnie

# 25. Wyświetl liczbę rekordów odpowiadających poszczególnym wartościom

# 26. Posortuj wiersze według wartości wybranej kolumny (rosnąco i malejąco)

# 27. Wyświetl wiersze dla 10 największych i 10 najmniejszych wartości wybranej kolumny

# 28. Wyświetl wiersze dla 10 największych wartości wybranej kolumny pod warunkiem określonych wartości innej kolumny

# 29. Pogrupuj wiersze według wartości kolumny kategoryzowanej i uśrednij wartości wszystkich kolumn w grupach (MultiIndex)

# 30. Pogrupuj wiersze według kolumny kategoryzowanej i policz: średnią dla wybranych kolumn oraz liczbę wartości i medianę dla pozostałych

# 31. Wyświetl nazwy kolumn indeksu złożonego

# 32. Posortuj po kolumnie indeksu złożonego

# 33. Utwórz tabelę przestawną (pivot table) na podstawie ramki danych

# 34. Wyświetl indeksy i kolumny tabeli przestawnej

# 35. Utwórz indeks złożony tabeli przestawnej i wyświetl go.

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