arrs = [
    "0D 02 0B 13 1B 09 0A 00 10 06 07 1A 05 12 04 19 11 0E 17 16 0F 1C 1D 18  08 15 01 03 1F 0C 1E 14",
    "A8 5F 43 DF 90 15 A2 F5 77 48 49 6C 67 20 0E CD B6 C8 4A E7 89 2F A1 A6 E8 B7 E1 C6 58 A9 D4 5A 4D 9E 34 05 53 C2 76 D3 C5 B3 BF C9 AF 98 25 68 D9 2D E6 65 D7 59 D6 0A 31 8F 99 AA 7C C0 35 B5 ED 4B EB D5 8E 6B 9D 37 2E 62 0F 07 9B 87 B8 BD DE 69 C7 CF 66 46 60 04 D0 A7 F8 70 7E FA 9A 03 08 C4 F6 8B 79 33 23 DD DA C1 13 CE 16 EE 93 63 12 6F 83 0D 71 64 4C 51 00 BA EF 95 6E 22 E5 94 30 FB 14 41 7A 1C 2A 56 B9 38 42 F0 44 F3 F2 9F 52 4E D8 CB 24 32 BE 0C A3 09 85 01 1D A5 28 45 F4 47 CC AE C3 AB A0 92 72 57 AC 3E E3 B4 74 1B 81 4F DC 2B 50 02 27 B2 6D F1 54 FE 80 5E 3B 36 E2 FF 11 EA FD 1A 97 86 26 73 B1 D2 3A 1E 5D 39 7F 1F A4 91 5C 55 EC E4 29 8C F7 7D 18 82 BC 2C 75 40 BB 17 8D F9 D1 E9 0B 7B 10 CA 6A FC 19 3C 8A B0 AD 21 96 5B 06 61 3D 3F 88 78 DB 84 9C E0",
    "42 33 21 68 00 00 00 00 00 00 00 00 00 00 00 00",
    "50 21 50 EB 86 B0 44 65 4F 3E 44 0D 41 EA A2 EB 13 E4 B2 0C 4F FD F6 9E C9 30 45 0D 54 30 D7 11",
]
arrs = [[int(x) for x in bytearray.fromhex(b)] for b in arrs]
src = [0] * 32

for i in range(32):
    src[i] = arrs[3][i] ^ arrs[2][i % 4]

arrs_1_reverse = {}
for i in range(256):
    arrs_1_reverse.update({arrs[1][i]: i})

src = [arrs_1_reverse[v] for v in src]

final = [0] * 32
for i in arrs[0]:
    final[arrs[0][i]] = src[i]

print("".join([chr(f) for f in final]))
