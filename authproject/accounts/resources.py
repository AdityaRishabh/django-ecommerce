from import_export import resources, fields
from .models import Product


class ProductResource(resources.ModelResource):

    category = fields.Field(attribute='category', column_name='category')
    image_url = fields.Field(attribute='image_url', column_name='image_url') 

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'stock',
            'category',
            'image_url',
        )
        import_id_fields = ()