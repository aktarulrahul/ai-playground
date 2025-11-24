import OpenAI from "openai";

// Implementation detail
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

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
    const response = await client.responses.create({
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
};
