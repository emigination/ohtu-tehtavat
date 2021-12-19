from ksptehdas import KSPtehdas


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            peli = KSPtehdas.tehtaile('kaksinpeli')
        elif vastaus.endswith("b"):
            peli = KSPtehdas.tehtaile('yksinpeli')
        elif vastaus.endswith("c"):
            peli = KSPtehdas.tehtaile('haastava')
        else:
            break

        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkin muun kuin k, p tai s")
        peli.pelaa()


if __name__ == "__main__":
    main()
