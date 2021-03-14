#Tuğçe Nur Ergen
#knowledge competition

questions = ["Göbekli tepe hangi ilimizdedir?",
             "Bursa'nın en ünlü tatlısıdır, Bursa'nın bir ilçesiyle aynı adı taşır?",
             "Japonların geleneksel güreşine ne ad verilir?",
             "Yeni bir işe girerken, iş yerlerine verdiğimiz kısa öz geçmişin kısa adı?",
             "Tarla, arsa, bina gibi taşınmazlar için ödediğimiz vergiye ne ad verilir?",
             "Kız Kalesi hangi ilimizdedir?",
             "Türkiye'de Hava durumu tahminlerini yapan hava durumu bilgilerini kamuoyu ile paylaşan kurumumuzun adı nedir?",
             "Hicri Takvime göre Kadir gecesi hangi aydadır?",
             "Ölenden geriye kalan mal veya para?",
             "Türkiye'nin gül ve gül yağı üretiminde dünya çapındaki şehrimiz neresidir?"]
answers = ["Şanlıurfa", "Mustafa Kemal Paşa tatlısı", "sumo","CV","emlak vergisi","mersin","meteoroloji","ramazan","miras","ısparta"]
score = 0
for i in range(0,9):
    if i!= 0:
     print("Next Question:")
    answer = input(str(questions[i]) + ": ")
    if answer.lower() == answers[i].lower():
        score +=10
        print("Your answer is correct! :D")
    else:
        print("your answer is wrong! :(")

if score<=50:
    print("..........FAİLED.........\nYour score :" + str(score))
elif score > 50:
    print("..........CONGRATULATIONS!!..........\nYour score :" + str(score))
