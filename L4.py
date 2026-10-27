class Playlist:
    def __init__(self,name,genre):
        self.name=name
        self.genre=genre
        self.songs=[]
        print(f"Playlist {self.name} created")

    def add_song(self,song):
        self.songs.append(song)
        print(f"Song {song} added to playlist {self.name}")

    def remove_song(self,song):
        self.songs.remove(song)
        print(f"Song {song} removed from playlist {self.name}")

    def display(self):
        print(f"Playlist {self.name} has {len(self.songs)} songs")

    def __del__(self):
        print(f"Playlist {self.name} deleted")

playlist1=Playlist("playlist1","rock")

while True: 
    print("1. Add song")
    print("2. Remove song")
    print("3. Display playlist")
    print("4. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        song=input("Enter song name: ")
        playlist1.add_song(song)
    elif choice==2:
        song=input("Enter song name: ")
        playlist1.remove_song(song)
    elif choice==3:
        playlist1.display()
    elif choice==4:
        break
    else:
        print("Invalid choice")

