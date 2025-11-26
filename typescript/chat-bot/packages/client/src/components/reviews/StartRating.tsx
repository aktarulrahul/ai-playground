import { FaStar } from "react-icons/fa";

type Props = {
  value: number;
};

const StartRating = ({ value }: Props) => {
  const placeholders = [1, 2, 3, 4, 5];
  return (
    <div className="flex items-center gap-1">
      {placeholders.map((placeholder) => (
        <FaStar
          key={placeholder}
          color={placeholder <= value ? "#ffc107" : "#e4e5e9"}
        />
      ))}
    </div>
  );
};

export default StartRating;
