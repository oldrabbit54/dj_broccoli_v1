from django.contrib.auth.models import User
log_menu = {
        'logged' : [
            {'title' : 'Logout', 'url' : 'user-logout', 'login' : 1},
        ],
        'outlogged' : [
            {'title' : 'Register', 'url' : 'register', 'login' : 1},
            {'title' : 'Login', 'url' : 'user-login', 'login' : 1},
        ]
}
menu = [
    # {'title' : 'Register', 'url' : 'register', 'login' : 1},
    # {'title' : 'Login', 'url' : 'login', 'login' : 1},
    # {'title' : 'Logout', 'url' : 'logout', 'login' : 1},
    {'title' : 'Home', 'url' : 'home-page', 'login' : 0},
    {'title' : 'Profile', 'url' : 'my_profile_edit', 'login' : 0},
    {'title' : 'Thoughts', 'url' : 'posts-preview', 'login' : 0},
    {'title' : 'Gallery', 'url' : 'gallery', 'login' : 0},
    {'title' : 'Help', 'url' : 'help-page', 'login' : 0},
    {'title' : 'Events', 'url' : 'event-page', 'login' : 0}
    #{'title' : 'Daily stuff', 'url' : ''}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = []
        # for index, m in enumerate(menu):
        #     if(self.request.user.is_authenticated):
        #         if index not in (0, 1):
        #             context['menu'].append(m)
        #     else:
        #         if index != 2:
        #             context['menu'].append(m)
        for m in menu:
            context['menu'].append(m)
        for log in log_menu['logged' if self.request.user.is_authenticated else 'outlogged']:
            context['menu'].append(log)


        context['this_page'] = self.request.get_full_path()
        if self.request.user.is_authenticated:
            context['this_user_id'] = self.request.user.my_profile.id
        return context
