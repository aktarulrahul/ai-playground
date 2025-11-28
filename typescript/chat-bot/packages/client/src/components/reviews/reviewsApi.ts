import axios from "axios";

export const reviewsApi = {
  async fetchReviews(productId: number) {
    const { data } = await axios.get(`/api/products/${productId}/reviews`);
    return data;
  },
  async SummarizeReviews(productId: number) {
    const { data } = await axios.post(
      `/api/products/${productId}/reviews/summarize`
    );
    return data;
  },
};
