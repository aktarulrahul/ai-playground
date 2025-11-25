import dayjs from "dayjs";
import { PrismaClient, type Review } from "../generated/prisma";
const prisma = new PrismaClient();

export const reviewRepository = {
  async getReviews(productId: number, limit?: number): Promise<Review[]> {
    return prisma.review.findMany({
      where: { productId: productId },
      orderBy: { createdAt: "desc" },
      take: limit,
    });
  },
  async storeReviewSummary(productId: number, summary: string): Promise<any> {
    const now = new Date();
    const expiresAt = dayjs().add(7, "days").toDate();

    const data = {
      productId: productId,
      content: summary,
      expiresAt: expiresAt,
      generatedAt: now,
    };
    return await prisma.summary.upsert({
      where: { productId: productId },
      create: data,
      update: data,
    });
  },

  async getReviewSummary(productId: number): Promise<string | null> {
    const summary = await prisma.summary.findFirst({
      where: {
        AND: [{ productId: productId }, { expiresAt: { gt: new Date() } }],
      },
    });
    return summary ? summary.content : null;
  },
};
