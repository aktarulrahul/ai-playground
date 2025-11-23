import type { Review } from "../generated/prisma";
import { reviewRepository } from "../repositories/review.repository";

export const reviewService = {
  async getReviews(productId: number): Promise<Review[]> {
    return reviewRepository.getReviews(productId);
  },
  async summarizeReviews(productId: number): Promise<string> {
    // Get the last 10 reviews for the product
    const reviews = await reviewRepository.getReviews(productId, 10);
    const reviewTexts = reviews.map((review) => review.content).join("\n\n");
    // Send the reviews to a LLM to generate a summary
    const summary = `Summary for product ${productId}: This is a placeholder summary based on the following reviews:\n${reviewTexts}`;
    return summary;
  },
};
