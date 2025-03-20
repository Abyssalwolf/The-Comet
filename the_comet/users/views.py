from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomerUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        org_name = request.POST.get('org')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the email already exists
        if CustomerUser.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})

        if password == confirm_password:
            # Create the user
            user = CustomerUser.objects.create_user(
                email=email,
                org_name=org_name,
                password=password
            )

            # Authenticate the user to get the backend
            user = authenticate(request, username=email, password=password)
            if user is not None:
                # Set the backend attribute explicitly
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)  # Log the user in
                return redirect('dashboard')  # Redirect to the dashboard
            else:
                # Handle authentication failure
                return render(request, 'register.html', {'error': 'Authentication failed'})
        else:
            # Handle password mismatch error
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    
    # Render the registration form for GET requests
    return render(request, 'register.html')

def custom_logout(request):
    logout(request)  # Log the user out
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')