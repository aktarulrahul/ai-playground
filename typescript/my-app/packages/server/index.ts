import express from "express";
import type { Request, Response } from "express";
import dotenv from "dotenv";

dotenv.config();

const app = express();
const port = process.env.PORT || 5001;

app.get("/", (req: Request, res: Response) => {
  res.send(`OPENAI_API_KEY: ${process.env.OPENAI_API_KEY}`);
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
