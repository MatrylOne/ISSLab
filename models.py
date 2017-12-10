# Histereza
# GŁÓWNE METODY
def model(T, h, y0, u0, d):
    # Inicjacja tablic

    a = -0.5
    histereza = 0.05

    times = mh.createArray(0, T, h)

    ys = [y0]
    es = [d - y0]
    us = [u0]

    isRising = es[0] < 0

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
        ys.append(ys[i] + h * (a * ys[i] + us[i]))
        es.append(d - ys[i])

        # Jeśli ma rosnąć
        if isRising:
            # Włącz
            # Jeśli rośnie, próg zadziałania ma być powyżej zadanej wartości
            if es[i] + histereza > 0:
                us.append(1)
                isRising = True
            # Wyłącz
            # Jeśli rośnie próg wyłaczenia ma być poniżej zadanej wartości
            elif es[i] - histereza <= 0:
                us.append(0)
                isRising = False
            # Nie podejmuj akcji
            # Jeśli nie przekraczasz wartości progowych, przyjmij ostatnią wartość
            else:
                us.append(us[i])

        # Jeśli ma maleć
        else:
            # Włącz
            # Jeśli maleje, próg zadziałania ma być poniżej zadanej wartości
            if es[i] - histereza > 0:
                us.append(1)
                isRising = True
            # Wyłącz
            # Jeśli maleje próg wyłaczenia ma być powyżej zadanej wartości
            elif es[i] + histereza <= 0:
                us.append(0)
                isRising = False
            else:
                us.append(us[i])

    return (times, ys, es, us)

# Regulator P
def model(T, h, y0, u0, d, kp):
    # Inicjacja tablic
    times = mh.createArray(0, T, h)

    ys = [y0]
    es = [d - y0]
    us = [u0]

    a = -0.5

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
        ys.append(ys[i] + h * (a * ys[i] + us[i]))
        es.append(d - ys[i + 1])
        us.append(kp * es[i + 1])


    return (times, ys, es, us)

# Regulator I
def model(T, h, y0, u0, d, ki):
    # Inicjacja tablic
    times = mh.createArray(0, T, h)

    ys = [y0]
    es = [d - y0]
    us = [u0]
    calka = 0

    a = -0.5

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
        ys.append(ys[i] + h * (a * ys[i] + us[i]))
        es.append(d - ys[i + 1])
        calka += (es[i]) * h
        us.append(ki * calka)


    return (times, ys, es, us)

# Regulator PI
def model(T, h, y0, u0, d, ki):
    # Inicjacja tablic
    times = mh.createArray(0, T, h)

    kp = 3

    ys = [y0]
    es = [d - y0]
    us = [u0]
    calka = 0

    a = -0.5

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
        ys.append(ys[i] + h * (a * ys[i] + us[i]))
        es.append(d - ys[i + 1])
        calka += (es[i]) * h
        us.append(kp * es[i+1] + ki * calka)


    return (times, ys, es, us)

# Model PD
def model(T, h, y0, u0, d, kd):
    # Inicjacja tablic
    times = mh.createArray(0, T, h)

    kp = 3

    ys = [y0]
    es = [d - y0]
    us = [u0]

    a = -0.5

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
        ys.append(ys[i] + h * (a * ys[i] + us[i]))
        es.append(d - ys[i + 1])
        us.append(kp * es[i+1] + kd * ((es[i+1] - es[i])/h))


    return (times, ys, es, us)

# Model PID
def model(T, h, y0, u0, d, kd):
    # Inicjacja tablic
    times = mh.createArray(0, T, h)

    kp = 30
    ki = 5
    kd = 0.2

    ys = [y0]
    es = [d - y0]
    us = [u0]

    a = -0.5

    calka = 0

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
        ys.append(ys[i] + h * (a * ys[i] + us[i]))
        es.append(d - ys[i + 1])
        calka += (es[i]) * h
        us.append(kp * es[i+1] + kd * ((es[i+1] - es[i])/h) + ki * calka)

    return (times, ys, es, us)