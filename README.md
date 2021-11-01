# Django Socialsite Blogs

1.  # Created new project SocialBlogs
    Created App blog, register App in the project settings,
    make migrations for the whole project.

2.  # Created models for the App
    Used django.utils timezone to get the current time,
    used reverse from django.urls,
    used TextField, CharField, DateTimeField, BooleanField from django.db.models.fields,
    created model 'Post' to save the posts of the site in database,
    created publish and approve_comment methods for Post Model,
    created model Comment with forienkey relation ship with post,
    create approve method to approve it.

3.  # Created ModelForm for the App
    Created forms for both the models Post and Comment,
    also declare Widgets dictionary for forms. A widget is Django’s representation of an HTML input element. The widget handles the rendering of the HTML, and the extraction of data from a GET/POST dictionary that corresponds to the widget.

4.  # Created views for the App
    Used django shortcuts render, get_object_or_404,redirect,
    decorator login_required,
    mixin LoginRequiredMixin,
    url reverse_lazy,
    Views TemplateView, ListView,DetailView,CreateView, UpdateView, DeleteView.

    Created AboutView to render About page for site using TemplateView,
    created PostListView to render All Posts list Page for site using ListView and get_queryset method to filter posts using Field lookups,
    created PostDetailView to render Post details Page for site using DetailView,
    created CreatePostView to render Post creation Page for site using CreateView and LoginRequiredMixin, added login_url and redirect_field_name attributes,
    created PostUpdateView to render Post updation Page for site using UpdateView and LoginRequiredMixin, added login_url and redirect_field_name attributes,
    created PostDeleteView to from site using DeleteView and LoginRequiredMixin, used reverse_lazy to render Post List Page,
    created DraftListView to render Draft Posts Page for site using ListView and LoginRequiredMixin, used get_queryset method to filter posts using Field lookups,
    created Urls For All View respectively.

5.  # Created views Methods 
    Created post_publish view to publish draft posts using model Post publish method and @login_required decorator, used get_object_or_404 to get the post,
    created add_comment_to_post view to add comments in posts using model Comments, ModelForm CommentForm and @login_required decorator, used get_object_or_404 to get the post,
    created comment_approve view to approve Unapproved comments in Post using model Comments approve method and @login_required decorator, used get_object_or_404 to get the Comment,
    created comment_remove view to remove comments from Post using model Comments Delete method and @login_required decorator, used get_object_or_404 to get the Comment,
    created Urls for the Views respectively.

6.  # Created Urls of project
    Created authentication system superuser login and logout using django LoginView and LogoutView,
    setup Redirect_login_url, STATIC_ROOT and TEMPLATE_DIR in Settings.py,
    created Template Html file for login page. Used POST method to send Login Details.

7.  # Created HTML, CSS and JAVASCRIPT FILES
    Created About.html file and Base.html,
    added CDNs of Bootstrap, CDN for Medium Style Editor,
    added custom CSS FIle Link,
    used codepen.io to search for desired css affects for our App and copy code from codepen.io and alter according to our effect,
    added Links for google fonts in Head.

    Created navbar for website using css classes, 
    created Post List, Post Detail, PostForm, DraftPost, Delete Post, Comment Form Templates,
    created Publish, Edit and Remove Post functionality
    created Approve or remove comments for Post functionality.
