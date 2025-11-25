import axios from "axios";
import { useEffect, useState } from "react";

type Props = {
  productId: number;
};

type Review = {
  id: number;
  author: string;
  content: string;
  rating: number;
  createdAt: string;
};

type GetReviewsResponse = {
  reviews: Review[];
  summary: string | null;
};

export const ReviewList = ({ productId }: Props) => {
  const [reviewData, setReviewData] = useState<GetReviewsResponse>({
    reviews: [],
    summary: null,
  });
  const fetchReviews = async () => {
    try {
      const { data } = await axios.get(`/api/products/${productId}/reviews`);
      setReviewData(data);
    } catch (error) {
      console.error("Error fetching reviews:", error);
    }
  };
  useEffect(() => {
    fetchReviews();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [productId]);
  return (
    <div className="flex flex-col gap-5">
      {reviewData?.reviews?.map((review) => (
        <div
          key={review.id}
          style={{
            border: "1px solid #ccc",
            padding: "10px",
            marginBottom: "10px",
          }}
        >
          <h4 className="font-semibold">
            {review.author} - Rating: {review.rating}/5
          </h4>
          <p className="py-2">{review.content}</p>
          <small>
            Reviewed on: {new Date(review.createdAt).toLocaleDateString()}
          </small>
        </div>
      ))}
    </div>
  );
};
