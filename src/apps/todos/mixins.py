class SerializerMapMixin:
    serializer_map = {}

    def get_serializer_class(self):
        serializer_class = self.serializer_map.get(
            self.action, self.serializer_class
        )
        return serializer_class
