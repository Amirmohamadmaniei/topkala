class SortMixin:
    def setup(self, request, *args, **kwargs):
        self.sort = request.GET.get('sort')
        if not self.sort:
            self.sort = 'title'
        super().setup(request, *args, **kwargs)
