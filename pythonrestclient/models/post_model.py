import abstract_model


class PostModel(abstract_model.AbstractModel):
    @classmethod
    def resources_name(cls):
        return 'posts'
