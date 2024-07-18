# detail_page/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import re
import unicodedata

def normalize_room_name(room_name):
    # Normalize the Unicode data
    normalized = unicodedata.normalize('NFKD', room_name)
    # Convert to ASCII
    ascii_name = normalized.encode('ascii', 'ignore').decode('ascii')
    # Replace spaces and other invalid characters with underscores
    safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', ascii_name)
    return safe_name

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{normalize_room_name(self.room_name)}'

        # 방 그룹에 가입
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # 방 그룹에서 나가기
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 웹소켓에서 메시지 받기
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        nickname = text_data_json['nickname']  # 닉네임 추가

        # 방 그룹에 메시지 보내기
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'nickname': nickname  # 닉네임 추가
            }
        )

    # 방 그룹에서 메시지 받기
    async def chat_message(self, event):
        message = event['message']
        nickname = event['nickname']  # 닉네임 추가

        # 웹소켓으로 메시지 보내기
        await self.send(text_data=json.dumps({
            'message': message,
            'nickname': nickname  # 닉네임 추가
        }))
