from django.shortcuts import render
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Personagem, Objeto_er, Objeto_er_map, Jogador
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test


def index(request):
    contexto = {}
    Personagem.objects.get_or_create(
        descricao="Moeda Dourada", prefab="MoedaDourada")
    Objeto_er.objects.get_or_create(personagem=Personagem.objects.first())
    return render(request, 'website_app/index.html', contexto)


def login_staff_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_staff,
        login_url="/",
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def Jogadores(request):
    jogadores = Jogador.objects.all()
    lista = []
    for i in jogadores:
        try:
            lista.append([float(i.longitude.replace(',', '.')),
                          float(i.latitude.replace(',', '.'))])
        except BaseException:
            pass
    contexto = {
        "jogadores": Jogador.objects.all(),
        "lista_js": lista
    }
    return render(request, 'website_app/jogadores.html', contexto)


class JogadorCreate(CreateView):
    model = Jogador
    fields = '__all__'
    template_name = 'website_app/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_active_jogador'] = "active"
        return context


class JogadorUpdateView(UpdateView):
    model = Jogador
    fields = '__all__'
    template_name = 'website_app/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_active_jogador'] = "active"
        return context


class JogadorDeleteView(DeleteView):
    model = Jogador
    success_url = reverse_lazy('website_app:Jogadores')
    template_name = 'website_app/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_active_jogador'] = "active"
        return context


def Objeto_ers(request):
    contexto = {
        "lista": Objeto_er.objects.all(),
    }
    contexto["item_active_objeto_er"] = "active"
    return render(request, 'website_app/objeto_ers.html', contexto)


class Objeto_erCreate(CreateView):
    model = Objeto_er
    fields = '__all__'
    template_name = 'website_app/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_active_objeto_er'] = "active"
        return context


class Objeto_erUpdateView(UpdateView):
    model = Objeto_er
    fields = '__all__'
    template_name = 'website_app/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_active_objeto_er'] = "active"
        return context


class Objeto_erDeleteView(DeleteView):
    model = Objeto_er
    success_url = reverse_lazy('website_app:Objeto_ers')
    template_name = 'website_app/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_active_objeto_er'] = "active"
        return context


# ---------- Objeto_er_maps ---------------------------------------------------


def Objeto_er_maps(request):
    objeto_er_maps = Objeto_er_map.objects.all()
    lista = []
    for i in objeto_er_maps:
        lista.append(
            [
                float(i.longitude.replace(',', '.')),
                float(i.latitude.replace(',', '.'))
            ]
        )
    contexto = {
        "lista": Objeto_er_map.objects.all(),
        "lista_js": lista
    }
    contexto["item_active_objeto_er_map"] = "active"
    # return HttpResponse(lista)
    return render(request, 'website_app/objeto_er_maps.html', contexto)


class Objeto_er_mapCreate(CreateView):
    model = Objeto_er_map
    fields = '__all__'
    template_name = 'website_app/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_active_objeto_er_map'] = "active"
        return context


class Objeto_er_mapUpdateView(UpdateView):
    model = Objeto_er_map
    fields = '__all__'
    template_name = 'website_app/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_active_objeto_er_map'] = "active"
        return context


class Objeto_er_mapDeleteView(DeleteView):
    model = Objeto_er_map
    success_url = reverse_lazy('website_app:Objeto_er_maps')
    template_name = 'website_app/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_active_objeto_er_map'] = "active"
        return context
