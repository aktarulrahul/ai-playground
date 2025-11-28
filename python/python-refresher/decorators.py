from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# say_hello()
# print(say_hello.__name__)  # Output: wrapper

# --------------------------------------------------------------------------
# Login Decorator Example
def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Logging activity for function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Activity logged for function: {func.__name__}")
        return result
    return wrapper


@log_activity
def user_login(username):
    print(f"User {username} has logged in.")
    return True

# user_login("alice")
# user_login("bob")
# --------------------------------------------------------------------------
# Admin Access Decorator Example
def require_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        # user is the first positional argument
        if not user.get("is_admin"):
            print("❌ Access denied. Admins only.")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@require_admin
def access_admin_panel(user):
    print(f"Welcome to the admin panel, {user['username']}!")
    return "Access Granted"

admin_user = access_admin_panel({"username": "admin", "is_admin": True})
regular_user = access_admin_panel({"username": "user", "is_admin": False})

print(admin_user)    # Should grant access
print(regular_user)  # Should deny access
# --------------------------------------------------------------------------