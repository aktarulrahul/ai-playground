import axios from "axios";
import StartRating from "./StartRating";
import Skeleton from "react-loading-skeleton";
import { useQuery } from "@tanstack/react-query";

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
  const fetchReviews = async () => {
    const { data } = await axios.get(`/api/products/${productId}/reviews`);
    return data;
  };
  const {
    data: reviewData,
    error,
    isLoading,
  } = useQuery<GetReviewsResponse>({
    queryKey: ["reviews", productId],
    queryFn: fetchReviews,
  });

  if (isLoading) {
    return (
      <div className="flex flex-col gap-5">
        {[1, 2, 3].map((_, index) => (
          <div
            key={index}
            style={{
              border: "1px solid #ccc",
              padding: "10px",
              marginBottom: "10px",
            }}
          >
            <h4 className="font-semibold">
              <Skeleton width={100} />
            </h4>
            <Skeleton width={80} height={20} style={{ marginBottom: "8px" }} />
            <p className="py-2">
              <Skeleton count={3} />
            </p>
            <small>
              <Skeleton width={120} />
            </small>
          </div>
        ))}
      </div>
    );
  }
  if (error) {
    return <div className="text-red-500">{error.message}</div>;
  }
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
          <h4 className="font-semibold">{review.author}</h4>
          <StartRating value={review.rating} />
          <p className="py-2">{review.content}</p>
          <small>
            Reviewed on: {new Date(review.createdAt).toLocaleDateString()}
          </small>
        </div>
      ))}
    </div>
  );
};
