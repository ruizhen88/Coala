from django.shortcuts import render

def play(request):
    return render(request, 'play.html')

def profile(request):
    return render(request, 'profile.html')

count = 0

def play2(request):
    jungyejin = '정예진'
    age = 26

    global count # 바깥영역의 변수를 사용할 때 global
    count = count +1 # 접속할 때마다 방문자 1 증가

    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    if count == 7:
        event = '당첨!'
    else:
        event = '꽝...'

    post = ['오늘은 날씨 맑음', '미세먼지 심한 날', '비 심하게 옴']

    return render(request, 'play2.html', {'name': jungyejin, 'diary': post, 'event': event, 'cnt': count, 'age': status})

def fail(request):
    return render(request, 'fail.html')

def help(request):
    return render(request, 'help.html')

def warn(request):
    return render(request, 'warn.html')

def newsfeed(request):
    return render(request, 'newsfeed.html')
