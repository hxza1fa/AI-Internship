"use client";

import localFont from "next/font/local";

const dmSansRegular = localFont({
  src: "../fonts/dm-sans/DMSans_36pt-Bold.ttf",
  display: "swap",
});

type TextButtonProps = {
  text: string;
  selected?: boolean;
  onSelect: (text: string) => void;
};

export default function TextButton({
  text,
  selected = false,
  onSelect,
}: TextButtonProps) {
  return (
    <button
      onClick={() => onSelect(text)}
      className={`${dmSansRegular.className} rounded-lg border px-4 py-2 text-sm shadow-sm transition-all ${
        selected
          ? "border-[#1e3a8a] bg-[#1e3a8a] text-white"
          : "border-[#e5e7eb] bg-white text-[#111827] hover:bg-[#f5f5f5]"
      }`}
    >
      {text}
    </button>
  );
}