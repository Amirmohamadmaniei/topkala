class SortMixin:
    def setup(self, request, *args, **kwargs):
        self.sort = request.GET.get('sort')
        if not self.sort:
            self.sort = 'title'
        super().setup(request, *args, **kwargs)

#
#
# self.available = request.GET.get('available')
#         print(self.available)
#         if self.available is None:
#             self.available = True
#         if self.available == 'on':
#             self.available = False
