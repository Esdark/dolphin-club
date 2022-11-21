from django.http import JsonResponse
from django.views.generic import TemplateView,View
from .models import (AgeMaster,MaterialMaster,ProductMaster,ProductAgeWiseList)

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class ProductsView(TemplateView):
    template_name = "products.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GalleryPageView(TemplateView):
    template_name = "gallery.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallerycontents'] = GalleryPageMaster.objects.filter(display='Y').order_by('displayorder')
        # try:
        #     context['photo'] = HomePageMaster.objects.all()[0]
        # except:
        #     pass
        return context


class CollectionView(TemplateView):
    template_name = "collection.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materials'] = MaterialMaster.objects.filter(hide='N').values('materialid','materialname').order_by('position')
        context['agefilter'] = AgeMaster.objects.filter(hide='N').values('ageid','description').order_by('position')
        return context
from django.template.loader import render_to_string
class ProductListView(View):
    template_name = "collection.html"
    def post(self, request):
        context = {}
        productlist = ProductAgeWiseList.objects.values('productid','productid__productid','productid__name','productid__productimage')
        materiallist = request.POST.getlist('materials[]')  
        agelist = request.POST.getlist('agegroup[]')  
        if materiallist:
            productlist = productlist.filter(productid__material__in = materiallist) 
        if agelist:
            productlist = productlist.filter(age__in = agelist) 

        context = {
            'productlist':productlist.distinct()
        }       
        html = render_to_string('render/product-list.html', context)
        return JsonResponse({'STATUS':1,'html':html})

class ProductInfoView(TemplateView):
    template_name = "productinfo.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            context['product'] = ProductMaster.objects.filter(productid=self.request.GET.get('product')).values('productid','name','Description','material','productimage','price')[0]
        except:
            pass
        # context['materials'] = MaterialMaster.objects.filter(hide='N').values('materialid','materialname').order_by('position')
        # context['agefilter'] = AgeMaster.objects.filter(hide='N').values('ageid','description').order_by('position')
        return context

class ContactPageView(TemplateView):
    template_name = "contactpage.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
class AboutPageView(TemplateView):
    template_name = "aboutpage.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context