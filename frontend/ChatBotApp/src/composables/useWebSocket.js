// src/composables/useWebSocket.js
import { ref } from 'vue';

export function useWebSocket() {
  const socket = ref(null);
  const messages = ref([]);

  const connectWebSocket = (url) => {
    socket.value = new WebSocket(url);
    socket.value.onmessage = (event) => {
      const message = JSON.parse(event.data);
      messages.value.push(message);
    };
  };

  const sendMessageToWebSocket = (message) => {
    if (socket.value) {
      socket.value.send(JSON.stringify(message));
    }
  };

  const receiveMessageFromWebSocket = (callback) => {
    socket.value.onmessage = (event) => {
      const message = JSON.parse(event.data);
      callback(message);
    };
  };

  return {
    connectWebSocket,
    sendMessageToWebSocket,
    receiveMessageFromWebSocket,
  };
}
