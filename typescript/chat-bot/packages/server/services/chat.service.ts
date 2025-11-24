import fs from "fs";
import path from "path";
import { conversationRepository } from "../repositories/conversation.repository";
import template from "../prompts/chatbot.txt";
import { llmClient } from "../llm/client";

const parkInfo = fs.readFileSync(
  path.join(__dirname, "..", "prompts", "park.md"),
  "utf-8"
);
const instructions = template.replace("{{parkInfo}}", parkInfo);

type ChatResponse = {
  id: string;
  message: string;
};

// Export public interface
// Leaky abstraction
export const chatService = {
  async sendMessage(
    prompt: string,
    conversationId: string
  ): Promise<ChatResponse> {
    const response = await llmClient.generateText({
      model: "gpt-4o-mini",
      prompt: prompt,
      temperature: 0.2,
      maxOutputTokens: 200,
      instructions: instructions,
      previous_response_id:
        conversationRepository.getLastResponseId(conversationId),
    });
    conversationRepository.setLastResponseId(conversationId, response.id);

    return {
      id: response.id,
      message: response.text,
    };
  },
};
