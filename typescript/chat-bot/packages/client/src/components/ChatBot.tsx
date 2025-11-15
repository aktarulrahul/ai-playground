import axios from "axios";
import ReactMarkdown from "react-markdown";
import { Button } from "./ui/button";
import { FaArrowUp } from "react-icons/fa";
import { useForm } from "react-hook-form";
import { useEffect, useRef, useState } from "react";

type FormData = {
  prompt: string;
};

type ChatResponse = {
  response: string;
};

type Message = {
  content: string;
  role: "user" | "bot";
};

const ChatBot = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isBotTyping, setIsBotTyping] = useState(false);
  const formRef = useRef<HTMLFormElement | null>(null);
  const conversationId = useRef(crypto.randomUUID());
  const { register, handleSubmit, reset, formState } = useForm<FormData>();
  useEffect(() => {
    formRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
  }, [messages, isBotTyping]);
  const onSubmit = async ({ prompt }: FormData) => {
    setMessages((prev) => [...prev, { content: prompt, role: "user" }]);
    reset();
    setIsBotTyping(true);
    const { data } = await axios.post<ChatResponse>("/api/chat", {
      prompt,
      conversationId: conversationId.current,
    });
    setMessages((prev) => [...prev, { content: data.response, role: "bot" }]);
    setIsBotTyping(false);
  };
  const onKeyDown = (e: React.KeyboardEvent<HTMLFormElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      handleSubmit(onSubmit)();
      e.preventDefault();
    }
  };
  const onCopyMessage = (e: React.ClipboardEvent<HTMLParagraphElement>) => {
    const selection = window.getSelection()?.toString()?.trim();
    if (selection) {
      e.preventDefault();
      e.clipboardData.setData("text/plain", selection || "");
    }
  };
  return (
    <div className="flex flex-col h-full">
      <div className="flex flex-col flex-1 gap-3 mb-3">
        {messages.map((msg, index) => (
          <p
            key={index}
            onCopy={(e) => onCopyMessage(e)}
            className={`my-2 px-2 py-1 rounded-xl ${
              msg.role === "user"
                ? "bg-blue-600 text-white self-end"
                : "bg-gray-100 text-black self-start"
            }`}
          >
            <ReactMarkdown>{msg.content}</ReactMarkdown>
          </p>
        ))}
        {isBotTyping && (
          <div className="flex gap-1 p-3">
            <div className="w-3 h-3 bg-gray-400 rounded-full animate-bounce"></div>
            <div className="w-3 h-3 bg-gray-400 rounded-full animate-bounce [animation-delay:0.2s]"></div>
            <div className="w-3 h-3 bg-gray-400 rounded-full animate-bounce [animation-delay:0.4s]"></div>
          </div>
        )}
      </div>
      <form
        onSubmit={handleSubmit(onSubmit)}
        onKeyDown={onKeyDown}
        className="flex flex-col gap-2 items-end border-2 p-4 rounded-3xl"
        ref={formRef}
      >
        <textarea
          {...register("prompt", {
            required: true,
            validate: (value) => value.trim().length > 0,
          })}
          placeholder="Ask Anything..."
          maxLength={1000}
          rows={4}
          cols={50}
          className="w-full border-0 p-2 focus:outline-0 resize-none"
        />
        <Button
          className="rounded-full w-9 h-9"
          type="submit"
          disabled={formState.isSubmitting || !formState.isValid}
        >
          <FaArrowUp />
        </Button>
      </form>
    </div>
  );
};

export default ChatBot;
