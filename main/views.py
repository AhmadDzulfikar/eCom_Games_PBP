from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name_owner': 'Ahmad Dzulfikar As Shavy',
        'class': 'PBP D',

        'title': 'DZOELFIEKAR GAME STORE',
        'name': 'Flappy Box',
        'price' : '24',
        'Description': 'The game is inspired by the classical Chinese novel Journey to the West and follows an anthropomorphic monkey based on the character of Sun Wukong from the novel.'
    }

    return render(request, "main.html", context)