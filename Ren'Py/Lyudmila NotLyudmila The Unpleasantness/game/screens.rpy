screen main_menu():
    tag menu

    # Добавляем твое фото с названием как фон
    # Файл должен лежать в папке images/main_bg.png (или .jpg)
    add "images/main_bg.jpg"

    # Контейнер для кнопок слева
    use navigation

    # --- НАДПИСЬ С ВЕРСИЕЙ СПРАВА ВНИЗУ ---
    text "v. [config.version] beta":
        xalign 0.99          
        yalign 0.99          
        size 28              # Сделали крупнее (было 18)
        color "#a0a0a0"      # Сделал цвет чуть светлее, чтобы лучше читалось
        outlines [(2, "#000000", 0, 0)] # Увеличили обводку до 2 пикселей под новый размер

screen navigation():
    vbox:
        style_prefix "navigation"
        
        xpos 0.05          # Отступ 5% от левого края экрана
        yalign 0.5         # Центрирование по вертикали
        spacing 20         # Расстояние между кнопками

        if main_menu:
            textbutton _("Новая игра") action Start()
        else:
            textbutton _("Сохранить") action ShowMenu("save")
            textbutton _("Вернуться") action Return()

        textbutton _("Загрузить") action ShowMenu("load")
        textbutton _("Настройки") action ShowMenu("preferences")

        if not main_menu:
            textbutton _("Главное меню") action MainMenu()

        textbutton _("Выход") action Quit(confirm=not main_menu)

screen ok_chat_list():
    # Затемнение фона вокруг телефона
    add Solid("#000000aa")

    # Корпус телефона
    frame:
        xalign 0.5
        yalign 0.5
        xsize 450
        ysize 800
        background Solid("#ffffff")
        padding (0, 0)

        vbox:
            # Шапка "Одноклассники"
            frame:
                xfill True
                ysize 80
                background Solid("#f58220")
                text "Одноклассники" xalign 0.5 yalign 0.5 size 28 bold True color "#ffffff"

            # Блок со списком чатов
            frame:
                background Solid("#e5e5e5")
                padding (0, 0)
                
                vbox:
                    # Spacing 2 и серый фон под ним создают эффект разделительных полос
                    spacing 2

                    # --- Чат 1: Группа класса ---
                    frame:
                        xfill True
                        ysize 95
                        background Solid("#ffffff")
                        padding (20, 10)
                        vbox:
                            spacing 5
                            # Название беседы
                            text "9-Б" size 24 bold True color "#000000"
                            # Кто написал и сообщение (в одну строчку)
                            text "Ольга Андреевна: Матвей больше не наш одноклассник, он переводится." size 18 color "#888888"

                    # --- Чат 2: Личные сообщения (Марина) ---
                    frame:
                        xfill True
                        ysize 95
                        background Solid("#ffffff")
                        padding (20, 10)
                        vbox:
                            spacing 5
                            text "Марина" size 24 bold True color "#000000"
                            text "хорошо" size 18 color "#888888"

                    # --- Чат 3: Личные сообщения (Савелий) ---
                    frame:
                        xfill True
                        ysize 95
                        background Solid("#ffffff")
                        padding (20, 10)
                        vbox:
                            spacing 5
                            text "Гриша" size 24 bold True color "#000000"
                            text "Я кататья, поедешь со мной?" size 18 color "#888888"

                    # --- Чат 4: Личные сообщения (Савелий) ---
                    frame:
                        xfill True
                        ysize 95
                        background Solid("#ffffff")
                        padding (20, 10)
                        vbox:
                            spacing 5
                            text "Савелий" size 24 bold True color "#000000"
                            text "Тумба юмба, у меня пауки на стене." size 18 color "#888888"
                            
                    # Оставшееся пустое белое место снизу (чтобы серый фон разделителей не торчал)
                    frame:
                        xfill True
                        yfill True
                        background Solid("#ffffff")

screen ok_messenger():
    # Полупрозрачный черный фон вокруг телефона, чтобы игра ушла на задний план
    add Solid("#000000aa")

    # Сам корпус телефона (по центру экрана)
    frame:
        xalign 0.5
        yalign 0.5
        xsize 450
        ysize 800
        background Solid("#ffffff") # Белый фон приложения
        padding (0, 0)

        vbox:
            # Шапка "Одноклассники"
            frame:
                xfill True
                ysize 80
                background Solid("#f58220") # Фирменный оранжевый цвет ОК
                text "Одноклассники" xalign 0.5 yalign 0.5 size 28 bold True color "#ffffff"

            # Окно с перепиской (можно скроллить)
            viewport:
                mousewheel True
                draggable True
                yfill True
                yadjustment ok_yadj
                
                frame:
                    background None
                    padding (20, 20)
                    xfill True

                    vbox:
                        spacing 15
                        xfill True

                        # Движок перебирает все сообщения и рисует их
                        for m in ok_messages:
                            if m["align"] == "left":
                                # Входящие (например, от Паши) - слева, серые
                                vbox:
                                    xalign 0.0
                                    spacing 5
                                    text m["sender"] size 16 color "#888888"
                                    frame:
                                        background Solid("#e5e5e5")
                                        padding (15, 10)
                                        text m["text"] size 22 color "#000000"
                            else:
                                # Исходящие (твои) - справа, светло-оранжевые
                                vbox:
                                    xalign 1.0
                                    spacing 5
                                    text m["sender"] size 16 color "#888888" xalign 1.0
                                    frame:
                                        background Solid("#ffebd6") 
                                        padding (15, 10)
                                        text m["text"] size 22 color "#000000"

screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu

    # Если мы в главном меню (до старта игры), показываем картинку школы
    if main_menu:
        add "main_bg.jpg"
    # А если мы нажали ESC во время игры — просто затемняем экран на 80%
    else:
        add Solid("#000000cc") 

    # Подключаем наши кнопки слева (они уже настроены!)
    use navigation

    # Дальше идет рамка, в которую подгружаются сами сохранения или настройки
    frame:
        style "game_menu_outer_frame"
        transclude

screen save():
    tag menu
    use file_slots(_("Сохранить"))

screen load():
    tag menu
    use file_slots(_("Загрузить"))

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Страница {}"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

    use game_menu(title):

        # Добавляем подложку для слотов
        frame:
            xalign 0.5
            yalign 0.5
            padding (30, 30)
            background Transform(Frame("gui/frame.png", 15, 15), matrixcolor=TintMatrix("#000000"), alpha=0.8) # Закругленная черная подложка

            fixed:
                # Этот блок отвечает за кнопки страниц (1, 2, 3, Авто, Быстрые)
                order_reverse True
                hbox:
                    xalign 0.5
                    yalign 0.0
                    spacing 20

                    textbutton _("<") action FilePagePrevious()
                    textbutton _("Авто") action FilePage("auto")
                    textbutton _("Быстрые") action FilePage("quick")
                    
                    # Генерация номеров страниц
                    for page in range(1, 10):
                        textbutton str(page) action FilePage(page)
                        
                    textbutton _(">") action FilePageNext()

                # Сетка самих слотов сохранения (3 колонки, 2 ряда = 6 слотов на страницу)
                grid 3 2:
                    style_prefix "slot"
                    xalign 0.5
                    yalign 0.5
                    spacing 20

                    for i in range(3 * 2):
                        $ slot = i + 1
                        
                        # Кнопка самого слота
                        button:
                            action FileAction(slot)
                            
                            has vbox
                            # Ren'Py сам делает скриншот в момент сохранения!
                            add FileScreenshot(slot) xalign 0.5
                            
                            text FileTime(slot, format=_("%b %d %Y, %H:%M"), empty=_("Пустой слот")) xalign 0.5
                            text FileSaveName(slot) xalign 0.5

screen history():
    tag menu

    # Если мы в главном меню (например, через горячую клавишу), показываем фон
    if main_menu:
        add "images/main_bg.jpg"
    else:
        add Solid("#000000cc")

    # Подключаем кнопки навигации слева
    use navigation

    # Основное окно истории
    frame:
        style_prefix "history"
        xalign 0.6
        yalign 0.5
        xsize 1000
        ysize 800
        padding (40, 40)
        background Transform(Frame("gui/frame.png", 15, 15), matrixcolor=TintMatrix("#000000"), alpha=0.8)

        # Вьюпорт для прокрутки
        viewport:
            id "history_viewport"
            mousewheel True
            draggable True
            scrollbars "vertical"
            yinitial 1.0 # Заставляет вьюпорт сразу прокручиваться вниз к последним репликам
            
            # Контейнер для всех реплик
            vbox:
                spacing 25
                xfill True

                for h in _history_list:
                    vbox:
                        spacing 10
                        
                        # Если есть имя персонажа — выводим его красным
                        if h.who:
                            label h.who:
                                style "history_name"
                                substitute False
                                
                        # Текст диалога
                        text h.what:
                            style "history_text"
                            substitute False

                if not _history_list:
                    label _("История пуста.") xalign 0.5 yalign 0.5 text_color "#ffffff" text_size 35

screen preferences():
    tag menu

    # Используем тот же фон, что и в главном меню, или другой "школьный"
    add "images/main_bg.jpg" 

    # Рамка-подложка, чтобы текст настроек был читаемым на фоне фото
    frame:
        style_prefix "pref"
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        background Transform(Frame("gui/frame.png", 15, 15), matrixcolor=TintMatrix("#000000"), alpha=0.8) # Полупрозрачный закругленный фон

        vbox:
            label _("Настройки") xalign 0.5
            null height 30

            hbox:
                spacing 50
                
                # Левая колонка: Режим экрана и Пропуск
                vbox:
                    spacing 20
                    label _("Экран")
                    textbutton _("Оконный") action Preference("display", "window")
                    textbutton _("Полный") action Preference("display", "fullscreen")

                    null height 20

                    label _("Пропуск")
                    textbutton _("Непрочитанный текст") action Preference("skip", "toggle")
                    textbutton _("После выборов") action Preference("after choices", "toggle")

                # Средняя колонка: Текст и Чтение
                vbox:
                    spacing 20
                    label _("Скорость текста")
                    bar value Preference("text speed") style "pref_slider"
                    
                    label _("Авто-чтение")
                    bar value Preference("auto-forward time") style "pref_slider"

                # Правая колонка: Аудио
                vbox:
                    spacing 20
                    label _("Музыка")
                    bar value Preference("music volume") style "pref_slider"
                    
                    label _("Звуки")
                    bar value Preference("sound volume") style "pref_slider"
                    
                    # Если вдруг решишь добавить озвучку
                    if config.has_voice:
                        label _("Голос")
                        bar value Preference("voice volume") style "pref_slider"

            null height 40
            
            # Кнопка возврата в меню
            textbutton _("Назад") action Return() xalign 0.5

screen choice(items):
    style_prefix "choice"

    # Контейнер для кнопок выравниваем строго по центру экрана
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30  # Делаем большой отступ, чтобы кнопки читались как отдельные рамки

        for i in items:
            textbutton i.caption action i.action

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        # Это вывод самого текста диалога
        text what id "what"

        # --- НАША НОВАЯ КНОПКА МЕНЮ ---
        textbutton _("Меню"):
            action ShowMenu("save")  # Открывает экран сохранений (эквивалент ESC)
            xalign 0.98              # Прижимаем к правому краю (98% ширины)
            yalign 0.95              # Прижимаем к низу
            
            # Настраиваем стиль текста кнопки прямо здесь, чтобы не плодить стили
            text_size 24
            text_idle_color "#888888"     # Неприметный серый в обычном состоянии
            text_hover_color "#ff4500"    # Агрессивно красный при наведении (Людмила-стайл)
            
            # Если хочешь, чтобы кнопка немного менялась при нажатии
            text_selected_color "#ffffff"

        hbox:
            xalign 0.98              # Прижимаем весь блок к правому краю
            yalign 0.95              # Прижимаем к низу
            spacing 20               # Расстояние между кнопками, чтобы не слипались

            # Кнопка Авточтения
            textbutton _("Авто"):
                action Preference("auto-forward", "toggle")
                text_size 24
                text_idle_color "#888888"     
                text_hover_color "#ff4500"    
                text_selected_color "#ffffff" # Когда авточтение включено, кнопка будет гореть белым!

            # Наша старая кнопка Меню (ESC)
            textbutton _("Меню"):
                action ShowMenu("save")  
                text_size 24
                text_idle_color "#888888"     
                text_hover_color "#ff4500"

    ## Дальше идет стандартный код движка (портреты и quick_menu), его не трогай

# Стиль самой кнопки выбора
style choice_button is default:
    properties gui.button_properties("choice_button")
    xalign 0.5
    xsize 1000           # Немного расширим кнопку для длинных вариантов
    padding (20, 20)     # Внутренние отступы вместо фиксированной высоты
    background Transform(Frame("gui/frame.png", 15, 15), matrixcolor=TintMatrix("#111111"), alpha=0.9)
    hover_background Transform(Frame("gui/frame.png", 15, 15), matrixcolor=TintMatrix("#ff4500"), alpha=1.0)

# Стиль текста внутри кнопки
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    xalign 0.5
    yalign 0.5
    text_align 0.5       # Центрирование текста, если он займет больше одной строки
    size 32
    idle_color "#cccccc"
    hover_color "#ffffff"
    outlines [(2, "#000000", 0, 0)] # Легкая черная обводка для лучшей читаемости

# Настройка стиля текста кнопок (чтобы были побольше и читались)
style navigation_button_text:
    size 40
    idle_color "#ffffff"      # Цвет в обычном состоянии
    hover_color "#ff0000"     # Цвет при наведении (сделаем красный под стиль Людмилы)

style pref_label:
    top_margin 10
    bottom_margin 5

style pref_label_text:
    size 35
    color "#ff4500" # Тот самый "Людмилин" красный
    bold True

style pref_vbox:
    xsize 300 # Ширина колонок

style pref_button_text:
    idle_color "#cccccc"
    hover_color "#ffffff"
    selected_color "#ff4500" # Цвет активного режима (например, "Полный экран")

style pref_slider:
    xsize 300 # Ширина ползунков громкости

# Настройка внешнего вида ползунков
style pref_slider:
    xsize 300                             # Длина ползунка
    ysize 25                              # Толщина ползунка
    base_bar Solid("#444444")             # Цвет пустой части (темно-серый)
    thumb Solid("#ffffff")                # Цвет самого "бегунка" (белый квадрат)
    thumb_offset 12                       # Смещение бегунка, чтобы он был по центру
    left_bar Solid("#ff4500")             # Цвет заполненной части (снова наш "красный")

    # Стили для слотов сохранения
style slot_button:
    xysize (350, 250)         # Размер одной карточки сохранения
    padding (10, 10, 10, 10)
    background Transform(Frame("gui/frame.png", 10, 10), matrixcolor=TintMatrix("#333333"))
    hover_background Transform(Frame("gui/frame.png", 10, 10), matrixcolor=TintMatrix("#ff4500"))

style slot_button_text:
    size 20
    color "#ffffff"
    top_margin 10

# Основная плашка с текстом
style window:
    xalign 0.5
    xsize 1800           # Немного сужаем окно, чтобы закругленные края не сливались со стенками экрана
    yalign 0.95          # Слегка приподнимаем от низа экрана
    ysize 280            # Высота текстового окна
    padding (80, 100, 80, 20) # ОПУСКАЕМ ТЕКСТ: увеличили отступ сверху с 60 до 100
    # Используем скругленный фрейм (стандартный из папки gui)
    background Transform(Frame("gui/frame.png", 15, 15), alpha=0.9)

# Плашка с именем персонажа
style namebox:
    xpos 80              # Сдвигаем вправо, чтобы было на уровне текста
    ypos -50             # Выдвигаем чуть вверх за пределы основного текстобокса
    background Transform(Frame("gui/frame.png", 10, 10), matrixcolor=TintMatrix("#ff4500"))
    padding (20, 5, 20, 5)

style namebox_label_text:
    color "#ffffff"      # Белый текст имени
    size 35
    bold True

# Стили для экрана истории
style history_name is gui_label

style history_name_text is gui_label_text:
    color "#ff4500"      # Выводим имя красным цветом, как указано в комментарии
    bold True
    size 35

style history_text is gui_text:
    color "#ffffff"
    size 30
