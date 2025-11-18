import { FaArrowUp } from "react-icons/fa";
import { Button } from "../ui/button";
import { useForm } from "react-hook-form";

export type ChatFormData = {
  prompt: string;
};

type Props = {
  onSubmit: (data: ChatFormData) => void;
};

export const ChatInput = ({ onSubmit }: Props) => {
  const { register, handleSubmit, reset, formState } = useForm<ChatFormData>();

  const onKeyDown = (e: React.KeyboardEvent<HTMLFormElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      handleFormSubmit();
      e.preventDefault();
    }
  };
  const handleFormSubmit = handleSubmit((data) => {
    reset({ prompt: "" });
    onSubmit(data);
  });
  return (
    <form
      onSubmit={handleFormSubmit}
      onKeyDown={onKeyDown}
      className="flex flex-col gap-2 items-end border-2 p-4 rounded-3xl"
    >
      <textarea
        {...register("prompt", {
          required: true,
          validate: (value) => value.trim().length > 0,
        })}
        autoFocus
        placeholder="Ask Anything..."
        maxLength={1000}
        rows={4}
        cols={50}
        className="w-full border-0 p-2 focus:outline-0 resize-none"
      />
      <Button
        className="rounded-full w-9 h-9"
        type="submit"
        disabled={formState.isSubmitting || !formState.isValid}
      >
        <FaArrowUp />
      </Button>
    </form>
  );
};
