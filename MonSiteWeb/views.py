from django.shortcuts import render, get_object_or_404
from MonSiteWeb.models import Articles
import json 
from django.core.paginator import Paginator, EmptyPage

def index(request,page=1):
	articles=Articles.objects.all()

	paginator = Paginator(articles,1)
	try:

        # La définition de nos URL autorise comme argument « page » uniquement 

        # des entiers, nous n'avons pas à nous soucier de PageNotAnInteger

		articles = paginator.page(page)

	except EmptyPage:

        # Nous vérifions toutefois que nous ne dépassons pas la limite de page

        # Par convention, nous renvoyons la dernière page dans ce cas

		articles = paginator.page(paginator.num_pages)
	return render(request,'MonSiteWeb/index.html',{'articles':articles})

"""
def index(request):
	TOTAL = 2
	OFFSET = request.GET.get('offset', 0)
	END = OFFSET + TOTAL
	articles=Articles.objects.all()[OFFSET:END]
	data = []
	for article in articles:
		data.append({'title': article.titre,
			'contenu': article.contenu})

	#data = json.dumps(json_list)
	return render(request,'MonSiteWeb/index.html',data)
def index(request):
	TOTAL = 1
	OFFSET = request.GET.get('offset', 0)
	END = OFFSET + TOTAL
	articles = Articles.objects.all()[OFFSET:END]
	json_list = []
	for article in articles:
		json_list.append({'title': article.titre,
			'contenu': article.contenu})

	data = json.dumps(json_list)

	return HttpResponse(data, content_type='application/json')
"""
def about(request):
	return render(request,'MonSiteWeb/about.html',locals())

def post(request,id,slug):
	article = get_object_or_404(Articles,id=id, slug=slug)
	return render(request,'MonSiteWeb/post.html',{'article':article})

def contact(request):
	return render(request,'MonSiteWeb/contact.html',locals())