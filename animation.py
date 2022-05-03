
from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys

def nowa_ramka(nr_ramki, rzuty_w_ramce, liczby_oczek, statystyka_oczek):

    for i in range(rzuty_w_ramce):
        statystyka_oczek[random.randrange(1, 7) - 1] += 1

    plt.cla()
    seria_str = sum(statystyka_oczek)
    nazwa_wykresu = 'Częstotliwość wystąpień po wykonaniu' f' {seria_str} rzutów'

    osie = sns.barplot(liczby_oczek, statystyka_oczek, palette='bright')
    osie.set_title(nazwa_wykresu)
    osie.set(xlabel='Liczba oczek', ylabel='Częstotliwość')
    osie.set_ylim(top=max(statystyka_oczek) * 1.10)


    for pasek, ile_razy_liczba_oczek in zip(osie.patches, statystyka_oczek):
        text_x = pasek.get_x() + pasek.get_width() / 2.0
        text_y = pasek.get_height()
        text = f'{ile_razy_liczba_oczek:,}\n{ile_razy_liczba_oczek / sum(statystyka_oczek):.3%}'
        osie.text(text_x, text_y, text, ha='center', va='bottom')


liczba_ramek = int(sys.argv[1])
rzuty_w_jednej_ramce = int(sys.argv[2])

sns.set_style('whitegrid')
obiekt_okna = plt.figure('Symulacja serii rzutów sześcienną kostką')
etykiety = list(range(1, 7))
licznik_oczek = [0] * 6


animacja = animation.FuncAnimation(
    obiekt_okna, nowa_ramka, repeat=False, frames=liczba_ramek, interval=33,
    fargs=(rzuty_w_jednej_ramce, etykiety, licznik_oczek))

plt.show()