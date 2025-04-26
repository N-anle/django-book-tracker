from django.shortcuts import render, redirect, get_object_or_404
from .models import BookRecord
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists():
            messages.error(request,'This user exists')
        else: 
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('login')

    return render(request,'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None: 
            login(request,user)
            messages.success(request, 'Welcome to your account')
            return redirect('all_books',username)
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

@login_required
def logout_view(request,username):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect ('login')

@login_required
def all_books(request, username):
    user = request.user
    query = request.GET.get('search_query')

    
    if query: 
        books = BookRecord.objects.filter(
            Q(title__icontains = query) | Q(author__icontains = query)
            )
    else: 
        books = BookRecord.objects.filter(user=user).order_by('created')

    context = {
        'books' : books,
        'search_query' : query
    }

    return render(request, 'all_books.html', context)

@login_required
def add_book(request,username):
    user = request.user
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        user = request.user
        rating = request.POST.get('rating')
        total_pages = request.POST.get('total_pages')
        current_page = request.POST.get('current_page')
        category = request.POST.get('category')


        try: 

            rating = int(rating)
            total_pages = int(total_pages)
            current_page = int(current_page)
            completed = (current_page == total_pages)

            book = BookRecord(
                user = user, 
                title = title,
                author = author,
                rating = rating,
                total_pages = total_pages,
                current_page = current_page,
                completed = completed,
                category = category
            )

            book.save()
            messages.success(request, 'Your book has been saved!')
            return redirect('all_books', user.username)
        
        except ValueError:
            messages.error(request, 'Your values are not compatible')
        
        
    return render(request, 'add_book.html')

@login_required
def edit_book(request, book_id):
    user = request.user
    book = get_object_or_404(BookRecord, id = book_id)
    if request.method == 'POST':
        book = get_object_or_404(BookRecord, id = book_id)

        title = request.POST.get('title')
        author = request.POST.get('author')
        user = request.user
        rating = request.POST.get('rating')
        total_pages = request.POST.get('total_pages')
        current_page = request.POST.get('current_page')
        category = request.POST.get('category')

        try: 
            rating = int(rating)
            total_pages = int(total_pages)
            current_page = int(current_page)
            completed = (total_pages == current_page)

            book.user = user
            book.title = title
            book.author = author
            book.rating = rating
            book.total_pages = total_pages
            book.current_page = current_page
            book.category = category
            book.completed = completed

            book.save()
            messages.success(request, "Your changes have been saved")
            return redirect ('all_books', user.username)

        except ValueError:
            messages.error(request, 'Could not save your changes')
            return redirect(request.META.get('HTTP_REFERER'))

    return render (request, 'edit_book.html', {'book' : book})


@login_required
def delete_book(request, book_id, username):
    book = get_object_or_404(BookRecord, id = book_id)
    book.delete()
    messages.success(request, 'Your book has been deleted')
    return redirect ('all_books')

@login_required
def category_search(request, category):
    books = BookRecord.objects.filter(category = category)
    return render(request,'category_view.html',{'books' : books})

@login_required
def user_profile(request,username):
    user = request.user
    books = BookRecord.objects.filter(user=user).order_by('created')
    currently_reading = books.filter(completed  = False)
    finished_reading = books.filter(completed = True)

    context = {
        'books' : books,
        'currently_reading' : currently_reading,
        'finished_reading' : finished_reading
    }


    return render(request, 'user_profile.html' , context)

@login_required
def edit_profile(request, username):
    user = request.user
    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_password = request.POST.get('password')

        if new_username and new_username != user.username:
            if User.objects.filter(username = new_username).exists():
                messages.error(request, 'This Username already exists')
            else: 
                user.username = new_username
            
        if new_password:
            user.set_password(new_password)

        messages.success(request, 'Your account has been edited')

        user.save()
        if new_password:
            return redirect('login')
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    

    return render(request, 'edit_profile.html')

@login_required
def book_details(request, book_id):
    book = get_object_or_404(BookRecord, id = book_id)
    context = {
        'book' : book
    }

    return render(request, 'book_detailed.html', context)