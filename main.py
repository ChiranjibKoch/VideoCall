from pyrogram import Client

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
from pytgcalls.types import VideoQuality

app = Client(
    'py-tgcalls',
    api_id=26676259,
    api_hash='a6194f7e8ec4adf87e5a50c7e9335f5c',
)

call_py = PyTgCalls(app)
call_py.start()
audio_file = 'input.webm'
call_py.play(
    -1001952511944,
    MediaStream(
        'test.jpg',
        audio_path=audio_file,
        video_parameters=VideoQuality.HD_720p,
    ),
)
idle()
