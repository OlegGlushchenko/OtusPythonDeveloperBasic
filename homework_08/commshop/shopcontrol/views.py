from django.shortcuts import render


# Create your views here.
def main_page(request):
    context = {
        'category': [
            {'deals': 'Договоры'},
            {'products': 'Товары'},
        ],
    }
    return render(request, 'shopcontrol/index.html', context=context)
