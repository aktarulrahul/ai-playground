import type { Review } from "../generated/prisma";
import { reviewRepository } from "../repositories/review.repository";
import { llmClient } from "../llm/client";
import template from "../prompts/summarize-reviews.txt";
import { response } from "express";

export const reviewService = {
  async getReviews(productId: number): Promise<Review[]> {
    return reviewRepository.getReviews(productId);
  },
  async summarizeReviews(productId: number): Promise<string> {
    const existingSummary = await reviewRepository.getReviewSummary(productId);
    if (existingSummary && existingSummary.expiresAt > new Date()) {
      return existingSummary.content;
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
