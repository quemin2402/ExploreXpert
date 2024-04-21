import math

import openrouteservice
import folium
import webbrowser

def createRoute(arr, type, htmlArr, iconArr, client_id):
    client = openrouteservice.Client(
        key='5b3ce3597851110001cf62482e73b746f8744f2380390743cbe3177d')  # Specify your personal API key
    average = averageLocation(arr)
    m = folium.Map(location=[arr[0][1], arr[0][0]], tiles='cartodbpositron', zoom_start=16, min_zoom=15)


    coordinates = arr
    # example arr: [71.41863683, 51.14931279], [71.41601637, 51.08926213], [71.41730189, 51.14842397], [71.46370553, 51.12337408]


    # The popup will show the ID in the coordinate list. In a non-optimized waypoint order, the waypoints
    # would have been visited from ID 0 to ID 3 sequentially.
    for idx, coords in enumerate(coordinates):
        folium.Marker(location=list(reversed(coords)),
                      popup=htmlArr[idx],
                      icon=folium.DivIcon(iconArr[idx])
                      ).add_to(m)


    if type == 0:
        route = client.directions(
            coordinates=coordinates,
            profile='foot-walking',
            format='geojson',
            validate=False,
            optimize_waypoints=True
        )
    elif type == 1:
        route = client.directions(
            coordinates=coordinates,
            profile='cycling-regular',
            format='geojson',
            validate=False,
            optimize_waypoints=True
        )
    else:
        route = client.directions(
            coordinates=coordinates,
            profile='driving-car',
            format='geojson',
            validate=False,
            optimize_waypoints=True
        )
    folium.PolyLine(locations=[list(reversed(coord))
                               for coord in
                               route['features'][0]['geometry']['coordinates']]).add_to(m)
    print(route)
    m.save(f"maps/map_{client_id}.html")

def averageLocation(arr):
    finalX = 0.0
    finalY = 0.0
    count = 0
    for loc in arr:
        finalX += loc[0]
        finalY += loc[1]
        count += 1
    return finalY / count, finalX / count

def locationOutput(locList, initCoordinates,client_id):
    arrInit = [[71.41863683,51.14931279], [71.41601637,51.08926213], [71.41730189,51.14842397], [71.46370553,51.12337408],
                [71.46975836,51.11886154], [71.43050477,51.12841024], [71.41730189,51.14842397], [71.41440359,51.14737197],
                [71.41730189,51.14842397], [70.30313949,53.08234897], [70.97145254,51.07830381], [71.42347091,51.17151691],
                [71.46975836,51.11886154], [71.47249244,51.12080712], [71.43023098,51.10448333], [71.42765522,51.13059594],
                [71.469689,51.122164], [71.473262,51.126175], [71.426961,51.156873], [71.42351286,51.16300066],
                [71.41932786,51.15701027], [71.41568305,51.12669614], [71.4399799,51.1131959], [71.48962866,51.1480329],
                [71.45008403,51.13622957], [71.40388685,51.13258349], [71.41283273,51.08951312], [71.43898057,51.13592905],
                [71.42135805,51.16513396], [71.43853063,51.1287448], [71.48240874,51.1495212], [71.41915323,51.166802],
                [71.44034461,51.1167171], [71.43173147,51.15590876], [71.41092402,51.13624783], [71.42371986,51.14649569]]
    arr = []
    htmlArrInit = ["""<div><img src="https://astana.citypass.kz/wp-content/uploads/2018/07/atam2-624x405.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">ETHNO-MEMORIAL COMPLEX «ATAMEKEN»</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-19:00</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2018/07/17/etno-memorialnyiy-kompleks-atameken/">LINK</a></div>""",
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/2017/11/1-624x405.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">«NUR-ALEM» FUTURE ENERGY MUSEUM (EXPO)</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-20:00</span><br><span STYLE="font-size:18.0pt">Tuesday-Sunday</span><br><a href="https://astana.citypass.kz/en/2017/11/24/obektyi-naslediya-ekspo/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/2017/09/da4-624x345.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">THEATER OF ANIMATRONICS «JUNGLE»</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-20:00</span><br><span STYLE="font-size:18.0pt">Monday-Friday</span><br><a href="https://astana.citypass.kz/en/2017/09/15/teatr-animatroniksov-dzhungli/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/пирамида.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">THE PALACE OF PEACE AND RECONCILIATION</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-18:00</span><br><span STYLE="font-size:18.0pt">Tuesday-Saturday</span><br><a href="https://astana.citypass.kz/en/2018/02/15/dvorets-mira-i-soglasiya/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/2017/05/nm1-624x345.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">NATIONAL MUSEUM OF THE REPUBLIC OF KAZAKHSTAN</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-18:00</span><br><span STYLE="font-size:18.0pt">Tuesday-Saturday</span><br><a href="https://astana.citypass.kz/en/2017/05/15/natsionalnyiy-muzey-respubliki-kazahstan/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/G6g4BFfWHK6qxwrmz-1.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">«ASTANA-BAITEREK» MONUMENT</span><br><span STYLE="font-size:18.0pt">Working Hours: 9:00-21:00</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2017/05/15/bayterek/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/2017/05/ok2-624x345.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">THE OCEANARIUM «AILAND»</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-20:00</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2017/05/15/rts-duman/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/s1200.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">THE FERRIS WHEEL «AILAND»</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-20:00</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2017/05/15/koleso-obozreniya-duman/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/ec97244da58e60554054757a94d5999c.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">EXOTARIUM “AILAND”</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-20:00</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2022/01/17/ekzotarium-ailand/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/2018/07/s1200-624x345.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">VISIT CENTER «BURABAY»</span><br><span STYLE="font-size:18.0pt">Working Hours: 9:00-18:00</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2018/07/05/vizit-tsentr/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/2018/06/M--razhay---imaratyi-kopiya-624x345.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">MUSEUM AND MEMORIAL COMPLEX «ALZHIR»</span><br><span STYLE="font-size:18.0pt">Working Hours: 9:00-18:00</span><br><span STYLE="font-size:18.0pt">Tuesday-Sunday</span><br><a href="https://astana.citypass.kz/en/2018/06/19/muzeyno-memorialnyiy-kompleks-alzhir/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/2018/02/70-624x405.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">MUSEUM OF SAKEN SEIFULLIN</span><br><span STYLE="font-size:18.0pt">Working Hours: 9:00-17:00</span><br><span STYLE="font-size:18.0pt">Monday-Friday</span><br><a href="https://astana.citypass.kz/en/2018/02/15/muzey-sakena-seyfullina/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/зал-золота1.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">“HALL OF GOLD” IN THE NATIONAL MUSEUM OF THE REPUBLIC OF KAZAKHSTAN</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-18:00</span><br><span STYLE="font-size:18.0pt">Tuesday-Sunday</span><br><a href="https://astana.citypass.kz/en/2018/09/05/zal-zoloto-v-nacionalynom-muzee-respubliki-kazahstan/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/2018/04/11-624x405.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">PALACE OF INDEPENDENCE</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-18:00</span><br><span STYLE="font-size:18.0pt">Tuesday-Sunday</span><br><a href="https://astana.citypass.kz/en/2018/04/28/dvorets-nezavisimosti/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/триумф-арка1.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">ARC DE TRIOMPHE «MӘҢGІLІK EL»</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-18:00</span><br><span STYLE="font-size:18.0pt">Monday-Friday</span><br><a href="https://astana.citypass.kz/en/2018/01/19/triumfalnaya-arka-m-gilik-el-2/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/DECHgV7XgAAJmIh.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">“NURZHOL” BOULEVARD</span><br><span STYLE="font-size:18.0pt">Any time</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/09/bulvar-nurzhol/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/1-4.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">MONUMENT «KAZAKH ELI»</span><br><span STYLE="font-size:18.0pt">Any time</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/09/monument-kazakh-eli/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/MxOCyZ.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">«HAZRAT SULTAN» MOSQUE</span><br><span STYLE="font-size:18.0pt">Any time</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/09/mechet-hazret-sultan/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/1be03bbed5957a58849daeb4b3497016.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">ATYRAU BRIDGE</span><br><span STYLE="font-size:18.0pt">Any time</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/09/most-atyrau-kopiri/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/img_5204_l1D4g6Vfel4B.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">ARBAT</span><br><span STYLE="font-size:18.0pt">Any time</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/09/arbat/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/7db97aa358c9dcf7b27cd405bceba5e3.jpeg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">METROPOLITAN PARK</span><br><span STYLE="font-size:18.0pt">Any time</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/09/stolichnyi-park/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/13c2f329ea944eaab82f6f3b229e4b42.max-1200x800.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">«NUR-ASTANA» MOSQUE</span><br><span STYLE="font-size:18.0pt">Working Hours: 4:00-22:00</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/09/mechet-nur-astana/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/21617815-image-crop-640x762-1532523924-728-556e79e152-1533105616.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">PRESIDENTIAL PARK</span><br><span STYLE="font-size:18.0pt">Any time</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/ru/2021/08/09/prezidentskii-park/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/1-10.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">«ZHERUYIK» PARK</span><br><span STYLE="font-size:18.0pt">Any time</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/09/park-zheruiyk/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/870_474_fixedwidth.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">TRIATHLON PARK “ASTANA”</span><br><span STYLE="font-size:18.0pt">Any time</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/11/triatlon-park-astana/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/ханшатыр.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">«KHAN SHATYR» SEC</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-22:00</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/11/trc-khan-shatyr/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/dji_0061f.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">EXPO-PARK</span><br><span STYLE="font-size:18.0pt">Any time</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/11/expo-park/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/1531305489_img_20180710_215714_746.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">«JETYSU» PARK</span><br><span STYLE="font-size:18.0pt">Any time</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/11/park-jetisu/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/1522237.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">OLD SQUARE</span><br><span STYLE="font-size:18.0pt">Working Hours: 9:00-18:00</span><br><span STYLE="font-size:18.0pt">Monday-Friday</span><br><a href="https://astana.citypass.kz/en/2021/08/11/staraya-ploshad/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/хас-санат1.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">THE HAS SANAT ART GALLERY</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-19:00</span><br><span STYLE="font-size:18.0pt">Monday-Saturday</span><br><a href="https://astana.citypass.kz/en/2020/07/29/galereya-isskustv-has-sanat/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/906.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">SVYAT USPENSKYI ORTHODOX CATHEDRAL</span><br><span STYLE="font-size:18.0pt">Working Hours: 8:00-19:00</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2021/08/11/svyat-uspenskii-kafedralnyi-sobor/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/2017/05/10-1-624x405.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">MUSEUM OF THE FIRST PRESIDENT OF KAZAKHSTAN</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-18:00</span><br><span STYLE="font-size:18.0pt">Tuesday-Sunday</span><br><a href="https://astana.citypass.kz/en/category/muzei-i-galerei/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/Назарбаев-центр.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">NAZARBAYEV CENTER</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-18:00</span><br><span STYLE="font-size:18.0pt">Tuesday-Sunday</span><br><a href="https://astana.citypass.kz/en/2017/05/15/prezidentskaya-biblioteka/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/военный.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">MILITARY-HISTORICAL MUSEUM OF THE ARMED FORCES OF THE REPUBLIC OF KAZAKHSTAN</span><br><span STYLE="font-size:18.0pt">Working Hours: 10:00-18:00</span><br><span STYLE="font-size:18.0pt">Tuesday-Sunday</span><br><a href="https://astana.citypass.kz/en/2017/05/15/voenno-istoricheskiy-muzey-vooruzhennyih-sil-respubliki-kazahstan/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/IMG_4714.jpg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">EXCURSION TO THE “ASTANA OPERA” HOUSE</span><br><span STYLE="font-size:18.0pt">Working Hours: 11:00-15:00</span><br><span STYLE="font-size:18.0pt">Tuesday-Sunday</span><br><a href="https://astana.citypass.kz/en/2018/06/19/vodnyie-progulki-po-reke-ishim/">LINK</a></div>""", 
"""<div><img src="https://astana.citypass.kz/wp-content/uploads/2018/06/f894ff3d-efe0-41fe-b487-826081f81409-624x345.jpeg" alt="image" width="320" height="200"><br /><span STYLE="font-size:18.0pt">WATER WALKS ALONG THE RIVER ISHIM</span><br><span STYLE="font-size:18.0pt">Working Hours: 12:00-20:30</span><br><span STYLE="font-size:18.0pt">Schedule: Daily</span><br><a href="https://astana.citypass.kz/en/2024/03/01/ekskursiya-v-teatre-astana-opera/">LINK</a></div>"""]
    htmlArr = []
    iconArrInit = ["""<img src="https://cdn-icons-png.flaticon.com/128/785/785432.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/785/785432.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/4432/4432858.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/785/785432.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/785/785432.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/3068/3068288.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/4432/4432858.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/4432/4432858.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/4432/4432858.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/3068/3068288.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/785/785432.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/785/785432.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/785/785432.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/3068/3068288.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/5934/5934169.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/5934/5934169.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/253/253298.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/785/785432.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/5934/5934169.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/785/785432.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/785/785432.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/785/785432.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">""",
"""<img src="https://cdn-icons-png.flaticon.com/128/2465/2465945.png" width="30" height="30">"""]
    iconArr = []

    arr.append(initCoordinates)
    htmlArr.append("""<div><span STYLE="font-size:18.0pt">Your Location</span></div>""")
    iconArr.append("""<img src="https://cdn-icons-png.flaticon.com/128/684/684908.png" width="30" height="30">""")
    # finding furthest location and setting it as last
    furthestLoc = 0
    furthestDist = 0.0
    for index in locList:
        if math.sqrt((arrInit[index][0]-initCoordinates[0])*(arrInit[index][0]-initCoordinates[0])+(arrInit[index][1]-initCoordinates[1])*(arrInit[index][1]-initCoordinates[1])) > furthestDist:
            furthestLoc = index
    locList.remove(furthestLoc)
    locList.append(furthestLoc)
    for index in locList:
        arr.append(arrInit[index])
        htmlArr.append(htmlArrInit[index])
        iconArr.append((iconArrInit[index]))

    createRoute(arr, 0, htmlArr, iconArr,client_id)




