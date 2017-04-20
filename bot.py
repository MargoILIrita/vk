import vk_api

_homework = {'ту': "homework",'англ божидар': "homework"}



#перезапись
def rewritehomework(lesson, homework):
    _homework[lesson] = homework
    return "Спасибо, котик"

#выдача нового дз
def givehomework(lessson):
    try: _homework[lessson]
    except BaseException:
        return "Там какая-то дрисня"
    return "Последнее сохраненное дз по {0}: {1}".format(lessson, _homework[lessson])


#формирвание массива - строки дз
def makestring(arg):
    s = "" + arg
    s = s.split(" ")
    if "англ" in s[1]:
        if "божидар" in s[2]:
            return ["англ божидар", " ".join(s[3:])]
        else:
            return ["англ вера", " ".join(s[3:])]
    return [s[1], " ".join(s[2:])]


#анализ входного сообщения
def analyzehomework(arg):
    s = "" + arg
    if s.startswith("записать"):
        res = makestring(s)
        return rewritehomework(res[0], res [1])
    if s.startswith("новый"):
        res = makestring(s)
        return rewritehomework(res[0], res[1])
    return givehomework(s)


while True:
    s = input()
    print(analyzehomework(s))
