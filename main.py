from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from utils import form_time, draw_avatar
import configs

def main():
    previous_time  = ''
    with TelegramClient(configs.session_name, configs.api_id, configs.api_hash) as client:
        while True:
            if previous_time != form_time():
                previous_time = form_time()
                draw_avatar(form_time())
                image = client.upload_file('image_time.jpg')
                client(DeletePhotosRequest(client.get_profile_photos('me')))
                client(UploadProfilePhotoRequest(image))

if __name__ == '__main__':
    main()