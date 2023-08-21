import datetime


class AddingMixin:
    def add_author_and_time(self, form):
        if not self.object.author:
            if self.request.user.username:
                self.object.author = self.request.user.username
            else:
                self.object.author = 'Unknown creator'
        if not self.object.date:
            dt = datetime.datetime.now()
            dt = dt.replace(microsecond=0)
            self.object.date = dt
        return super().form_valid(form)
