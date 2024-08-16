import json

def load_data():
    try:
        with open('youtube_maneger.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []    

# It helps to save the videos list when it requires
def save_data_helper(videos):
    with open('youtube_maneger.txt', 'w') as file:
        json.dump(videos, file)

def list_all_youtube_videos(videos):
    print("\n")
    print("*" * 60)

    for index, video in enumerate(videos, start=1):
        print(f"{index}. name = {video['name']}, duration = {video['time']}")
    
    print("\n")
    print("*" * 60)

def add_videos(videos):
    name = input("Enter the name of the video ")
    time = input("Enter time of the video ")
    videos.append({"name": name, "time" : time})
    save_data_helper(videos)


def update_video_details(videos):
    list_all_youtube_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new duration of the video ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else: 
        print("Enter valid video number")

def delete_video(videos):
    list_all_youtube_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index-1]        
        save_data_helper(videos)
    else: 
        print("Enter valid video number")


def main():
    videos = load_data()
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
                list_all_youtube_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_video_details(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            #default case
            case _:
                print("Invalid choice")

#General and very common way to run main function 
if __name__ == "__main__":
    main()