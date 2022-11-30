import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

champion_list = "champs.txt" #Pfad der .txt mit den Champion-Namen
champion_icons = "tiles" #Pfad des tiles Ordners mit den Champion Icons
champion_list_unformatiert = open(champion_list, "r")

champion_final = []
champion_final_list = []

#Champion Namen aus dem .txt auslesen und in Liste schreiben
for line in champion_list_unformatiert:
    champion_cut = line.replace('\n','').replace('}','').replace("'","").replace(" ","")
    champion_final = champion_cut.split("|", 2)[1]
    champion_final_list.append(str(champion_final)) #Liste mit allen Champion-Namen erstellen

#Zufällige Champions aus der Liste würfeln
champion_raffle = random.sample(champion_final_list, k=30) #Würfle 30 Random Champions ohne Dopplung
#print(champion_raffle)
team_blue = champion_raffle[0:15] #1-15 sind Team Blau
team_red = champion_raffle[15:32] #16-30 sind Team Rot

#Grafik Erstellung für Team Blau
spalten_b = 0
zeilen_b = 0
team_blue_grid, axarr = plt.subplots(3, 5) #3 Zeilen, 5 Spalten
team_blue_grid.suptitle('Team Blau', fontsize=20)
for element_b in team_blue:
    champion_pic = element_b + "_0.jpg" #Ergänzen des gerollten Champions mit der Bildendung aus dem tiles Ordner
    path_icon = champion_icons + "/" + champion_pic #Path im Ordner mit den Bildern
    icon = mpimg.imread(path_icon) #Finden des Bildes im Ordner
    plt.imshow(icon)
    axarr[zeilen_b, spalten_b].axis('off') #Achsen nicht anzeigen
    axarr[zeilen_b, spalten_b].imshow(icon) #Bild plotten
    axarr[zeilen_b, spalten_b].set_title(element_b) #Champion-Name als Titel
    spalten_b += 1
    if spalten_b == 5:
        spalten_b = 0
        zeilen_b += 1
    else:
        pass
team_blue_grid.savefig("TeamBlau.jpg", bbox_inches='tight') #S

#Grafik Erstellung für Team Rot
team_red_grid, axarr = plt.subplots(3, 5)
team_red_grid.suptitle('Team Rot', fontsize=20)
spalten_r = 0
zeilen_r = 0
for element_r in team_red:
    champion_pic = element_r + "_0.jpg"
    path_icon = champion_icons + "/" + champion_pic
    icon = mpimg.imread(path_icon)
    plt.imshow(icon)
    axarr[zeilen_r, spalten_r].imshow(icon)
    axarr[zeilen_r, spalten_r].axis('off')
    axarr[zeilen_r, spalten_r].imshow(icon)
    axarr[zeilen_r, spalten_r].set_title(element_r)

    spalten_r += 1

    if spalten_r == 5:
        spalten_r = 0
        zeilen_r += 1
    else:
        pass
team_red_grid.savefig("TeamRot.jpg", bbox_inches='tight')