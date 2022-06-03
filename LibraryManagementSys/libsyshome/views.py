from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from libsyshome.models import Books
# Create your views here.

#HOME PAGE BACKEND
def home(request):
    databasebooks = []
    books = Books.objects.values("book_title","desc","image","id")
    for i in books:
        databasebooks.append(i)
    context = {
        "books" : databasebooks
    }
    if request.user.is_superuser:
        return render(request, 'libhome/home.html', context)
    elif request.user.is_authenticated:
        return render(request, 'libhome/home.html', context)
    else:
        messages.warning(request,"Please LogIn first to visit LibSys")
        return redirect('signin')

#STUDENTS AND ADMIN LOGIN/LOGOUT BACKEND

#SIGNUP
def signup(request):
    if request.method == 'POST':
        username = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            return redirect('signin')

        if User.objects.filter(email=email):
            messages.warning(request,"Email already exists !!!")
            return redirect('signin')

        if "@" not in username:
            messages.warning(request,"Enter a valid Email")
            return redirect('signin')

        if pass1!=pass2:
            messages.warning(request,"Passwords didn't match !!!")
            return redirect('signin')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        return redirect('signin')

    return  render(request, 'libhome/signup.html')

#SIGNIN
def signin(request):
    if request.method == 'POST':
        username = request.POST['email']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Wrong Credentials. PassWord or Username is Case Sensitive")
            return redirect('signin')

    return render(request, 'libhome/signin.html')

#SIGNOUT
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('signin')

#ADMIN CRUD BACKEND

#ADD BOOKS
def addbooks(request):
    if request.method == 'POST':
        title = request.POST['book_title']
        desc = request.POST['desc']
        image = request.FILES['image']
        book_pdf = request.FILES['book_pdf']
    
        addbook = Books(book_title=title,desc=desc,image=image,book_pdf=book_pdf)
        addbook.save()
        return redirect('home')
    return render(request, "libhome/addbooks.html")

#UPDATE BOOKS
def updatebooks(request, id):
    if request.method == "POST" :
        book = Books.objects.get(id=id)
        book.book_title = request.POST['book_title']
        book.desc = request.POST['desc']
        book.image = request.FILES['image']
        book.save()
        return redirect('home')
    book = Books.objects.get(id=id)
    context = {
        "book" : book
    }
    return render(request, "libhome/updatebooks.html",context)

#DELETE BOOKS
def deletebooks(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect("home")