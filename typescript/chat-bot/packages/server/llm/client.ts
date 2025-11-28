import OpenAI from "openai";
import { InferenceClient } from "@huggingface/inference";
import summarizePrompt from "../llm/prompts/summarize-reviews.txt";
import { Ollama } from "ollama";

// Implementation detail
const openAIClient = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const inferenceClient = new InferenceClient(process.env.HF_TOKEN);

const ollamaClient = new Ollama();

type GenerateTextOptions = {
  model?: string;
  prompt: string;
  temperature?: number;
  maxOutputTokens?: number;
  instructions?: string;
  previous_response_id?: string;
};

type GenerateResponse = {
  id: string;
  text: string;
};

export const llmClient = {
  async generateText({
    model = "gpt-4o-mini",
    prompt,
    temperature = 0.2,
    maxOutputTokens = 500,
    instructions,
    previous_response_id,
  }: GenerateTextOptions): Promise<GenerateResponse> {
    const response = await openAIClient.responses.create({
      model: model,
      input: prompt,
      temperature: temperature,
      max_output_tokens: maxOutputTokens,
      instructions: instructions,
      previous_response_id: previous_response_id,
    });
    return {
      id: response.id,
      text: response.output_text,
    };
  },
  async summarizeReview(review: string): Promise<GenerateResponse> {
    const chatCompletion = await ollamaClient.chat({
      model: "tinyllama",
      messages: [
        {
          role: "system",
          content: summarizePrompt,
        },
        {
          role: "user",
          content: review,
        },
      ],
    });
    return {
      text: chatCompletion.message.content,
      id: "",
    };
  },
};
