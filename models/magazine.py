class Magazine:
    def __init__(self, id, title, publisher):
        # Validate data types and values
        if not isinstance(id, int):
            raise ValueError("Magazine ID must be an integer")
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Magazine title must be a non-empty string")
        if not isinstance(publisher, str) or len(publisher) == 0:
            raise ValueError("Magazine publisher must be a non-empty string")

        self._id = id
        self._title = title
        self._publisher = publisher

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def publisher(self):
        return self._publisher

    def __repr__(self):
        return f'<Magazine {self.title}>'
