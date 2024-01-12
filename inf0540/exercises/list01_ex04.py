
def get_time_units(hours, minutes, seconds):
    return (hours, 
            minutes + 60 * hours,
            seconds + 60 * minutes + 60 * hours)


if __name__ == "__main__":
    time = input("Digite um horário (HH:MM:SS): ")

    ts = time.split(":")
    h, m, s = get_time_units(int(ts[0]), int(ts[1]), int(ts[2]))

    print(f"s = {s}s / minutos = {m}m / horas = {h}h")
