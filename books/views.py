from logging import exception
from django.shortcuts import render, redirect
from django.http import HttpResponse
from books.models import User, Book


def register(request):
    return render(request, 'register.html')


def postRegister(request):
    try:
        if(request.POST['name'] and request.POST["email"] and request.POST["password"]):
            form = User.objects.create(
                name=request.POST['name'], email=request.POST["email"], password=request.POST["password"])
            form.save()
            return render(request, 'register.html', {'msg': "Registered succesfully. Click on login"})
        else:
            return redirect('/register')
    except:
        return render(request, 'register.html', {'msg': "User already exists"})


def login(request):
    return render(request, 'login.html', {})


def post_login(request):
    if(request.method == "POST" and (request.POST["email"] and request.POST["password"])):
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            users = User.objects.get(email=email)
            if(users != "" and password == users.password):
                return redirect('/showBook')
            else:
                return render(request, 'login.html', {"msg": "wrong credentials"})
        except:
            return render(request, 'login.html', {"msg": "wrong credentials"})

    else:
        return render(request, 'login.html')


def createBook(request):
    return render(request, 'createBook.html')


def postBook(request):
    if(request.method == "POST"):
        if(request.POST['bookname'] and request.POST["author"] and request.POST["publications"]):
            form = Book.objects.create(
                book_name=request.POST['bookname'], author=request.POST["author"], publications=request.POST["publications"])
            form.save()
            return redirect('/showBook')
        else:
            msg = "Please enter details"
            return render(request, 'createBook.html', {"msg": msg})
    else:
        return render(request, 'createBook.html')


def showBook(request):
    books = Book.objects.all()
    return render(request, 'show.html', {"books": books})


def editBook(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'edit.html', {'book': book})


def updateBook(request, id):
    book = Book.objects.filter(id=id).update(
        book_name=request.POST['bookname'], author=request.POST["author"], publications=request.POST["publications"])

    return redirect('/showBook')


def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/showBook')
