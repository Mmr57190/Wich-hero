from django.shortcuts import render
from Django.models import PersonalityTest 
from Django.answers import answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10

def process_answer(request, id):
    if (id // 10 == 1):
        return answer1(id)
    elif (id // 10 == 2):
        return answer2(id)
    elif (id // 10 == 3):
        return answer3(id)
    elif (id // 10 == 4):
        return answer4(id)
    elif (id // 10 == 5):
        return answer5(id)
    elif (id // 10 == 6):
        return answer6(id)
    elif (id // 10 == 7):
        return answer7(id)
    elif (id // 10 == 8):
        return answer8(id)
    elif (id // 10 == 9):
        return answer9(id)
    elif (id // 10 == 10):
        return answer10(id)

def home_page(request):
    return render(request, 'home.html')

def page_2(request):
    return render(request, 'page_2.html')

def page_3(request):
    return render(request, 'page_3.html')

def page_4(request):
    return render(request, 'page_4.html')

def page_5(request):
    return render(request, 'page_5.html')

def page_6(request):
    return render(request, 'page_6.html')

def page_7(request):
    return render(request, 'page_7.html')

def heros(request):
    obj = PersonalityTest()
    context = {
        'heros': zip(obj.all(), obj.img_path())
    };
    return render(request, 'heros.html', context)

def page_8(request):
    return render(request, 'page_8.html')

def page_9(request):
    return render(request, 'page_9.html')

def page_10(request):
    return render(request, 'page_10.html')

def page_11(request):
    return render(request, 'page_11.html')

def segv(request):
    return render(request, 'segv.html')

def trap(request):
    return render(request, 'trap.html')

def cs(request):
    return render(request, 'cs.html')

def res_cs(request):
    return render(request, 'res_cs.html')
