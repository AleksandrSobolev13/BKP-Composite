# BKP-Composite. Выпускная квалификационная работа по программе повышения квалификации «Data Science» 
### Тема - «Прогнозирование конечных свойств композиционных материалов» 
### Цель работы - изучение способов прогнозирования конечных свойств новых композиционных материалов и разработка моделей для выполнения прогнозов. 
##### В качестве инструментов в работе использовались свободнораспространяемое программное обеспечение: операционная система Linux Mint 19.3, conda 23.3.1, IDE Microsoft Visual Studio Code v 1.74.3, IDE Spyder v5.4.2, Google colab
##### В процессе работы обнаружено, что на представленном датасете рассчитанные по Кендаллу парные корреляции параметров содержат некоторые трудно объяснимые с физической точки зрения на композитный материал соотношения, когда наблюдаемая корреляция относительно велика там, где она должна быть низкой и относительно мала там, где она должна быть существенно выше. Например, модули упругости.  Их два и, чтобы в них был смысл, измеряться они должны одинаково - например вдоль волокон наполнителя. На нашем датасете оказалось низкое значение корреляции = 0.005458 для пары «Модуль упругости - Модуль упругости при растяжении» (если считать, что под термином «Модуль упругости» подразумевается модуль Юнга-модуль упругости при сжатии). 
##### Это  означает, что при изменении соотношения матрица-наполнитель модули упругости сжатия и растяжения ведут себя независимо друг от друга. Это возможно в том случае, если наполнитель (базальтовое волокно) влияет только на какой-то один параметр: либо на модуль упругости при сжатии (модуль Юнга), либо на модуль упругости при растяжении, то есть волокно “работает” либо на сжатие, либо на растяжение. Но тогда влияние угла нашивки на “модуль упругости”, либо на “модуль упругости при растяжении” тоже должно различаться, а коэффициенты корреляции по Кендаллу показывают наличие связи, хоть и обратной в одном из случаев: -0.031 и  0.022, (противоположные по знаку, но близкие по значению). Dрочем, метод Пирсона на тех же данных подобных аномалий не демонстрирует.