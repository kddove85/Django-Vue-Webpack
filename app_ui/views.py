from . import models
# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class IndexView(TemplateView):
    def get(self, request):
        # if request.GET.get('login_required'):
        #     messages.error(request, 'Please log in to continue')

        # if request.user.is_authenticated or request.path == '/':
            return render(request, 'app_ui/index.html')
        # else:
        #     return redirect('portal_ui:home')
