import tkinter as tk
import urllib.request
from PIL import Image, ImageTk
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
urllib.request.urlretrieve(
  'https://i.imgur.com/NTZn4Tg.jpg',
   "薛狗.jpg")
window = tk.Tk()
window.title('IMAC 聘人計算機')
window.geometry('800x800')
window.configure(background='white')
img = Image.open("薛狗.jpg")  
photo = ImageTk.PhotoImage(img)


def resize(img2, w, h):
    size = (w, h)
    resized = img.resize(size,Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(resized)

    return img2

photo = resize(photo, 400, 400)
bk_label = tk.Label(window, image=photo)
bk_label.pack(expand=False)

def Insurance():
    realmoney = round(int(realmoney_button.get())*(1.0211))
    surfacemoney = int(surfacemoney_button.get())
    Insurance_table =[[0, 1500, 11100, 26400, 1500, 244, 22, 266, 855, 78, 26, 0, 933, 409, 1286, 90, 2335, 26400],
        [1501, 3000, 11100, 26400, 3000, 244, 22, 266, 855, 78, 26, 0, 933, 409, 1286, 180, 2425, 26400],
        [3001, 4500, 11100, 26400, 4500, 244, 22, 266, 855, 78, 26, 0, 933, 409, 1286, 270, 2515, 26400],
        [4501, 6000, 11100, 26400, 6000, 244, 22, 266, 855, 78, 26, 0, 933, 409, 1286, 360, 2605, 26400],
        [6001, 7500, 11100, 26400, 7500, 244, 22, 266, 855, 78, 26, 0, 933, 409, 1286, 450, 2695, 26400],
        [7501, 8700, 11100, 26400, 8700, 244, 22, 266, 855, 78, 26, 0, 933, 409, 1286, 522, 2767, 26400],
        [8701, 9900, 11100, 26400, 9900, 244, 22, 266, 855, 78, 26, 0, 933, 409, 1286, 594, 2839, 26400],
        [9901, 11100, 11100, 26400, 11100, 244, 22, 266, 855, 78, 26, 0, 933, 409, 1286, 666, 2911, 26400],
        [11101, 12540, 12540, 26400, 12540, 276, 25, 301, 966, 88, 26, 0, 1054, 409, 1286, 752, 3118, 26400],
        [12541, 13500, 13500, 26400, 13500, 297, 27, 324, 1040, 95, 26, 0, 1135, 409, 1286, 810, 3257, 26400],
        [13501, 15840, 15840, 26400, 15840, 348, 32, 380, 1220, 111, 26, 0, 1331, 409, 1286, 950, 3593, 26400],
        [15841, 16500, 16500, 26400, 16500, 363, 33, 396, 1271, 116, 26, 0, 1387, 409, 1286, 990, 3689, 26400],
        [16501, 17280, 17280, 26400, 17280, 380, 35, 415, 1331, 121, 26, 0, 1452, 409, 1286, 1037, 3801, 26400],
        [17281, 17880, 17880, 26400, 17880, 393, 36, 429, 1377, 125, 26, 0, 1502, 409, 1286, 1073, 3887, 26400],
        [17881, 19047, 19047, 26400, 19047, 419, 38, 457, 1467, 133, 26, 0, 1600, 409, 1286, 1143, 4055, 26400],
        [19048, 20008, 20008, 26400, 20008, 440, 40, 480, 1541, 140, 26, 0, 1681, 409, 1286, 1200, 4193, 26400],
        [20009, 21009, 21009, 26400, 21009, 462, 42, 504, 1618, 147, 26, 0, 1765, 409, 1286, 1261, 4338, 26400],
        [21010, 22000, 22000, 26400, 22000, 484, 44, 528, 1694, 154, 26, 0, 1848, 409, 1286, 1320, 4480, 26400],
        [22001, 23100, 23100, 26400, 23100, 508, 46, 554, 1779, 162, 26, 0, 1941, 409, 1286, 1386, 4639, 26400],
        [23101, 24000, 24000, 26400, 24000, 528, 48, 576, 1848, 168, 26, 0, 2016, 409, 1286, 1440, 4768, 26400],
        [24001, 25250, 25250, 26400, 25250, 556, 51, 607, 1944, 177, 26, 0, 2121, 409, 1286, 1515, 4948, 26400],
        [25251, 26400, 26400, 26400, 26400, 581, 53, 634, 2033, 185, 26, 0, 2218, 409, 1286, 1584, 5114, 26400],
        [26401, 27600, 27600, 27600, 27600, 607, 55, 662, 2125, 193, 28, 0, 2318, 428, 1344, 1656, 5346, 27600],
        [27601, 28800, 28800, 28800, 28800, 634, 58, 692, 2218, 202, 29, 0, 2420, 447, 1403, 1728, 5580, 28800],
        [28801, 30300, 30300, 30300, 30300, 667, 61, 728, 2333, 212, 30, 0, 2545, 470, 1476, 1818, 5869, 30300],
        [30301, 31800, 31800, 31800, 31800, 700, 64, 764, 2449, 223, 32, 0, 2672, 493, 1549, 1908, 6161, 31800],
        [31801, 33300, 33300, 33300, 33300, 733, 67, 800, 2564, 233, 33, 0, 2797, 516, 1622, 1998, 6450, 33300],
        [33301, 34800, 34800, 34800, 34800, 766, 70, 836, 2680, 244, 35, 0, 2924, 540, 1695, 2088, 6742, 34800],
        [34801, 36300, 36300, 36300, 36300, 799, 73, 872, 2795, 254, 36, 0, 3049, 563, 1768, 2178, 7031, 36300],
        [36301, 38200, 38200, 38200, 38200, 840, 76, 916, 2941, 267, 38, 0, 3208, 592, 1860, 2292, 7398, 38200],
        [38201, 40100, 40100, 40100, 40100, 882, 80, 962, 3088, 281, 40, 0, 3369, 622, 1953, 2406, 7768, 40100],
        [40101, 42000, 42000, 42000, 42000, 924, 84, 1008, 3234, 294, 42, 0, 3528, 651, 2045, 2520, 8135, 42000],
        [42001, 43900, 43900, 43900, 43900, 966, 88, 1054, 3380, 307, 44, 0, 3687, 681, 2138, 2634, 8503, 43900],
        [43901, 45800, 45800, 45800, 45800, 1008, 92, 1100, 3527, 321, 46, 0, 3848, 710, 2231, 2748, 8873, 45800],
        [45801, 48200, 45800, 48200, 48200, 1008, 92, 1100, 3527, 321, 48, 0, 3848, 748, 2347, 2892, 9135, 48200],
        [48201, 50600, 45800, 50600, 50600, 1008, 92, 1100, 3527, 321, 51, 0, 3848, 785, 2464, 3036, 9399, 50600],
        [50601, 53000, 45800, 53000, 53000, 1008, 92, 1100, 3527, 321, 53, 0, 3848, 822, 2581, 3180, 9662, 53000],
        [53001, 55400, 45800, 55400, 55400, 1008, 92, 1100, 3527, 321, 55, 0, 3848, 859, 2698, 3324, 9925, 55400],
        [55401, 57800, 45800, 57800, 57800, 1008, 92, 1100, 3527, 321, 58, 0, 3848, 896, 2815, 3468, 10189, 57800],
        [57801, 60800, 45800, 60800, 60800, 1008, 92, 1100, 3527, 321, 61, 0, 3848, 943, 2961, 3648, 10518, 60800],
        [60801, 63800, 45800, 63800, 63800, 1008, 92, 1100, 3527, 321, 64, 0, 3848, 990, 3107, 3828, 10847, 63800]]
    for i in range(len(Insurance_table)):
        money_Minrange = int(Insurance_table[i][0])
        money_Maxrange = int(Insurance_table[i][1])
        if ( realmoney > money_Minrange and realmoney < money_Maxrange):
            accident = int(Insurance_table[i][10])
            labor = int(Insurance_table[i][12])
            retire = int(Insurance_table[i][15])
            Insurance_total = accident + labor + retire

    print(realmoney)
    expr = surfacemoney - (realmoney + Insurance_total)
    labor_label.configure(text="勞保金額：{} 元 勞退金額：{} 元 職災金額：{} 元 \n 總共金額：{} 元".format(labor,retire,accident,Insurance_total))
    result = '{} \n 實領金額扣除帳面金額剩餘：{} 元'.format(get_bmi_status_description(expr),expr)
    result_label.configure(text=result)
    
# 顯示評語
def get_bmi_status_description(expr):
    if expr > 0:
        return '實領金額符合公式'
    else:
        return '實領金額不符合公式'

# 標題
header_label = tk.Label(window, text='IMAC 聘人計算機', font='_ 30')
header_label.pack()

# 實領金額區域
realmoney_frame = tk.Frame(window)
realmoney_frame.pack(side=tk.TOP, pady=10)
realmoney_label = tk.Label(realmoney_frame, text='實際金額', font='_ 30')
realmoney_label.pack(side=tk.LEFT)
realmoney_button = tk.Entry(realmoney_frame, font='_ 30')
realmoney_button.insert(0,'')
realmoney_button.pack(side=tk.LEFT)

# 帳面金額區域
surfacemoney_frame = tk.Frame(window)
surfacemoney_frame.pack(side=tk.TOP)
surfacemoney = tk.Label(surfacemoney_frame, text='帳面金額', font='_ 30', foreground='black', bg='white')
surfacemoney.pack(side=tk.LEFT)
surfacemoney_button = tk.Entry(surfacemoney_frame, font='_ 30')
surfacemoney_button.insert(0, '30000')
surfacemoney_button.pack(side=tk.LEFT)

# 勞保金額區域
labor_label = tk.Label(window, font='_ 20')
labor_label.pack()

# # 帳面金額區域
# surfacemoney_frame = tk.Frame(window)
# surfacemoney_frame.pack(side=tk.TOP)
# surfacemoney = tk.Label(surfacemoney_frame, text='帳面金額', font='_ 30', foreground='black', bg='white')
# surfacemoney.pack(side=tk.LEFT)
# surfacemoney_button = tk.Entry(surfacemoney_frame, font='_ 30')
# surfacemoney_button.insert(0, '30000')
# surfacemoney_button.pack(side=tk.LEFT)

# 計算結果

result_label = tk.Label(window, font='_ 20')
result_label.pack()
calculate_button = tk.Button(window, text='開始計算', command=Insurance, font='_ 20', foreground='#00ff00', background='blue')
calculate_button.pack()

window.mainloop()
