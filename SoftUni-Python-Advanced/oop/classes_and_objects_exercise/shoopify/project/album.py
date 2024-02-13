from project.song import Song

class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs = [*args]
    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        elif self.published:
            return "Cannot add songs. Album is published."

        elif song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        for sng in self.songs:
            if sng.name == song_name:
                if self.published:
                    return "Cannot remove songs. Album is published."

                self.songs.remove(sng)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return "\n== ".join([f"Album {self.name}", *[x.get_info() for x in self.songs]]) + "\n"
