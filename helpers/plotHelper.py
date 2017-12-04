def extrema(xs, times):
    # Inicjacja tablic
    extremas = []
    eTimes = []
    # Sprawdzenie czy ilość danych jest wystarczajca
    if(len(xs) > 2):
        # Zapamiętanie obecnej monotoniczności funkcji
        rising = xs[1] > xs[0]
        for i in range(0, len(xs) - 2):
            # Jeśli funkcja zmienia monotoniczność = ekstremum lokalne
            if((xs[i+1] > xs[i]) != rising):
                # Dodaję punkt do tablicy
                extremas.append(xs[i+1])
                eTimes.append(times[i+1])
                # Zapamiętanie obecnego stanu funkcji
                rising = xs[i+1] > xs[i]
    return (extremas, eTimes)

