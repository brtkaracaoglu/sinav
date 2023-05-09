class UzunlukHesapla:

    def __init__(self, text):
        if len(text) > 100:
            raise ValueError("Girdi dizesi en fazla 100 karakter olmalıdır.")

        invalid_chars = set(text) - set("0123456789abcdefghijklmnopqrstuvwxyz")
        if invalid_chars:
            raise ValueError("Girdi dizesi yalnızca küçük harfli İngilizce harfleri ve rakamları içermelidir.")

        self.text = text

    def __len__(self):
        # length uzunluğunu tutmak için kullanılır.
        length = 0
        i = 0
        while i < len(self.text):
            char = self.text[i]
            count = int(self.text[i + 1])
            length += count
            i += 2
        return length

    def count(self, char):
        # count karakterin kaç kez tekrarlandığını tutmak için kullanılır.
        count = 0
        i = 0
        while i < len(self.text):
            if self.text[i] == char:
                count += int(self.text[i + 1])
            i += 2
        return count

with open("giris_dosyası.txt","r",encoding="utf-8") as file:
    for i in file:
        value = i.strip()
        giris_dosyasi_listesi = []
        giris_dosyasi_listesi.append(value)

        for s in giris_dosyasi_listesi:
            length = len(UzunlukHesapla(s))
            a = UzunlukHesapla(s).count('a')
            b = UzunlukHesapla(s).count('b')
            c = UzunlukHesapla(s).count('c')
            z = UzunlukHesapla(s).count('z')
            print(f"Girdi: {s} -> Uzunluk: {length}, 'a' sayısı: {a}")
            print(f"Girdi: {s} -> Uzunluk: {length}, 'b' sayısı: {b}")
            print(f"Girdi: {s} -> Uzunluk: {length}, 'c' sayısı: {c}")
            print(f"Girdi: {s} -> Uzunluk: {length}, 'z' sayısı: {z}")




