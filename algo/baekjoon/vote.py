region = { "Seoul" : 8346647, "Busan" : 2921510, "Daegu" : 2046714, "Incheon" : 2519225, "Gwangju" : 1209206,\
        "Daejeon" : 1233177, "Ulsan" : 942210, "Sejong" : 288895, "Gyeonggi" : 11433288, "Gangwon" : 1333621, \
        "Chungbook" : 1365033, "Chungnam" : 1796474,"Junbook" : 1533125, "Junnam" : 1581278 ,"Gyeongbook" : 2273028,\
    "Gyeongnam" : 2809907 ,"Jeju" : 564354}

ratio = { "Seoul" : [50.35, 45.94], "Busan" : [58.53, 37.92], "Daegu" : [75.32, 21.55], "Incheon" : [46.97, 49.11], "Gwangju" : [12.28, 85.31] ,\

        "Daejeon" : [49.66, 46.53], "Ulsan" : [55.16, 40.16], "Sejong" : [43.40, 52.67], "Gyeonggi" : [45.94, 50.65], "Gangwon" : [54.55, 41.48], \
                "Chungbook" : [51.31, 44.59], "Chungnam" : [51.65, 44.45] ,"Junbook" : [13.74, 83.77], "Junnam" : [10.90, 86.71] ,"Gyeongbook" : [73.31, 23.38],\

    "Gyeongnam" : [60.62, 35.20] ,"Jeju" : [43.2, 52.49]}

Yoon = 0
Lee = 0
for i in region:
    Yoon += region[i] * ratio[i][0] * 1/100
    Lee += region[i] * ratio[i][1] * 1/100

#개표율 <= 10 : 서울(17.07) 대구(18.25) 인천(14.89) 울산(17.77) 세종(7.91) 경기(16.03) 보정해야함
# 개표율 >= 50 : 강원 충북 충남 전남 

name = "윤석열" if Yoon > Lee else "이재명"
print("Yoon")
print(Yoon)
print("Lee")
print(Lee)
print("")
print(f'{name}이 우세합니다.')
