### tuple (demet) veri yapisi:

dersler_tuple=("fizik","kimya","matematik")
print(dersler_tuple)

## tuple=> immutable(sonradan degistirilemez)
mevsimler=("ilkbahar","yaz","sonbahar","kış")
print(mevsimler.count("ilkbahar"))
print(mevsimler.index("yaz"))
print(len(mevsimler))

## liste=> mutable
## str => immutable 

## SET (KÜME) VERİ YAPISI: verilerin sırası cıktı olarak farklı olabilir.
## unordered (sırasız)
## mutable (sonradan degistirilebilir)
##elemanlar unique(benzersiz) olarak tutulur          ## matematikte küme konusu mantıgı

dersler_set={"fizik","tarih","mat"}
print(dersler_set)

dersler_set.add("kimya")
print(dersler_set)

dersler_set.remove("fizik")
print(dersler_set)

## Kesişim(intersection)

muh_dersler_set={"algo","mat","fizik"}
blg_muh_dersler_set={"algo","mat"}

ortak_dersler_set=muh_dersler_set.intersection(blg_muh_dersler_set)
print(ortak_dersler_set)

## Fark(difference)

print(muh_dersler_set.difference(blg_muh_dersler_set))

## Birleşim(Union):

print(muh_dersler_set.union(blg_muh_dersler_set))