"use client";

import localFont from "next/font/local";

const dmSansRegular = localFont({
  src: "../fonts/dm-sans/DMSans_18pt-Regular.ttf",
  display: "swap",
});

type ColorButtonProps = {
  color: string;
  grade: string;
  selected?: boolean;
  onSelect: (grade: string) => void;
};

export default function ColorButton({
  color,
  grade,
  selected = false,
  onSelect,
}: ColorButtonProps) {
  return (
    <button
      onClick={() => onSelect(grade)}
      className={`${dmSansRegular.className} flex flex-col items-center gap-2`}
    >
      <div
        className={`h-12 w-12 rounded-full border-2 shadow-sm transition-all ${
          selected
            ? "scale-110 border-[#1e3a8a]"
            : "border-[#e5e7eb]"
        }`}
        style={{
          backgroundColor: color,
        }}
      />

      <span className="text-sm text-[#111827]">
        {grade}
      </span>
    </button>
  );
}