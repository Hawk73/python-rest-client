import abstract_model

class Post(abstract_model.AbstractModel):
    def resources_name(self):
        return 'posts'
