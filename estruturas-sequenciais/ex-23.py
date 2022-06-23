def ritmoMedio(h, m, s, d):
    s += m*60 + h*3600
    minutes = str(int(s/60//d))
    seconds = str(int(s/60%d/d*60))
    print(f'{minutes.zfill(2)}:{seconds.zfill(2)} min/km')