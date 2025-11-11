import express from "express";
import type { Request, Response } from "express";
import dotenv from "dotenv";

dotenv.config();

const app = express();
const port = process.env.PORT || 5001;

app.get("/", (req: Request, res: Response) => {
  res.send(`OPENAI_API_KEY: ${process.env.OPENAI_API_KEY}`);
});
app.get("/api/hello", (req: Request, res: Response) => {
  res.json({ message: "Hello from the server!" });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
