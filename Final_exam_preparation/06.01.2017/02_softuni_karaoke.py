line = input().split(", ")
participants = []
for part in line:
    participants.append(part.strip())

line_songs = input().split(", ")
songs = []
for song in line_songs:
    songs.append(song.strip())

awards = {}

while True:
    line = input()
    if line == "dawn":
        break

    line_args = line.split(", ")
    performances = []
    for line_arg in line_args:
        performances.append(line_arg.strip())

    participant = performances[0]
    song = performances[1]
    award = performances[2]

    if participant in participants and song in songs:
        if participant not in awards:
            awards[participant] = []
        if award not in awards[participant]:
            awards[participant].append(award)

if not awards:
    print("No awards")

sorted_awards = dict(sorted(awards.items(), key=lambda x: (-len(x[1]), x)))
for part, values in sorted_awards.items():
    print(f"{part}: {len(values)} awards")
    for val in values:
        print(f"--{val}")
