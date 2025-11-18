import axios from "axios";
import { useRef, useState } from "react";
import { TypingIndicator } from "./TypingIndicator";
import { ChatMessages, Message } from "./ChatMessages";
import { ChatFormData, ChatInput } from "./ChatInput";

export type ChatResponse = {
  response: string;
};

const ChatBot = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isBotTyping, setIsBotTyping] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const conversationId = useRef(crypto.randomUUID());

  const onSubmit = async ({ prompt }: ChatFormData) => {
    try {
      setMessages((prev) => [...prev, { content: prompt, role: "user" }]);
      setIsBotTyping(true);
      setError(null);
      const { data } = await axios.post<ChatResponse>("/api/chat", {
        prompt,
        conversationId: conversationId.current,
      });
      setMessages((prev) => [...prev, { content: data.response, role: "bot" }]);
    } catch (error) {
      setError("An error occurred. Please try again.");
    } finally {
      setIsBotTyping(false);
    }
  };

  return (
    <div className="flex flex-col h-full">
      <div className="flex flex-col flex-1 gap-3 mb-3 overflow-y-auto">
        <ChatMessages messages={messages} isBotTyping={isBotTyping} />
        {isBotTyping && <TypingIndicator />}
        {error && <div className="text-red-600 text-sm mb-2">{error}</div>}
      </div>
      <ChatInput onSubmit={onSubmit} />
    </div>
  );
};

export default ChatBot;
