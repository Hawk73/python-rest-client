import abstract_model


class PostModel(abstract_model.AbstractModel):
    def _resources_name(self):
        return 'posts'
