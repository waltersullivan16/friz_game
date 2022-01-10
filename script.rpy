label start:
    jump test
    scene background bedroom with fade
    show friz otojasleeping with easeinbottom
    pause 1.0
    show friz otojaa
    pause 1.0
    show background bedroom blurr

    Friz "Nic nie stawia na nogi lepiej niż świadomość bycia multimiliardem."
    pause 1.0
    #show friz main_talking
    Friz "Niestety nie każdy dysponuje budżetem pozwalającym na tego typu zastrzyk energii."

    show nowciax main at pos_nowciax with moveinbottom
    Nowciax "Nie martwcie się jednak niezamożne istoty, wasza dobroduszna ekipa znalazła remedę na wasze problemy, mianowicie..."
    #show nowciax

    #show friz main_talking
    Friz "Zakup mojego kursu."
    #show friz main

    Nowciax "..."
    pause 1.0
    Nowciax "Najnowszy energetyk ekipy"
    #show "EKIPUP" with vpunch
    #show nowciax main

    Friz "Montażysta, reklame poprosze."

    #$ renpy.movie_cutscene("ekipup.webm")
#show movbie
    Friz "Nie zwlekajcie moi drodzy, już teraz biegnijcie do rodziców i poproście, aby kupili wam całą zgrzewkę."
    Nowciax "Dodam jeszcze, że eipup występuje w dwóch przepysznie orzeźwiających wariantach smakowych."
    Friz "Moim faworytem jest smak cytrynowego napoju ekipy."
    Nowciax "Ja natomiast preferuję truskawkę."
    Friz "Koniecznie dajcie nam znać w komentarzach, do którego teamu należycie: #teamtruskawka czy #teamcytryna."
    Friz "A teraz przejdźmy już do meritum."
    Friz "Montażysta, czołóweczkę poproszę."
    pause 1.0
    Friz "Jak to nie mamy czołóweczki?"

    Friz "Mam nadzieję, że przygotowaliście się już na tsunami dobrej zabawy, bo przygotowaliśmy dziś dla was coś specalneego."
    Friz "Odwiedzimy miejsce zupełnie oderwane od rzeczywistości."
    Nowciax "Miejsce, o którym większość z was nie ma nawet pojęcia."
    Friz "Antyczną cywilizację, której obcą jest idea płatności bezgotówkowej."
    Friz "Wbrew pozorom nie jest to prank."
    Nowciax "Ani skansen."
    Friz "Używając dialektu tutejszej społeczności jest to..."
    "BAZAR" with vpunch
    jump bazar

label filmik:
    Friz "Damy wam teraz chwilę abyście mogli otrząsnąć się z szoku."
    Friz "Ok, już."
    Friz "No ale dość już tych ciekawostek agroturystycznych."
    Nowciax "To już najwyższy czas, żeby zdradzić wam powód naszej dzisiejszej eskapady."
    Friz "W tym celu chciałbymc zapoznać was z materiałem źródłowym."
    Friz "Pragnę zaznaczyć, że powstał on dzięki uprzejmości naszych najwiernijszych fanów."
    Nowciax "Zdjęcia, które zaraz zobaczycie są właśnie ich autorstwa. Gdyby nie ich czujność, być może cała
    sprawa nigdy nie wyszłaby na jaw."
    Friz "Cóż za mrożąca krew w żyłach wizja!"
    Nowciax "Chcemy jakoś wyrazić naszą wdzięczność, więc prosimy wszystkie osoby, których zdjęć
    użyliśmy w materiale, który zaraz zobaczycie, o przesłanie nam swoich adresów." 
    Nowciax "Przygotowaliśmy dla was specjalne upominki."
    Friz "Ekipa jest teameem sprawiedliwym moi kochani, który za dobro wynagradza, a za zło karze."
    pause 1.0
    Friz "Zapraszamy na filmik."

label bazar:
    Nowciax "Szokujące, nieprawdaż?"
    Friz "Osobiście nie mógłbym spać spokojnie, gdybym miał jakikolwiek udział w rozpowszechnianiu
    tego, godnego pożałowania, partactwa!"
    Nowciax "To niebywałe, do czego mogą posunąć się ludzie, chcący zarobić parę nędznych groszy!"
    Friz "A przecież można włożyć trochę wysiłku i zabrać się do legitnej pracy!"
    Nowciax "Influensterstwu!"
    Friz "Wystarczy nagrać kilka challengy typu 'jem tylko jedzenie koloru wylosowanego przez koło fortuny'"
    Nowciax "No cóż, niektórzy wolą iść na łatwiznę i żerować na ciężkiej pracy innych."
    Friz "Należy stale mieć się na baczności, bo zło może czaić się tuż za rogiem."
    Nowciax "Popatrzcie na ten urokliwy stragan."
    Nowciax "Czy ta staroświecka dobroduszność możee budzić jakiekolwiek podejrzenia?"
    Nowciax "Przyjrzyjcie się uważniej..."
    Friz "NIEWIARYGODNE!"
    Nowciax "Nie mogę na to patrzeć, widok tych abominacji to istna tortura!"
    Friz "Overkill estetyki!"
    Friz "Proszę, aby każda osoba, która miała lub ma udział w tym niechlubnym procederze, bez względu
    na to, czy była to rola sprzedawdy czu kupującego..."
    Friz "NATYCHMIAST NAS ODSUBSKRYBUJE!"
    Nowciax "Idźcie do teamu X judasze, tam gdzie wasze miejsce!"
    Friz "Skoro oddzieliliśmy już ziarno od plew, przejdźmy do sedna sprawy."
    Nowciax "Możecie odetchnąć z ulgą, bo sytuacja nie jest aż tak zła, jak mogłoby się to wydawać."
    Friz "W imię walki z tym nielegalnym procederem stworzyliśmy nową serię."
    "EKIPA DONOSI"
    Nowciax "Ta nazwa to nie bgył nasz pomysł, możecie podziękować wujkowi Lukiemu za tą przeszywającą falę cringu, 
    która właśnie przeszła przez wasze ciała."
    Friz "Jak widać urodzeni z nas konfidenci."
    Friz "Skońćzmy już ten przydługi wstęp i bierzmy się do dzieła!"

    return
