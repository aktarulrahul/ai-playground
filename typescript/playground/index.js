// // ES module syntax
// import { get_encoding } from "tiktoken";

// // CommonJS syntax
// // const { get_encoding } = require("tiktoken");

// // token Id -> token
// // 904 -> "hello"

// const encoding = get_encoding("cl100k_base");
// const tokens = encoding.encode(
//   "Hello world! This is the first test of tiktoken library."
// );
// console.log("Tokens:", tokens);
import dotenv from "dotenv";
import OpenAI from "openai";
dotenv.config();
const OPENAI_API_KEY = dotenv.config().parsed.OPENAI_API_KEY;
console.log("OpenAI API Key:", OPENAI_API_KEY);

const client = new OpenAI({
  apiKey: OPENAI_API_KEY,
});

const stream = await client.responses.create({
  model: "gpt-4.1",
  input: "Write a story about a robot",
  temperature: 0.7,
  max_output_tokens: 256,
  stream: true,
});

// console.log("Response:", res);
for await (const chunk of stream) {
  // console.log("Chunk:", chunk);
  if (chunk.delta) {
    process.stdout.write(chunk.delta || "");
  }
}
