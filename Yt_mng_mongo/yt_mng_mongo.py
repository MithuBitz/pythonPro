from pymongo import MongoClient #Specific import
from bson import ObjectId

# import pymongo 
# client = pymongo.MongoClient("mongodb+srv://<username>:<pass>@mitpyth.neh4v.mongodb.net/")

client = MongoClient("mongodb+srv://<usrname>:<pass>@mitpyth.neh4v.mongodb.net/")

db = client["ytmaneger"] #create a db in mongo as ytmaneger
video_collection = db["videos"] # create a list as videos in ytmangeger

print(video_collection)

def list_all_videos():
    for videos in video_collection.find():
        print(f"ID: {videos['_id']}, Name: {videos['name']}, Duration: {videos['time']}")

def add_videos(name, time):
    video_collection.insert_one({"name": name, "time": time})
    # above line add name and time into videos

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {"_id": ObjectId(video_id)},
        {"$set": {
            "name": new_name,
            "time": new_time
        }}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


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
                list_all_videos()
            case '2':
                name = input("Enter name of the video: ")
                time = input("Enter duration of the video: ")
                add_videos(name, time)

            case '3':
                video_id = input("Enter video id to update: ")
                name = input("Enter new name of the video: ")
                time = input("Enter new duration of the video: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter video id to be deleted: ")
                delete_video(video_id)
            case '5':
                break
            #default case
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()