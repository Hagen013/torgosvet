class CategoryViewMixin(object):

    """
    Класс-миксин для категории

    Алгоритм работы:
        1. Получение категории
            get_category(), ожидает получения урла из параметров
        2. Получение условия вхождения в категорию
            get_сondition_of_occurrence() - добавляет условие category__in
        3. Получение выборки по условия вхождения
            get_queryset() - переопределение кверисета

    """

    category = None
    category_model = None
    product_model = None
    сondition_of_occurrence = {}

    def get(self, request, *args, **kwargs):
        # Получение категории
        self.category = get_category(
            *args,
            **kwargs
        )
        # Получение условия вхождения в категорию
        self.сondition_of_occurrence = self.get_сondition_of_occurrence(
            *args,
            **kwargs
        )
        return(super(CategoryViewMixin, self).get(
               request,
               *args,
               **kwargs)
               )

    def get_queryset(self, *args, **kwargs):
        return self.product_model.filter(
            **self.сondition_of_occurrence
        )

    def def get_context_data(self, *args, **kwargs):
        context = super(CategoryViewMixin, self).get_context_data(
            *args,
            **kwargs
        )
        context['category'] = self.category
        return context

    def get_category(self, *args, **kwargs):
        url = self.kwargs.get('url')
        if url:
            try:
                category = self.category_model.public.get(url=url)
                return category
            except ObjectDoesNotExist:
                raise Http404
        else:
            return(self.category_model.get_or_create(
                url=""))[0]

    def get_сondition_of_occurrence(self, *args, **kwargs):
        return {
            "category__in": self.category.get_descendants(include_self=True),
        }
