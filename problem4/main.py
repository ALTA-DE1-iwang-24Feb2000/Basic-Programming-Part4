def ubah_huruf(sentence):
    pattern = ""
    n = 10
    for i in range (len(sentence)):
        ch = sentence [i] 
        if (ch.isupper()):
            pattern += chr((ord(ch)+n-65)%26+65)
        elif ch ==" ":
            pattern += " "
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB