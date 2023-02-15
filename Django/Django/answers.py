from django.shortcuts import redirect, render
from Django.models import PersonalityTest

obj = PersonalityTest()

def answer1(id):
    global obj
    if (id == 11):
        obj.superhero_scores['Superman'] += 3
        obj.superhero_scores['Spiderman'] += 2
        obj.superhero_scores['Wonder Woman'] += 1
    elif (id == 12):
        obj.superhero_scores['Iron Man'] += 3
        obj.superhero_scores['Batman'] += 2
        obj.superhero_scores['Captain America'] += 1
    elif (id == 13):
        obj.superhero_scores['Thor'] += 3
        obj.superhero_scores['Black Widow'] += 2
        obj.superhero_scores['Hawkeye'] += 1
    elif (id == 14):
        obj.superhero_scores['Black Panther'] += 3
        obj.superhero_scores['Captain Marvel'] += 2
        obj.superhero_scores['Ant-Man'] += 1
    elif (id == 15):
        obj.superhero_scores['Doctor Strange'] += 3
        obj.superhero_scores['Scarlet Witch'] += 2
        obj.superhero_scores['Vision'] += 1
    return redirect('page3')

def answer2(id):
    global obj
    if (id == 21):
        obj.superhero_scores['Superman'] += 3
        obj.superhero_scores['Captain America'] += 2
        obj.superhero_scores['Wonder Woman'] += 1
    elif (id == 22):
        obj.superhero_scores['Batman'] += 3
        obj.superhero_scores['Iron Man'] += 2
        obj.superhero_scores['Spiderman'] += 1
    elif (id == 23):
        obj.superhero_scores['Thor'] += 2
        obj.superhero_scores['Black Widow'] += 1
        obj.superhero_scores['Hawkeye'] += 3
    elif (id == 24):
        obj.superhero_scores['Black Panther'] += 2
        obj.superhero_scores['Captain Marvel'] += 1
        obj.superhero_scores['Ant-Man'] += 3
    elif (id == 25):
        obj.superhero_scores['Doctor Strange'] += 2
        obj.superhero_scores['Scarlet Witch'] += 1
        obj.superhero_scores['Vision'] += 3
    return redirect('page4')

def answer3(id):
    global obj
    if (id == 31):
        obj.superhero_scores['Spiderman'] += 3
        obj.superhero_scores['Superman'] += 2
        obj.superhero_scores['Captain America'] += 1
    elif (id == 32):
        obj.superhero_scores['Batman'] += 3
        obj.superhero_scores['Iron Man'] += 2
        obj.superhero_scores['Wonder Woman'] += 1
    elif (id == 33):
        obj.superhero_scores['Thor'] += 1
        obj.superhero_scores['Black Widow'] += 3
        obj.superhero_scores['Hawkeye'] += 2
    elif (id == 34):
        obj.superhero_scores['Black Panther'] += 1
        obj.superhero_scores['Captain Marvel'] += 3
        obj.superhero_scores['Ant-Man'] += 2
    elif (id == 35):
        obj.superhero_scores['Doctor Strange'] += 1
        obj.superhero_scores['Scarlet Witch'] += 3
        obj.superhero_scores['Vision'] += 2
    return redirect('page5')

def answer4(id):
    global obj
    if (id == 41):
        obj.superhero_scores['Wonder Woman'] += 3
        obj.superhero_scores['Captain America'] += 2
        obj.superhero_scores['Spiderman'] += 1
    elif (id == 42):
        obj.superhero_scores['Iron Man'] += 3
        obj.superhero_scores['Batman'] += 2
        obj.superhero_scores['Superman'] += 1
    elif (id == 43):
        obj.superhero_scores['Thor'] += 3
        obj.superhero_scores['Black Widow'] += 2
        obj.superhero_scores['Hawkeye'] += 1
    elif (id == 44):
        obj.superhero_scores['Black Panther'] += 3
        obj.superhero_scores['Captain Marvel'] += 2
        obj.superhero_scores['Ant-Man'] += 1
    elif (id == 45):
        obj.superhero_scores['Doctor Strange'] += 3
        obj.superhero_scores['Scarlet Witch'] += 2
        obj.superhero_scores['Vision'] += 1
    return redirect('page6')

def answer5(id):
    global obj
    if (id == 51):
        obj.superhero_scores['Wonder Woman'] += 3
        obj.superhero_scores['Captain America'] += 2
        obj.superhero_scores['Spiderman'] += 1
    elif (id == 52):
        obj.superhero_scores['Iron Man'] += 3
        obj.superhero_scores['Batman'] += 2
        obj.superhero_scores['Superman'] += 1
    elif (id == 53):
        obj.superhero_scores['Thor'] += 2
        obj.superhero_scores['Black Widow'] += 1
        obj.superhero_scores['Hawkeye'] += 3
    elif (id == 54):
        obj.superhero_scores['Black Panther'] += 2
        obj.superhero_scores['Captain Marvel'] += 1
        obj.superhero_scores['Ant-Man'] += 3
    elif (id == 55):
        obj.superhero_scores['Doctor Strange'] += 2
        obj.superhero_scores['Scarlet Witch'] += 1
        obj.superhero_scores['Vision'] += 3
    return redirect('page7')

def answer6(id):
    global obj
    if (id == 61):
        obj.superhero_scores['Spiderman'] += 3
        obj.superhero_scores['Wonder Woman'] += 2
        obj.superhero_scores['Superman'] += 1
    elif (id == 62):
        obj.superhero_scores['Iron Man'] += 3
        obj.superhero_scores['Batman'] += 2
        obj.superhero_scores['Captain America'] += 1
    elif (id == 63):
        obj.superhero_scores['Thor'] += 1
        obj.superhero_scores['Black Widow'] += 3
        obj.superhero_scores['Hawkeye'] += 2
    elif (id == 64):
        obj.superhero_scores['Black Panther'] += 1
        obj.superhero_scores['Captain Marvel'] += 3
        obj.superhero_scores['Ant-Man'] += 2
    elif (id == 65):
        obj.superhero_scores['Doctor Strange'] += 1
        obj.superhero_scores['Scarlet Witch'] += 3
        obj.superhero_scores['Vision'] += 2
    return redirect('page8')

def answer7(id):
    global obj
    if (id == 71):
        obj.superhero_scores['Superman'] += 3
        obj.superhero_scores['Captain America'] += 2
        obj.superhero_scores['Wonder Woman'] += 1
    elif (id == 72):
        obj.superhero_scores['Batman'] += 3
        obj.superhero_scores['Iron Man'] += 2
        obj.superhero_scores['Spiderman'] += 1
    elif (id == 73):
        obj.superhero_scores['Thor'] += 3
        obj.superhero_scores['Black Widow'] += 2
        obj.superhero_scores['Hawkeye'] += 1
    elif (id == 74):
        obj.superhero_scores['Black Panther'] += 3
        obj.superhero_scores['Captain Marvel'] += 2
        obj.superhero_scores['Ant-Man'] += 1
    elif (id == 75):
        obj.superhero_scores['Doctor Strange'] += 3
        obj.superhero_scores['Scarlet Witch'] += 2
        obj.superhero_scores['Vision'] += 1
    return redirect('page9')

def answer8(id):
    global obj
    if (id == 81):
        obj.superhero_scores['Wonder Woman'] += 3
        obj.superhero_scores['Spiderman'] += 2
        obj.superhero_scores['Superman'] += 1
    elif (id == 82):
        obj.superhero_scores['Iron Man'] += 3
        obj.superhero_scores['Batman'] += 2
        obj.superhero_scores['Captain America'] += 1
    elif (id == 83):
        obj.superhero_scores['Thor'] += 2
        obj.superhero_scores['Black Widow'] += 1
        obj.superhero_scores['Hawkeye'] += 3
    elif (id == 84):
        obj.superhero_scores['Black Panther'] += 2
        obj.superhero_scores['Captain Marvel'] += 1
        obj.superhero_scores['Ant-Man'] += 3
    elif (id == 85):
        obj.superhero_scores['Doctor Strange'] += 2
        obj.superhero_scores['Scarlet Witch'] += 1
        obj.superhero_scores['Vision'] += 3
    return redirect('page10')

def answer9(id):
    global obj
    if (id == 91):
        obj.superhero_scores['Captain America'] += 3
        obj.superhero_scores['Superman'] += 2
        obj.superhero_scores['Wonder Woman'] += 1
    elif (id == 92):
        obj.superhero_scores['Batman'] += 3
        obj.superhero_scores['Iron Man'] += 2
        obj.superhero_scores['Spiderman'] += 1
    elif (id == 93):
        obj.superhero_scores['Thor'] += 1
        obj.superhero_scores['Black Widow'] += 3
        obj.superhero_scores['Hawkeye'] += 2
    elif (id == 94):
        obj.superhero_scores['Black Panther'] += 1
        obj.superhero_scores['Captain Marvel'] += 3
        obj.superhero_scores['Ant-Man'] += 2
    elif (id == 95):
        obj.superhero_scores['Doctor Strange'] += 1
        obj.superhero_scores['Scarlet Witch'] += 3
        obj.superhero_scores['Vision'] += 2
    return redirect('page11')

def answer10(id):
    global obj
    if (id == 101):
        obj.superhero_scores['Spiderman'] += 3
        obj.superhero_scores['Wonder Woman'] += 2
        obj.superhero_scores['Superman'] += 1
    elif (id == 102):
        obj.superhero_scores['Iron Man'] += 3
        obj.superhero_scores['Batman'] += 2
        obj.superhero_scores['Captain America'] += 1
    elif (id == 103):
        obj.superhero_scores['Thor'] += 3
        obj.superhero_scores['Black Widow'] += 2
        obj.superhero_scores['Hawkeye'] += 1
    elif (id == 104):
        obj.superhero_scores['Black Panther'] += 3
        obj.superhero_scores['Captain Marvel'] += 2
        obj.superhero_scores['Ant-Man'] += 1
    elif (id == 105):
        obj.superhero_scores['Doctor Strange'] += 3
        obj.superhero_scores['Scarlet Witch'] += 2
        obj.superhero_scores['Vision'] += 1
    return redirect('result')

def result(request):
    global obj
    context = {
        'hero': obj.assign_superhero(),
        'img': obj.assign_image()
    }
    return render(request, 'result.html', context)