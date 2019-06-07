from django.shortcuts import render

def HOME(request):
    return render(request, 'home.html')

def ABOUT(request):
    return render(request, 'about.html')

def RESULT(request):
    text = request.GET['fulltext']   
    words = text.split ()
    word_count = {}

    

        
   
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1

    return render(request, 'result.html', {
        'full' : text, 
        'total' : len(words),
        'count' : word_count.items(), 
        'letter' : len(text),
        'space' : len(text.replace('\n','').replace(' ',''))
    })


