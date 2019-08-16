from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import *
from django.conf import settings

'''
    # Imports libs Ontologias
    from owlready2 import *
    #Setando o diretorio das ontologias
    onto_path.append(settings.BASE_DIR+"/ontologys/")
    #Carregando as ontologias
    autismo_ontology = get_ontology("DSMV_Autism_XML_RDF.owl") 
    autismo_ontology.load()
    strategy_ontology = get_ontology("LearningStrategy_XML_RDF.owl") 
    strategy_ontology.load()

    print("\n")

    # Listar Instacias de classes e subclasses
    for i in autismo_ontology.DSMV_Autism_Definition.instances(): print(i)

    #destroy_entity(autismo_ontology.Nome_do_individuo)
    print("\n")

    #test_individuo = autismo_ontology.DSMV_Autism_Definition("Nome_do_individuo")
    #autismo_ontology.save()
'''

def index(request):
    return HttpResponse("autismo_ontology")