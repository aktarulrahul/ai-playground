import { reviewRepository } from "../repositories/review.repository";
import { llmClient } from "../llm/client";
import template from "../prompts/summarize-reviews.txt";

export const reviewService = {
  async summarizeReviews(productId: number): Promise<string> {
    const existingSummary = await reviewRepository.getReviewSummary(productId);
    if (existingSummary) {
      return existingSummary;
    }
    // Get the last 10 reviews for the product
    const reviews = await reviewRepository.getReviews(productId, 10);
    const joinedReview = reviews.map((review) => review.content).join("\n\n");
    const prompt = template.replace("{{joinedReview}}", joinedReview);
    const { text: summary } = await llmClient.generateText({
      model: "gpt-4o-mini",
      prompt: prompt,
      temperature: 0.2,
      maxOutputTokens: 500,
    });
    // Store the summary in the database
    await reviewRepository.storeReviewSummary(productId, summary);
    return summary;
  },
};
