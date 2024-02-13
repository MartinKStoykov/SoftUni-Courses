class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photo_count: int):
        return cls(photo_count // 4 + photo_count % 4)


    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return (f"{label} photo added successfully on page"
                        f" {page+1} slot {self.photos[page].index(label)+1}")

        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            if page:
                result += (' '.join([f"[]" for p in page])) + "\n"
            else:
                result += "\n"
            result += "-----------\n"

        return result
