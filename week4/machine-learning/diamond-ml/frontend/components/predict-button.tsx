"use client";

import localFont from "next/font/local";

const dmSansBold = localFont({
  src: "../fonts/dm-sans/DMSans_36pt-Bold.ttf",
  display: "swap",
});

type PredictButtonProps = {
  onClick: () => void;
};

export default function PredictButton({
  onClick,
}: PredictButtonProps) {
  return (
    <div className="flex w-full items-center justify-center pt-14">
      <button
        onClick={onClick}
        className={`${dmSansBold.className} h-18 w-36 rounded-lg bg-[#1e3a8a] px-6 py-3 text-[24px] text-white shadow-md transition duration-200 hover:scale-105 hover:bg-[#1e40af]`}
      >
        Predict
      </button>
    </div>
  );
}