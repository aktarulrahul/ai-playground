import { ReviewList } from "./components/reviews/ReviewList";

function App() {
  return (
    <div className="h-screen p-4">
      <ReviewList productId={2} />
    </div>
  );
}

export default App;
