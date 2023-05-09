from django.shortcuts import render
from django.shortcuts import redirect

def party(request):
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScHjksqOaBXrBiPuGtu6W5v1tSK9NE_YJr9xjjTkINkhQR9lA/viewform?usp=sf_link")

def simple_page(template):
    def handler(request):
        context = {}
        return render(request,template,context)
    return handler

def main(request):
    """View function for home page of site."""

    context = {
        'faq' : [
            {
                'q' : 'quesiton1',
                'a' : 'question2',
             },
            {
                'q' : 'quesiton1',
                'a' : 'question2',
             },
        ]
#        'num_books': num_books,
#        'num_instances': num_instances,
#        'num_instances_available': num_instances_available,
#        'num_authors': num_authors,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    

