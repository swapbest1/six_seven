def find_six_seven(stroka):
    cnt = 0
    for i in range(len(stroka)):
        if stroka[i] == '6' and stroka[i+1] == '7':
            cnt += 1
            print(f'сикс севен найден на координатах {i+1} {i+2}')
    if cnt > 0:
        print(f'найдено {cnt} сикс севен')
    else:
        print('сикс севен не найден :(')
a = '63485367079458396785097836745645654667453536456797856758546567'
find_six_seven(a)
        