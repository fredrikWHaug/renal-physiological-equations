from plasma_creatinine import plasma_concentration

def main():
    A = -60
    time = 2880
    tau = 240
    p_inf = 80

    print(plasma_concentration(A, p_inf, time, tau))

if __name__ == '__main__':
    main()
