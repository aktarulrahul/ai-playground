import { useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";
export type Message = {
  content: string;
  role: "user" | "bot";
};

type Props = {
  messages: Message[];
  isBotTyping: boolean;
};

export const ChatMessages = ({ messages, isBotTyping }: Props) => {
  const lastMessageRef = useRef<HTMLDivElement | null>(null);
  const onCopyMessage = (e: React.ClipboardEvent<HTMLParagraphElement>) => {
    const selection = window.getSelection()?.toString()?.trim();
    if (selection) {
      e.preventDefault();
      e.clipboardData.setData("text/plain", selection || "");
    }
  };
  useEffect(() => {
    lastMessageRef.current?.scrollIntoView({
      behavior: "smooth",
      block: "end",
    });
  }, [messages, isBotTyping]);
  return (
    <>
      {messages.map((msg, index) => (
        <div
          key={index}
          onCopy={(e) => onCopyMessage(e)}
          className={`my-2 px-2 py-1 rounded-xl ${
            msg.role === "user"
              ? "bg-blue-600 text-white self-end"
              : "bg-gray-100 text-black self-start"
          }`}
          ref={index === messages.length - 1 ? lastMessageRef : null}
        >
          <ReactMarkdown>{msg.content}</ReactMarkdown>
        </div>
      ))}
    </>
  );
};
