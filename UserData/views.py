from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostFormDetail
from django.views import View as djviews
from .models import UserDataDetail,MultipleImg
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

@method_decorator(login_required, name='dispatch')
class DisplayImages(ListView):
    # template_name = 'pic.html'

    def get(self, request):
        User_list = UserDataDetail.objects.filter(user=request.user)
        # User_Data =UserTitle.objects.filter(user=self.request.user)

        return render(self.request, 'pic.html', {'data':User_list })


class UserDataDet(CreateView):
    model = UserDataDetail
    fields = ['user','title', 'description','image']

    # template_name = 'details.html'
    # select_related = ("user","title", "description","image")
    # # return queryset.filter(user_id=self.request.user.id)

    def get(self, request,pk):
        detail = UserDataDetail.objects.get(id=pk)
        return render(request,'details.html',{'detail':detail})


@method_decorator(login_required, name='dispatch')
class BasicUploadView(djviews):
    def get(self, request):
        User_Data =PostFormDetail()
        return render(self.request, 'data.html', {'data':User_Data })

    def post(self, request,):
        form = PostFormDetail(self.request.POST,self.request.FILES)
        pic = request.FILES.getlist('image')
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            for i in pic:
                pictures = MultipleImg(name = form, picture= i)
                pictures.save()

            return redirect('home')


class UserDetailUpdate(UpdateView): 
    model = UserDataDetail
    success_url = reverse_lazy('home') 
    fields = ['title', 'description','image']


class UserDetailDelete(DeleteView): 
    model = UserDataDetail
    success_url = reverse_lazy('home')



# def DisplayImages(request):
#     if request.method == 'GET':
#         form = PostData.objects.all()
#         return render(request, 'pic.html',{'form': form})

################


# def productpage(request, product_image_id):
#     product = get_object_or_404(Image, product_image=product_image_id)        stack
#     render(request, 'polls/productpage.html', {'product': product})

# class Product(models.Model):
#     product_name = models.CharField(max_length=200)
#     product_description = models.TextField()
#     def __unicode__(self):
#         return self.product_name

# class Image(models.Model):
#     product_image = models.ForeignKey(Product)
#     image = models.ImageField(upload_to='image')

# <h1>{{ product.product_name }}</h1>
# <br>
# {{ product.product_description  }}
# <br>
# {{ product.image.url }}


# def productpage(request, product_image_id):
#     product = get_object_or_404(Product, pk=product_image_id) error
#     render(request, 'polls/productpage.html', {'product': product})

###########






    # def get_queryset(self,**kwargs):
    #     return PostFormDetail.objects.all()



# def PostData(request):
#     form = PostFormDetail()
#     if request.method == 'POST':
#         form = PostFormDetail(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#
#             return redirect('home')
#     else:
#         return render(request,'data.html', {'form' : form})
#



# 1 more
# class UserProfile(models.Model):
#   user = models.OneToOneField(User, related_name='uploaded_by')
#   names = models.CharField(max_length=40)
#   lastname = models.CharField(max_length=50)
#   email = models.EmailField()


# class UserFiles(models.Model):
#   user = models.ForeignKey(UserProfile)
#   file = models.FileField(upload_to= 'blablabla')

# 1 more
# profile, created = UserProfile.objects.get_or_create(user=request.user)
# form = UserProfileForm(
#     requst.POST,
#     requst.FILES,
#     instance=profile
# )
# 1 more
# form = UserProfileForm(
#    requst.POST,
#    requst.FILES,
#    instance=UserProfile(user=self.request.user)
# )

#   <h1>Django Image Uploading</h1>
# <ul>
#   {% for post in object_list %}
#     <h2>{{ post.title }}</h2>
#     <img src="{{ post.cover.url}}" alt="{{ post.title }}">
#   {% endfor %}
# </ul>

# @login_required
# def PostData(request):
#     ImageFormSet = modelformset_factory(PostData,form=PostFormDetail)
#  #   'extra' means the number of photos that you can upload

#     if request.method == 'POST':

#         postForm = PostFormDetail(request.POST)
        
#         if postForm.is_valid() and formset.is_valid():
#             post_form = postForm.save(commit=False)
#             post_form.user = request.user
#             post_form.save()

#             for form in formset.cleaned_data:
#                 #this helps to not crash if the user
#                 #do not upload all the photos
#                 if form:
#                     title = form['title']
#                     body = form['body']
#                     image = form['image']
#                     file = form['file']
#                     photo = PostData(title=title,body=body,image=image,file=file)
#                     photo.save()
#             messages.success(request,"Yeeew, check it out on the home page!")
#             return HttpResponseRedirect("/")
#         else:
#             print(postForm.errors, formset.errors)
#     else:
#         postForm = PostData()
#         # formset = ImageFormSet(queryset=Images.objects.none())
#         return render(request, 'index.html',{'postForm': postForm})
            # course = form.cleaned_data.get('courses')
            # section = form.cleaned_data.get('section')
            # year = form.cleaned_data.get('year')
            # profile = UserProfile.objects.get_or_create(user=request.user)
            # userobj = UserProfile(qrcode=unique_id)
            # userobj.save().filter(course=course, section=section, year=year)