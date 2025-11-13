import type { Request, Response } from "express";
import { chatService } from "../services/chat.service";
import z from "zod";

// Implementation detail
const chatSchema = z.object({
  prompt: z
    .string("Prompt is required")
    .trim()
    .min(1, "Prompt cannot be empty")
    .max(100, "Prompt is too long, Max 100 characters"),
  conversationId: z.string("Conversation ID is required").uuid(),
});

// Export public interface
export const chatController = {
  async sendMessage(req: Request, res: Response) {
    const parsedResult = chatSchema.safeParse(req.body);
    if (!parsedResult.success) {
      return res.status(400).json({ error: parsedResult.error.format() });
    }
    try {
      const { prompt, conversationId } = req.body;
      const completion = await chatService.sendMessage(prompt, conversationId);
      res.json({ response: completion.message });
    } catch (error) {
      res.status(500).json({ error: "Failed to generate a response" });
    }
  },
};
