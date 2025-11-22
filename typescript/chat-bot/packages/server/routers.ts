import express from "express";
import type { Request, Response } from "express";
import { chatController } from "./controllers/chat.controller";
import { PrismaClient } from "./generated/prisma";

const router = express.Router();

router.get("/", (req: Request, res: Response) => {
  res.send(`Chat Bot Server is running`);
});

router.get("/api/hello", (req: Request, res: Response) => {
  res.json({ message: "Hello from the server!" });
});

router.post("/api/chat", express.json(), chatController.sendMessage);

router.get("/api/products/:id/reviews", async (req: Request, res: Response) => {
  const prisma = new PrismaClient();
  const productId = Number(req.params.id);

  const reviews = await prisma.review.findMany({
    where: { productId: productId },
    orderBy: { createdAt: "desc" },
  });
  res.json(reviews);
});

export default router;
