from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, TemplateView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _

from ilan.forms import IlanForm, CommentForm
from ilan.models import Ilan, Comment

class AnasayfaView(TemplateView):
    template_name = 'anasayfa.html'
    model = Ilan

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['ilanlar'] = Ilan.objects.filter(yayinlandimi=True)
        context['ilan_sayisi'] = Ilan.objects.all().count()
        return context

class IlanEkleView(LoginRequiredMixin, CreateView):
    form_class = IlanForm
    template_name = 'ilan_ekle.html'
    
    def get_initial(self):
        return {'user': self.request.user.id}

    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.user = self.request.user
        obj.save
        if self.request.POST.get('action') == 'Kaydet':
            return super().form_valid(form)
        ''' elif action == 'PREVIEW':
            preview = Ilan(
                baslik = form.cleaned_data['baslik'],
                metin = form.cleaned_data['metin'],
                )
            ctx = self.get_context_data(preview = preview)
            return self.render_to_response(context = ctx) '''
        return HttpResponseBadRequest()

class IlanUpdateView(LoginRequiredMixin, UpdateView):
    model = Ilan
    fields = ['baslik','metin','ilan_foto', 'ilan_fon_muzik', 'arkaplan_rengi', 'arkaplan_resmi']
    template_name = 'ilan_update_form.html'
    
class IlanListView(ListView):
    model = Ilan
    template_name = 'ilanlar.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['ilanlar'] = Ilan.objects.filter(yayinlandimi=True)
        context['ilan_sayisi'] = Ilan.objects.all().count()
        return context

class IlanDeleteView(LoginRequiredMixin, DeleteView):
    model = Ilan
    template_name = 'ilan_sil.html'
    success_url = reverse_lazy('dashboard')


def ilan_detail(request, pk):
    ilan = Ilan.objects.get(id=pk)
    yorumlar = ilan.yorumlar.filter(active=True)
    if ilan.mutluluk_dileyenler.filter(id=request.user.id).exists():
        begeni = 'btn-warning'
        begeni_kalp = 'fas'
    else:
        begeni = 'btn-success'
        begeni_kalp = 'far'
    new_comment = None
    if request.method == 'POST':
    # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.ilan = ilan
            # Save the comment to the database
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'ilan_goster.html', {
    'ilan': ilan, 
    'mutluluk_dileyen_sayisi': ilan.mutluluk_dileyenler.count(), 
    'yorumlar': yorumlar, 
    'new_comment': new_comment, 
    'comment_form': comment_form,
    'begeni': begeni,
    'begeni_kalp': begeni_kalp,
    })

@login_required
def mutluluk_dile(request, pk):
    ilan = Ilan.objects.get(id=pk)
    begeni = 'btn-success'
    begeni_kalp = 'far'
    if ilan.mutluluk_dileyenler.filter(id=request.user.id).exists():
        # eğer giriş yapan user bu ilanı beğenenlerde ise sil
        ilan.mutluluk_dileyenler.remove(request.user)
        begeni = 'btn-success'
        begeni_kalp = 'far'
        #ilanı begenenler arasında kullanıcı
    else: 
        # değilse bu ilanı beğenenlere ekle
        ilan.mutluluk_dileyenler.add(request.user)
        begeni = 'btn-warning'
        begeni_kalp = 'fas'
    data = {'mutluluk_dileyen_sayisi': ilan.mutluluk_dileyenler.count(), 
    'ilan_id': ilan.id, 
    'begeni': begeni, 
    'begeni_kalp': begeni_kalp
    }
    return JsonResponse(data)

''' @login_required
def yorum_ekle(request, pk):
    ilan = Ilan.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.save()
       
        if form.is_valid(): 
            print(form)
            yeni_yorum = form.save(commit = False)
            yeni_yorum.user = request.user
            yeni_yorum.save()
            ##ilan.yorumlar.create(user = request.user, yorum_metni = form.fields['yorum_metni'])
        else:
            yeni_yorum = ilan.yorumlar.create(user = request.user, yorum_metni = "lalalalala")
    data = {'yorum': yeni_yorum.yorum_metni }
    return JsonResponse(data) '''