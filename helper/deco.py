from django.contrib.auth.decorators import user_passes_test




def chech_user(user):
    return not user.is_authenticated

user_logout = user_passes_test(chech_user,'/',None)


def auth_user_not_to_access(viewfunc):
    return user_logout(viewfunc)