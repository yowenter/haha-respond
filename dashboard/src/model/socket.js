import io from 'socket.io-client';
import { API_URL, bus } from '@/model/const';

const url = API_URL === '.' ? '' : API_URL;
const commentRoomId = '88888';

let commentSocket;

if (commentSocket) commentSocket.disconnect();
commentSocket = io(`${url}`, {
  path: '/danmus/socket.io',
});
commentSocket.on('connect', () => {
  commentSocket.emit('enter_room', commentRoomId);
  console.log('enter_comment_room');
});
commentSocket.on('comment', (data) => {
  console.log('comment', data);
  bus.$emit('comment', data);
});
commentSocket.on('disconnect', () => {
  console.log('comment_disconnect');
});
