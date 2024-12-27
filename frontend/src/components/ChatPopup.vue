<template>
  <div class="chat-container">
    <!-- Chat Icon with Notification Dot -->
    <!-- <div 
      class="chat-icon" 
      @click="toggleChat"
    > -->
    <div class="chat-icon" @click="toggleChat">
    <img 
      :src="customIconPath" 
      alt="Chatbot Icon" 
      class="chat-icon-image"
    >
      <!-- <span class="notification-dot" v-if="unreadMessages"></span>
      <i class="fas fa-comment-dots"></i> -->
    </div>

    <!-- Elegant Chat Popup -->
    <div 
      v-if="isChatOpen" 
      class="chat-popup"
      :class="{ 'chat-open': isChatOpen }"
    >
      <!-- Gradient Header -->
      <div class="chat-header">
        <div class="header-content">
          <img 
            :src="TitanicIcon"
            alt="Bot Avatar" 
            class="bot-avatar"
          >
          <div class="header-text">
            <h3>Titanic Dataset Assistant</h3>
            <span class="status-text">Online</span>
          </div>
        </div>
        <button @click="toggleChat" class="close-btn">
          <i class="fas fa-times"></i>
        </button>
      </div>

      <!-- Messages Container -->
      <div class="chat-messages" ref="messagesContainer">
        <div 
          v-for="(message, index) in messages" 
          :key="index"
          class="message-wrapper"
        >
          <div 
            :class="[
              'message', 
              message.type === 'user' ? 'user-message' : 'bot-message'
            ]"
          >
            {{ message.text }}
          </div>
        </div>
      </div>

      <!-- Input Area -->
      <div class="chat-input-area">
        <input 
          type="text"
          v-model="newMessage"
          @keyup.enter="sendMessage"
          placeholder="Ask about Titanic dataset..."
          class="chat-input"
        >
        <button 
          @click="sendMessage" 
          class="send-button"
          :disabled="!newMessage.trim()"
        >
          <i class="fas fa-paper-plane"></i>
        </button>
      </div>
    </div>
  </div>
</template>



<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'
import customIcon from '@/assets/bot.png'
import TitanicIcon from '@/assets/titanic_bot.png'

const customIconPath = customIcon
// Reactive state variables
const isChatOpen = ref(false)
const messages = ref([])
const newMessage = ref('')
const unreadMessages = ref(0)

// Toggle chat popup
const toggleChat = () => {
  isChatOpen.value = !isChatOpen.value
  unreadMessages.value = 0  // Reset unread messages when opened
}

// Send message function
const sendMessage = async () => {
  // Trim and validate message
  if (!newMessage.value.trim()) return

  // Add user message
  messages.value.push({
    text: newMessage.value,
    type: 'user'
  })

try {
    // Actual API call with full URL
    const response = await axios.post('http://localhost:8000/api/chat', {
      message: newMessage.value
    })

    // Add bot response
    messages.value.push({
      text: response.data.message || 'Processing your query...',
      type: 'bot'
    })

    // Clear input after sending
    newMessage.value = ''
  } catch (error) {
    console.error('Chat error:', error.response ? error.response.data : error)
    messages.value.push({
      text: error.response?.data?.detail || 'Sorry, something went wrong.',
      type: 'bot'
    })
  }
}

// Track unread messages when chat is closed
watch(messages, () => {
  if (!isChatOpen.value) {
    unreadMessages.value++
  }
})
</script>


<style scoped>
.chat-container {
  position: fixed;
  bottom: 30px;
  right: 30px;
  z-index: 1000;
}

.chat-icon {
  position: relative;
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #8a4fff, #4ecdc4);
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.3s ease;
}

.chat-icon:hover {
  transform: scale(1.1);
}

.chat-icon i {
  color: white;
  font-size: 24px;
}

.chat-icon-image {
  color: white;
  width: 50px;  /* Adjust size as needed */
  height: 50px;
   border-radius: 50%;
}

.notification-dot {
  position: absolute;
  top: 0;
  right: 0;
  width: 15px;
  height: 15px;
  background-color: red;
  border-radius: 50%;
}

.chat-popup {
  position: absolute;
  bottom: 80px;
  right: 0;
  width: 350px;
  background: white;
  border-radius: 15px;
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  animation: slideUp 0.3s ease;
}

.chat-header {
  background: linear-gradient(135deg, #8a4fff, #4ecdc4);
  color: white;
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-content {
  display: flex;
  align-items: center;
}

.bot-avatar {
  width: 70px;
  height: 70px;
  border-radius: 100%;
  margin-right: 5px;
}

.header-text h3 {
  margin: 0;
  font-size: 16px;
}

.status-text {
  font-size: 12px;
  opacity: 0.7;
}

.close-btn {
  background: none;
  border: none;
  color: white;
  font-size: 20px;
  cursor: pointer;
}

.chat-messages {
  height: 350px;
  overflow-y: auto;
  padding: 15px;
  background-color: #f9f9f9;
}

.message-wrapper {
  display: flex;
  margin-bottom: 15px;
}

.message {
  max-width: 80%;
  padding: 10px 15px;
  border-radius: 15px;
  font-size: 14px;
}

.user-message {
  background-color: #7a5cff;
  color: white;
  align-self: flex-end;
  margin-left: auto;
}

.bot-message {
  background-color: #e6e6e6;
  color: #333;
  align-self: flex-start;
}

.chat-input-area {
  display: flex;
  padding: 15px;
  background-color: white;
  border-top: 1px solid #f1f1f1;
}

.chat-input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 20px;
  margin-right: 10px;
}

.send-button {
  background: linear-gradient(135deg, #8a4fff, #4ecdc4);
  color: white;
  border: none;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.send-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

@keyframes slideUp {
  from { 
    opacity: 0; 
    transform: translateY(20px); 
  }
  to { 
    opacity: 1; 
    transform: translateY(0); 
  }
}
</style>
