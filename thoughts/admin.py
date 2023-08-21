from django.contrib import admin
from .models import NoteModel

# @admin.register(NoteModel)
# class NoteModelAdmin(admin.ModelAdmin):
#     list_display = ['header', 'author', 'note', 'date', 'unknown_author_id', 'id']
#     list_editable = ['note']
#     ordering = ['date']
#     search_fields = ['note', 'header', 'author']
#     list_per_page = 7
#
#     @admin.display(description='nickname')
#     def unknown_author_id(self, note: NoteModel):
#         if note.author is None:
#             return f'Unknown author{note.id}'
#         elif('unknown author' in note.author.lower()):
#             return f'Unknown author #{note.id}'
#         return note.author