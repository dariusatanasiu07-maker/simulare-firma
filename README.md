# Simulare firmă

Program în Python care simulează un an de activitate al unei firme
și generează un raport anual.

## Ce face

- generează aleator numărul de clienți pentru fiecare lună
- calculează venitul și profitul lunar și anual
- numără lunile pe profit, pe pierdere și pe zero
- găsește luna cu cei mai mulți și cu cei mai puțini clienți

## Parametri

| Parametru | Ce reprezintă | Valoare implicită |
|---|---|---|
| `incasari_clienti` | cât plătește un client | 100 lei |
| `cheltuieli` | cheltuielile lunare | 8000 lei |
| `luni` | durata simulării | 12 |

## Exemplu de raport

```
===== RAPORT ANUAL AL FIRMEI =====
Clienti totali: 1260
Venit anual: 126000 lei
Profit anual: 30000 lei

Luni pe profit: 8
Luni pe pierdere: 3
Luni pe zero: 1

Cea mai buna luna: luna 11, cu 147 clienti
Cea mai slaba luna: luna 12, cu 60 clienti
```

## Ce am învățat

Funcții cu parametri impliciți, acumulatoare, găsirea maximului și minimului
fără `max()` și `min()`, f-strings.