from pytube import YouTube
import os

def download_youtube_video(yt_id, video_id):
	try:
        youtube_url = f"https://www.youtube.com/watch?v={youtube_id}"
        yt = YouTube(youtube_url)
        stream = yt.streams.get_highest_resolution()
        save_path = f"dataset/youtube/{video_id}"
        if not os.path.exists(save_path):
			os.makedirs(save_path)
        stream.download(output_path="dataset/youtube/{video_id}", filename=video_id)
        print(f"successfully download video to{save_path}")

        title = yt.title
        description = yt.description
        info_path = os.path.join(save_path, f"{video_id}_info.txt")
        with open(info_path, "w") as f:
			f.write(f"Video Title: {title}\n")
			f.write(f"Description: {description}\n")
        print(f"successfully save video info to {info_path}")
        
    except Exception as e:
        print(f"Error downloading video {video_id}: {e}")


meta_data = "dataset/metadata.csv"
df = pd.read_csv(meta_data)
for row in tqdm(df.itertuples()):
	yt_id = row.youtube_id
	video_id = row.video_id
    download_youtube_video(yt_id, video_id)
