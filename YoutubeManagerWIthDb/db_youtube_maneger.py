import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL    
    )
""")

def list_all_youtube_videos():
    cur.execute("SELECT * FROM videos")
    print("\n")
    print("*" * 60)
    for row in cur.fetchall():
        print(row)
    print("\n")
    print("*" * 60)

def add_videos(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video_details(video_id, new_name, new_time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))

    conn.commit()

def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,)) # comma(,) is must needed after video_id
    conn.commit()

def main():
    while True:
        print("\n Youtube Maneger | Choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit from the app")

        choice = input("Enter your choice ")

        # print(videos)

        match choice:
            case '1':
                list_all_youtube_videos()
            case '2':
                name = input("Enter name of the video: ")
                time = input("Enter duration of the video: ")
                add_videos(name, time)

            case '3':
                video_id = input("Enter video id to update: ")
                name = input("Enter new name of the video: ")
                time = input("Enter new duration of the video: ")
                update_video_details(video_id, name, time)
            case '4':
                video_id = input("Enter video id to be deleted: ")
                delete_video(video_id)
            case '5':
                break
            #default case
            case _:
                print("Invalid choice")
    # close the db connection so that db not currupt: best practice
    conn.close()


#General and very common way to run main function 
if __name__ == "__main__":
    main()