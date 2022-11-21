from ejemplo.models import Vivienda

Vivienda(nombre="Nueva", habitaciones="1", tipo_casa="Casa", banos="1", descripcion="Algo").save()


print(Vivienda.objects.all())
#from blog.models import Post

#Post(title="Mi post", short_content="un post", content="sadljalsjdlkajsdljasljdlaksjd").save()
#Post(title="Mi post", short_content="un post", content="sadljalsjdlkajsdljasljdlaksjd").save()
#Post(title="Mi post", short_content="un post", content="sadljalsjdlkajsdljasljdlaksjd").save()
#Post(title="Mi post", short_content="un post", content="sadljalsjdlkajsdljasljdlaksjd").save()

#print(Post.objects.all())

