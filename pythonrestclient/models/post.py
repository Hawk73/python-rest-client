import abstract_model


class Post(abstract_model.AbstractModel):
    def _resources_name(self):
        return 'posts'
