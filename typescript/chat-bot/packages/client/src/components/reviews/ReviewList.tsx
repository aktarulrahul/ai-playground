import StartRating from "./StartRating";
import Skeleton from "react-loading-skeleton";
import { useMutation, useQuery } from "@tanstack/react-query";
import { Button } from "../ui/button";
import { HiSparkles } from "react-icons/hi2";
import { reviewsApi } from "./reviewsApi";

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
  const reviewsQuery = useQuery<GetReviewsResponse>({
    queryKey: ["reviews", productId],
    queryFn: () => reviewsApi.fetchReviews(productId),
  });

  const summarizeMutation = useMutation({
    mutationFn: () => reviewsApi.SummarizeReviews(productId),
    onSuccess: () => {
      reviewsQuery.refetch();
    },
  });
  if (reviewsQuery.isLoading) {
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
  if (reviewsQuery.isError) {
    return <div className="text-red-500">{reviewsQuery.error.message}</div>;
  }
  if (!reviewsQuery.data?.reviews.length) {
    return <div>No reviews available.</div>;
  }
  return (
    <div>
      <div className="mb-5">
        {reviewsQuery.data?.summary ? (
          <p>{reviewsQuery.data.summary}</p>
        ) : (
          <Button
            onClick={() => summarizeMutation.mutate()}
            disabled={summarizeMutation.isPending}
          >
            <HiSparkles className="inline" /> Summaries
          </Button>
        )}
        {summarizeMutation.isError && (
          <p className="text-red-500 mt-2">
            Error generating summary. Please try again.
          </p>
        )}
      </div>
      <div className="flex flex-col gap-5">
        {reviewsQuery.data?.reviews?.map((review) => (
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
    </div>
  );
};
