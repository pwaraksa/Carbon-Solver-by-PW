import numpy as np
import pandas as pd
from datetime import date


print("""
                 _                             _                  _
                | |                           | |                | |                          
   ___ __ _ _ __| |__   ___  _ __    ___  ___ | |_   _____ _ __  | |__  _   _   _ ____      __
  / __/ _` | '__| '_ \ / _ \| '_ \  / __|/ _ \| \ \ / / _ \ '__| | '_ \| | | | | '_ \ \ /\ / /
 | (_| (_| | |  | |_) | (_) | | | | \__ \ (_) | |\ V /  __/ |    | |_) | |_| | | |_) \ V  V / 
  \___\__,_|_|  |_.__/ \___/|_| |_| |___/\___/|_| \_/ \___|_|    |_.__/ \__, | | .__/ \_/\_/  
                                                                         __/ | | |            
      """)
print("")
print("Aplikacja do modelowania zasobow wegla 1.3. Autor: pwaraksa@gmail.com")
print("")

#########licencja###################
today = date.today()
# dd/mm/YY
date = today.strftime("%d/%m/%Y")
day = today.strftime("%d")
month = today.strftime("%m")

day = int(day)
month = int(month)
# print(intday)

# if month == 8:
#     lic = "betatester"
# elif month == 9:
#     if day < 15:
#         lic = "emiliawysockafijorek"
#     else:
#         lic = "wer334fq4tqe4654756"
# elif month == 10:
#     if day < 15:
#         lic = "sdfsdv76v53xc5v7x6v"
#     else:
#         lic = "vplxcokv84021dkcz0c"
# elif month == 11:
#         lic = "cxdc98237r78cc9xca0"
# elif month == 12:
#         lic = "skfjmkcssd87fsdd88d"
# elif month == 1:
#         lic = "q32dksm9csiodlk3kksk"
# elif month == 2:
#         lic = "93498kasa932ec22c32c"
# else: lic = "adminadmin"

# verify_licence = ""
# while verify_licence != lic:
#     verify_licence = input("wprowadż kod licencji: ")
#     if verify_licence == lic:
#         print("prawidlowy kod licencji")
#     else:
#         print("bledny kod licencji")


# licencje:
# betatester
# emiliawysockafijorek
# wer334fq4tqe4654756
# sdfsdv76v53xc5v7x6v
# vplxcokv84021dkcz0c
# cxdc98237r78cc9xca0
# skfjmkcssd87fsdd88d
# q32dksm9csiodlk3kksk
# 93498kasa932ec22c32c


print("####################################################################################")
print("")
print("O programie:")
print("Program generuje ilosc wegla za pomoca wbudowanego algorytmu na podstawie powierzchni i miazszosci dla dowolnej zdefiniowanej jednostki administarcyjnej np. obrebu. ")
print("Bieżąca wersja programu wykonuje oblicznia dla danych z lat 2019 oraz 2020")
print("Program uwzglednia gestosc gatunkow, Biomass Conversion and Expansion Factor (BCEF), Carbon Factor, Root to shot ratio")
print("")
print("Wynikiem obliczeń są:")
print("[carbonYYYY] Zasoby węgla [tony] w żywej biomasie")
print("[carbon_aboveYYYY] Zasoby węgla [tony] w żywej biomasie nadziemnej")
print("[carbon_belowYYYY] Zasoby węgla [tony] w żywej biomasie podziemnej")
print("[biomassYYYY] Zasoby biomasy [m3] w żywej biomasie")
print("[biomass_aboveYYYY] Zasoby biomasy [m3] w żywej biomasie nadziemnej")
print("[biomass_belowYYYY] Zasoby biomasy [m3] w żywej biomasie podziemnej")
print("Wszystkie powyższe wartosci przeliczone sa na hektar np. [carbonYYYY_ha]")
print("")
print("Instrukcja:")
print("Do poprawnego dzialania programu potrzebny jest plik wsadowy z rozszerzeniem .xlsx zawierajacy arkusz o nazwie 'dane_do_obliczen' o nastepujacej strukturze: ")
print(" ")
print("kolumny o nazwach i wartosciach")
print("obreb	    gat_pan     kl_wiek	    pow2019	    vol2019	    pow2020	    vol2020")
print("np.01-01-3	np. BRZ     np. Ib	    np. 1.65	np.354.45	np. 2.98	np. 370.83")
print(" ")


print("####################################################################################")
print(" ")
input_filename = input(r"Podaj sciezke pliku wsadowego. (Np. C:\folder\plik_wsadowy.xlsx ): ")
print("")
# print(input_filename)
output_filename = input(r"Podaj sciezke i nazwe(!) pliku wynikowego ale bez rozszerzenia. (Np. C:\folder\nazwa_pliku ): ")

print(" ")
print(" ")
print("obliczanie...")

# input_filename = r"C:\Users\cicindela\Desktop\aplikacja_carbon_analizy_ekosystemowe\Kopia Potencjalne szacunki zasobów węgla.xlsx"
# output_filename = r"C:\Users\cicindela\Desktop\aplikacja_carbon_analizy_ekosystemowe\wynik"

df = pd.read_excel(io=input_filename, sheet_name="dane_do_obliczen", engine='openpyxl')

repl_dict1 = {"Ia": "I", "Ib": "I", "IIa": "II", "IIb": "II", "IIIa": "III", "IIIb": "III"}
repl_dict2 = {"IVa": "IV", "IVb": "IV", "Va": "V", "Vb": "V", "VIa": "VI", "VIb": "VI"}
df["kl_wiek"].replace(repl_dict1, inplace=True)
df["kl_wiek"].replace(repl_dict2, inplace=True)


# BCEFS classification
def BCEF_classify(x, v):
    if x == "SO":
        if v < 20:
            p = 1.8
        elif v < 50:
            p = 1
        elif v < 100:
            p = 0.75
        else:
            p = 0.7

    elif x == "ŚW" or x == "JD":
        if v < 20:
            p = 3
        elif v < 50:
            p = 1.4
        elif v < 100:
            p = 1
        else:
            p = 0.75
    else:
        if v < 20:
            p = 3
        elif v < 50:
            p = 1.7
        elif v < 100:
            p = 1.4
        else:
            p = 1.05
    return p


# Density classification by species
def TreeDensity(species):
    if species == "SO":
        d = 0.42924
    elif species == "ŚW":
        d = 0.37840
    elif species == "JD":
        d = 0.36203
    elif species == "BK":
        d = 0.56856
    elif species == "DB":
        d = 0.56810
    elif species == "GB":
        d = 0.63437
    elif species == "BRZ":
        d = 0.52338
    elif species == "OL":
        d = 0.42826
    elif species == "TP":
        d = 0.35137
    elif species == "OS":
        d = 0.35600
    else:
        d = 0.5
    return d


# Root_to_shoot_ratio
def Root_to_shoot_ratio(species, value):
    if species == "SO" or species == "ŚW" or species == "JD":
        if value < 50:
            r = 0.40
        elif value < 100:
            r = 0.29
        else:
            r = 0.2

    elif species == "DB":
        if value < 50:
            r = 0.46
        elif value < 100:
            r = 0.3
        else:
            r = 0.3
    # pozostale gatunki
    else:
        if value < 50:
            r = 0.46
        elif value < 100:
            r = 0.23
        else:
            r = 0.24
    return r


# CF Carbon Factor
def CarbonFactor(species):
    if species == "SO":
        cf = 0.51
    elif species == "ŚW":
        cf = 0.51
    elif species == "JD":
        cf = 0.51
    elif species == "BK":
        cf = 0.48
    elif species == "DB":
        cf = 0.48
    elif species == "GB":
        cf = 0.48
    elif species == "BRZ":
        cf = 0.48
    elif species == "OL":
        cf = 0.48
    elif species == "TP":
        cf = 0.48
    elif species == "OS":
        cf = 0.48
    else:
        cf = 0.5
    return cf


##################### 2019 #######################

# dodanie do df: Średnia miąższość  wg klas wieku i gatunów panujących
df.loc[:, 'vol/pow2019'] = df['vol2019'] / df['pow2019']
# zmiana NaN na 0
df.loc[df['vol/pow2019'].notna() == False, 'vol/pow2019'] = 0

# dodanie do df: Miąższość biomasy nadziemnej   wg klas wieku i gatunów panujących
gat_pan_array = df["gat_pan"].values
vol2019_array = df["vol2019"].values
vol_pow2019_array = df["vol/pow2019"].values
# type(X)
ls_gat = []
ls_vol2019 = []
ls_vol_pow2019 = []

for i in gat_pan_array:
    ls_gat.append(i)

for i in vol2019_array:
    ls_vol2019.append(i)

for i in vol_pow2019_array:
    ls_vol_pow2019.append(i)

bcef2019_ls = []
for i in range(len(ls_gat)):
    bcef_classified = BCEF_classify(ls_gat[i], ls_vol_pow2019[i])
    #     print(bcef_classified)
    #     print(ls_vol2019[i])

    bcef2019_ls.append(bcef_classified * ls_vol2019[i])

bcef2019_arr = np.array(bcef2019_ls)
df.loc[:, 'biomass_above2019'] = bcef2019_arr

# dodanie do df: Miąższość suchej  biomasy   wg klas wieku i gatunów panujących

gat_pan_array = df["gat_pan"].values
ls_gat = []
for i in gat_pan_array:
    ls_gat.append(i)

bcef2019_array = df['biomass_above2019'].values
ls_bcef = []
for i in bcef2019_array:
    ls_bcef.append(i)

density_bcef2019_ls = []
for i in range(len(ls_gat)):
    tree_density = TreeDensity(ls_gat[i])
    density_bcef2019 = tree_density * ls_bcef[i]
    density_bcef2019_ls.append(density_bcef2019)

len(density_bcef2019_ls)
density_bcef2019_arr = np.array(density_bcef2019_ls)

df.loc[:, 'dry_biomass_above2019'] = density_bcef2019_arr

# dodanie do df: Średnia miąższość suchej  biomasy   wg klas wieku i gatunów panujących

df.loc[:, 'mean_dry_biomass_above2019'] = df['dry_biomass_above2019'] / df['pow2019']
# zmiana NaN na 0
df.loc[df['mean_dry_biomass_above2019'].notna() == False, 'mean_dry_biomass_above2019'] = 0

# dodanie do df: Miąższość biomasy wg klas wieku i gatunów panujących
gat_pan_array = df["gat_pan"].values
ls_gat = []
for i in gat_pan_array:
    ls_gat.append(i)

mean_dens_bcef2019_array = df['mean_dry_biomass_above2019'].values
ls_m_d_bcef2019 = []
for i in mean_dens_bcef2019_array:
    ls_m_d_bcef2019.append(i)

bcef2019_arr = df['biomass_above2019'].values
bcef2019_ls = []
for i in bcef2019_arr:
    bcef2019_ls.append(i)

Biomass_ls = []
for i in range(len(ls_m_d_bcef2019)):
    Root2Shoot_r = Root_to_shoot_ratio(ls_gat[i], ls_m_d_bcef2019[i])

    Biomass = (Root2Shoot_r + 1) * bcef2019_ls[i]
    Biomass_ls.append(Biomass)

Biomass_arr = np.array(Biomass_ls)

df.loc[:, 'biomass2019'] = Biomass_arr

# dodanie do df: Miąższość zasobów węgla wg klas wieku i gatunów panujących

biomass2019_array = df["biomass2019"].values
ls_biomass = []
for i in biomass2019_array:
    ls_biomass.append(i)

gat_pan_array = df["gat_pan"].values
ls_gat = []
for i in gat_pan_array:
    ls_gat.append(i)

carbon_ls = []
for i in range(len(ls_gat)):
    carbon_f = CarbonFactor(ls_gat[i])
    carbon_biomass = carbon_f * ls_biomass[i]
    carbon_ls.append(carbon_biomass)
    # print(carbon_biomass)

carbon_arr = np.array(carbon_ls)

df.loc[:, 'carbon2019'] = carbon_arr

# dodanie do df: Miąższość zasobów węgla w biomasie nadziemnej wg klas wieku i gatunów panujących

bcef2019_array = df['biomass_above2019'].values
ls_bcef2019 = []
for i in bcef2019_array:
    ls_bcef2019.append(i)

gat_pan_array = df["gat_pan"].values
ls_gat = []
for i in gat_pan_array:
    ls_gat.append(i)

carbon_ls = []
for i in range(len(ls_gat)):
    carbon_f = CarbonFactor(ls_gat[i])
    carbon_above_biomass = carbon_f * ls_bcef2019[i]
    carbon_ls.append(carbon_above_biomass)
    # print(carbon_biomass)

carbon_arr = np.array(carbon_ls)

df.loc[:, 'carbon_above2019'] = carbon_arr

# dodanie do df: Miąższość zasobów węgla w biomasie podziemnej wg klas wieku i gatunów panujących

df.loc[:, 'carbon_below2019'] = df['carbon2019'] - df['carbon_above2019']

# dodanie do df: Miąższość w biomasie podziemnej wg klas wieku i gatunów panujących

df.loc[:, 'biomass_below2019'] = df['biomass2019'] - df['biomass_above2019']

# pd.set_option('display.float_format', '{:.5f}'.format)


# Grupowanie suma obreb
# df_sum_by_obreb = df.groupby(['obreb']).sum()


##################### 2020 #######################


# dodanie do df: Średnia miąższość  wg klas wieku i gatunów panujących
df.loc[:, 'vol/pow2020'] = df['vol2020'] / df['pow2020']
# zmiana NaN na 0
df.loc[df['vol/pow2020'].notna() == False, 'vol/pow2020'] = 0

# dodanie do df: Miąższość biomasy nadziemnej   wg klas wieku i gatunów panujących
gat_pan_array = df["gat_pan"].values
vol2020_array = df["vol2020"].values
vol_pow2020_array = df["vol/pow2020"].values
# type(X)
ls_gat = []
ls_vol2020 = []
ls_vol_pow2020 = []

for i in gat_pan_array:
    ls_gat.append(i)

for i in vol2020_array:
    ls_vol2020.append(i)

for i in vol_pow2020_array:
    ls_vol_pow2020.append(i)

bcef2020_ls = []
for i in range(len(ls_gat)):
    bcef_classified = BCEF_classify(ls_gat[i], ls_vol_pow2020[i])
    #     print(bcef_classified)
    #     print(ls_vol2020[i])

    bcef2020_ls.append(bcef_classified * ls_vol2020[i])

bcef2020_arr = np.array(bcef2020_ls)
df.loc[:, 'biomass_above2020'] = bcef2020_arr

# dodanie do df: Miąższość suchej  biomasy   wg klas wieku i gatunów panujących

gat_pan_array = df["gat_pan"].values
ls_gat = []
for i in gat_pan_array:
    ls_gat.append(i)

bcef2020_array = df['biomass_above2020'].values
ls_bcef = []
for i in bcef2020_array:
    ls_bcef.append(i)

density_bcef2020_ls = []
for i in range(len(ls_gat)):
    tree_density = TreeDensity(ls_gat[i])
    density_bcef2020 = tree_density * ls_bcef[i]
    density_bcef2020_ls.append(density_bcef2020)

len(density_bcef2020_ls)
density_bcef2020_arr = np.array(density_bcef2020_ls)

df.loc[:, 'dry_biomass_above2020'] = density_bcef2020_arr

# dodanie do df: Średnia miąższość suchej  biomasy   wg klas wieku i gatunów panujących

df.loc[:, 'mean_dry_biomass_above2020'] = df['dry_biomass_above2020'] / df['pow2020']
# zmiana NaN na 0
df.loc[df['mean_dry_biomass_above2020'].notna() == False, 'mean_dry_biomass_above2020'] = 0

# dodanie do df: Miąższość biomasy wg klas wieku i gatunów panujących
gat_pan_array = df["gat_pan"].values
ls_gat = []
for i in gat_pan_array:
    ls_gat.append(i)

mean_dens_bcef2020_array = df['mean_dry_biomass_above2020'].values
ls_m_d_bcef2020 = []
for i in mean_dens_bcef2020_array:
    ls_m_d_bcef2020.append(i)

bcef2020_arr = df['biomass_above2020'].values
bcef2020_ls = []
for i in bcef2020_arr:
    bcef2020_ls.append(i)

Biomass_ls = []
for i in range(len(ls_m_d_bcef2020)):
    Root2Shoot_r = Root_to_shoot_ratio(ls_gat[i], ls_m_d_bcef2020[i])

    Biomass = (Root2Shoot_r + 1) * bcef2020_ls[i]
    Biomass_ls.append(Biomass)

Biomass_arr = np.array(Biomass_ls)

df.loc[:, 'biomass2020'] = Biomass_arr

# dodanie do df: Miąższość zasobów węgla wg klas wieku i gatunów panujących

biomass2020_array = df["biomass2020"].values
ls_biomass = []
for i in biomass2020_array:
    ls_biomass.append(i)

gat_pan_array = df["gat_pan"].values
ls_gat = []
for i in gat_pan_array:
    ls_gat.append(i)

carbon_ls = []
for i in range(len(ls_gat)):
    carbon_f = CarbonFactor(ls_gat[i])
    carbon_biomass = carbon_f * ls_biomass[i]
    carbon_ls.append(carbon_biomass)
    # print(carbon_biomass)

carbon_arr = np.array(carbon_ls)

df.loc[:, 'carbon2020'] = carbon_arr

# dodanie do df: Miąższość zasobów węgla w biomasie nadziemnej wg klas wieku i gatunów panujących

bcef2020_array = df['biomass_above2020'].values
ls_bcef2020 = []
for i in bcef2020_array:
    ls_bcef2020.append(i)

gat_pan_array = df["gat_pan"].values
ls_gat = []
for i in gat_pan_array:
    ls_gat.append(i)

carbon_ls = []
for i in range(len(ls_gat)):
    carbon_f = CarbonFactor(ls_gat[i])
    carbon_above_biomass = carbon_f * ls_bcef2020[i]
    carbon_ls.append(carbon_above_biomass)
    # print(carbon_biomass)

carbon_arr = np.array(carbon_ls)

df.loc[:, 'carbon_above2020'] = carbon_arr

# dodanie do df: Miąższość zasobów węgla w biomasie podziemnej wg klas wieku i gatunów panujących

df.loc[:, 'carbon_below2020'] = df['carbon2020'] - df['carbon_above2020']

# dodanie do df: Miąższość w biomasie podziemnej wg klas wieku i gatunów panujących

df.loc[:, 'biomass_below2020'] = df['biomass2020'] - df['biomass_above2020']

# pd.set_option('display.float_format', '{:.5f}'.format)


# #Grupowanie suma obreb
df_sum_by_obreb = df.groupby(['obreb']).sum()

# przeliczenie wartosci obrebow na hektar:

df_sum_by_obreb.loc[:, 'carbon2019_ha'] = df_sum_by_obreb['carbon2019'] / df_sum_by_obreb['pow2019']
df_sum_by_obreb.loc[:, 'carbon_above2019_ha'] = df_sum_by_obreb['carbon_above2019'] / df_sum_by_obreb['pow2019']
df_sum_by_obreb.loc[:, 'carbon_below2019_ha'] = df_sum_by_obreb['carbon_below2019'] / df_sum_by_obreb['pow2019']
df_sum_by_obreb.loc[:, 'biomass2019_ha'] = df_sum_by_obreb['biomass2019'] / df_sum_by_obreb['pow2019']
df_sum_by_obreb.loc[:, 'biomass_above2019_ha'] = df_sum_by_obreb['biomass_above2019'] / df_sum_by_obreb['pow2019']
df_sum_by_obreb.loc[:, 'biomass_below2019_ha'] = df_sum_by_obreb['biomass_below2019'] / df_sum_by_obreb['pow2019']

# przeliczenie wartosci obrebow na hektar:

df_sum_by_obreb.loc[:, 'carbon2020_ha'] = df_sum_by_obreb['carbon2020'] / df_sum_by_obreb['pow2020']
df_sum_by_obreb.loc[:, 'carbon_above2020_ha'] = df_sum_by_obreb['carbon_above2020'] / df_sum_by_obreb['pow2020']
df_sum_by_obreb.loc[:, 'carbon_below2020_ha'] = df_sum_by_obreb['carbon_below2020'] / df_sum_by_obreb['pow2020']
df_sum_by_obreb.loc[:, 'biomass2020_ha'] = df_sum_by_obreb['biomass2020'] / df_sum_by_obreb['pow2020']
df_sum_by_obreb.loc[:, 'biomass_above2020_ha'] = df_sum_by_obreb['biomass_above2020'] / df_sum_by_obreb['pow2020']
df_sum_by_obreb.loc[:, 'biomass_below2020_ha'] = df_sum_by_obreb['biomass_below2020'] / df_sum_by_obreb['pow2020']

##################################################
df_selected = df_sum_by_obreb[
    ["carbon2019", "carbon_above2019", "carbon_below2019", "biomass2019", "biomass_above2019", "biomass_below2019",
     "carbon2019_ha", "carbon_above2019_ha", "carbon_below2019_ha", "biomass2019_ha", "biomass_above2019_ha",
     "biomass_below2019_ha", "carbon2020", "carbon_above2020", "carbon_below2020", "biomass2020", "biomass_above2020",
     "biomass_below2020", "carbon2020_ha", "carbon_above2020_ha", "carbon_below2020_ha", "biomass2020_ha",
     "biomass_above2020_ha", "biomass_below2020_ha"]]

df_selected.to_csv(output_filename+".txt", index=True, sep=' ', mode='w')
df_selected.to_excel(output_filename+".xlsx", sheet_name='wyniki')

print("")
print("pomyslnie wyeksportowano do pliku.")
input("naciśnij enter aby wyjsc z programu.")
