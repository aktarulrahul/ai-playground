export const TypingIndicator = () => {
  return (
    <div className="flex gap-1 p-3">
      <DotsTypingIndicator />
      <DotsTypingIndicator className="[animation-delay:0.2s]" />
      <DotsTypingIndicator className="[animation-delay:0.4s]" />
    </div>
  );
};

type DotsTypingIndicatorProps = {
  className?: string;
};
const DotsTypingIndicator = ({ className }: DotsTypingIndicatorProps) => (
  <div
    className={`w-3 h-3 bg-gray-400 rounded-full animate-bounce ${className}`}
  ></div>
);
