from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from ilan.models import Ilan, Comment
from django.shortcuts import render


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('anasayfa')
    template_name = 'registration/login.html'
    authenticated_redirect_url = "/2"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        paspsword = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

class LogOutView(LoginRequiredMixin, generic.RedirectView):
    url = reverse_lazy('anasayfa')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Yeni bir User nesnesi olustur
            new_user = user_form.save(commit=False)
            # sifreyi yenile
            new_user.set_password(user_form.cleaned_data['password'])
            # User nesnesini kaydet
            new_user.save()
            # Kullanıcı Profili olustur
            Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'user_form': user_form})


@login_required
def dashboard(request):
    if 0:
        print(request.user.ilan)
        ilanim = Ilan.objects.filter(user=request.user)
        yorum_ilan = {'ilanim': ilanim,
                'yorumlarim': Comment.objects.filter(user=request.user),
                'ilanima_yorumlar': Comment.objects.filter(ilan = request.user.ilan),
                'mutluluk_dilediklerim': Ilan.objects.filter(mutluluk_dileyenler = request.user),
                'mutluluk_dileyenler': User.objects.filter(mutluluk_dilenen_ilan = request.user.ilan)
                }
    else:
        yorum_ilan = {
                'yorumlarim': Comment.objects.filter(user=request.user),
                'mutluluk_dilediklerim': Ilan.objects.filter(mutluluk_dileyenler = request.user),
                }
    return render(request, 'registration/dashboard.html', yorum_ilan)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'registration/edit.html', {'user_form': user_form, 'profile_form': profile_form})
