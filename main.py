from easygui import *
import pygame


pygame.init()
m = pygame.mixer.Sound("10_ур.mp3")
# m.play()


pygame.init()
m_2 = pygame.mixer.Sound("конец.mp3")
# m_2.play()


pygame.init()
m_3 = pygame.mixer.Sound("не правильно.mp3")
# m_3.play()
pygame.init()
m_4 = pygame.mixer.Sound("правильно.mp3")
# m_4.play()


pygame.init()
m_5 = pygame.mixer.Sound("run-vine-sound.mp3")
# m_5.play()


pygame.init()
m_6 = pygame.mixer.Sound("epic.swf.mp3")
# m_6.play()


pygame.init()
m_7 = pygame.mixer.Sound("bruh-sound.mp3")
# m_7.play()


# dir/s


goo = 0


abc = choicebox("Сколько тебе лет ?", choices=["1","2","3","4","5","6","7","я взрослее"])
if abc == "1":
    msgbox("тебе рано но попробуй !")
if abc == "2":
    msgbox("тебе рано но попробуй !")
if abc == "3":
    msgbox("тебе рано но попробуй !")
if abc == "4":
    msgbox("давай начнём !")
if abc == "5":
    msgbox("давай начнём !")
if abc == "6":
    msgbox("ты большой но попробуй !")
if abc == "7":
    msgbox("ты большой но попробуй !")
if abc == "я взрослее":
    msgbox("ты большой но попробуй !")


bbb = choicebox("1 уровень 5 + 5", choices=["10","11"])
if bbb == "10":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1
if bbb == "11":
    m_7.play()
    msgbox("Ошибся ! Не правильно")


ccc = choicebox("2 уровень 2 + 8", choices=["10", "28"])
if ccc == "10":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1
if ccc == "28":
    m_3.play()
    msgbox("Ошибся ! Не правильно")


ddd = choicebox("3 уровень 6 + 7", choices=["13", "33"])
if ddd == "13":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1
if ddd == "33":
    m_3.play()
    msgbox("Ошибся ! Не правильно")


kyt = choicebox("4 уровень 8 + 3", choices=["11", "12"])
if kyt == "12":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyt == "11":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("5 уровень 11 + 2", choices=["15", "13"])
if kyy == "15":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "13":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


# чтото


bbb = choicebox("6 уровень 5 + 7", choices=["12","13"])
if bbb == "12":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1
if bbb == "13":
    m_3.play()
    msgbox("Ошибся ! Не правильно")


ccc = choicebox("7 уровень 6 + 4", choices=["10", "24"])
if ccc == "10":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1
if ccc == "24":
    m_3.play()
    msgbox("Ошибся ! Не правильно")


ddd = choicebox("8 уровень 3 + 6", choices=["9", "8"])
if ddd == "9":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1
if ddd == "8":
    m_3.play()
    msgbox("Ошибся ! Не правильно")


kyt = choicebox("9 уровень 11 + 4", choices=["15", "12"])
if kyt == "12":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyt == "15":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("10 уровень 12 + 7", choices=["18", "19"])
if kyy == "18":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "19":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


m.play()
msgbox("Поздравляю ты прошёл 10 уровней")


kyy = choicebox("11 уровень 14 + 7", choices=["22", "21"])
if kyy == "22":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "21":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("12 уровень 15 + 8", choices=["22", "21"])
if kyy == "25":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "23":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("13 уровень 37 + 8", choices=["44", "45"])
if kyy == "44":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "45":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("13 уровень 10 + 38", choices=["54", "48"])
if kyy == "54":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "48":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("14 уровень 13 + 38", choices=["52", "51"])
if kyy == "52":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "51":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("15 уровень 45 + 50", choices=["85", "95"])
if kyy == "95":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "85":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("16 уровень 50 + 50", choices=["100", "95"])
if kyy == "95" \
          "":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "100":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("17 уровень 55 + 55", choices=["85", "95"])
if kyy == "110" \
          "":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "155":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("18 уровень 75 + 32", choices=["107", "97"])
if kyy == "97" \
          "":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "107":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("19 уровень 80 + 13", choices=["103", "93"])
if kyy == "103" \
          "":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "93":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


kyy = choicebox("19 уровень 95 + 20", choices=["115", "105"])
if kyy == "105" \
          "":
    m_3.play()
    msgbox("Ошибся ! Не правильно")
if kyy == "115":
    m_4.play()
    msgbox("Молодец правильно !")
    goo += 1


m.play()
# чтото 2


m_2.play()
msgbox(str(goo)+" правильных ответов из 20 вопросов")
if goo < 5:
    m_5.play()
    msgbox("ты ответил мало правильных ответов")


if goo > 15 :
    m_6.play()
    msgbox("молодец !!!")

