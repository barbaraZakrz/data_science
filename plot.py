import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

seria = 1000
rzuty = [random.randrange(1,7) for i in range(seria)]
oczka, ile_razy = np.unique(rzuty, return_counts=True)
print(oczka, ile_razy)

seria_str = f'{seria:,}'.replace(',', ' ')

nazwa_wykresu = f'Częstotliwość wystąpień liczb oczek po wykonaniu {seria_str} rzutów'

sns.set_style('whitegrid')
osie = sns.barplot(x=oczka, y =ile_razy, palette = 'bright')
osie.set_title(nazwa_wykresu)
osie.set(xlabel='Liczba oczek', ylabel='Częstotliwość')
osie.set_ylim(top=max(ile_razy)*1.10)

for pasek, ile_razy_liczba_oczek in zip(osie.patches, ile_razy):
    tekst_x = pasek.get_x() + pasek.get_width() / 2.0
    tekst_y = pasek.get_height()
    ile_razy_liczba_oczek_str = f'{ile_razy_liczba_oczek:,}'.replace(',',' ')
    tekst = f'{ile_razy_liczba_oczek_str}\n{ile_razy_liczba_oczek/seria:.3%}'.replace('.',',')
    osie.text(tekst_x, tekst_y, tekst, fontsize = 11, ha ='center', va = 'bottom')
plt.show()